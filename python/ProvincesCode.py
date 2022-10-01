from datetime import date
if __name__ == "__main__":
    with open(f"{date.today()}.txt", "w") as f:
        while True:
            provinceID = input("\nProvince ID:\t")
            provinceName = input("Province Name:\t")
            
            #prov_names_l_english
            f.write(f' PROV{provinceID}:0 "{provinceName}"\n')
            f.write(f' PROV{provinceID}_desc:0 "{provinceName}"\n')
            try:
                with open(f"history\provinces\{provinceID} - UNNAMED.txt", "r+") as historyF:
                   strID = historyF.read()
                   strID = strID.replace('capital = "UNNAMED"',f'capital = "{provinceName}"')
                   strID = strID.replace('capital = "Unnamed"',f'capital = "{provinceName}"')
                   strID = strID.replace('capital = "unnamed"',f'capital = "{provinceName}"')
                with open(f"history\provinces\{provinceID} - UNNAMED.txt", "w") as historyF:
                   historyF.write(strID) #replace city name
            except IOError:
                print("error making history file")