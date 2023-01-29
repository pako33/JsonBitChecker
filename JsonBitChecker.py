import json
import os

folder_path = "C:\\" #path to folder with jsons
key_path = input("Enter the JSON path for 'Key': ").strip()
print("key_path: ",key_path)
subkey_path = input("Enter the JSON path for 'Subkey': ").strip()
print("subkey_path: ",subkey_path)
while True:
    bits_to_extract = input("Enter the bits you want to extract (comma separated): ") #Ask user which bits they want to extract
    if bits_to_extract.isnumeric():
        bits_to_extract = [int(bits_to_extract)] 
    else:
        bits_to_extract = [int(bit) for bit in bits_to_extract.split(",")] #add to a list
    files_with_bits = set() #initialise empty set for later use
    for file_name in os.listdir(folder_path): #handling the jsons
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                data = json.load(file)
                accu_list = data["key"].get(key_path, {}).get(subkey_path, None) #find the path to desired values, specify first key in "key"
                if accu_list is not None: #if not empty then perform bit operations to find out if specified bits are enabled
                    if isinstance(accu_list, int): #if variable does not contain a list
                        accu = accu_list
                        extracted_bits = []
                        for bit in bits_to_extract:
                            extracted_bits.append((accu >> bit) & 1)
                        if all(bit == 1 for bit in extracted_bits):
                            files_with_bits.add(file_name) #if apparent add filename to a list
                    else:
                        for accu in accu_list: #if variable does contain a list
                            extracted_bits = []
                            for bit in bits_to_extract:
                                extracted_bits.append((accu >> bit) & 1)
                            if all(bit == 1 for bit in extracted_bits):
                                files_with_bits.add(file_name) #if apparent add filename to a list
    print(files_with_bits) #print the jsons with the specified variables that have the specified bits enabled
    redo = input("Retry/Quit/Change Path? (Y/Q/C): ") #Redo based on inputs
    if redo.lower() == "c":
        key_path = input("Enter the JSON path for 'Key': ").strip()
        subkey_path = input("Enter the JSON path for 'Subkey': ").strip()
    elif redo.lower() != "y":
        break
