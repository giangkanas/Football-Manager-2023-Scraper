import get_player_page
import pandas as pd
import json


def startScrapping(first,last):
    links = links = list(pd.read_csv("player_links.csv",delimiter=" ",header=None)[0])
    try:
        with open('FM23_dataset.json', 'r',encoding='utf-8') as openfile:
            # Reading from json file
            dataset = json.load(openfile) 
    except:
        dataset = {}

    for i in range(first,last):
        
        try:
            player_data = get_player_page.getPlayerPage(links[i])
            urlIndex = i
            dataset[urlIndex] = player_data 
            print(i,player_data["Name"])
            if (i+1)%250==0:
                with open('FM23_dataset.json', 'w',encoding='utf-8') as openfile:
                    # Writing to json file
                    json.dump(dataset,openfile,indent=4,ensure_ascii=False)
                    print("=========================>CHECKPOINT: {} ENTRIES ARE SAVED".format(len(dataset)))
           
        except:
            print("\n",i,"\n")
            continue
        
        
    with open('FM23_dataset.json', 'w',encoding='utf-8') as openfile:
        # Writing to json file
        json.dump(dataset,openfile,indent=4,ensure_ascii=False)
    return dataset



dataset = startScrapping(0,49934)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        