def organize_data(project_info, precedence_relations, requests_durations, resources_avail):

    tasks = []
    for j in range(1, project_info["jobs"]+3):
        tasks.append(j)

    durations = {}
    for i in requests_durations:
        durations[i['jobnr']] = i['duration']

    res_req = {}
    keys = [*resources_avail]
    for i in requests_durations:
        res = {}
        for index, j in enumerate(keys):
            res[j] = i['resources'][index]
        res_req[i['jobnr']] = res
    
    dependencies = {}
    for job in range(1, project_info["jobs"]+3):
        dependencies[job] = []
    for line in precedence_relations[:-1]:
        for sucessor in line['successors']:
            dependencies[sucessor].append(line['jobnr'])

    return tasks, resources_avail, durations, res_req, dependencies