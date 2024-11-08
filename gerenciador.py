import json
from datetime import datetime

class Tarefa:
    def __init__(self, descricao, prazo, prioridade, concluida=False):
        self.descricao = descricao
        self.prazo = prazo
        self.prioridade = prioridade
        self.concluida = concluida

    def para_dict(self):
        return {
            "descricao": self.descricao,
            "prazo": self.prazo,
            "prioridade": self.prioridade,
            "concluida": self.concluida
        }

class GerenciadorTarefas:
    def __init__(self, arquivo="tarefas.json"):
        self.arquivo = arquivo
        self.tarefas = self.carregar_tarefas()

    def adicionar_tarefa(self, descricao, prazo, prioridade):
        tarefa = Tarefa(descricao, prazo, prioridade)
        self.tarefas.append(tarefa)
        self.salvar_tarefas()

    def listar_tarefas(self, concluida=False):
        return [tarefa for tarefa in self.tarefas if tarefa.concluida == concluida]

    def marcar_concluida(self, descricao):
        for tarefa in self.tarefas:
            if tarefa.descricao == descricao:
                tarefa.concluida = True
                self.salvar_tarefas()
                return tarefa
        return None

    def remover_tarefa(self, descricao):
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.descricao != descricao]
        self.salvar_tarefas()

    def filtrar_tarefas(self, prioridade):
        return [tarefa for tarefa in self.tarefas if tarefa.prioridade == prioridade]

    def salvar_tarefas(self):
        with open(self.arquivo, "w") as file:
            json.dump([tarefa.para_dict() for tarefa in self.tarefas], file)

    def carregar_tarefas(self):
        try:
            with open(self.arquivo, "r") as file:
                dados = json.load(file)
                return [Tarefa(**dados_tarefa) for dados_tarefa in dados]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

# teste de adição tarefa
if __name__ == "__main__":
    gerenciador = GerenciadorTarefas()

    gerenciador.adicionar_tarefa("Estudar Python", "2024-11-01", "alta")
    gerenciador.adicionar_tarefa("Ler um livro", "2024-12-01", "media")


    print("Tarefas pendentes:")
    for tarefa in gerenciador.listar_tarefas():
        print(tarefa.para_dict())


    gerenciador.marcar_concluida("Estudar Python")

    print("\nTarefas concluídas:")
    for tarefa in gerenciador.listar_tarefas(concluida=True):
        print(tarefa.para_dict())
