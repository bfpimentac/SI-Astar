#ao longo do código, haverão comentários para facilitar o entendimento do que foi feito
time = [
    [0.0, 20.0, 37.0, 49.6, 72.8, 77.6, 71.6, 50.8, 35.2, 18.2, 33.4, 54.6, 55.2, 59.6],  
    [20.0, 0.0, 17.0, 29.6, 53.2, 58.2, 52.2, 34.6, 20.0, 7.0, 31.0, 41.8, 38.2, 43.6],  
    [37.0, 17.0, 0.0, 12.6, 36.4, 41.2, 35.2, 27.2, 18.8, 20.6, 39.0, 38.2, 24.2, 33.2],  
    [49.6, 29.6, 12.6, 0.0, 24.0, 28.8, 23.0, 24.8, 25.2, 33.4, 47.2, 37.2, 21.2, 30.8],  
    [72.8, 53.2, 36.4, 24.0, 0.0, 6.0, 4.8, 38.8, 46.6, 56.4, 68.4, 49.6, 29.0, 35.8],  
    [77.6, 58.2, 41.2, 28.8, 6.0, 0.0, 6.6, 44.6, 51.4, 60.6, 73.4, 55.2, 30.4, 36.4],  
    [71.6, 52.2, 35.2, 23.0, 4.8, 6.6, 0.0, 40.0, 46.0, 54.6, 68.4, 51.4, 24.8, 31.2],  
    [50.8, 34.6, 27.2, 24.8, 38.8, 44.6, 40.0, 0.0, 16.4, 40.6, 32.2, 12.8, 45.4, 55.2],  
    [35.2, 20.0, 18.8, 25.2, 46.6, 51.4, 46.0, 16.4, 0.0, 27.0, 22.4, 21.8, 42.4, 53.2],  
    [18.2, 7.0, 20.6, 33.4, 56.4, 60.6, 54.6, 40.6, 27.0, 0.0, 35.2, 48.4, 37.4, 42.4],  
    [33.4, 31.0, 39.0, 47.2, 68.4, 73.4, 68.4, 32.2, 22.4, 35.2, 0.0, 31.8, 67.4, 78.8],  
    [54.6, 41.8, 38.2, 37.2, 49.6, 55.2, 51.4, 12.8, 21.8, 48.4, 31.8, 0.0, 59.2, 69.8], 
    [55.2, 38.2, 24.2, 21.2, 29.0, 30.4, 24.8, 45.4, 42.4, 37.4, 67.4, 59.2, 0.0, 13.4],  
    [59.6, 43.6, 33.2, 30.8, 35.8, 36.4, 31.2, 55.2, 53.2, 42.4, 78.8, 69.8, 13.4, 0.0],  
]

#aqui temos uma matriz dos tempos das distancias diretas entre as estacoes. Transformamos em tempo atraves da multiplicacao por 2 para faciltar
#a primeira linha corresponde a E1, a segunda a E2.... A decima quarta a E14

realtime = {
    1 : [(2, 20, 'azul')], 
    2 : [(3, 17, 'azul'), (1, 20, 'azul'), (9, 20, 'amarela'), (10, 7, 'amarela')], 
    3 : [(2, 17, 'azul'), (4, 12.6, 'azul'), (9, 18.8, 'vermelha'), (13, 37.4, 'vermelha')],
    4 : [(3, 12.6, 'azul'), (5, 26, 'azul'), (8, 30.6, 'verde'), (13, 25.6, 'verde')],
    5 : [(4, 26, 'azul'), (6, 6, 'azul'), (7, 4.8, 'amarela'), (8, 60, 'amarela')],
    6 : [(5, 6, 'azul')],
    7 : [(5, 4.8, 'amarela')],
    8 : [(5, 60, 'amarela'), (4, 30.6, 'verde'), (9, 19.2, 'amarela'), (12, 12.8, 'verde')],
    9 : [(8, 19.2, 'amarela'), (2, 20, 'amarela'), (3, 18.8, 'vermelha'), (11, 24.4, 'vermelha')],
    10: [(2, 7, 'amarela')],
    11: [(9, 24.4, 'vermelha')],
    12: [(8, 12.8, 'verde')],
    13: [(3, 37.4, 'vermelha'), (4, 25.6, 'verde'), (14, 10.2, 'verde')],
    14: [(13, 10.2, 'verde')]
    
}
# aqui temos um dicionario cujas keys são o numero da estação origem. O valor é uma lista cujo cada elemento é uma tupla que contem a estacao destino, o tempo real e a linha

