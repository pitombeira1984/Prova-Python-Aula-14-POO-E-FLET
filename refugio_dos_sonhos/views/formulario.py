import flet as ft
from models.gerenciador import GerenciadorReservas

class FormularioReserva:
    def __init__(self, page: ft.Page, gerenciador: GerenciadorReservas):
        self.page = page
        self.gerenciador = gerenciador
        self.mensagem_confirmacao = ft.Text("", color="green")

    def criar_reserva(self, e):
        cliente_nome = self.dropdown_cliente.value
        quarto_numero = self.dropdown_quarto.value
        check_in = self.input_checkin.value
        check_out = self.input_checkout.value

        if cliente_nome and quarto_numero and check_in and check_out:
            cliente = next((c for c in self.gerenciador.clientes if c.nome == cliente_nome), None)
            quarto_numero = int(quarto_numero)

            if cliente:
                reserva = self.gerenciador.criar_reserva(cliente, quarto_numero, check_in, check_out)
                if reserva:
                    self.mensagem_confirmacao.value = f"Reserva confirmada para {cliente_nome} no quarto {quarto_numero}!"
                else:
                    self.mensagem_confirmacao.value = "Erro ao criar reserva."
                self.page.update()

    def voltar_tela_inicial(self, e):
        from views.tela_inicial import TelaInicial
        self.page.clean()
        tela_inicial = TelaInicial(self.page, self.gerenciador)
        self.page.add(tela_inicial.exibir())

    def exibir(self):
        self.dropdown_cliente = ft.Dropdown(
            label="Selecione um Cliente",
            options=[ft.dropdown.Option(cliente.nome) for cliente in self.gerenciador.clientes]
        )

        self.dropdown_quarto = ft.Dropdown(
            label="Selecione um Quarto",
            options=[ft.dropdown.Option(str(quarto.numero)) for quarto in self.gerenciador.quartos if quarto.disponivel]
        )

        self.input_checkin = ft.TextField(label="Data de Check-in (YYYY-MM-DD)")
        self.input_checkout = ft.TextField(label="Data de Check-out (YYYY-MM-DD)")

        return ft.Column([
            ft.Text("Criar Nova Reserva", size=20, weight=ft.FontWeight.BOLD),
            self.dropdown_cliente,
            self.dropdown_quarto,
            self.input_checkin,
            self.input_checkout,
            ft.Row([
                ft.ElevatedButton("Criar Reserva", on_click=self.criar_reserva),
                ft.ElevatedButton("Voltar", on_click=self.voltar_tela_inicial),
            ]),
            self.mensagem_confirmacao,  # Exibe a mensagem de confirmação
        ])

