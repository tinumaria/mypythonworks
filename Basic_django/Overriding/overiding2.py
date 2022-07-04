class Ide:
    def functionalities(self):
        funcs=["createfile","rename","delete"]
        return funcs

class Pycharm(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("execute")
        funcs.append("debug")
        return funcs

py=Pycharm()
print(py.functionalities())