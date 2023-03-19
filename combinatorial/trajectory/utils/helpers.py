def imp_first(objective_fn, curr, neighbors):
    cost = objective_fn(curr)
    for sol in neighbors:
        if objective_fn(sol) > cost:
            return sol, objective_fn(sol)
    return curr, cost


def imp_best(objective_fn, curr, neighbors):
    best = curr
    cost = objective_fn(curr)
    for sol in neighbors:
        if objective_fn(sol) > cost:
            cost = objective_fn(sol)
            best = sol
    return best, cost
