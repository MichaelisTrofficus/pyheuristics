def imp_first(objective_fn, curr_sol, curr_cost, neighbors):
    for sol in neighbors:
        if objective_fn(sol) < curr_cost:
            return sol, objective_fn(sol)
    return curr_sol, curr_cost


def imp_best(objective_fn, curr_sol, curr_cost, neighbors):
    best = curr_sol
    for sol in neighbors:
        candidate_cost = objective_fn(sol)
        if candidate_cost < curr_cost:
            curr_cost = objective_fn(sol)
            best = sol
    return best, curr_cost
