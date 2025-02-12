import flet as ft
from views.formulario import FormularioReserva
from models.gerenciador import GerenciadorReservas
from models.cliente import Cliente
from models.quarto import Quarto

def main(page: ft.Page):
    gerenciador = GerenciadorReservas()

    # Criando dados fictícios para testes
    gerenciador.adicionar_cliente(Cliente("Ana Costa", "11999999999", "ana@email.com"))
    gerenciador.adicionar_cliente(Cliente("Carlos Mendes", "11888888888", "carlos@email.com"))

    gerenciador.adicionar_quarto(Quarto(101, "single", 200.00))
    gerenciador.adicionar_quarto(Quarto(102, "double", 350.00))

    formulario = FormularioReserva(page, gerenciador)
    page.add(formulario.exibir())

ft.app(target=main)


