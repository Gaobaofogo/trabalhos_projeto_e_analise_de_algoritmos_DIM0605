# import pandas as pd
# from src.read_data_convert_dataframe import parse_file
# from src.noh import Noh
from src.generate_graph import problem_generator

# file_name = "../../data/data/j30/j3010_1.sm"

base_no, not_processing, resources = problem_generator("data/data/j30/j3010_1.sm")


def greedy_solution(base_no, not_processing, resources):
    total = len(not_processing)
    sequence = []
    running = set()
    queue = set()
    queue.add(base_no)
    timee = 0
    resources_ammount = len(resources)
    while len(sequence) < total:
        running_list = list(running)
        for item in running_list:
            if item.custo_de_tempo == 0:
                sequence.append(item)
                running.remove(item)
                for no in item.sucessores:
                    if no not in sequence:
                        if no not in running:
                            queue.add(no)
                            no.predecessores.remove(item)
                for i in range(0, resources_ammount):
                    resources[i] += item.lista_de_recursos[i]
            else:
                item.custo_de_tempo -= 1
        queue_list = sorted(queue, key=lambda x: sum(x.lista_de_recursos))
        for item in queue_list:
            can_run = True
            for i in range(0, resources_ammount):
                if resources[i] < item.lista_de_recursos[i]:
                    can_run = False
            if can_run:
                running.add(item)
                queue.remove(item)
                for i in range(0, resources_ammount):
                    resources[i] -= item.lista_de_recursos[i]
        timee += 1
    return sequence


resultado = greedy_solution(base_no, not_processing, resources)

print(resultado)
