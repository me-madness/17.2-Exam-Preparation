encrypted_message = input().split()

while True:
    command = input().split("|")
    if command[0] == "Decode":
        break
    elif command[0] == "Move":
        index = command[1]
        for letter in encrypted_message:
            encrypted_message.remove(letter)
            encrypted_message.append(letter)
            print(encrypted_message)
    elif command[0] == "Insert":
        index_value = command[1]
        insert_value = command[2]
        encrypted_message.insert(int(index_value), insert_value)
        # encrypted_message.insert(int(index_value), insert_value)
        # encrypted_message = list(map(lambda x: x.insert(index_value, insert_value), encrypted_message))
        print(encrypted_message)
    elif command[0] == "ChangeAll":
        first_index = command[1]
        second_index = command[2]
        # encrypted_message.replace(first_index, second_index)
        encrypted_message = list(map(lambda x: x.replace(first_index, second_index), encrypted_message))
        print(encrypted_message)
        
        
print(f"The decrypted message is: {encrypted_message}")        
 
 
    