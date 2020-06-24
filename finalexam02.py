import math

class Point:

    def __init__(self, x = 0, y = 0):
        self.__x_location = x
        self.__y_location = y

    def get_x_location(self,):
        return self.__x_location

    def get_y_location(self,):
        return self.__y_location

    def point_to_point_distance(self, point_2):

        x = (self.__x_location - point_2.get_x_location()) ** 2
        y = (self.__y_location - point_2.get_y_location()) ** 2
        distance = math.sqrt(x + y)

        return distance

    def __add__(self, point_2):
        x = self.__x_location + point_2.get_x_location()
        y = self.__y_location + point_2.get_y_location()
        return x, y


p1 = Point(1,1)
p2 = Point(2,2)

print(p1.point_to_point_distance(p2))
print(p1 + p2)

