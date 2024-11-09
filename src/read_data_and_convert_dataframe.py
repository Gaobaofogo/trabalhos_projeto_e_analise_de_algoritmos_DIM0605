import pandas as pd, re

def read_data(path: str = "../data/pure/j30hrs.sm"):
    with open(path, "r") as file:
        lines = file.readlines()

    pattern = r"^(\d+)\s+(\d+)\s+(\d+)\s+(\w{3}\s+\w{3}\s+\d+\s+\d+:\d+:\d+\s+\d+)\s+([\w\s./,]+)\n$"
    columns_pattern = r"^(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+).*$"

    data = []
    data_columns = []

    match = re.match(columns_pattern, lines[2].strip())
    if match:
        data_columns = [str(col) for col in match.groups()]

    for line in lines[4:]:
        match = re.match(pattern, line)
        if match:
            data.append(match.groups())

    df = pd.DataFrame(data, columns=data_columns)

    return df
