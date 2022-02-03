import lib


numbers = "numbers.csv"
counter = 0

lib.fw(numbers, "")
while counter != 10:
    usr_num = input("Write a number: ")
    lib.fa(numbers, f"{usr_num}, ")
    data = lib.fr(numbers)
    num_list = data.split(", ")
    counter += 1
print(num_list)