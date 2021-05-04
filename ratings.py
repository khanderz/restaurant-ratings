"""Restaurant rating lister."""


# put your code here
#declare function
def restaurant_ratings(filename):
    """read ratings file and add to dictionary"""

#open the file
    the_file = open(filename)

# add new dictionary
    ratings = {}

#for loop to split the words and add to dictionary
    for line in the_file:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        ratings[restaurant] = int(rating)

    return ratings
    print(ratings)

#close file
    the_file.close()


def print_sorted_ratings(ratings):
    """print sorted restaurant and ratings"""
    for restaurant, rating in sorted(ratings.items()):
        print(f' {restaurant} is rated at {rating}.')



#call the function
ratings = restaurant_ratings("scores.txt")

print_sorted_ratings(ratings)
