
import os

def main():
  for filename in os.listdir(os.getcwd()):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
      data = f.read
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
    with open(os.path.join(os.getcwd(), filename), 'w') as f:
      f.write(data)

if __name__ == __main__:
  main()
