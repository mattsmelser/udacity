# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures.\
Bill is connected to Sam.\
Bill likes to play ."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure
def create_data_structure(string_input):  #this section is complete and returns the list of lists "network[[connections],[likes]]""
    split_input = string_input.split(".")  #splits "string_input" list into two lists, connections and likes, then appends them together
    connections = []                       #into the bigger list "network"
    likes = []
    network = []
    for element in split_input: 

        if element == "":
            continue
        else:
            if "connected" in element:  # checking if connected in the string and appending it to the connections list
                connections.append(element)
            else: #otherwise we are adding it to the likes list
                likes.append(element)
    network.append(connections) #append connections to the network list
    network.append(likes) #append likes to the network list
    #print (connections)
    #print(likes)
    #print(network) #this will print the network
    return network #return the network list so we can use it below

"""connections = {
    "John": ["Debra", "Donald", "Bob"],
    "Bob": ["Wendy", "John", "Tom"]
}

likes = {
    "John": ["Pizza"],
    "Bob": ["Tomatoes"]
}
network = [connections, likes]


def create_data_structure_map(string_input):  #this is Donald's modded section, showing how to create a map of the data
    split_input = string_input.split(".")
    connections = {}
    likes = {}
    network = []
    for element in split_input:
        if element == "":
            continue

        if "connected" in element: #this is another version of the code and searches for keywords and separates based on those
            target, source = element.split(" is connected to ")
            source_list = source.split(",")
            connections[target] = source_list
        else:
            target, source = element.split(" likes to play ")
            source_list = source.split(",")
            likes[target] = source_list

    network.append(connections)
    network.append(likes)
    return network #return the network list so we can use it below"""
# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_user_list(network): #this is a function that loops through the network and pulls off each person that is in the network and puts them into this list.
    user_list = []          #This can be used later to compare if a user is "in network" by comparing if the user is in user_list
    imported_list = network[0]
    while len(user_list) < len(network[0]):
        for element in imported_list: #looping through each string in imported_list
            person, connections_string = element.split(" is connected to ")
            user_list.append(person)
    return user_list


def get_connections(network, user): #This code works as intended.  It returns the connections of the user as ['user'['connection', 'connection']]
    connections = []
    imported_list = network[0]
    person = ""
    connections_string = ""
    cleaned_list = []
    for element in imported_list: #looping through each string in imported_list
        person, connections_string = element.split(" is connected to ") #splitting the strings into names and the connection values
        if person == user: #checking if the name of the person matches the passed in name
            links = connections_string.split(",") #splitting the connections string on the comma to get individual strings
            for connection in links: 
                cleaned_list.append(connection.strip()) #appending the connections to the new list
            connections = [person.strip(), cleaned_list] #stripping of while space to make a clean list
    if cleaned_list == []: #if the user isn't part of the network, return None
        return None
    return connections #return the connections for the user input

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user): #This section is complete and returns the list "likes" as ['person', ['like', 'like']]
    likes = []
    imported_list = network[1]
    person = ""
    likes_string = ""
    cleaned_list = []
    for element in imported_list: #looping through each string in imported_list
        person, likes_string = element.split(" likes to play ") #splitting the strings into names and the likes values
        if person == user: #checking if the name of the person matches the passed in name
            links = likes_string.split(",") #splitting the likes string on the comma to get individual strings
            for like in links: 
                cleaned_list.append(like.strip()) #appending the like to the new list
            likes = [person.strip(), cleaned_list] #stripping of while space to make a clean list
    if cleaned_list == []: #if the user isn't part of the network, return None
        return None
    return likes #return the likes for the user input

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B): #I think this works as intended.  Checks the user_list and then adds the new connection if they are in the list and aren't already connected
    user_list = get_user_list(network) #making the user list to be able to check if user_A and user_B are part of the network later
    imported_list = network[0] #bringing in the connections part of the network
    person = ""
    connections_string = imported_list[1]
    cleaned_list = []
    if user_A not in user_list: #this if/else statement returns False if either user_A or user_B aren't in the network
        return False
    else:
        if user_B not in user_list:
            return False
    for idx, element in enumerate(imported_list): #looping through each string in imported_list and keeping count as we go
        person, connections_string = element.split(" is connected to ") #splitting the strings into names and the connection values
        for element in imported_list:
            if person == user_A: #checking if the name of the person matches the passed in name
                if user_B in connections_string: #if they already have a connection, return the network unchanged
                    return network
                else: #if they aren't connected
                    connections_string = imported_list[idx] + ", " + user_B #creating a string and adding the new user on to the end
                    imported_list[idx] = connections_string #replacing the string at the specific location with our new string that has the new connection
    if cleaned_list == []: #if the user isn't part of the network, return None #I don't think we ever hit this case, but I'm leaving it in just in case
        return None
    return network

