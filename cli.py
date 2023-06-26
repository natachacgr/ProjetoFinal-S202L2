class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class AvaliacaoCLI(SimpleCLI):
    def __init__(self, avaliacao_model):
        super().__init__()
        self.avaliacao_model = avaliacao_model
        self.add_command("create_person", self.create_person)
        self.add_command("create_movie", self.create_movie)
        self.add_command("create_aval", self.create_aval)
        self.add_command("update_aval", self.update_aval)
        self.add_command("read_person", self.read_person)
        self.add_command("read_movie", self.read_movie)
        self.add_command("read_aval", self.read_aval)
        self.add_command("delete_person", self.delete_person)
        self.add_command("delete_movie", self.delete_movie)
        self.add_command("delete_aval", self.delete_aval)

    def create_person(self):
        name = input("Entre com o nome da pessoa: ")
        idade = input("Entre com a idade da pessoa: ")
        sexo = input("Entre com o sexo da pessoa: ")
        self.avaliacao_model.create_person(name, idade, sexo)

    def create_movie(self):
        name = input("Entre com o nome do filme: ")
        ano_lanc = input("Entre com o ano de lancamento do filme: ")
        diretor = input("Entre com o diretor do filme: ")
        genero = input("Entre com o genero do filme: ")
        self.avaliacao_model.create_movie(name, ano_lanc, diretor, genero)

    def create_aval(self):
        name_pessoa = input("Entre com o nome da pessoa: ")
        name_movie = input("Entre com o nome do filme: ")
        nota = input("Entre com a nota do filme: ")
        comentario = input("Entre com o comentario do filme: ")
        self.avaliacao_model.create_aval(name_pessoa, name_movie, nota, comentario)

    def update_aval(self):
        name_pessoa = input("Entre com o nome da pessoa: ")
        name_movie = input("Entre com o nome do filme: ")
        new_nota = input("Entre com a nova nota do filme: ")
        new_comentario = input("Entre com o novo comentario do filme: ")
        self.avaliacao_model.update_aval(name_pessoa, name_movie, new_nota, new_comentario)

    def read_person(self):
        name = input("Entre com o nome da pessoa: ")
        print(self.avaliacao_model.read_person(name))

    def read_movie(self):
        name = input("Entre com o nome do filme: ")
        print(self.avaliacao_model.read_movie(name))

    def read_aval(self):
        name_pessoa = input("Entre com o nome da pessoa: ")
        name_movie = input("Entre com o nome do filme: ")
        print(self.avaliacao_model.read_aval(name_pessoa, name_movie))

    def delete_person(self):
        name = input("Entre com o nome da pessoa: ")
        self.avaliacao_model.delete_person(name)

    def delete_movie(self):
        name = input("Entre com o nome do filme: ")
        self.avaliacao_model.delete_movie(name)

    def delete_aval(self):
        name_pessoa = input("Entre com o nome da pessoa: ")
        name_movie = input("Entre com o nome do filme: ")
        self.avaliacao_model.delete_aval(name_pessoa, name_movie)

    def run(self):
        print("Welcome to the Movie CLI!")
        print("Available commands: {}".format(list(self.commands.keys())))
        super().run()