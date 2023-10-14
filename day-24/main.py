# with open("my_text.txt") as file:
#     content = file.read()
#     print(content)

with open("names.txt", "r") as file:
    names = file.readlines()
    for name in names:
        with open(f"list_do_{name}.txt", "w") as msg:
            with open("my_text.txt", "r")as txt:
                lines = txt.readlines()
                for line in lines:
                    tekst = line
                    if "[name]" in tekst:
                        tekst = tekst.replace("[name]", name)
                        tekst = tekst.rstrip()
                        tekst = tekst + "\n"
                        print(tekst)
                    msg.write(tekst)
    
