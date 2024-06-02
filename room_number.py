def porch_and_floor(input_room):
    porch = (input_room - 1) // 20 + 1
    floor = (input_room - 1) % 20 // 4 + 1

    return porch, floor

if __name__ == "__main__":
    input_room = int(input("Введите квартиру: "))
    porch, floor = porch_and_floor(input_room)
    print("Подъезд: ", porch)
    print("Этаж: ", floor)
