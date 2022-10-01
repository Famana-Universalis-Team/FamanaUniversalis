import os
if __name__ == "__main__":
    
    for filename in os.listdir("common"):
       with open(os.path.join("common", filename), 'r') as f:
       text = f.read()
       text = text.replace("East_Emastalian","Maxan_East_Emastalian")
       text = text.replace("West_Emastalian","Maxan_West_Emastalian")
       f.write(text)