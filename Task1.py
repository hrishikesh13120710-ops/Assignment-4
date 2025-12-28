try:
    with open("sample.txt","rt") as file:
        line1=file.readline()
        line2=file.readline()
        print(f"Line 1: {line1}")
        print(f"Line 2: {line2}")
except FileNotFoundError:
    print("Error: The \'sample.txt\' was not found.")