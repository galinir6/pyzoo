import json

def save_list(data_file , animals):
    json_string = json.dumps(animals)
    with open(data_file, 'w') as file:
      file.write(json_string)

def load_list(data_file , animals):
   try:
      with open(data_file, 'r') as file:
         json_string = file.read()
         animals = json.loads(json_string)
         return animals
   except: pass