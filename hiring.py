
def cost(candidates):
#    total_daily_rate = 0
#    for skill_list, daily_rate in candidates:
#        total_daily_rate += daily_rate
#    return total_daily_rate
    return sum(list(zip(*candidates))[1])

def skills(candidates):
#    all_skills = set()
#    for skill_list, daily_rate in candidates:
#        all_skills |= set(skill_list)
#    return list(all_skills)
    return list(set(s for skills, _ in candidates for s in skills))

def uncovered(project, skills):
    return list(set(project) - set(skills))

def best_individual_candidate(project, candidates):
#    best_rate = 0
#    for i, (skill_list, daily_rate) in enumerate(candidates):
#        relevant_skills = 0
#        for skill in skill_list:
#            if skill in project:
#                relevant_skills += 1
#        skills_per_dollar = relevant_skills / daily_rate
#        if best_rate < skills_per_dollar:
#            best_rate = skills_per_dollar
#            best_candidate = i
#    return best_candidate
    counts = [sum([sk in project for sk in sks]) for sks, _ in candidates]
    rates = [rate for _, rate in candidates]
    scores = [c / r for c, r in zip(counts, rates)]
    return scores.index(max(scores))

def team_of_best_individuals(project, candidates):
    project_set = set(project)
    candidates_copy = candidates[:]
    maybe_best_team = []
    while project_set:
        next_best = best_individual_candidate(list(project_set), candidates_copy)
        project_set -= set(candidates_copy[next_best][0])
        maybe_best_team.append(candidates_copy.pop(next_best))
    return maybe_best_team

def must_haves(project, candidates):
    print(candidates)
    skillsets = [skills for skills, _ in candidates]
    print(skillsets)
    rare_skills = []
    for skill in project:
        count = 0
        for skillset in skillsets:
            if skill in skillset:
                count += 1
        if count == 1:
            rare_skills.append(skill)
    rare_candidates = []
    for candidate in candidates:
        for skill in rare_skills:
            if skill in candidate[0]:
                rare_candidates.append(candidate)
                break
    print(rare_skills)
    print(rare_candidates)
    return rare_candidates

def best_team(project, candidates):
    team = must_haves(project, candidates)
    skills = [skill for skills, _ in team for skill in skills]
    while set(project) - set(skills):
        pass
    print(team)

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

