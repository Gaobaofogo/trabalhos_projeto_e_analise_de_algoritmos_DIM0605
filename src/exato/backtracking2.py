class RCPSP:
    def __init__(self, tasks, resources, durations, resource_requirements, dependencies):
        self.tasks = tasks
        self.resources = resources
        self.durations = durations
        self.resource_requirements = resource_requirements
        self.dependencies = dependencies

    def is_allowed(self, schedule, task, start_time):
        for pred in self.dependencies.get(task, []):
            if pred not in schedule["tasks"]:
                return False
            pred_end_time = schedule["tasks"][pred] + self.durations[pred]
            if start_time < pred_end_time:
                return False

        end_time = start_time + self.durations[task]
        for t in range(start_time, end_time):
            for resource, requirement in self.resource_requirements[task].items():
                current_usage = schedule["resource_usage"].get((resource, t), 0)
                if current_usage + requirement > self.resources[resource]:
                    return False

        return True


    def backtrack(self, schedule, task_index):
        if task_index == len(self.tasks):
            return schedule

        task = self.tasks[task_index]

        max_time = sum(self.durations.values())
        for start_time in range(max_time + 1):
            if self.is_allowed(schedule, task, start_time):
                schedule["tasks"][task] = start_time
                for t in range(start_time, start_time + self.durations[task]):
                    for resource, requirement in self.resource_requirements[task].items():
                        schedule["resource_usage"][(resource, t)] = (
                            schedule["resource_usage"].get((resource, t), 0) + requirement
                        )

                result = self.backtrack(schedule, task_index + 1)
                if result:
                    return result

                del schedule["tasks"][task]
                for t in range(start_time, start_time + self.durations[task]):
                    for resource, requirement in self.resource_requirements[task].items():
                        schedule["resource_usage"][(resource, t)] -= requirement

        return None

    def solve(self):
        initial_schedule = {
            "tasks": {},
            "resource_usage": {},
        }
        return self.backtrack(initial_schedule, 0)