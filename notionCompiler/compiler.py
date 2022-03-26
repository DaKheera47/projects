with open("input.py", "r") as f:
    inp = f.read().split("\n")

    if "get" in inp[0]:
        data = inp[0].replace('get(', "").replace(')', "")
        print(f"prop({data})")
