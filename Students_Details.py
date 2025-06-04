 
data=(
        "Rahim,85"
        "\nKarim,67"
        "\nAnika,45"
        "\nSumaiya,92"
        "\nJamal,39"
        "\nFarzana,76"
        "\nTamim,55"
        "\nSadia,30"
        "\nNasir,49"
        "\nMeherin,99"
    )
    
with open("student.txt", "r+") as student:
    student.seek(0)
    if data in student.read():
        print("Already exists.")
    else:
        student.write(data)


with open("student.txt","r") as student:
    lines=student.readlines()

name_list=[]
mark_list=[]

for line in lines:
    current_name=""
    current_mark=""
    i=0
    while i<len(line):
        if line[i] !="," and line[i]!="\n":
            current_name+=line[i]
            i+=1
        else:
            i+=1
            while i<len(line) and "0"<=line[i]<="9":
                current_mark+=line[i]
                i+=1
            break

    name_list.append(current_name.strip())
    mark_list.append(int(current_mark.strip()))

print(name_list)
print(mark_list)

student_info=dict(zip(name_list,mark_list))
print(student_info)


usr_input=input("Please type a name to see details or 'Exit' to exit: ").lower()

#without flag it will only check 1st name and break the loop without check the whole hashmap
found=False
for name, mark in student_info.items():
    if usr_input==name.lower():
        print(f"Mark of {name} is {mark}")
        found=True
        break
if not found and usr_input != "exit":
    print(f"There is no such name called {usr_input}")
    new_name=input(f"\nIf want to save details of {usr_input} into file type 'continue': ").lower()
    if new_name == 'continue'.lower():
        new_mark=input(f"Enter mark for {usr_input}: ")
        student_info[usr_input]=new_mark
        with open("student.txt","a") as student:
            student.write(f"\n{usr_input},{new_mark}")
            print("Succesfully Added.")
    else:
        print("Invalid Input.")


        
