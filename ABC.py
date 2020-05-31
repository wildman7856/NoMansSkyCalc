a = ['a',100,4]
b = ['b',1,5]
c = ['c',2,6]
d = ['d',3,7]
e = ['e',4,8]
f = ['f',5,9]
g = ['g',6,10]


ships = [a,b,c,d,e,f,g]
target = 20

name = 0; score = 1; fuel = 2

var = [0,0,0,0,0]
combo = 1 # Number of combinations of ships.
##while combo <= 5:
while var[0]<len(ships):
    var[1] = var[0] + 1
    while var[1]<len(ships):
        var[2] = var[1] + 1
        while var[2]<len(ships):
            var[3] = var[2] + 1
            while var[3]<len(ships):
                var[4] = var[3] + 1
                while var[4]<len(ships):
                    stars = 0; fuelUsage = 0
                    string = ''
                    for i in range(combo):
                        stars = stars + ships[var[i]][score]
                        fuelUsage = fuelUsage + ships[var[i]][fuel]
                        string = string + ships[var[i]][name]
                        if i < (combo - 1):
                            string = string + ' + '
                    if stars <= target: #filter results
                        print(string)
                        print(stars)
                        print(fuelUsage)
                    var[4] = var[4] + 1
                var[3] = var[3] + 1
            var[2] = var[2] + 1
        var[1] = var[1] + 1
    var[0] = var[0] + 1
##combo = combo + 1

var = [0,0,0,0,0]
combo = 2 # Number of combinations of ships.
##while combo <= 5:
while var[0]<len(ships):
    var[1] = var[0] + 1
    while var[1]<len(ships):
        var[2] = var[1] + 1
        while var[2]<len(ships):
            var[3] = var[2] + 1
            while var[3]<len(ships):
                var[4] = var[3] + 1
                while var[4]<len(ships):
                    stars = 0; fuelUsage = 0
                    string = ''
                    for i in range(combo):
                        stars = stars + ships[var[i]][score]
                        fuelUsage = fuelUsage + ships[var[i]][fuel]
                        string = string + ships[var[i]][name]
                        if i < (combo - 1):
                            string = string + ' + '
                    if stars <= target: #filter results
                        print(string)
                        print(stars)
                        print(fuelUsage)
                    var[4] = var[4] + 1
                var[3] = var[3] + 1
            var[2] = var[2] + 1
        var[1] = var[1] + 1
    var[0] = var[0] + 1
##combo = combo + 1

var = [0,0,0,0,0]
combo = 3 # Number of combinations of ships.
##while combo <= 5:
while var[0]<len(ships):
    var[1] = var[0] + 1
    while var[1]<len(ships):
        var[2] = var[1] + 1
        while var[2]<len(ships):
            var[3] = var[2] + 1
            while var[3]<len(ships):
                var[4] = var[3] + 1
                while var[4]<len(ships):
                    stars = 0; fuelUsage = 0
                    string = ''
                    for i in range(combo):
                        stars = stars + ships[var[i]][score]
                        fuelUsage = fuelUsage + ships[var[i]][fuel]
                        string = string + ships[var[i]][name]
                        if i < (combo - 1):
                            string = string + ' + '
                    if stars <= target: #filter results
                        print(string)
                        print(stars)
                        print(fuelUsage)
                    var[4] = var[4] + 1
                var[3] = var[3] + 1
            var[2] = var[2] + 1
        var[1] = var[1] + 1
    var[0] = var[0] + 1
##combo = combo + 1

var = [0,0,0,0,0]
combo = 4 # Number of combinations of ships.
##while combo <= 5:
while var[0]<len(ships):
    var[1] = var[0] + 1
    while var[1]<len(ships):
        var[2] = var[1] + 1
        while var[2]<len(ships):
            var[3] = var[2] + 1
            while var[3]<len(ships):
                var[4] = var[3] + 1
                while var[4]<len(ships):
                    stars = 0; fuelUsage = 0
                    string = ''
                    for i in range(combo):
                        stars = stars + ships[var[i]][score]
                        fuelUsage = fuelUsage + ships[var[i]][fuel]
                        string = string + ships[var[i]][name]
                        if i < (combo - 1):
                            string = string + ' + '
                    if stars <= target: #filter results
                        print(string)
                        print(stars)
                        print(fuelUsage)
                    var[4] = var[4] + 1
                var[3] = var[3] + 1
            var[2] = var[2] + 1
        var[1] = var[1] + 1
    var[0] = var[0] + 1
##combo = combo + 1

var = [0,0,0,0,0]
combo = 5 # Number of combinations of ships.
##while combo <= 5:
while var[0]<len(ships):
    var[1] = var[0] + 1
    while var[1]<len(ships):
        var[2] = var[1] + 1
        while var[2]<len(ships):
            var[3] = var[2] + 1
            while var[3]<len(ships):
                var[4] = var[3] + 1
                while var[4]<len(ships):
                    stars = 0; fuelUsage = 0
                    string = ''
                    for i in range(combo):
                        stars = stars + ships[var[i]][score]
                        fuelUsage = fuelUsage + ships[var[i]][fuel]
                        string = string + ships[var[i]][name]
                        if i < (combo - 1):
                            string = string + ' + '
                    if stars <= target: #filter results
                        print(string)
                        print(stars)
                        print(fuelUsage)
                    var[4] = var[4] + 1
                var[3] = var[3] + 1
            var[2] = var[2] + 1
        var[1] = var[1] + 1
    var[0] = var[0] + 1
##combo = combo + 1



##i=0;j=1
    
##var = [0,0,0,0,0]
##while var[0]<len(ships):
##    var[1] = var[0] + 1
##    while var[1]<len(ships):
##        var[2] = var[1] + 1
##        while var[2]<len(ships):
##            var[3] = var[2] + 1
##            while var[3]<len(ships):
##                stars = ships[var[0]][score] + ships[var[1]][score] + ships[var[2]][score] + ships[var[3]][score]
##                if stars <= target:
##                    print(ships[var[0]][name] + ' + ' + ships[var[1]][name]+ ' + ' + ships[var[2]][name] + ' + ' + ships[var[3]][name])
##                    fuelUsage = ships[var[0]][fuel] + ships[var[1]][fuel] + ships[var[2]][fuel] + ships[var[3]][fuel]
##                    print(stars)
##                    print(fuelUsage)
##                var[3] = var[3] + 1
##            var[2] = var[2] + 1
##        var[1] = var[1] + 1
##    var[0] = var[0] + 1

##asdf = [234,6323,1234,23456,1243]
##qwerty = 0
##for i in range(5):
##    qwerty = qwerty + asdf[i]
##print(qwerty)


##i = 0; j = 0; k = 0; l = 0; m = 0;
##while i<len(ships):
##    j = i + 1
##    while j<len(ships):
##        k = j + 1
##        while k<len(ships):
##
##            stars = ships[i][score] + ships[j][score] + ships[k][score]
##            if stars >= 0:
##                print(ships[i][name] + ' + ' + ships[j][name]+ ' + ' + ships[k][name])
##                print(stars)
##                print(ships[i][fuel] + ships[j][fuel] + ships[k][fuel])
##            k = k + 1
##        j = j + 1
##    i = i + 1







    
    