"""def add_connection_map(network, user_A, user_B):
    connections = network[0]

    if user_A in connections:
        user_connections = connections[user_A]
        if user_B not in user_connections:
            user_connections.append(user_B)
            return network
    else: 
        return False"""



# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games): ##I think this section is complete.  It seems to work correctly for all the cases provided and updates the network with the new user
    user_list = get_user_list(network) #creating a list of users in the network to check if the user is already part of the network
    games_liked = network[1] #getting the original games_liked list
    connections = network[0] #getting the original connections list
    if user in user_list: #if the user is part of the network already, return the network unchanged
        return network
    else: #if the user isn't part of the network, we are going to add them to the network
        new_connections_string = user + " is connected to " # making the new user and the string "is connected to" into one useful string
        games_string = ', '.join(games) #making the games list into a string separated by commas
        new_games_liked = user + " likes to play " + games_string #adding the user and games together into one string
        connections.append(new_connections_string) #appending the new user into the connections list
        games_liked.append(new_games_liked) # appending the new user's likes to the games list
        #print (connections, games_liked)
        network[0] = connections
        network[1] = games_liked
        return connections, games_liked, network #returning the new lists
        #print("they're not in the network") #this is the part I'm on right now.  Trying to figure out how to add the new user, I have the base case finished.
        #return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user): #this section is complete and follows the specifications from the class
    user_list = get_user_list(network) #bringing in the user_list again, to check if the passed in user is part of the network
    primary_connections_list = get_connections(network, user) #bringing in the connections of the passed in user
    secondary_connections_list = [] #initialize the final list as an empty list to being
    if user not in user_list: #if the passed in user is not part of the network, return None
        return None
    else: #if the passed in user is part of the network, continue below
        for element in primary_connections_list[1]: #this takes the connections of the user
            secondary_connections = get_connections(network, element) #this gets the connections of the connections to the user
            for connection in secondary_connections[1]: # looping through the second level connections
                if connection not in secondary_connections_list: #if the second level connection isn't in our final list, add it below
                    secondary_connections_list.append(connection)
                else: #if the second level connection is a part of the final list, do nothing
                    continue
    return secondary_connections_list

# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B): #this section is now complete and uses sets to count the number of commonalities
    user_list = get_user_list(network) #getting the list of users in the network to check if the passed in users are a part of the network
    user_A_connections = get_connections(network, user_A) # getting the connections of the first user
    user_B_connections = get_connections(network, user_B) # getting the connections of the second user
    counter = 0 #initializing the counter to zero
    if user_A not in user_list or user_B not in user_list: # if the users aren't part of the network, return False
        return False
    counter = len(set(user_A_connections[1]).intersection(user_B_connections[1])) #comparing the connections of user_A and user_B as sets, and then finding the length of that new set
    return int(counter) #returning the number as an int

# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
path = []
viewed_people = []
def find_path_to_friend(network, user_A, user_B):
    user_list = get_user_list(network)
    user_A_connections = get_connections(network, user_A)
    if user_A not in user_list or user_B not in user_list:
        return None
    else:
        path.append(user_A)
        if user_B in user_A_connections[1]:
            path.append(user_B)
            return path
        else:
            for element in user_A_connections[1]:
                if element not in viewed_people:
                    viewed_people.append(element)
                    find_path_to_friend(network, element, user_B)
                    return path
                else:
                    continue

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

"""def pretty_print_network(network):
    connections = network[0]
    likes = network[1]

    connections_output = []
    likes_output = []
    for key in connections:
        str = ", ".join(connections[key])
        connections_output.append("" + key + " is connected to " + str)

    for key in likes:
        str = ", ".join(likes[key])
        likes_output.append("" + key + " likes to play " + str)

    print([connections_output, likes_output])"""

net = (create_data_structure(example_input))
# print (net)                                                                           #done
#print (get_connections(net, "John"))                                                   #done
#print (get_connections(net, "Mercedes"))                                               #done
#print (get_connections(net, "Olive"))                                                  #done
#print (get_games_liked(net, "Sam"))                                                    #done
#print (get_games_liked(net, "Bill"))                                                   #done
#print (get_games_liked(net, "John"))                                                   #done
#print(add_connection(net, "John", "Freda"))                                            #done
#print(add_connection(net, "John", "Debra"))                                            #done
#print(get_user_list(net))                                                              #done
#print (add_new_user(net, "Debra", []))                                                 #done
#print (add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"])) # True    #done
#print (get_secondary_connections(net, "Mercedes"))                                     #done
#print (count_common_connections(net, "Mercedes", "John"))                              #done
print (find_path_to_friend(net, "John", "Ollie"))                                      #working on this

