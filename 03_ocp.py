from abc import ABC, abstractmethod


# Classe abstrata que define a estrutura para os relatórios
class Relatorio(ABC):
    @abstractmethod
    def gerar(self):
        pass


# Classes concretas para cada tipo de relatório
class RelatorioPDF(Relatorio):
    def gerar(self):
        return "Gerando relatório PDF"


class RelatorioCSV(Relatorio):
    def gerar(self):
        return "Gerando relatório CSV"


class RelatorioHTML(Relatorio):
    def gerar(self):
        return "Gerando relatório HTML"


class RelatorioExcel(Relatorio):
    def gerar(self):
        return "Gerando relatório em Excel"


# Classe que gera o relatório sem precisar ser modificada
class GeradorRelatorio:
    def gerar(self, relatorio: Relatorio):
        return relatorio.gerar()


# Exemplo de uso:
pdf = RelatorioPDF()
csv = RelatorioCSV()
html = RelatorioHTML()
excel = RelatorioExcel()

gerador = GeradorRelatorio()

print(gerador.gerar(pdf))  # Saída: Gerando relatório PDF
print(gerador.gerar(csv))  # Saída: Gerando relatório CSV
print(gerador.gerar(html))  # Saída: Gerando relatório HTML
print(gerador.gerar(excel))  # Saída: Gerando relatório em Excel
