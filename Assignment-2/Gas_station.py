#Given a circular list of gas stations, where we can go from a station i to the station i + 1, and the last one goes back to the first one, find the index of the station from where we start to be able to traverse all the stations and go back to the initial one without running out of gas

def can_traverse(gas, cost, start):
    n= len(gas)
    remaining = 0
    started = False
    i = start
    while i != start or not started:
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:
            return False
        i = (i+1)%n
    return True
    
def gas_station(gas, cost):
    for j in range(len(gas)):
        if can_traverse(gas, cost, j):
            return j
    return -1
    
gas = [1,5,3,3,5,3,1,3,4,5]
cost = [5,2,2,8,2,4,2,5,1,2]
print(gas_station(gas, cost))
