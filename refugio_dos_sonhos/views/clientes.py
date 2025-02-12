import flet as ft
from models.cliente import Cliente
from models.gerenciador import GerenciadorReservas

class TelaClientes:
    def __init__(self, page: ft.Page, gerenciador: GerenciadorReservas):
        self.page = page
        self.gerenciador = gerenciador
        self.lista_clientes = ft.Column()

    def adicionar_cliente(self, e):
        nome = self.input_nome.value
        telefone = self.input_telefone.value
        email = self.input_email.value

        if nome and telefone and email:
            cliente = Cliente(nome, telefone, email)
            self.gerenciador.adicionar_cliente(cliente)
            self.atualizar_lista()
            self.input_nome.value = ""
            self.input_telefone.value = ""
            self.input_email.value = ""
            self.page.update()

    def remover_cliente(self, cliente):
        self.gerenciador.clientes.remove(cliente)
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_clientes.controls.clear()
        for cliente in self.gerenciador.clientes:
            self.lista_clientes.controls.append(
                ft.Row([
                    ft.Text(cliente.nome),
                    ft.Text(cliente.telefone),
                    ft.Text(cliente.email),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, c=cliente: self.remover_cliente(c))
                ])
            )
        self.page.update()

    def exibir(self):
        self.input_nome = ft.TextField(label="Nome")
        self.input_telefone = ft.TextField(label="Telefone")
        self.input_email = ft.TextField(label="E-mail")

        form = ft.Column([
            self.input_nome,
            self.input_telefone,
            self.input_email,
            ft.ElevatedButton("Adicionar Cliente", on_click=self.adicionar_cliente)
        ])

        return ft.Column([
            ft.Text("Gerenciamento de Clientes", size=20, weight=ft.FontWeight.BOLD),
            form,
            ft.Divider(),
            ft.Text("Lista de Clientes"),
            self.lista_clientes
        ])
