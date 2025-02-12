import flet as ft
from models.quarto import Quarto
from models.gerenciador import GerenciadorReservas
from views.clientes import TelaClientes
from views.reservas import TelaReservas
from views.formulario import FormularioReserva

class TelaInicial:
    def __init__(self, page: ft.Page, gerenciador: GerenciadorReservas):
        self.page = page
        self.gerenciador = gerenciador
        self.lista_quartos = ft.Column()

    def atualizar_lista_quartos(self):
        self.lista_quartos.controls.clear()
        for quarto in self.gerenciador.quartos:
            status = "Disponível" if quarto.disponivel else "Ocupado"
            self.lista_quartos.controls.append(
                ft.Row([
                    ft.Text(f"Quarto {quarto.numero} - {quarto.tipo} - R$ {quarto.preco:.2f}"),
                    ft.Text(f"Status: {status}", color="green" if quarto.disponivel else "red"),
                ])
            )
        self.page.update()

    def abrir_tela_clientes(self, e):
        self.page.clean()
        tela_clientes = TelaClientes(self.page, self.gerenciador)
        self.page.add(tela_clientes.exibir())

    def abrir_tela_reservas(self, e):
        self.page.clean()
        tela_reservas = TelaReservas(self.page, self.gerenciador)
        self.page.add(tela_reservas.exibir())

    def abrir_formulario_reserva(self, e):
        self.page.clean()
        formulario = FormularioReserva(self.page, self.gerenciador)
        self.page.add(formulario.exibir())

    def exibir(self):
        self.atualizar_lista_quartos()

        return ft.Column([
            ft.Text("Refúgio dos Sonhos - Gestão de Reservas", size=20, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            ft.Text("Lista de Quartos Disponíveis"),
            self.lista_quartos,
            ft.Divider(),
            ft.Row([
                ft.ElevatedButton("Gerenciar Clientes", on_click=self.abrir_tela_clientes),
                ft.ElevatedButton("Criar Reserva", on_click=self.abrir_formulario_reserva),
                ft.ElevatedButton("Consultar Reservas", on_click=self.abrir_tela_reservas),
            ], alignment=ft.MainAxisAlignment.CENTER),
        ])
