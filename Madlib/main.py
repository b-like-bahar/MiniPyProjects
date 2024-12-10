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
