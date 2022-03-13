import json
import csv
import sys

    # symbolize useful number us a name
time, source, destination, allocate = 1, 2, 3, 5
DOWN, REST, UP = -1, 0, 1

    # load json file to "building"
json_file = open('Building.json')
building = json.load(json_file)
json_file.close()

    # insert elevators list to "elevators" as a list
elevators = building["_elevators"]

    # get building details
min_floor = building["_minFloor"]
max_floor = building["_maxFloor"]

    # set permanent variable
location, status, toSrc, fromSrc, stops = [], [], [], [], []
for i in range(len(elevators)):
    location.append(0)
    status.append(REST)
    stops.append([])

    # insert call list to "calls" as a list
csv_file = open('Calls.csv')
csvreader = csv.reader(csv_file)
calls = []
for row in csvreader:
    calls.append(row)
csv_file.close()

    #count how much stops will take the elevator to reach the source floor
def statesNumSrc(elev_j, src):
    states = 0
    if (status[elev_j] != DOWN):
        for i in range(len(stops[elev_j])):
            if (src > stops[elev_j][i]):
                states = states + 1
    else:
        for i in range(len(stops[elev_j])):
            if (src < stops[elev_j][i]):
                states = states + 1
    return states

    #calculate how much time will take the elevator to reach the source floor
def calculateToSrc(elev_j, src):
    states = statesNumSrc(elev_j, src)
    dif = abs(location[elev_j] - src)
    closeTime = elevators[elev_j].get("_closeTime") * (states)
    startTime = elevators[elev_j].get("_startTime") * (states+1)
    speed = elevators[elev_j].get("_speed")
    stopTime = elevators[elev_j].get("_stopTime") * (states+1)
    openTime = elevators[elev_j].get("_openTime") * (states+1)
    toSrc = closeTime + startTime + dif/speed + stopTime + openTime
    return toSrc

#count how much stops will take the elevator to reach the destination floor
def statesNumDest(dest, elev_j):
    states = 0
    if (status[elev_j] != DOWN):
        for i in range(len(stops[elev_j])):
            if (dest > stops[elev_j][i]):
                states = states + 1
    else:
        for i in range(len(stops[elev_j])):
            if (dest < stops[elev_j][i]):
                states = states + 1
    return states

    #calculate how much time will take the elevator to reach the destination floor from the destination
def calculateFromSrc(dest, elev_j ,src):
    states = statesNumDest(dest, elev_j)
    dif = abs(src - dest)
    closeTime = elevators[elev_j].get("_closeTime") * states
    startTime = elevators[elev_j].get("_startTime") * (states+1)
    speed = elevators[elev_j].get("_speed")
    stopTime = elevators[elev_j].get("_stopTime") * (states+1)
    openTime = elevators[elev_j].get("_openTime") * (states+1)
    toDest = closeTime + startTime + dif / speed + stopTime + openTime
    return toDest

    #change elevator status
def changeStatus(src, dest, theElev):
    if (src < dest):
        status[theElev] = UP
    elif (src > dest):
        status[theElev] = DOWN

    #add the call if that alovator is allocated to take care to this call
def addstops(src, dest, theElev):
    if (src < dest):
        if(len(stops[theElev])==0):
            stops[theElev].append(src)
            stops[theElev].append(dest)
            status[theElev] = UP
        else:
            stops[theElev].append(src)
            stops[theElev].append(dest)
    else:
        if(len(stops[theElev])==0):
            stops[theElev].append(src)
            stops[theElev].append(dest)
            status[theElev] = DOWN
        else:
            stops[theElev].append(src)
            stops[theElev].append(dest)
    location[theElev] = dest


    #change elevator location after the elevator change her way
def changeLocation(theElev, dest):
    location[theElev] = dest
    stops[theElev].clear()
    status[theElev] = REST

    #'main' function that call all other function to calculate who is the most efficiant elevator to send to a specific call
def allocateElevator ():
    for call_i in range(len(calls)):
        src = int(float(calls[call_i][source]))
        dest = int(float(calls[call_i][destination]))
        if (src > max_floor or src < min_floor or dest > max_floor or dest < min_floor):
            raise Exception("calls have to be in building range!")
        min = sys.maxsize
        for elev_j in range(len(elevators)):
            if (location[elev_j] == src):
                theElev = elev_j
                break
            toSrc.insert(elev_j, calculateToSrc(elev_j, src))
            fromSrc.insert(elev_j, calculateFromSrc(dest, elev_j, src))
            temp = toSrc[elev_j] + fromSrc[elev_j]
            if(temp<min):
                min = temp
                theElev = elev_j
        addstops(src, dest, theElev)
        calls[call_i][allocate] = theElev

if __name__ == '__main__':
    allocateElevator()
    #edit the output file with the update aloocation of elevator to each call
    with open('output.csv', 'w', newline="") as f:
        write = csv.writer(f)
        write.writerows(calls)