row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]  

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?  ")

# col_p = int(position[0])
# row_p = int(position[1])


# Method 1

# if row_p == 1:
#     if col_p == 1:
#         row1[0] = "X"
#     elif col_p == 2:
#         row1[1] = "X"
#     elif col_p == 3:
#         row1[2] = "X"
# elif row_p == 2:
#     if col_p == 1:
#         row2[0] = "X"
#     elif col_p == 2:
#         row2[1] = "X"
#     elif col_p == 3:
#         row2[2] = "X"
#         print(map)
# elif row_p == 3:
#     if col_p == 1:
#         row3[0] = "X"
#     elif col_p == 2:
#         row3[1] = "X"
#     elif col_p == 3:
#         row3[2] = "X"
#         print(f"{row1}\n{row2}\n{row3}")
# else:
#     print("Enter a valid number!")

# Method 2
# Using the variable map as the row checker
# if row_p == len(map)-2:
#     if col_p == 1:
#         row1[0] = "X"
#     elif col_p == 2:
#         row1[1] = "X"
#     elif col_p == 3:
#         row1[2] = "X"
# elif row_p == 2:
#     if col_p == len(map)-1:
#         row2[0] = "X"
#     elif col_p == 2:
#         row2[1] = "X"
#     elif col_p == 3:
#         row2[2] = "X"
#         print(map)
# elif row_p == len(map):
#     if col_p == 1:
#         row3[0] = "X"
#     elif col_p == 2:
#         row3[1] = "X"
#     elif col_p == 3:
#         row3[2] = "X"
#         print(f"{row1}\n{row2}\n{row3}")
# else:
#     print("Enter a valid number!")

#Method 3
# The shortest approach

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical-1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

