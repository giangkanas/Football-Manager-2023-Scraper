# Web-Scarpping

In this project I apply web scrapping to https://fminside.net to create a dataset for FM23.

Initially, with get_player_links module, I get the url links for the best 50.000 players and save them to a csv file.

With, get_player_page module, I get the player's data (given his player's url) in a json format.

Finally, with fmScrapper module, I run repeatedly getPlayerPage function from get_player_page module, to create the final dataset.
