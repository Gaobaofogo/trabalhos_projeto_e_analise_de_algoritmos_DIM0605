from src.noh import Noh, busca_em_profundidade


def backtracking_for_rcpsp(
    initial_node,
    all_valid_node_ids,
    available_resources,
    processed_ids,
    in_process_nodes,
    total_processing_time,
):
    if len(all_valid_node_ids) == len(processed_ids):
        return processed_ids, total_processing_time

    for node_id in all_valid_node_ids:
        """
        A cada iteração do algoritmo eu vou pegando um novo nó para ir processando. Porém, como que eu vou
        contabilizar o processamento de tempo?

        Uma ideia que eu tive é de pegar os nós elegíveis, ir botando e quando eu não puder mais
        eu faço a contabilização do tempo. Se eu começar com processed_ids com o nó "1" eu tenho os nós iniciais
        válidos e processo todos eles. Problema: quando vai ocorrer esse processamento?

            4
        1   2   3   6
            5

        """
        if node_id == 2:
            node = busca_em_profundidade(node_id, initial_node)
            print(node.predecessores)
            print(can_be_processed(initial_node, node_id, processed_ids))
        if can_be_processed(initial_node, node_id, processed_ids):
            print(processed_ids)
            node = busca_em_profundidade(node_id, initial_node)
            result_processed_ids = backtracking_for_rcpsp(
                initial_node,
                all_valid_node_ids,
                available_resources,
                processed_ids + [node_id],
                in_process_nodes,
                total_processing_time + node.custo_de_tempo,
            )

            if result_processed_ids:
                return result_processed_ids


def can_be_processed(initial_node, node_id, processed_ids):
    if node_id == 2:
        if node_id in processed_ids:
            return False

        node = busca_em_profundidade(node_id, initial_node)

        for pred in node.predecessores:
            if pred.identificador not in processed_ids:
                return False

    if node_id in processed_ids:
        return False

    node = busca_em_profundidade(node_id, initial_node)

    for pred in node.predecessores:
        if pred.identificador not in processed_ids:
            return False

    return True


def get_eligible_nodes(initial_node, already_processed_id_nodes, in_process_nodes):
    # Aqui pegamos todos os sucessores dos nós que podem ser elegíveis como candidatos a serem processados naquele momento de tempo Que são os sucessores dos nós que já foram processados que todos os antecessores já foram processados
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
    in_process_nodes_ids = set([noh.identificador for noh in in_process_nodes])  # O(n)
    actual_sucessors_ids = list(
        (sucessors_processed_nodes_ids - set(already_processed_id_nodes))
        - in_process_nodes_ids
    )
    actual_sucessors_nodes = [
        busca_em_profundidade(suc_id, initial_node) for suc_id in actual_sucessors_ids
    ]  # O(n^2)

    return actual_sucessors_nodes
