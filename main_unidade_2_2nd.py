import argparse

from src.exato.backtracking2 import RCPSP
from src.exato.read_data_without_pandas import parse_file
from src.exato.organize_data import organize_data

parser = argparse.ArgumentParser(
    description="Programa para encontrar uma solução de execução para o problema RCPSP"
)

parser.add_argument(
    "--file",
    type=str,
    default="./data/data/j30/j301_1.sm",
    help="O caminho do arquivo da instância do problema",
)
parser.add_argument(
    "--alfa",
    type=float,
    default=0.5,
    help="Parâmetro do algoritmo que ajusta os possíveis candidatos selecionados na etapa de busca por possíveis candidatos a serem processados. Se alfa=0, todas as atividades se tornam possíveis de serem selecionadas. Se alfa=1, só a atividade com maior valor de recursos será selecionada sempre e seria equivalente a deixar o algoritmo a uma construção gulosa sem a parte da aleatoriedade.",
)

args = parser.parse_args()

a, b, c, d = parse_file(args.file)
tasks, resources, durations, resource_requirements, dependencies = organize_data(a, b, c, d)

problem = RCPSP(tasks, resources, durations, resource_requirements, dependencies)
solution = problem.solve()

if solution:
    print("Solução encontrada:", solution["tasks"])
else:
    print("Nenhuma solução viável foi encontrada.")

