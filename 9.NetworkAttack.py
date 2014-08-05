#!/usr/bin/python

def capture(matrix):
    """ Network attack, returns the time taken to shit all the systems!"""
    net = {}
    num_systems = len(matrix)
    #Counts number of systems
    totalsys = [x for x in range(num_systems)]
    #Take out the daigonal from matrix
    timeneed = [matrix[i][i] for i in xrange(num_systems)]
    #Creates a dict. with system number as key and connected
    #systems as values in a list
    for sys in range(num_systems):
        cur_row = matrix[sys]
        dumb = []
        for k,v in enumerate(cur_row):
             if v == 1:
                 dumb.append(k)
        net[sys] = dumb
    #print net
    done = [0]
    inpro = [n for n in net[0]]
    time  = 0
    #Loop until all systems are cracked.
    while sum(timeneed)!=0: 
        for node in inpro:
            timeneed[node] = timeneed[node] - 1 
        time = time + 1
        for i,j in enumerate(timeneed):
            if j == 0:
                if i in inpro:
                    inpro.remove(i)
                    done.append(i)
                    inpro = list(set(inpro + net[i])-set(done))
    return time
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
