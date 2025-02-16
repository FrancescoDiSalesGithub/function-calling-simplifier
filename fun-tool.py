class Executioner:
    def __init__(self,real_function:object,name_function:str,dict_function:dict,response_ollama):
        self.name_function= name_function
        self.dict_function= {str(self.name_function):self.real_function}
        self.response_ollama = response_ollama

    def run(self):
        for tool in self.response_ollama.message.tool_calls or []:
            function_to_call = self.dict_function.get(tool.function.name)
            if function_to_call:
                print('Function output:', function_to_call(**tool.function.arguments))
            else:
                print('Function not found:', tool.function.name)

    def run_with_return_value(self):
        for tool in self.response_ollama.message.tool_calls or []:
            function_to_call = self.dict_function.get(tool.function.name)
            if function_to_call:
                return function_to_call(**tool.function.arguments)
            else:
                return None