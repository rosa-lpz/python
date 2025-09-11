def get_permutations(w):
    if len(w) <= 1:
        return set([w])  # Return a set with a single string
    smaller = get_permutations(w[1:])
    perms = set()  # Initialize perms as an empty set
    for x in smaller:
        for pos in range(0, len(x) + 1):
            perm = x[:pos] + w[0] + x[pos:]
            perms.add(perm)
    return perms

print(get_permutations('cat'))
