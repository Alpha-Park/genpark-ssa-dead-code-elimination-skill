import sys
import json
from client import DeadCodeEliminator

def main():
    dce = DeadCodeEliminator()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "eliminate":
            insts = [tuple(x) for x in params.get("instructions", [])]
            res = {"live_instructions": dce.eliminate(insts)}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
