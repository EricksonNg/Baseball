import statsapi

def dynamic_add():

  players=['Donovan Solano','Chris Shaw','Mauricio Dubon','Alex Dickerson','Mike Yastrzemski','Evan Longoria','Brandon Crawford','Buster Posey','Aramis Garcia','Austin Slater','Brandon Belt','Pablo Sandoval','Joey Rickard','Jaylin Davis','Hunter Pence','Wilmer Flores']

  for i in range(len(players)):
    
    playername = players[i]

    with open("sfhitters.txt", "r") as FILE:
      content = FILE.read()
      try:
        content_dict = eval(content)[playername]['2020']
      except Exception as e:
        print( "we got an error ", e )
      player_id = eval(content)[playername]['ID']

    with open("2020/"+str(playername)+".txt", "w") as f:
      try:
        f.write("{'"+playername+"': {'ID': "+player_id+", '2020': "+str(content_dict)+"}}")
        print("Write Success")
      except Exception as e:
        print( "we got an error ", e )  