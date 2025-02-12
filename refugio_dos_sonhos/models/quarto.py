class Quarto:
    def __init__(self, numero: int, tipo: str, preco: float, disponivel=True):
        self.numero = numero
        self.tipo = tipo  # 'single', 'double', 'suite'
        self.preco = preco
        self.disponivel = disponivel

    def __str__(self):
        status = "Disponível" if self.disponivel else "Ocupado"
        return f"Quarto {self.numero} - {self.tipo} - R$ {self.preco:.2f} ({status})"
