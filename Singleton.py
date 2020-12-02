class Singleton:
    _instance = None
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = Singleton()
        return cls._instance

    def saludar(self,hola):
        print(hola)

    def ayuda(self,saludar):
        print(saludar)



