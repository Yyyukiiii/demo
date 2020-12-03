def yuesefu(x,y):
    print(x)
    print(y)
    list1=[1 for i in range(1,x+1)]
    while len(list1) > y:
        list2=list1[0:3]
        list1.append(list2[0])
        list1.append(list2[1])
        list1.append(list2[2])
        del list1[0:4]
        return list1

    def move(list1, step):
        num = step - 1
        while num > 0:
            tmp = list1.pop(0)
            list1.append(tmp)
            num = num - 1

        return list1

    def play(players, step, alive):

        list1 = [i for i in range(1, players + 1)]

        while len(list1) > alive:
            list1 = move(list1, step)

            list1.pop(0)

        return list1

    players_num = int(input("请输入参加游戏的人数"))
    step_num = int(input("请输入淘汰的数字"))
    alive_num = int(input("请输入幸存的人数"))
    list1 = []
    alive_list = play(players_num, step_num, alive_num)
    print(alive_list)