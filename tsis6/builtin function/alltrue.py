def all_true(t):
    return all(t)

t1 = (True, True, True)
t2 = (True, False, True)
t3 = (1, "hello", [1, 2, 3])
t4 = (0, "", [])
print(all_true(t1))
print(all_true(t2))
print(all_true(t3))
print(all_true(t4))
