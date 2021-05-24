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
