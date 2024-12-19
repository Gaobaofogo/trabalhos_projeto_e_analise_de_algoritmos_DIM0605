import random

from copy import deepcopy

from src.generate_graph import problem_generator
from src.noh import Noh, busca_em_profundidade


def greedy_randomized_procedure(initial_node, all_ids_nodes, available_resources, alfa):
    """
    Essa função representa a fase construtiva onde o resultado é uma lista contendo a sequência
    de tarefas a serem executadas por aquele projeto visando o menor custo encontrado nessa execução.
    A função é criada baseada na seção 5.2 do artigo:
        A HYBRID HEURISTIC ALGORITHM FOR SOLVING THE
        RESOURCE CONSTRAINED PROJECT SCHEDULING PROBLEM (RCPSP)

    n = quantidade dos nós no grafo
    k = quantidade de recursos
    w = somatório de todos os custos de tempo dos nós

    O(w * ((k + 5)*n^2 + 2k + 4n) + (k + 3)n^2 + 2k)
    """
    activity_list_result = []
    total_time = 0
    already_processed_id_nodes = [all_ids_nodes[0], all_ids_nodes[-1]]
    in_process_nodes = []
    all_ids_activitie_nodes = all_ids_nodes[1:-1]
    actual_available_resources = deepcopy(available_resources)

    resources_i = resources(
        initial_node.sucessores, [initial_node], available_resources
    )  # O(n^2 * k)
    actual_candidate_list = restricted_candidate_list(
        initial_node.sucessores, resources_i, alfa
    )  # O(3n^2)
    selected_candidate = random.choice(actual_candidate_list)

    try:
        ok, actual_available_resources = decrease_available_resources(
            actual_available_resources, selected_candidate.lista_de_recursos
        )  # O(2k)
        if ok:
            in_process_nodes.append(selected_candidate)
            activity_list_result.append(selected_candidate.identificador)
    except Exception:
        pass

    while len(already_processed_id_nodes) <= len(all_ids_activitie_nodes):  # O(w * ?)
        # Aqui o tempo passa em uma unidade para todos. Assim, deve ser decrementado a variável custo_de_tempo em uma unidade
        total_time += 1
        for noh in in_process_nodes:  # O(n)
            noh.custo_de_tempo -= 1

        # Se o custo de tempo for zero, ou seja, acabou o tempo de processamento, tira da lista de
        # que tá em processamento e joga na lista de já processados e devolve o recurso para a lista de recursos atual
        to_remove_process_nodes = [
            node for node in in_process_nodes if node.custo_de_tempo == 0
        ]  # O(n)
        in_process_nodes = [
            node for node in in_process_nodes if node.custo_de_tempo > 0
        ]  # O(n)
        for node in to_remove_process_nodes:  # O(n * k)
            already_processed_id_nodes.append(node.identificador)
            actual_available_resources = increase_available_resources(
                actual_available_resources, node.lista_de_recursos
            )

        # Aqui pegamos todos os sucessores dos nós que podem ser elegíveis como candidatos a serem processados naquele momento de tempo
        # Que são os sucessores dos nós que já foram processados que todos os antecessores já foram processados
        alrd_processed_nodes = [
            busca_em_profundidade(processed_node_id, initial_node)
            for processed_node_id in already_processed_id_nodes
        ]  # O(n^2)
        sucessors_processed_nodes = []
        for sucessors_nodes in alrd_processed_nodes:  # O(n^2)
            for s in sucessors_nodes.sucessores:
                sucessors_processed_nodes.append(s)

        sucessors_processed_nodes_ids = set(
            [suc.identificador for suc in sucessors_processed_nodes]
        )  # O(n)
        in_process_nodes_ids = set(
            [noh.identificador for noh in in_process_nodes]
        )  # O(n)
        actual_sucessors_ids = list(
            (sucessors_processed_nodes_ids - set(already_processed_id_nodes))
            - in_process_nodes_ids
        )
        actual_sucessors_nodes = [
            busca_em_profundidade(suc_id, initial_node)
            for suc_id in actual_sucessors_ids
        ]  # O(n^2)

        resources_i = resources(
            actual_sucessors_nodes, in_process_nodes, available_resources
        )  # O(n^2 * k)
        actual_candidate_list = restricted_candidate_list(
            actual_sucessors_nodes, resources_i, alfa
        )  # O(3n^2)
        if len(actual_candidate_list) > 0:
            selected_candidate = random.choice(actual_candidate_list)

            try:
                ok, actual_available_resources = decrease_available_resources(
                    actual_available_resources, selected_candidate.lista_de_recursos
                )  # O(2k)
                if ok:
                    in_process_nodes.append(selected_candidate)
                    activity_list_result.append(selected_candidate.identificador)
            except Exception:
                pass

    return activity_list_result, total_time


def decrease_available_resources(available_resources, selected_resources):
    """
    Função auxiliar para retirar os recursos para que uma tarefa possa executar algo
    Complexidade O(2k)
    """
    for k in range(len(available_resources)):
        if available_resources[k] - selected_resources[k] < 0:
            return False, []

    for k in range(len(available_resources)):
        available_resources[k] -= selected_resources[k]

    return True, available_resources


def increase_available_resources(available_resources, selected_resources):
    """
    Função auxiliar para reinserir os recursos que uma tarefa tinha alocado previamente
    Complexidade O(k)
    """
    for k in range(len(available_resources)):
        available_resources[k] += selected_resources[k]

    return available_resources


def restricted_candidate_list(nohs, resources_activities, alfa):
    """
    Essa função representa a equação (7) do artigo:
        A HYBRID HEURISTIC ALGORITHM FOR SOLVING THE
        RESOURCE CONSTRAINED PROJECT SCHEDULING PROBLEM (RCPSP)

    Complexidade O(3n^2)
    """
    candidate_list = []

    for i in range(len(nohs)):  # O(n)
        if resources_activities[i] >= (
            min(resources_activities)
            + alfa * (max(resources_activities) - min(resources_activities))
            # O(3n)
        ):
            candidate_list.append(nohs[i])  # O(1)

    return candidate_list


def resources(can_be_scheduled_activities, scheduled_activities, R):
    """
    Essa função representa a equação (6) do artigo:
        A HYBRID HEURISTIC ALGORITHM FOR SOLVING THE
        RESOURCE CONSTRAINED PROJECT SCHEDULING PROBLEM (RCPSP)

    Complexidade O(n^2 * k)
    """
    resources_total = []
    for i in range(len(can_be_scheduled_activities)):  # O(n)
        actual_resource_value = 0
        for k in range(len(R)):  # O(k)
            actual_resource_value += (
                can_be_scheduled_activities[i].lista_de_recursos[k]
                + sum(
                    [
                        activitie.lista_de_recursos[k]
                        for activitie in scheduled_activities
                    ]  # O(n)
                )
            ) / R[k]

        resources_total.append(actual_resource_value)

    return resources_total
