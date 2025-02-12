import flet as ft
from models.gerenciador import GerenciadorReservas

class TelaReservas:
    def __init__(self, page: ft.Page, gerenciador: GerenciadorReservas):
        self.page = page
        self.gerenciador = gerenciador
        self.lista_reservas = ft.Column()

    def cancelar_reserva(self, reserva):
        self.gerenciador.cancelar_reserva(reserva)
        self.atualizar_lista_reservas()

    def atualizar_lista_reservas(self):
        self.lista_reservas.controls.clear()
        for reserva in self.gerenciador.reservas:
            self.lista_reservas.controls.append(
                ft.Row([
                    ft.Text(f"Cliente: {reserva.cliente.nome}"),
                    ft.Text(f"Quarto: {reserva.quarto.numero} - {reserva.quarto.tipo}"),
                    ft.Text(f"Check-in: {reserva.check_in.date()}"),
                    ft.Text(f"Check-out: {reserva.check_out.date()}"),
                    ft.Text(f"Status: {reserva.status}", color="green" if reserva.status == "Ativa" else "red"),
                    ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e, r=reserva: self.cancelar_reserva(r))
                ])
            )
        self.page.update()

    def voltar_tela_inicial(self, e):
        from views.tela_inicial import TelaInicial
        self.page.clean()
        tela_inicial = TelaInicial(self.page, self.gerenciador)
        self.page.add(tela_inicial.exibir())

    def exibir(self):
        self.atualizar_lista_reservas()

        return ft.Column([
            ft.Text("Lista de Reservas", size=20, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            self.lista_reservas,
            ft.Divider(),
            ft.ElevatedButton("Voltar para Tela Inicial", on_click=self.voltar_tela_inicial),
        ])