def vizinhos(state):
    if state in realtime:
        return realtime[state]
    # funcao p retornar os tempos reais entre os nos adjcentes (se forem adjcentes)
    
def AStar(start, end):
    #g é a distancia de n ao no inicial 
    #h é a distancia estimada de n ao no final
    board = []   #criando nossa fronteira                     
    board.append(start)    #colocando a tupla da estacao inicial na fronteira      
    board_final = []  #array da fronteira final
    g = {}      #aqui temos a funcao G. Grava a distancia da estacao ate a estcao  inicial           
    parents = {}       #é necessario saber os pais                    
    g[start] = 0        #como a distancia da estacao inicil p a estacao inicial eh zero          
    parents[start] = start #o estacao inicial eh pai dos outros, inclusive dele mesmo
    while len(board) != 0: #enquanto nossa fronteira nao esta vazia
        aux = 0 #inicializando nossa variavel auxiliar que vai servir p comparar as funcoes f()
        for state in board: #vamos realizar isso para cada estacao da fronteira
            if aux == 0: #quando iniciamos o auxiliar, o auxiliar vai ser o nó de inicial
                aux = state 
            #g()                    #h()
            if g[state] + time[state[0] - 1][end[0] - 1] < g[aux] + time[aux[0] - 1][end[0] - 1]:
                aux = state #depois, faz-se necessario checar a funcao f(). Lembrando que f()= g()+h
                #se a o tempo de state for menor, aux = state
        if aux != end: #se n é o nó de destino, ignoramos
            for (number, distance, line) in vizinhos(aux[0]): 
                vec = (number, line) 
                if vec not in board and vec not in board_final: #se vec nao ta na fronteira, a gnt coloca
                    board.append(vec)                
                    print(f'Fronteira: {board}') 
                    parents[vec] = aux   #aux vai ser pai do no          
                    g[vec] = g[aux] + distance #calculando funcao g
                    if aux[1] != vec[1]: #verificao mudar de linha
                        g[vec] = g[vec] + 4 #mais 4 minutos
                else: # se ja tiver na fronteira, compara com a distância inicial para conferir qual é o menor
                    if g[vec] > g[aux] + distance:
                        g[vec] = g[aux] + distance
                        parents[vec] = aux #fazendo atualizacpes necessarias
                        if number in board_final:
                            board_final.remove(vec)
                            board.append(vec)  #removendo 
        if aux == end:
            path = []
            while parents[aux] != aux:
                path.append(aux)
                aux = parents[aux]
            path.append(start) 
            path.reverse() 
            print('o caminho a se seguir é {}'.format(path))
            print(f'o menor tempo eh de: {g[state] + time[state[0] - 1][end[0] - 1]} minutos')
            return path
        board.remove(aux)
        board_final.append(aux)
def main(start_station,start_line,final_station,final_line):
    AStar((start_station, start_line), (final_station, final_line))

# user screen
print("-----------------------------------------")
print("bonjour, voyons le chemin le plus rapide!")
print("-----------------------------------------")
print("quel est le numéro de la gare de départ?:")
start_station = int(input())
print("quelle est la couleur de la ligne de départ?")
start_line = input()
print("quel est le numéro de la gare d'arrivée")
final_station = int(input())
print("de quelle couleur est la ligne d'arrivée")
final_line = input()

main(start_station,start_line,final_station,final_line)
print("bon voyage!")

