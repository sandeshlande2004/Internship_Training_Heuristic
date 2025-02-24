print("Nested If-else loop") #if ke andar aur ek if aur aise chalne do (ek ke andar aur ek phir ek, phir ek and so on)

gender = input("Enter your gender: ")
age = int(input("Enter your age: "))

if age <= 0:
    print("Invalid age")
elif age <= 18:
    if gender == "Male":
        print("You are a young male")
    else:
        print("You are a young female")
elif age <= 60:
    if gender == "Male":
        print("You are a male")
    else:
        print("You are a female")
elif age > 60:
    if gender == "Male":
        print("You are an old male")
    else:
        print("You are an old female")