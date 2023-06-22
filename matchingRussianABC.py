from colorama import init, Fore, Style

def highlight_russian_letters(text):
    russian_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    found_letters = set(text.lower())
    highlighted_text = ""

    for char in russian_letters:
        if char in found_letters:
            highlighted_text += f"{Fore.GREEN}{char.upper()}{Style.RESET_ALL}|"
        else:
            highlighted_text += f"{Fore.RED}{char.upper()}{Style.RESET_ALL}|"

    return highlighted_text[:-1]

init()

user_input = input("Enter text: ")

highlighted_letters = highlight_russian_letters(user_input)

print("Result:")
print(highlighted_letters)
