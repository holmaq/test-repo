from .test2 import class2

class class3(class2):

    input_string = "Clara"
    
    def __init__(self) -> None:
        pass

    def method_1(self, input=input_string):
        return super().method_1(input)


classinstance = class3()

classinstance.map()