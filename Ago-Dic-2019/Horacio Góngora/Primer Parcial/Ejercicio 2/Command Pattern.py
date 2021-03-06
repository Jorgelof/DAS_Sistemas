from abc import ABCMeta, abstractmethod
#Clase Abstracta
class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

# Receiver
class Television():
    """docstring for Television"""

    def encender(self):
        print('Encendida!')

    def apagar(self):
        print('Apagada!')

    def cambiarCanal(numCanal):
        print(f'Cambiamos al canal {numCanal}')

    def subirVolumen(self):
        print('Subimos volumen!')

    def bajarVolumen(self):
        print('Bajamos volumen!')

class encender(Command):
    def __init__(self, encender):
        self._encender = encender

    def execute(self):
        print(f"{self._encender}")

class ComandoApagar(Command):
    def __init__(self, apagar):
        self._apagarr = apagar

    def execute(self):
        print(f"{self._apagarr}")

class ComandoCambiarCanal(Command):
    def __init__(self, cambiarCanal, canal):
        self._cambiarCanal = cambiarCanal
        self._canal = canal

    def execute(self):
        print(f"{self._cambiarCanal}, canal cambio al {self._canal}")

class SubirVolumen(Command):
    def __init__(self, subirVolumen):
        self._subirVolumen = subirVolumen

    def execute(self):
        print(f"{self._subirVolumen}")

class BajarVolumen(Command):
    def __init__(self, bajarVolumen):
        self._bajarVolumen = bajarVolumen

    def execute(self):
        print(f"{self._bajarVolumen}")

#Invoker
class ControlRemoto():
    """docstring for ControlRemoto"""
    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()


def main():
    tv = Television()
    Encender = encender(tv)

    control = ControlRemoto(Encender)
    control.invoke()

if __name__ == '__main__':
    main()