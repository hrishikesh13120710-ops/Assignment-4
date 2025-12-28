file=open("output.txt",'wt')
n=str(input("Enter text to write to the file: "))
file.write(n + "\n")

print("Data successfully written to output.txt.")
file.close()



file=open("output.txt",'at')
m=str(input("Enter additional text to append: "))
file.write(m + "\n")
print("Data successfully appended.")
file.close()

file=open("output.txt",'rt')

print("Final content of output.txt: ",file.read())
file.close()