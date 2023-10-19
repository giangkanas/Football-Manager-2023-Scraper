import requests
from bs4 import BeautifulSoup

def getPlayerBasicInfo(url):
    
    response = requests.get(url)
    html_document = response.text         
    soup = BeautifulSoup(html_document , 'html.parser')
    
    player_basic_info = soup.find(attrs={"id":"player_info"})
    
    return player_basic_info

def getPlayerAttributes(player_basic_info):
    player_stats = player_basic_info.find(attrs = {"id":"player_stats"})

    attributes = player_stats.find_all("tr")
    player_attributes = {}
    for i in attributes:
        attribute = i.get_text().strip()
        key_value = attribute.split("\n")
        player_attributes[key_value[0]] = key_value[1]
    return player_attributes

def getMainInfo(player_basic_info):
    main_info = player_basic_info.find(attrs = {"class":"title"})
    basic_info = {}
    ability = {}
    ability["Current"] = main_info.find(attrs = {"id":"ability"}).get_text()
    ability["Potential"] = main_info.find(attrs = {"id":"potential"}).get_text()
    basic_info["Ability"] = ability
    
    extra_info = []
    for i in main_info.find_all(attrs = { "class": "value" }):
        extra_info.append(i.get_text().strip())
    
    try:
        basic_info["Club"] = extra_info[0]
        basic_info["Nationality"] = extra_info[1]
    except:
        basic_info["Club"] = ""
        basic_info["Nationality"] = extra_info[0]
        
    columns = player_basic_info.find_all(attrs = {"class":"column"})
    for index,column in enumerate(columns):
        field = column.find("h2").get_text()
        keys = column.find_all(attrs = {"class":"key"})
        values = column.find_all(attrs = {"class":"value"})
        
        if field == "Player info":  
            for i in range(len(keys)):
                key = keys[i].get_text().strip()
                value = values[i].get_text().strip()
                basic_info[key] = value
        else:
            column_info = {}
            keys = column.find_all(attrs = {"class":"key"})
            values = column.find_all(attrs = {"class":"value"})
            
            for i in range(len(keys)):
                key = keys[i].get_text().strip()
                value = values[i].get_text().strip()
                column_info[key] = value
            basic_info[field] = column_info
            column_info = {}
            if field=="Best roles (suitable) ":break
        
    """ Some final changes """
    basic_info["Position"] = player_basic_info.find("span",{"class" : "desktop_positions"}).get_text().split(", ")
    # basic_info.pop("Unique ID")
    return basic_info


def getPlayerPage(url):
    player_basic_info = getPlayerBasicInfo(url)
    player_attributes = getPlayerAttributes(player_basic_info)
    basic_info = getMainInfo(player_basic_info)
    basic_info["Attributes"] = player_attributes
    return basic_info

# urls = list(pd.read_csv("player_links.csv",header=None)[0])
# url = urls[0]
# basic_info = getPlayerPage(url)

# """ TEST """
# urls = ["https://fminside.net/players/3-fm-23/29179241-erling-haaland",
#         "https://fminside.net/players/3-fm-23/14000745-mateo-musacchio",
#         "https://fminside.net/players/3-fm-23/19000030-renan-ribeiro",
#         "https://fminside.net/players/3-fm-23/18026122-thibaut-courtois"]

# dataset = []
# for url in urls:
#     dataset.append(getPlayerPage(url))
#     print(url)




  

    




    
 
    
    
    