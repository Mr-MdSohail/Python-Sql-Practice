import json
path = "practice/json/player.json"
with open(path,"r") as file:
    player_data = json.load(file)
print(player_data)
print("Welcome back your level is ", player_data['level'])
player_data['level']+=1
print("LEVEL UP!!")
print("Now youre on level",player_data['level'])
# saving the data in the json file
with open(path,"w") as file:
    json.dump(player_data,file)
    