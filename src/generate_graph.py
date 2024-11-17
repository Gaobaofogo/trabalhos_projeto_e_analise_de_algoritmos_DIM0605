import pandas as pd
from read_data_convert_dataframe import parse_file
from noh import Noh


def problem_generator(file_name):
    project_info, precedence_relations, requests_durations, resources_avail = (
        parse_file(file_name)
    )

    noh_list = []

    for index, row in requests_durations.iterrows():
        no = Noh(row["jobnr"], row["duration"], row["resources"])
        noh_list.append(no)

    for index, row in precedence_relations.iterrows():
        for item in row["successors"]:
            noh_list[index].add_sucessor(noh_list[item - 1])

    resources = resources_avail.values.tolist()[0]
    ids = precedence_relations["jobnr"].to_list()

    return noh_list[0], ids, resources


# problem_generator("../data/data/j30/j3010_1.sm")
