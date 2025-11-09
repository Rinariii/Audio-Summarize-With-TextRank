from csp import CSP, UniversalDict, first_unassigned_variable, unordered_domain_values, no_inference

def different_values_constraint(A, a, B, b):
    return a != b

neighbors = {
    "Tenjo": ["Parung Panjang", "Jasinga", "Cigudeg"],
    "Parung Panjang": ["Tenjo", "Rumpin", "Cigudeg"],
    "Rumpin": ["Parung Panjang", "Cigudeg", "Cibungbulang", "Leuwiliang", "Leuwisadeng"],
    "Cigudeg": ["Tenjo", "Parung Panjang", "Rumpin", "Leuwisadeng", "Nanggung", "Sukajaya", "Jasinga"],
    "Jasinga": ["Tenjo", "Cigudeg", "Sukajaya"],
    "Sukajaya": ["Jasinga", "Cigudeg", "Nanggung"],
    "Nanggung": ["Sukajaya", "Cigudeg", "Leuwisadeng", "Leuwiliang"],
    "Leuwisadeng": ["Cigudeg", "Nanggung", "Leuwiliang", "Rumpin"],
    "Leuwiliang": ["Nanggung", "Leuwisadeng", "Pamijahan", "Rumpin", "Cibungbulang"],
    "Pamijahan": ["Leuwiliang", "Cibungbulang", "Tenjolaya", "Ciampea"],
    "Cibungbulang": ["Rumpin", "Pamijahan", "Ciampea", "Leuwiliang", "Tenjolaya"],
    "Dramaga": ["Tenjolaya", "Ciampea"],
    "Ciampea": ["Cibungbulang", "Dramaga", "Tenjolaya", "Pamijahan"],
    "Tenjolaya": ["Ciampea", "Pamijahan", "Dramaga", "Cibungbulang"]
}

colors = ["Biru", "Hijau", "Merah", "Kuning"]

def MapColoringCSP(colors, neighbors):
    variables = list(neighbors.keys())
    domains = UniversalDict(colors) 
    return CSP(variables, domains, neighbors, different_values_constraint)

coloring_problem = MapColoringCSP(colors, neighbors)

def backtracking_search(csp):
    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment
        var = first_unassigned_variable(assignment, csp)
        for value in unordered_domain_values(var, assignment, csp):
            if csp.nconflicts(var, value, assignment) == 0:
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value)
                if no_inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result is not None:
                        return result
                csp.restore(removals)
                csp.unassign(var, assignment)
        return None

    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result

solution = backtracking_search(coloring_problem)


for node, color in sorted(solution.items()):
        print(f"{node}: {color}")
