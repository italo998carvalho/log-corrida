from src.grid import getFinalResultKeepRunning, getMelhorVoltaDaCorrida
from src.logs import inputLog

resultadoFinal = getFinalResultKeepRunning(inputLog)

print("POSIÇÃO   CÓD. PILOTO   NOME DO PILOTO    VOLTAS COMPLETADAS    TEMPO TOTAL DE PROVA        MELHOR VOLTA       VEL. MÉDIA        DIFERENÇA")

for piloto in resultadoFinal:
    if piloto['posicao'] == 1:
        piloto['diferenca'] = '-'
    else:
        if piloto['voltas_completadas'] == resultadoFinal[0]['voltas_completadas']:
            piloto['diferenca'] = piloto['tempo_total_de_prova'] - resultadoFinal[0]['tempo_total_de_prova']
        else:
            piloto['diferenca'] = 'Não completou a prova'

    grid_position = ''
    grid_position += str(piloto['posicao'])  + 'º'

    while len(grid_position) < 13:
        grid_position += ' '
    
    grid_position += str(piloto['cod_piloto'])

    while len(grid_position) < 24:
        grid_position += ' '
    
    grid_position += str(piloto['nome_piloto'])

    while len(grid_position) < 49:
        grid_position += ' '
    
    grid_position += str(piloto['voltas_completadas'])

    while len(grid_position) < 66:
        grid_position += ' '
    
    grid_position += str(piloto['tempo_total_de_prova'])

    while len(grid_position) < 91:
        grid_position += ' '
    
    grid_position += str(piloto['melhor_volta'])

    while len(grid_position) < 111:
        grid_position += ' '

    grid_position += str(piloto['vel_media']) + " Km/h"

    while len(grid_position) < 129:
        grid_position += ' '

    grid_position += str(piloto['diferenca'])

    print(grid_position)

melhor_volta = getMelhorVoltaDaCorrida(resultadoFinal)
print("\nMELHOR VOLTA DA CORRIDA")
print("Piloto: " + str(melhor_volta['piloto']))
print("Tempo: " + str(melhor_volta['tempo']))