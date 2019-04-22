
def cost(candidates):
    total_daily_rate = 0
    for skill_list, daily_rate in candidates:
        total_daily_rate += daily_rate
    return total_daily_rate

def skills(candidates):
    all_skills = set()
    for skill_list, daily_rate in candidates:
        all_skills |= set(skill_list)
    return list(all_skills)

def uncovered(project, skills):
    return list(set(project) - set(skills))

def best_individual_candidate(project, candidates):
    best_rate = 0
    for i, (skill_list, daily_rate) in enumerate(candidates):
        relevant_skills = 0
        for skill in skill_list:
            if skill in project:
                relevant_skills += 1
        skills_per_dollar = relevant_skills / daily_rate
        if best_rate < skills_per_dollar:
            best_rate = skills_per_dollar
            best_candidate = i
    return best_candidate

def team_of_best_individuals(project, candidates):
    maybe_best_team = []
    while project:
        next_best = best_individual_candidate(project, candidates)
        for skill in candidates[next_best][0]:
            if skill in project:
                project.remove(skill)
        maybe_best_team.append(candidates.pop(next_best))
    return maybe_best_team

def best_team(project, candidates):
    raise NotImplementedError

# =======================================================================

def main():
    jess = (['php', 'java'], 200)
    clark = (['php', 'c++', 'go'], 1000)
    john = (['lua'], 500)
    cindy = (['php', 'go', 'word'], 240)

    candidates = [jess, clark, john, cindy]
    project = ['php', 'java', 'c++', 'lua', 'go']

    examples = ['print(cost([john, cindy]))',
                'print(skills([clark, cindy]))',
                'print(uncovered(project, skills([clark])))',
                'print(best_individual_candidate(project, candidates))',
                'print(team_of_best_individuals(project, candidates))',
                'print(best_team(project, candidates))']

    for example in examples:
        print(example)
        eval(example)
        print()

if __name__ == '__main__':
    main()

