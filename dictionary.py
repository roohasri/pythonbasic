dictionary={ "alice":75, "rooha":98,"ramya":100,"swati":87 }
x=input()
value=dictionary.get(x)
if value is not None:
    print(value)
else:
    print("given key is not present")
    