turns = []
reject = [0, 0, 1]
turns = sum((reject[i] + 1) * 2 for i in range(len(reject)))
print(type(turns), turns)
reject = sum(reject) 