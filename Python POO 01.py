class Usuario:
    cargo = 'Usuario do sistema'

    def __init__(self, idade, nome, altura):
        self.altura = altura
        self.idade = idade
        self.nome = nome

    def retorna_altura(self):
        print(self.altura)

    def retorna_idade(self):
        print(self.idade)

    def retorna_nome(self):
        print(self.nome)

    def show_cargo(cls):
        print(cls.cargo)


usuario1 = Usuario(19, 'Thiago', '170cm')

usuario2 = Usuario(25, 'Tatiana', '161cm')

Usuario.cargo = 'Gerente '

usuario1.show_cargo()

usuario2.show_cargo()