from abc import ABC, abstractmethod

class CalculoFreteInterface(ABC):
    @abstractmethod
    def calcular_frete(self):
        pass
