from client import DeadCodeEliminator

def main():
    print("=== Testing SSA Dead Code Elimination Engine ===")
    dce = DeadCodeEliminator()
    prog = [
        ("x", "CONST", []),
        ("y", "CONST", []),
        ("z", "ADD", ["x"]),
        (None, "RETURN", ["z"])
    ]
    live = dce.eliminate(prog)
    print("Live instructions after ADCE:", live)
    assert len(live) == 3
    assert not any(inst[0] == "y" for inst in live)
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
