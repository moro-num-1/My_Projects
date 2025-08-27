als_num = int(input("How many alias do u want?: "))
als = []
for al_num in range(als_num):
    al_num += 1
    als_name = input(f"Enter the name of alias number {al_num}: ")
    als.append(f"alias {als_name}='google-chrome --new-window --app=https://www.{als_name}.com'")
print("Here are your alias:-")
print("-------------------\n")
counter = 0
for al in als:
    counter += 1
    print(f"{counter}- {al}")