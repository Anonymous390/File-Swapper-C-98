def swap(file1, file2):
    with open(file1) as f:
        data1 = f.read()

    with open(file2) as f:
        data2 = f.read()

    with open(file1, 'w') as f:
        f.write(data2)

    with open(file2, 'w') as f:
        f.write(data1)

file1 = input("Enter the first file path: ")
file2 = input("Enter the second file path: ")
swap(file1, file2)
print("Completed!")