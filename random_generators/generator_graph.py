from random import randint, shuffle

MAX_RANDOM_WEIGHT = 40

def random_adjacency_list(n: int, m: int, weighted: bool = True, directed: bool = True) -> str:
    output = f"{n} {m}\n"

    if directed:
        random_choices = [(u, v) for u in range(n) for v in range(n) if u != v]
    else:
        random_choices = [(u, v) for u in range(n) for v in range(u + 1, n)]

    shuffle(random_choices)

    random_choices = random_choices[:m]

    for (u, v) in random_choices:
        if weighted:
            output += f"{u} {v} {randint(1, MAX_RANDOM_WEIGHT)}\n"
        else:
            output += f"{u} {v}\n"

    return output

def random_adjacency_list_only_one_component(n: int, m: int, weighted: bool = True, directed: bool = True) -> str:

    output = f"{n} {m}\n"

    random_choices = [(u,u+1) for u in range(n-1)]

    if directed:
        temp_random_choices = [(u, v) for u in range(n) for v in range(n) if u != v and u != v-1]
    else:
        temp_random_choices = [(u, v) for u in range(n) for v in range(u + 1, n) if u != v-1]

    shuffle(temp_random_choices)
    temp_random_choices = temp_random_choices[:m-n+1]

    random_choices.extend(temp_random_choices)

    for (u, v) in random_choices:
        if weighted:
            output += f"{u} {v} {randint(1, MAX_RANDOM_WEIGHT)}\n"
        else:
            output += f"{u} {v}\n"

    return output