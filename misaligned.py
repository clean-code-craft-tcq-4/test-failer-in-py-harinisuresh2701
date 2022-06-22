printable_string = []
final_string = []
def create_printable_string():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            printable_string.append(formatter(i * 5 + j, major, minor))
    return len(major_colors) * len(minor_colors), printable_string
def formatter(pairNum, Major, Minor):
    formatted_string = f'{pairNum} | {Major} | {Minor}'
    return formatted_string
def print_color_map_on_console(String):
    for i in String:
        print (i,"\n")
result, final_string = create_printable_string()
print_color_map_on_console(final_string)
assert(result == 25)
assert(formatter(10, "Black", "Blue").find("|") == formatter(0, "White" ,"Blue"))
print("All is well (maybe!)\n")
