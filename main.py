from database import Database
from avaliacao_crud import AvaliacaoCRUD
from cli import AvaliacaoCLI

db=Database("bolt://localhost:7687", "neo4j", "password")

cli_db = AvaliacaoCRUD(db)

avalcli = AvaliacaoCLI(cli_db)
avalcli.run()

db.close()