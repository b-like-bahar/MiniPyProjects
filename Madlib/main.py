import SampleMadlibs as sm

def get_user_inputs(temp):
    # Extract placeholders in the correct order
    placeholders = []
    clean_word=''
    for word in temp.split():

        if word.startswith("{") or word.endswith("}.") or word.endswith("},"):
            clean_word = word.strip("{}.,")
            placeholders.append(clean_word)

    inputs = {}
    for placeholder in placeholders:
        user_input = input(f"Please enter {placeholder.replace('_', ' ')}: ")
        inputs[placeholder]= user_input
    return inputs

def main():
    while True:
        print("There are 5 mad libs in this list :")
        print("1. The Adventure")
        print("2. The Party")
        print("3. The Mystery")
        print("4. The Superhero Story")
        print("5. The Robot")
        choice = input("Please choose a madlib by its number(1, 2, 3, 4, or 5: ")
        if choice == "1":
            template = sm.adventure()
            break
        elif choice == "2":
            template = sm.party()
            break
        elif choice == "3":
            template = sm.mystery()
            break
        elif choice == "4":
            template = sm.superhero_story()
            break
        elif choice == "5":
            template = sm.robot()
            break
        else:
            print("Invalid option, Try again.")
            continue
    user_inputs=get_user_inputs(template)
    print(f"Here is your madlib:\n{template.format(**user_inputs)}")

if __name__ == "__main__":
    main()