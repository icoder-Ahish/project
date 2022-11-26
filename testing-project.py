names = []
phone_numbers = []
label = []

# Take a user Input  
num = int(input("How many contact  do you want to add:"))

for i in range(num):
    name1 = input("Name: ")
    phone_number1 =  int(input("Phone Number: "))
    print("Give Some Label to this Number") 
    label1 = input("Label: ") 

    label.append(label1)
    names.append(name1)
    phone_numbers.append(phone_number1)
    
    PN = str(phone_number1)
    f = open("contact.txt","a")
    f.write("Name: " + name1 +"\t\t Phone_number: " + PN +  "\t\tlabel:" + label1 + "\n\n")
    # print(f.read())
    f.close()

print("Do You Wish To Print Your Contact list:- ")

var1 = input("Type 'Yes' or 'No'")

if var1 == 'yes':
    print("\nName\t\tPhone Number\t\tLabel")

    for i in range(num):
        print(names[i], "\t\t", phone_numbers[i], "\t\t",label[i])

       
else:
    print("I think You don't Want To Print Your Contact List\n")


print("Do You Want To search Your Contact \n")

var2 = input("Type 'Yes' or 'No'")

if var2 == 'yes':

    search_term = input("\nEnter search term: ")
    print("Search result:")

    if search_term in names:
            index = names.index(search_term)
            phone_number = phone_numbers[index]
            print("Name:",search_term , "Phone Number:",phone_number)


    else:
            print("Name Not Found")

else:
    print("Thanku.......")        