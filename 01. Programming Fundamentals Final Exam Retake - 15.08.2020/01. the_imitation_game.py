encrypted_message = input().split()

while True:
    command = input().split("|")
    if command[0] == "Decode":
        break
    elif command[0] == "Move":
        index = command[1]
        for i in range(index):
            
    elif command[0] == "Insert":
        pass
    elif command[0] == "ChangeAll":
        pass
    