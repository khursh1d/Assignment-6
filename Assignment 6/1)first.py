def convert_file_to_uppercase(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.upper(), end='')
    except FileNotFoundError:
        print("Error: Input file does not exist.")

# Test the function
file_name = input("Enter a file name : ")
convert_file_to_uppercase(file_name)