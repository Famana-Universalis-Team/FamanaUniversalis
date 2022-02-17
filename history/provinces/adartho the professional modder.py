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
      data = data.replace("center_of_trade = 1","")
    with open(filename, 'w', encoding="iso8859-1") as f:
      f.write(data)

if __name__ == "__main__":
  main()
