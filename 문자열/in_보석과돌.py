
jewlery = "aA"
stone = "aAABBBb"
def jewl(jewlery, stone):
    count = 0
    for j in jewlery:
        count += stone.count(j)
    return count

def jewl2(jewlery, stone):
    jSet = set(jewlery)
    count = 0
    for s in stone:
        if s in jSet:
            count += 1
    return count
print(jewl2(jewlery, stone))