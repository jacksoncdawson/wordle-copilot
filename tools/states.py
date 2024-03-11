import json

def get_states():
  states = []
  settings = ["x", "y", "g"]

  for i in range(3):
    for j in range(3):
      for k in range(3):
        for l in range(3):
          for m in range(3):
            states.append(settings[i] + settings[j] + settings[k] + settings[l] + settings[m])
  return states

if __name__ == "__main__":

  json.dump(get_states(), open("states.json", "w"))