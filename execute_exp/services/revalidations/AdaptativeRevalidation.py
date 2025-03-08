from execute_exp.services.revalidations.AbstractRevalidation import AbstractRevalidation
from execute_exp.services.execution_modes.AbstractExecutionMode import AbstractExecutionMode
from execute_exp.entitites.Metadata import Metadata
from execute_exp.entitites.FunctionCallProv import FunctionCallProv

class AdaptativeRevalidation(AbstractRevalidation):
    def __init__(self, exec_mode:AbstractExecutionMode, initial_num_exec_til_reval:int, adaptative_factor:float):
        self.__exec_mode = exec_mode
        self.__current_num_exec_til_reval = initial_num_exec_til_reval
        self.__adaptative_factor = adaptative_factor
    
    def calculate_next_revalidation(self, fc_prov:FunctionCallProv, metadata:Metadata) -> None:
        next_reval = self.__current_num_exec_til_reval
        if self.__exec_mode.func_call_acted_as_expected(fc_prov, metadata):
            next_reval *= (1 + self.__adaptative_factor)
        else:
            next_reval *= (1 - self.__adaptative_factor)
        self.__current_num_exec_til_reval = round(next_reval)
        self.set_next_revalidation(self.__current_num_exec_til_reval, fc_prov, force=True)
