#tower of hanoi
def hanoi(Total_disks, first, center, last):

    if Total_disks > 0:
        # move tower of size n - 1 to center:
        hanoi(Total_disks - 1, first, last, center)

        # move disk from first to last
        if first[0]:
            disk = first[0].pop()
            print("moving " + str(disk) + " from " + first[1] + " to " + last[1])
            last[0].append(disk)

        # move tower of size n-1 from center to last
        print(first, center, last)
        hanoi(Total_disks - 1, center, first, last)


##Eerste paal
first = ([4, 3, 2, 1], "first")
##Laatste paal
last = ([], "last")
##Middelste paal
center = ([], "center")

hanoi(len(first[0]), first, center, last)
print(first, center, last)
