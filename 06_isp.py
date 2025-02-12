from abc import ABC, abstractmethod


class Veiculo(ABC):
    pass


class VeiculoCarga(Veiculo):
    @abstractmethod
    def calculate_capacidade_carga(self):
        pass


class VeiculoAutonomia(Veiculo):
    @abstractmethod
    def calculate_autonomia(self):
        pass


class VeiculoBateria(Veiculo):
    @abstractmethod
    def calculate_duracao_bateria(self):
        pass


class Carro(VeiculoAutonomia):
    def calculate_autonomia(self):
        return 600  # autonomia em km


class Caminhao(VeiculoCarga, VeiculoAutonomia):
    def calculate_capacidade_carga(self):
        return 20000  # capacidade de carga em kg

    def calculate_autonomia(self):
        return 1200  # autonomia em km


class BicicletaEletrica(VeiculoBateria):
    def calculate_duracao_bateria(self):
        return 80  # duração da bateria em km


# Exemplo de uso
carro = Carro()
caminhao = Caminhao()
bicicleta = BicicletaEletrica()

print(f"Autonomia do carro: {carro.calculate_autonomia()} km")
print(f"Capacidade de carga do caminhão: {caminhao.calculate_capacidade_carga()} kg")
print(f"Duração da bateria da bicicleta: {bicicleta.calculate_duracao_bateria()} km")
