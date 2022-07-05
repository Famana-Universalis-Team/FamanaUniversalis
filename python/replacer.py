with open("NameListMaxan.txt", "r+") as f:
    stringe = f.read()
with open("NameListMaxan.txt", "w") as f:
    stringe = stringe.replace("Ğ", "H")
    stringe = stringe.replace("ğ", "h")
    stringe = stringe.replace("r", "w")
    stringe = stringe.replace("R", "W")
    stringe = stringe.replace("y", "ë")
    stringe = stringe.replace("Y", "Ë")
    f.write(stringe)