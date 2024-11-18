import argparse

from src.greedy_randomized_procedure import greedy_randomized_procedure
from src.generate_graph import problem_generator

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

initial_node, all_ids_nodes, available_resources = problem_generator(args.file)
resultado = greedy_randomized_procedure(
    initial_node, all_ids_nodes, available_resources, float(args.alfa)
)
print(resultado)
