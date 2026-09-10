class DeadCodeEliminator:
    """
    SSA Aggressive Dead Code Elimination (ADCE) engine.
    Traverses dependency graphs to purge non-live instructions.
    """
    def eliminate(self, instructions):
        used = set()
        for var, op, deps in instructions:
            if op == "RETURN":
                used.update(deps)

        changed = True
        while changed:
            changed = False
            for var, op, deps in instructions:
                if var in used:
                    for d in deps:
                        if d not in used:
                            used.add(d)
                            changed = True

        live = [inst for inst in instructions if inst[0] in used or inst[1] == "RETURN"]
        return live
