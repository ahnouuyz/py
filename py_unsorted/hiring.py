def cost(candidates):
    return sum(c for s, c in candidates)
#    return sum(tuple(zip(*candidates))[1])

def skills(candidates):
    return list(set(s for skills, _ in candidates for s in skills))

def uncovered(project, skills):
    return list(set(project) - set(skills))

def best_individual_candidate(project, candidates):
#    counts = [sum([sk in project for sk in sks]) for sks, _ in candidates]
#    rates = [rate for _, rate in candidates]
#    scores = [c / r for c, r in zip(counts, rates)]
    scores = [sum([sk in project for sk in sks]) / c for sks, c in candidates]
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
    skillsets = [skills for skills, _ in candidates]
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
#    print(rare_skills)
#    print(rare_candidates)
    return rare_candidates

def best_team(project, candidates):
    team = must_haves(project, candidates)
    skills = [skill for skills, _ in team for skill in skills]
    skills_needed = uncovered(project, skills)
    candidates_left = []
    for candidate in candidates:
        if candidate not in team:
            candidates_left.append(candidate)
    print('Skills available:', set(skills))
    print('Skills still needed:', skills_needed)
    print('Candidates left:', candidates_left)
    while skills_needed:
        pass
    return team

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
