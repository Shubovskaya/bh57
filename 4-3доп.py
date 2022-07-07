n = int(input("Введите число: "))
d = {key:{"name":input("name: "), "email":input("email: ")} for key in range(n)}
print(d)