def Task1():
    import pdb
    a = 5
    pdb.set_trace()
    b = 10
    c = 6
    answer1 = a + b * c
    print("answer1 =", answer1)
    answer2 = (a + b) * c
    print("answer2 =", answer2)

def Task2():
    room_dimensions = []
    for _ in range(3):
        room_dimensions.append(int(input()))
    # next _
    unpaintable = 0
    more_areas_unpaintable = True
    while more_areas_unpaintable == True:
        width = int(input())
        height = int(input())
        unpaintable += width * height
        more_areas_unpaintable = bool(input("More areas that cannot be painted? (True/False): "))
    # endwhile
    coats = int(input())
    room_surface_area = (((room_dimensions[0] * room_dimensions[1] * 2) + 
                        (room_dimensions[0] * room_dimensions[2] * 2) + 
                        (room_dimensions[1] * room_dimensions[2] * 2) -
                        unpaintable) * coats)
    print(room_surface_area/11)
# endprocedure

def Task3():
    pass
    # Task written in pseudocode

    """

    mileage_last_filled = input()
    mileage_present = input()
    litres = input()
    gallons = litres * 4.546
    miles = milage_present - mileage_last_filled
    mpg = miles/gallons
    print(mpg)

    """

    """
    (i) 4.546
    (ii) litres
    (iii) gallons
    """

def Task4Q4():
    numstudents = input("How many students?")
    numbooks = input("How many books?")
    print(f"You can give out {numbooks // numstudents} per student with {numbooks % numstudents} books left over")
# endprocedure

def Task4Q5():
    name = input("Enter a name")
    print(f"The name is {len(name)} characters long.")
# endprocedure
