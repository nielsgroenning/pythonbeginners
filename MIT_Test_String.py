varA = 3
varB = 3

if isinstance(varA, str) or isinstance(varB, str):
    print("string involved")
elif varA > varB:
    print("bigger")
elif varA == varB:
    print("equal")
elif varA < varB:
    print("smaller")


