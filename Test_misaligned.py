import misaligned
result, final_string = misaligned.create_printable_string()
misaligned.print_color_map_on_console(final_string)
assert(result == 25)
assert(formatter(10, "Black", "Blue").find("|") == formatter(0, "White" ,"Blue"))
print("All is well (maybe!)\n")
