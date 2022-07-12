import os
if __name__ == "__main__":
    
    for filename in os.listdir("common"):
       with open(os.path.join("common", filename), 'r') as f:
       text = f.read()
       text = text.replace("East_Emastalian","East_Maxan")
       text = text.replace("West_Emastalian","West_Maxan")
       f.write(text)