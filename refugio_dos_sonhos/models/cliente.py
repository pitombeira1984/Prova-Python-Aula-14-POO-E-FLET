import uuid

class Cliente:
    def __init__(self, nome: str, telefone: str, email: str):
        self.id = str(uuid.uuid4())  # Gera um ID único
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome} ({self.email})"
