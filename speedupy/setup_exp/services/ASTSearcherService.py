import ast

class ASTSearcherService(ast.NodeVisitor):
    """This class searches for all imports ('import ...', 'from ...  import ... ' and implicitly __init__.py imports) and all functions declared by the user on a file"""
    def __init__(self, AST):
        self.__AST = AST
        self.__import_commands = []
        self.__functions = {}


    def search(self):
        #Finding all declared functions and imported modules
        #in the AST

        self.__current_function = None
        self.__current_function_name = ""
        self.visit(self.__AST)


    def visit_Import(self, node):
        if(node not in self.__import_commands):
            self.__import_commands.append(node)
        self.generic_visit(node)


    def visit_ImportFrom(self, node):
        if(node not in self.__import_commands):
            self.__import_commands.append(node)
        self.generic_visit(node)


    def visit_ClassDef(self, node):
        """This function avoids that child nodes of a ClassDef node
        (ex.: class methods) be visited during search"""


    def visit_FunctionDef(self, node):
        previous_function_name = self.__current_function_name
        self.__current_function_name = node.name if self.__current_function_name == "" else self.__current_function_name + ".<locals>." + node.name
        previous_function = self.__current_function
        self.__current_function = node


        self.__functions[self.__current_function_name] = node

        self.generic_visit(node)


        self.__current_function = previous_function
        self.__current_function_name = previous_function_name


    @property
    def AST(self):
        return self.__AST


    @property
    def import_commands(self):
        return self.__import_commands


    @property
    def functions(self):
        return self.__functions
