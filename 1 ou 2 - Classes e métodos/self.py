class Exemplo:
    def asteritico(self)->str:
        print('*****')
    def xis(self)->str:
        print('xxxx')
        self.xis()

exem = Exemplo()
exem.xis()
