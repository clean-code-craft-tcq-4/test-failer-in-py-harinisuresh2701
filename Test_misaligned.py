import misaligned
result, final_string = misaligned.create_printable_string()
misaligned.print_color_map_on_console(final_string)
assert(result == 25)
assert(misaligned.formatter(10, "Black", "Blue").find("|") == misaligned.formatter(0, "White" ,"Blue"))
print("All is well (maybe!)\n")
