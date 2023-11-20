
# デフォルト表示
row = [" ", "a", "b", "c", "d", "e", "f", "g", "h"]

# i_list = []
# j_list = []

# index 0 a
# index 0 a
list = [
    [" ", "a", "b", "c", "d", "e", "f", "g", "h"]
]
for i in range(1, 9):
    for j in range(9):
        if j == 0:
            list.append([i])
            # list[i][0] = i
        elif (i == 4 and j ==4) or (i == 5 and j == 5):
            # print("w", end=" ")
            list[i].append('w')
        elif (i == 4 and j ==5) or (i == 5 and j == 4):
        #     print("b", end=" ")
            list[i].append('b')
        else:
            # list[i][j] == "*"
            list[i].append('*')
            

        # elif j == 0:
        #     print(i, end=" ")
        #     list[i][j].append(i)
        # else:
        #     print("*", end=" ")
        #     list[i][j].append("*")
    # print()

# print(f"{list}テスト")
# player = ["black", "white"]
# place = tuple(input(f"{player[0]}の番です。盤目を入力してくだい(a1)>>>"))

# print(place)

# i,j = place
# print(i,j)

for li in list:
    for l in li:
        print(l, end=" ")
    print()

# playerから盤の位置を受け取る
player = 'b'
i = 1
j = 'a'
j = list[0].index(j)
p = [i,j]
# print(list[0].index(p[1]))
print(player)
list[i][j] = player

for li in list:
    for l in li:
        print(l, end=" ")
    print()

# 置いたところの周りに相手の石がないと置けない

right = list[i][j+1]
left = list[i][j-1]
up = list[i-1][j]
down = list[i+1][j]
ru = list[i-1][j+1]
lu = list[i-1][j-1]
rd = list[i+1][j+1]
lu = list[i+1][j-1]

print(right)