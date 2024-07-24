def robotWalk(arr):
    x, y = 0, 0
    hotspots = []
    for idx, steps in enumerate(arr):
        #print ('Step', idx)
        # Moving Robot up, right, down, left
        for fp in range(steps):
            match idx%4:
                case 0:
                    y += 1
                case 1:
                    x += 1
                case 2:
                    y -= 1
                case 3:
                    x -= 1
            #print('\tVisiting:',x,y)
            if [x,y] in hotspots:
                #print('Already visited!')
                return [x,y]
            hotspots.append([x,y])
    #print(hotspots)
    return [x,y]

arr = [1,2,4,1,5]
print(robotWalk(arr))
