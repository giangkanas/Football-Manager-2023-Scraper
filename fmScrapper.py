import get_player_page
import pandas as pd
from time import sleep
import random
import json

def startScrapping(first,last):
    links = list(pd.read_csv("player_links.csv",delimiter=" ",header=None)[0])

    try:
        with open('FM23_dataset.json', 'r',encoding='utf-8') as openfile:
            # Reading from json file
            dataset = json.load(openfile,ensure_ascii=False) 
    except:
        dataset = {}

    for i in range(first,last):
        
        player_data = get_player_page.getPlayerPage(links[i])
        name = player_data["Name"]
        player_data.pop("Name")
        dataset[name] = player_data 
        
        with open('FM23_dataset.json', 'w',encoding='utf-8') as openfile:
            # Reading from json file
            json.dump(dataset,openfile,indent=4,ensure_ascii=False)
        print(i,links[i])
        # sleep(random.randint(1,5))
    return dataset
        

dataset = startScrapping(0,5000)


        
        
       
        
        
        
        
        
        
        