char = input()
samo = ["a", "e", "i", "o", "u", "y"]
inp = ""
while inp != "koniec":
    inp = input()
    if inp != "koniec":
        for s in samo:
            inp = inp.replace(s, char)
        print(inp)
