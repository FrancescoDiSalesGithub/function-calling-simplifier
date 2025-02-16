class Executioner:
    def __init__(self,name_function,dict_function:dict,response_ollama):
        self.name_function= name_function
        self.dict_function= dict_function
        self.response_ollama = response_ollama

    def run(self):
        for tool in self.response_ollama.message.tool_calls or []:
            function_to_call = self.dict_function.get(tool.function.name)
            if function_to_call:
                print('Function output:', function_to_call(**tool.function.arguments))
            else:
                print('Function not found:', tool.function.name)

