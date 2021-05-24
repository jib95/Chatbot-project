def emergency(): #create function

  emergencytype = input() #take input from user

  if emergencytype == "emergency":

    run()

    emergency() #start function

    print("please dial 911 or 112 on your phone immediately")

    print("who is experiencing an issue?")

    who = input() #find out if it's the user experiencing an emergency or someone else

    if who == "me": #following code will be executed if condition returns true

      print("take deep breaths and remain calm") #outputs text to the user giving advice

      print("if possible, dial 911 or 112 on your phone") #outputs text to the user displaying emergency services number

    if who == "someone else": #following lines of code will be executed if statement returns true

      print("what is the emergency?") #output question to user

      problem = input() #take input from user

      if problem == "heart attack": #if condition returns true exexute the following lines of code

        print("have the person chew and swallow and aspirin. MAKE SURE THEY DONT SWALLOW IT WHOLE") #output message to the user

        print("give the person CPR.")

      elif problem == "stroke": #if condition returns true execute the following lines of code

        print("don't let them fall asleep!!") #output messages to the user

        print("don't give them anything to eat, drink or consume.")

        print("look for a seizure identity card if possible. It may contain advice on what to do in this situation")

      else:

        print("sorry, that emergency is not registered with me") #Output error message if none of the above conditions return true

    else:

      print("please enter (me) or (someone else)") #directs the user incase they enter they wrong input

        

import requests #import module



res = requests.get('https://ipinfo.io/') #request url to get users location

data = res.json() #convert format of data so its easier to extract



city = data['city'] #extract users city from location details

print("You are currently in" + city) #tell user what city they are in
  


  Vitamin grabber function

	def vitamin_grabber():

    global ingredients

    print("Please enter the vitamin/mineral you're deficient in") #output to user asking them to enter a vitamin

    vitamin = input().capitalize() #take input from user

    if vitamin == "Q": #if condition returns true execute following code

        run() 

        vitamin_grabber() #start function

    vitamin = str(vitamin) #for some reason despite 'input()' function storing strings,  this is the only way it could be evaluated with the data from the database



    query = "SELECT vitamin, food from Vitamins where vitamin = ?" #look up vitamin in database

    c.execute(query, [vitamin])

    records = c.fetchall()



    if records == []: #if condition returns true execute following lines of code

        print("I'm sorry, that vitamin or mineral is not listed. \n Try again!") #if the user enters something that is not listen the sentence will be outputted

        vitamin_grabber()

    else:

        for row in records:

            print("A good food to increase your intake of " + row[0]) #output food user including vitamin mention

            print("is by having more ", row[1]) #output food

##            return_value = subscriptionSPKey.get_food_information(row[1])

##            information = return_value.json()

##            print(information) ## make sure it only brings information on the food

            print()

