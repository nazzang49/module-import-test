from test2 import module2

class Module1:
    def get_module1(self):
        print("this is module1")

mod = module2.Module2
mod.get_module2(0)

module2.get_general_func()