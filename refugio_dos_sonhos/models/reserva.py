from datetime import datetime

class Reserva:
    def __init__(self, cliente, quarto, check_in: str, check_out: str):
        self.cliente = cliente
        self.quarto = quarto
        self.check_in = datetime.strptime(check_in, "%Y-%m-%d")
        self.check_out = datetime.strptime(check_out, "%Y-%m-%d")
        self.status = "Ativa"

    def cancelar(self):
        self.status = "Cancelada"
        self.quarto.disponivel = True  # Libera o quarto

    def __str__(self):
        return f"Reserva de {self.cliente.nome} para o {self.quarto} de {self.check_in.date()} até {self.check_out.date()} - {self.status}"
