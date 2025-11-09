def agent(percept,location):
    if percept == "See People":
        action = "Brake"
        location += 0
    elif percept == "See Nothing":
        action = "Accelerate"
        location += 1
    elif percept == "See Blind Alley":
        action = "Reverse"
        location -= 1
    return action,location

location = 0
percept = input().split(",")
for p in percept:
    p = p.strip()
    action,location = agent(p,location)
    print(f"Percept: {p}, Action: {action}, Location: {location}")