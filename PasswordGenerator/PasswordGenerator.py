import random
from pathlib import Path

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=?><,."

all_chars = lower + upper + numbers + symbols
length = int(input("Enter a length : "))

password = ''.join(random.sample(all_chars,length))
print("Generated Password: ", password)

#save to file and if file exist made a new file
i = 1
while True:
    file_path = Path("Generated Password" + str(i) + ".txt")
    if file_path.is_file():
        i += 1
    else:
        with open("Generated Password" + str(i) + ".txt", "w", encoding="utf-8") as file:
            file.write(password)
            print("Save to File :" + "Generated Password" + str(i) + ".txt")
        break;
