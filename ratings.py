"""Restaurant rating lister."""


# put your code here
#declare function
def restaurant_ratings(filename):

#open the file
    the_file = open(filename)

# add new dictionary
    ratings = {}

#for loop to split the words and add to dictionary
    for line in the_file:
        line = line.rstrip()
        words = line.split(":")

        # print(words)

        # restaurant = words[0]
        # rating = words[1]
        ratings[words[0]] = words[1]

        print(ratings)
        
        # sorted(ratings)


        #for restaurant, rating in ratings.items():
            #print(f' {restaurant} is rated at {rating}.')

    return ratings

#sorted()

#close file
    the_file.close()
#call the function
ratings = restaurant_ratings("scores.txt")
