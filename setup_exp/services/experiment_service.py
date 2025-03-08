import os
from typing import List, Dict, Set

from setup_exp.entities.Script import Script
from setup_exp.entities.Experiment import Experiment
from setup_exp.entities.FunctionGraph import FunctionGraph
from execute_exp.services.DataAccess import get_id
from setup_exp.services.script_service import create_script, create_script_function_graph, decorate_script_functions, overwrite_decorated_script, add_decorator_import
from setup_exp.services.function_service import decorate_main_function
from util import is_an_user_defined_script, get_script_path

#TODO: TEST
def create_experiment(user_script_path:str) -> Experiment:
    experiment_base_dir, user_script_name = os.path.split(user_script_path)
    experiment = Experiment(experiment_base_dir)
    scripts_analized = []
    scripts_to_be_analized = [user_script_name]
    while(len(scripts_to_be_analized) > 0):
        script_name = scripts_to_be_analized.pop(0)
        script = create_script(script_name, experiment.base_dir)
        if(script_name == user_script_name):
            experiment.set_main_script(script)
        experiment.add_script(script)
        __update_scripts_to_be_analized(script, scripts_analized, scripts_to_be_analized, experiment.base_dir)
        scripts_analized.append(script_name)
    return experiment

def __update_scripts_to_be_analized(script:Script, scripts_analized:List[str], scripts_to_be_analized:List[str], experiment_base_dir:str):
    imported_scripts = script.get_imported_scripts()        
    for imp_script in imported_scripts:
        if __script_needs_to_be_analyzed(imp_script, experiment_base_dir, scripts_analized):
            scripts_to_be_analized.append(imp_script)

            init_scripts = _get_all_init_scripts_implicitly_imported(imp_script, experiment_base_dir)
            for i_script in init_scripts:
                if __script_needs_to_be_analyzed(i_script, experiment_base_dir,scripts_analized):
                    scripts_to_be_analized.append(i_script)

def _get_all_init_scripts_implicitly_imported(imported_script:str, experiment_base_dir:str) -> Set[str]:
    init_scripts_implicitly_imported = set()
    if(imported_script.rfind(os.sep) != -1):
        current_init_script_path = imported_script[0:imported_script.rfind(os.sep) + 1] + "__init__.py"
        while(current_init_script_path != "__init__.py"):
            if(os.path.exists(get_script_path(current_init_script_path, experiment_base_dir))):
                init_scripts_implicitly_imported.add(current_init_script_path)
            current_init_script_path = current_init_script_path.split(os.sep)
            current_init_script_path.pop(-2)
            current_init_script_path = os.sep.join(current_init_script_path)
    return init_scripts_implicitly_imported

def __script_needs_to_be_analyzed(script:str, experiment_base_dir:str, scripts_analized:List[str]) -> bool:
    return is_an_user_defined_script(script, experiment_base_dir) and \
            not __script_already_analized(script, scripts_analized)

def __script_already_analized(script_name:str, scripts_analized:List[str]) -> bool:
    return script_name in scripts_analized
    
def create_experiment_function_graph(experiment:Experiment) -> FunctionGraph:
    create_script_function_graph(experiment.main_script, experiment)
    script = experiment.main_script
    return script.function_graph

def get_experiment_functions_hashes(experiment_function_graph:FunctionGraph) -> Dict[str, str]:
    functions2hashes = {}
    for vertice in experiment_function_graph.graph:
        source_code = experiment_function_graph.get_source_code_executed(vertice)
        hash = get_id(source_code)
        functions2hashes[vertice.qualname] = hash
    return functions2hashes

def decorate_experiment_functions(experiment:Experiment) -> None:
    _prepare_experiment_main_function_for_execution(experiment)
    for script in experiment.scripts.values():
        script_decorated = decorate_script_functions(script)
        if script_decorated:
            add_decorator_import(script, 'maybe_deterministic')

def _prepare_experiment_main_function_for_execution(experiment:Experiment):
    main_script = experiment.main_script
    add_decorator_import(main_script, 'initialize_speedupy')
    decorate_main_function(main_script.functions['main'])

def overwrite_decorated_experiment(experiment:Experiment):
    for script in experiment.scripts.values():
        overwrite_decorated_script(script)
