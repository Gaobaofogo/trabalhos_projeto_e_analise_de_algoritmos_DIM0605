import re
import pandas as pd


def parse_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    sections = {
        "PROJECT_INFORMATION": [],
        "PRECEDENCE_RELATIONS": [],
        "REQUESTS/DURATIONS": [],
        "RESOURCEAVAILABILITIES": [],
    }

    current_section = None

    for line in lines:
        line = line.strip()

        if line.startswith("PROJECT INFORMATION"):
            current_section = "PROJECT_INFORMATION"
            continue
        elif line.startswith("PRECEDENCE RELATIONS"):
            current_section = "PRECEDENCE_RELATIONS"
            continue
        elif line.startswith("REQUESTS/DURATIONS"):
            current_section = "REQUESTS/DURATIONS"
            continue
        elif line.startswith("RESOURCEAVAILABILITIES"):
            current_section = "RESOURCEAVAILABILITIES"
            continue

        if current_section and line:
            sections[current_section].append(line)

    project_info = parse_project_information(sections["PROJECT_INFORMATION"])
    precedence_relations = parse_precedence_relations(sections["PRECEDENCE_RELATIONS"])
    requests_durations = parse_requests_durations(sections["REQUESTS/DURATIONS"])
    resources_avail = parse_resource_availabilities(sections["RESOURCEAVAILABILITIES"])

    return project_info, precedence_relations, requests_durations, resources_avail


def parse_project_information(lines):
    project_info = {}
    for line in lines[1:]:
        if not line.startswith("*"):
            parts = re.split(r"\s+", line)
            if len(parts) >= 6:
                project_info[parts[0]] = {
                    "jobs": int(parts[1]),
                    "release_date": int(parts[2]),
                    "due_date": int(parts[3]),
                    "tard_cost": int(parts[4]),
                    "mpm_time": int(parts[5]),
                }
    return project_info


def parse_precedence_relations(lines):
    relations = []
    for line in lines[1:]:
        if not line.startswith("*"):
            parts = re.split(r"\s+", line)
            jobnr = int(parts[0])
            modes = int(parts[1])
            successorsCounter = int(parts[2])
            successors = list(map(int, parts[3:]))
            relations.append(
                {
                    "jobnr": jobnr,
                    "modes": modes,
                    "successorsCounter": successorsCounter,
                    "successors": successors,
                }
            )
    return pd.DataFrame(relations)


def parse_requests_durations(lines):
    durations = []
    for line in lines[2:]:
        if not line.startswith("*"):
            parts = re.split(r"\s+", line)
            if len(parts) >= 6:
                jobnr = int(parts[0])
                mode = int(parts[1])
                duration = int(parts[2])
                resources = list(map(int, parts[3:]))
                durations.append(
                    {
                        "jobnr": jobnr,
                        "mode": mode,
                        "duration": duration,
                        "resources": resources,
                    }
                )
    return pd.DataFrame(durations)


def parse_resource_availabilities(lines):
    resources = []
    for line in lines[1:]:
        if not line.startswith("*"):
            parts = re.split(r"\s+", line)
            if len(parts) >= 4:
                r1 = int(parts[0])
                r2 = int(parts[1])
                r3 = int(parts[2])
                r4 = int(parts[3])
                resources.append({"r1": r1, "r2": r2, "r3": r3, "r4": r4})
    return pd.DataFrame(resources)


# file_name = "../data/data/j30/j3010_1.sm"
# project_info, precedence_relations, requests_durations, resources_avail = parse_file(
#     file_name
# )

# precedence_relations.to_csv("precedence_relations.csv", index=False)
# requests_durations.to_csv("requests_durations.csv", index=False)
# resources_avail.to_csv("resources_availabilities.csv", index=False)

# print("Project Information:", project_info)
