import pyperclip

code_input = pyperclip.paste()
replace = input("Input what you want to replace: ")
replacement = input("Input what you want to replace it with: ")

replaced_code = code_input.replace(replace, replacement)
pyperclip.copy(replaced_code)