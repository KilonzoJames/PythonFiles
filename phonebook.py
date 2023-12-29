import csv

# file = open("phonebook.csv", "a")

# name = input("Name: ")
# number = input("Number: ")

# writer = csv.writer(file)
# writer.writerow([name, number])

# file.close()

with open("phonebook.csv", "a") as file:

    name = input("Name: ")
    number = input("Number: ")

    writer = csv.DictWriter(file, fieldnames=["name","number"])

    # Check if the file is empty and write header if needed
    if file.tell() == 0:
        writer.writeheader()
    writer.writerow({"name" : name, "number" : number})

