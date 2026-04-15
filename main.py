from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# =========================
# MODELO DE DADOS
# =========================
class Diagnostico(BaseModel):
    tipo_projeto: str
    usuarios: int
    tem_sistema: bool
    integracoes: bool
    urgencia: str

# =========================
# ROTA TESTE
# =========================
@app.get("/")
def home():
    return {"status": "API rodando 🚀"}

# =========================
# ROTA PRINCIPAL
# =========================
@app.post("/diagnostico")
def analisar(dados: Diagnostico):

    recomendacoes: List[str] = []

    # tipo de projeto
    if dados.tipo_projeto == "Sistema personalizado":
        recomendacoes.append("Sistema web com painel administrativo")

    if dados.tipo_projeto == "Automação de processos":
        recomendacoes.append("Automação de tarefas e processos internos")

    if dados.tipo_projeto == "Site institucional":
        recomendacoes.append("Site institucional moderno e responsivo")

    # integrações
    if dados.integracoes:
        recomendacoes.append("Integração com APIs e sistemas externos")

    # escala
    if dados.usuarios > 10:
        recomendacoes.append("Arquitetura escalável para múltiplos usuários")

    # problema identificado
    if dados.tem_sistema:
        problema = "Seu sistema atual pode estar limitando o crescimento do negócio"
    else:
        problema = "Processos manuais e falta de automação"

    # urgência
    if dados.urgencia == "Urgente":
        prioridade = "Alta prioridade: recomendamos iniciar o quanto antes"
    else:
        prioridade = "Projeto pode ser planejado de forma estratégica"

    return {
        "diagnostico": recomendacoes,
        "problema_identificado": problema,
        "prioridade": prioridade,
        "proximo_passo": "Falar com especialista"
    }