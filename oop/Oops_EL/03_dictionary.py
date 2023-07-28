dict= {}
n = int(input("Enter the number of entries: "))

for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict[key] = value

while True:
    print("1.Values. \n2.Get. \n3.Pop. \n4.Pop Item. \n5.Clear. \n0.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        d = dict.values()
        print(d)
    elif choice == 2:
        key = input("Enter the key: ")
        print(dict.get(key))
    elif choice == 3:
        key = input("Enter the key to pop: ")
        dict.pop(key)
        print(dict)
    elif choice == 4:
        dict.popitem()
        print(dict)
    elif choice == 5:
        dict.clear()
        print("Successfully cleared!",dict)
    elif choice == 0:
        break
