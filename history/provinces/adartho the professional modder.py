import glob, os

def main():
  os.chdir(os.getcwd())
  for filename in glob.glob("*.txt"):
    with open(filename, 'r', encoding="iso8859-1") as f:
      data = f.read()
      data = data.replace("discovered_by = eastern","")
      data = data.replace("discovered_by = ottoman","")
      data = data.replace("discovered_by = muslim","")
      data = data.replace("discovered_by = indian","")
      data = data.replace("discovered_by = chinese","")
      data = data.replace("discovered_by = east_african","")
      data = data.replace("discovered_by = central_african","")
      data = data.replace("discovered_by = nomad_group","")
      data = data.replace("discovered_by = sub_saharan","")
      data = data.replace("discovered_by = western","")
      data = data.replace("discovered_by = andean","")
      data = data.replace("discovered_by = south_american","")
      data = data.replace("discovered_by = north_american","")
      data = data.replace("discovered_by = mesoamerican","")
      data = data.replace("trade_goods = \n","")
      data = data.replace("culture = \n","culture = Placeholder_culture\n")
      data = data.replace("religion = \n","religion = animism\n")
      data = data.replace("add_core = \n","")
      data = data.replace("owner = \n","")
      data = data.replace("controller = \n","")
      data = data.replace("native_size = \n","")
      data = data.replace("native_ferocity = \n","")
      data = data.replace("native_hostileness = \n","")
    with open(filename, 'w', encoding="iso8859-1") as f:
      f.write(data)

if __name__ == "__main__":
  main()
