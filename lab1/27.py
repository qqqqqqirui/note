def giveChange(cost, paid):
    change = paid - cost
    notes = [20, 10, 5, 1]
    for note in notes:
        count = change // note
        if count > 0:
            print(count, "x", "￥", note)
            change -= count * note


giveChange(13, 50)
