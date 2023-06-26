class AvaliacaoCRUD:
    def __init__(self, database):
        self.db = database

    def create_person(self, name, idade, sexo):
        query = "CREATE (:Pessoa {name: $name, idade: $idade, sexo: $sexo})"
        parameters = {"name": name, "idade": idade, "sexo": sexo}
        self.db.execute_query(query, parameters)

    def create_movie(self, name, ano_lanc, diretor, genero):
        query = "CREATE (:Filme {name: $name, ano_lanc: $ano_lanc, diretor: $diretor, genero: $genero})"
        parameters = {"name": name, "ano_lanc": ano_lanc, "diretor": diretor, "genero": genero}
        self.db.execute_query(query, parameters)

    def create_aval(self, name_pessoa, name_filme, nota, comentario):
        query = "MATCH (p:Pessoa {name: $name_pessoa}), (f:Filme {name: $name_filme}) CREATE (p)-[:AVALIOU {nota: $nota, comentario: $comentario}]->(f)"
        parameters = {"name_pessoa": name_pessoa, "name_filme": name_filme, "nota": nota, "comentario": comentario}
        self.db.execute_query(query, parameters)

    def update_aval(self, name_pessoa, name_filme, newNota, newComentario):
        query = "MATCH (p:Pessoa {name: $name_pessoa})-[a:AVALIOU]->(f:Filme {name: $name_filme}) SET a.nota = $newNota, a.comentario = $newComentario"
        parameters = {"name_pessoa": name_pessoa, "name_filme": name_filme, "newNota": newNota,
                      "newComentario": newComentario}
        self.db.execute_query(query, parameters)

    def read_person(self, name):
        query = "MATCH (p:Pessoa {name: $name}) RETURN p.name AS pessoa_name, p.idade AS pessoa_idade, p.sexo AS pessoa_sexo"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        pessoa_name = str([result["pessoa_name"] for result in results])
        pessoa_idade = str([result["pessoa_idade"] for result in results])
        pessoa_sexo = str([result["pessoa_sexo"] for result in results])
        return ["O nome da pessoa é: " + pessoa_name + ", a idade é: " + pessoa_idade + " e o sexo é: " + pessoa_sexo]
        # return [(result["pessoa_name"], result["pessoa_idade"], result["pessoa_sexo"]) for result in results]

    def read_movie(self, name):
        query = "MATCH (f:Filme {name: $name}) RETURN f.name AS filme_name, f.ano_lanc AS filme_ano_lanc, f.diretor AS filme_diretor, f.genero AS filme_genero"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        filme_name = str([result["filme_name"] for result in results])
        filme_ano_lanc = str([result["filme_ano_lanc"] for result in results])
        filme_diretor = str([result["filme_diretor"] for result in results])
        filme_genero = str([result["filme_genero"] for result in results])
        return [
            "O nome do filme é: " + filme_name + ", o ano de lançamento é: " + filme_ano_lanc + ", o diretor é: " + filme_diretor + " e o gênero é: " + filme_genero]

    def read_aval(self, name, movie):
        query = "MATCH (p:Pessoa {name: $name})-[a:AVALIOU]->(f:Filme {name: $movie}) RETURN a.nota AS filme_nota, a.comentario AS filme_comentario"
        parameters = {"name": name, "movie": movie}
        results = self.db.execute_query(query, parameters)
        filme_nota = str([result["filme_nota"] for result in results])
        filme_comentario = str([result["filme_comentario"] for result in results])
        return [
            "A pessoa " + name + " deu nota " + filme_nota + " e comentou: " + filme_comentario + " sobre o filme " + movie]

    def delete_movie(self, name):
        query = "MATCH (f:Filme {name: $name}) DETACH DELETE f"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_person(self, name):
        query = "MATCH (p:Pessoa {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_aval(self, name_pessoa, name_movie):
        query = "MATCH (p:Pessoa {name: $name_pessoa})-[a:AVALIOU]->(f:Filme {name: $name_movie}) DELETE a"
        parameters = {"name_pessoa": name_pessoa, "name_movie": name_movie}
        self.db.execute_query(query, parameters)