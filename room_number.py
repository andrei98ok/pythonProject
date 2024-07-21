def porch_and_floor(input_floors_number, input_rooms_per_floor, input_room):

    rooms_per_porch = input_floors_number * input_rooms_per_floor
    porch = (input_room - 1) // rooms_per_porch + 1
    floor = ((input_room - 1) % rooms_per_porch) // input_rooms_per_floor + 1

    return porch, floor

if __name__ == "__main__":
    input_room = int(input("Введите квартиру: "))
    input_floors_number = int(input("Введите количество этажей: "))
    input_rooms_per_floor = int(input("Введите количество квартир на этаже: "))
    porch, floor = porch_and_floor(input_floors_number, input_rooms_per_floor, input_room)
    print("Подъезд: ", porch)
    print("Этаж: ", floor)
