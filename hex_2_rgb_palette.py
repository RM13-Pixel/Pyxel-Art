# --------------------------------------------------------------------
# Hex 2 RGB Palette
# A program to add hex color codes to palettes for Pyxel Art
# Creator: RM13-Pixel
# --------------------------------------------------------------------
def hex_to_rgb(value):
    value = value[1:]
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def list_to_string(s):
    str1 = "["
    for ele in s:
        tup = "("
        tup += str(ele[0])
        tup += ", "
        tup += str(ele[1])
        tup += ", "
        tup += str(ele[2])
        tup += ")"
        str1 += tup
        str1 += ", "
    str1 = str1[:-2]
    str1 += "]"
    return str1


# variables
paletteName = ""
palette = []
start = "y"
file = open("palette_list.py", "a+")

# try:
while start == "y":
    hex = ""
    # hex2rgb conversion
    while hex.lower() != "end":
        print("Enter hex code to add to palette or \"end\" to stop")
        hex = input("")
        if hex.lower() != "end":
            print('RGB =', hex_to_rgb(hex))
            palette.append(hex_to_rgb(hex))
        else:
            print("Palette created:")
            print(palette)

    # palette export
    print("Export to palette list?(Y/N)")
    export = input("")
    if export.lower() == "y":
        print("Enter palette name:")
        paletteName = input("")
        file.write(" \n")
        file.write(paletteName + "_" + str(len(palette)) + " = ")
        file.write(list_to_string(palette))
        file.close()
        print(paletteName + " saved to palette list.")

    # restart
    print("Restart palette?(Y/N)")
    start = input("").lower()
print("Get back to work!")  # A reminder to the user to stay on task
# except:
# print("Invalid input")
