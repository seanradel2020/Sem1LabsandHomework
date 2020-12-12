#HW1c
#Author: Sean Radel
#September 16, 2020
#Section 1004
#Sean.Radel@maine.edu
#Kemba walkers average points

points1 = int(input("How many points did Kemba Walker score in game 1?"))
total_points = points1
points2 = int(input("How many points did Kemba Walker score in game 2?"))
total_points = total_points + points2
points3 = int(input("How many points did Kemba Walker score in game 3?"))
total_points = total_points + points3
points4 = int(input("How many points did Kemba Walker score in game 4?"))
total_points = total_points + points4
points5 = int(input("How many points did Kemba Walker score in game 5?"))
total_points = total_points + points5
points6 = int(input("How many points did Kemba Walker score in game 6?"))
total_points = total_points + points6
points7 = int(input("How many points did Kemba Walker score in game 7?"))
total_points = total_points + points7
avgPoints = total_points / 7
print("Kemba Walker scored in total:", total_points, "and an average of",
avgPoints, "points per game. Wow!")
