import json
import glob

blocks = {}
with open('/mnt/c/Users/cerbu/OneDrive/Escritorio/MinecraftRawCounter/Minecraft_archives/en_us.json','r') as file:
    minecraft_data = json.load(file)
    blocks = {key: value for key,value in minecraft_data.items() if (key.startswith('block.minecraft') or key.startswith('item.minecraft'))}

with open('/mnt/c/Users/cerbu/OneDrive/Escritorio/MinecraftRawCounter/Minecraft_archives/minecraft_items.json','w') as saved:
    json.dump(blocks, saved, ensure_ascii=False, indent=2)

minecraft_recipe_list = glob.glob("./Minecraft_archives/recipe/*.json")
for minecraft_recipe in minecraft_recipe_list:
    with open(minecraft_recipe, "r") as f:
        recipe_data = json.load(f)
        result_dict = {} # "items": (item,amount), "item_result": amount 
        
        if recipe_data["type"] == "minecraft:crafting_shaped":
            key_counts = {}
            
            # Extract the keys symbols and it's repeatence
            for row in recipe_data["pattern"]:
                    for symbol in row:
                        if symbol != " ":
                            key_counts[symbol] = key_counts.get(symbol,0)+1

            # translating the key into the item ID
            for key_symbol, item_id in recipe_data["key"].items():
                count = key_counts.get(key_symbol, 0)
                if count > 0:
                    result_dict["items"][item_id] = result_dict["items"].get(item_id, 0) + count
                    
            result_id = recipe_data["result"]["id"]
            result_count = recipe_data["result"].get("count", 1)
            result_dict["result"] = (result_id, result_count)
        else:
            continue
        
    
        


