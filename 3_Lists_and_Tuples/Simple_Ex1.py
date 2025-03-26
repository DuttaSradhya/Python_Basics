# WAP to ask the user to enter names of their 3 favorite movies and store them in a list
movie1=input("Enter any your first favorite movie : ")
movie2=input("Enter any your second favorite movie : ")
movie3=input("Enter any your third favorite movie : ")
movielist=[movie1, movie2, movie3]
print("Your all favorite movies are : ", movielist)

# other way
movies = []
mov=input("Enter any your first favorite movie : ")
movies.append(mov)
mov=input("Enter any your second favorite movie : ")
movies.append(mov)
mov=input("Enter any your third favorite movie : ")
movies.append(mov)
print(movies)

# other way
movies = []
movies.append(input("Enter any your first favorite movie : "))
movies.append(("Enter any your second favorite movie : "))
movies.append(("Enter any your third favorite movie : "))
print(movies)



