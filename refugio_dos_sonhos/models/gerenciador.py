from models.reserva import Reserva

class GerenciadorReservas:
    def __init__(self):
        self.reservas = []
        self.clientes = []
        self.quartos = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def verificar_disponibilidade(self, numero_quarto, check_in, check_out):
        for reserva in self.reservas:
            if reserva.quarto.numero == numero_quarto and reserva.status == "Ativa":
                if (reserva.check_in <= check_out and reserva.check_out >= check_in):
                    return False  # Quarto já reservado nas datas informadas
        return True

    def criar_reserva(self, cliente, numero_quarto, check_in, check_out):
        for quarto in self.quartos:
            if quarto.numero == numero_quarto and quarto.disponivel:
                if self.verificar_disponibilidade(numero_quarto, check_in, check_out):
                    reserva = Reserva(cliente, quarto, check_in, check_out)
                    self.reservas.append(reserva)
                    quarto.disponivel = False  # Ocupa o quarto
                    return reserva
        return None

    def cancelar_reserva(self, reserva):
        reserva.cancelar()

    def listar_reservas(self):
        return [str(reserva) for reserva in self.reservas]
