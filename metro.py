Directdistance = [
    
        [0,    10,   18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1,  16.7, 27.3, 27.6, 29.8], # Estação E1
        [10,   0,    8.5,  14.8, 26.6, 29.1, 26.1, 17.3, 10,   3.5,  15.5, 20.9, 19.1, 21.8], # Estação E2
        [18.5, 8.5,  0,    6.3,  18.2, 20.6, 17.6, 13.6, 9.4,  10.3, 19.5, 19.1, 12.1, 16.6], # Estação E3
        [24.8, 14.8, 6.3,  0,    12,   14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4], # Estação E4
        [36.4, 26.6, 18.2, 12,   0,    3,    2.4,  19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9], # Estação E5
        [38.8, 29.1, 20.6, 14.4, 3,    0,    3.3,  22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2], # Estação E6
        [35.8, 26.1, 17.6, 11.5, 2.4,  3.3,  0,    20,   23,   27.3, 34.2, 25.7, 12.4, 15.6], # Estação E7
        [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20,   0,    8.2,  20.3, 16.1, 6.4,  22.7, 27.6], # Estação E8
        [17.6, 10,   9.4,  12.6, 23.3, 25.7, 23,   8.2,  0,    13.5, 11.2, 10.9, 21.2, 26.6], # Estação E9
        [9.1,  3.5,  10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0,    17.6, 24.2, 18.7, 21.2], # Estação E10
        [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0,    14.2, 31.5, 35.5], # Estação E11
        [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4,  10.9, 24.2, 14.2, 0,    28.8, 33.6], # Estação E12
        [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0,    5.1],  # Estação E13
        [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1,  0]     # Estação E14
    ]

realDistance = {"E1-E10":10, "E2-E3": 3, "E2-E9":10, "E2-E10":3.5, "E3-E4":6.3, "E3-E9":9.4,
"E3-E13": 18.7, "E4-E5":13, "E4-E8":15.3, "E4-E13": 12.8, "E5-E6": 3, "E5-E7":2.4, "E5-E8": 30,
"E8-E9":9.6, "E8-E12":6.4, "E9-E11":12.2, "E13-E14": 5.1}

RedLine = ["E11", "E9", "E3", "E14"]
BlueLine = ["E1", "E2", "E3", "E4", "E5", "E6"]
YellowLine = ["E7", "E5", "E8", "E9", "E2", "E10"]
GreenLine = ["E12", "E4", "E8", "E13", "E14"]

matrix_neighbors = {
"E1" : ["E2"],
"E2" : ["E1", "E3", "E9", "E10"],
"E3" : ["E2", "E4", "E9", "E13"],
"E4" : ["E3", "E5", "E8", "E13"],
"E5" : ["E4", "E6", "E7", "E8"],
"E6" : ["E5"],
"E7" : ["E5"],
"E8" : ["E4", "E5", "E9", "E12"],
"E9" : ["E2", "E3", "E8", "E11"],
"E10" : ["E2"],
"E11" : ["E9"],
"E12" : ["E8"],
"E13" : ["E3", "E4", "E14"],
"E14" : ["E13"]
}

def get_neighbors(station):
    if (station in matrix_neighbors):
        return matrix_neighbors[station]

def get_distance(array, currentstation): 
    newArray = []
    distance = 0
    for station in array: 
        if (f'{currentstation}-{station}' in realDistance):
            distance = realDistance[f'{currentstation}-{station}']
        elif (f'{station}-{currentstation}' in realDistance):
            distance =  realDistance[f'{station}-{currentstation}']
        newArray.append([station, distance ])
    return newArray

def distanceToTime(station1, station2):
    #luquinhasss preciso de ajuda p fazer uma funcao q va de distancia p tempo, considerando os 4 minutos se forem linhas diferete


def best_way(start, end):
    border = []
    functionG = []
    border.append(start)
    while len(border) != 0:
        aux= 0;
        for station in border:
            if aux == 0:
                aux = station
            


        








