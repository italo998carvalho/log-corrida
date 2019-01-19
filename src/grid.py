from src.logs import *

# Quebra a string de input em uma lista contendo as informações separadas
# (hora, cod do piloto, nome, ...)
def splitInput(inputlog):
    try:
        inputlog = inputlog.split(" ")
        inputList = []

        for info in inputlog:
            # Remove os espaços em branco em excesso
            if info != '':
                inputList.append(info)
        
        return inputList
    except AttributeError:
        raise AttributeError

# Pega os 7 próximos itens da lista (hora, cod piloto, traço, nome, nº da volta, tempo da volta, vel média)
# E os salva numa volta repetindo o processo até o fim da string
def getLaps(inputList):
    lapList = []
    while len(inputList) > 6:
        lap = {}
        lap['hora'] = inputList[0].split("\n")[1]
        lap['cod_piloto'] = inputList[1]

        # A posição de número 2 do array é sempre o traço entre o código e o nome do piloto, por isso é ignorada
        
        lap['nome_piloto'] = inputList[3]
        lap['n_volta'] = inputList[4]
        lap['tempo_volta'] = inputList[5]
        lap['vel_media_volta'] = inputList[6].split("\n")[0]

        lapList.append(lap)

        # Remove os 7 primeiros intens da lista visto que já foram usados
        inputList = inputList[6:]

    return lapList

# Separa em uma lista o código dos pilotos participantes na corrida
def getCodPiloto(laps):
    listCodPiloto = []
    for lap in laps:
        if lap['cod_piloto'] not in listCodPiloto:
            listCodPiloto.append(lap['cod_piloto'])
    return listCodPiloto

# Calcula as informações finais de cada piloto
def generateFinalInfosStop(laps):
    import datetime

    drivers_code = []
    drivers = []

    for lap in laps:
        # Transforma o tempo da volta de string para timedelta
        try:
            minutes, seconds = lap['tempo_volta'].split(":")
            seconds, milliseconds = seconds.split(".")
            voltaAtual = datetime.timedelta(minutes = int(minutes), seconds = int(seconds), milliseconds = int(milliseconds))
        except ValueError:
            raise ValueError

        if not lap['cod_piloto'] in drivers_code:
            drivers_code.append(lap['cod_piloto'])

            driver = {}
            
            driver['tempo_total_de_prova'] = voltaAtual
            driver['cod_piloto'] = lap['cod_piloto']
            driver['nome_piloto'] = lap['nome_piloto']
            driver['vel_total'] = float(lap['vel_media_volta'].replace(',', '.'))
            driver['vel_media'] = float(lap['vel_media_volta'].replace(',', '.'))
            driver['voltas_completadas'] = lap['n_volta']
            driver['melhor_volta'] = voltaAtual

            drivers.append(driver)
        else:
            for driver in drivers:
                if driver['cod_piloto'] == lap['cod_piloto']:
                    driver['tempo_total_de_prova'] += voltaAtual
                    driver['vel_total'] += float(lap['vel_media_volta'].replace(',', '.'))
                    driver['vel_media'] = round(driver['vel_total'] / int(lap['n_volta']), 3)
                    driver['voltas_completadas'] = lap['n_volta']

                    if voltaAtual < driver['melhor_volta']:
                        driver['melhor_volta'] = voltaAtual
        
        # Após o primeiro piloto completar a 4ª volta, todo o processo da corrida é finalizado
        if int(lap['n_volta']) == 4:
            break

    return drivers

# Calcula as informações finais de cada piloto
def generateFinalInfosKeepRunning(laps, listCodPiloto):
    import datetime

    infosPiloto = []
    for codPiloto in listCodPiloto:
        info = {}
        info['cod_piloto'] = codPiloto
        info['melhor_volta'] = datetime.timedelta()
        info['vel_media'] = 0.0
        soma_velocidade = 0.0

        countVoltas = 0
        countTempoTotalDaProva = datetime.timedelta()

        for lap in laps:
            if codPiloto == lap['cod_piloto']:

                if countVoltas == 4:
                    break
                
                # Transforma o tempo da volta de string para timedelta
                try:
                    minutes, seconds = lap['tempo_volta'].split(":")
                    seconds, milliseconds = seconds.split(".")
                    voltaAtual = datetime.timedelta(minutes = int(minutes), seconds = int(seconds), milliseconds = int(milliseconds))
                except ValueError:
                    raise ValueError

                # Se não houver uma melhor volta (se for a primeira), a melhor volta é a atual
                # Se houver, verifica se a atual é menor que a anterior para checar a mais rápida
                if not info['melhor_volta']:
                    info['melhor_volta'] = voltaAtual
                else:
                    if voltaAtual < info['melhor_volta']:
                        info['melhor_volta'] = voltaAtual

                countTempoTotalDaProva += voltaAtual
                countVoltas += 1

                soma_velocidade += float(lap['vel_media_volta'].replace(',', '.'))
                info['vel_media'] = round(soma_velocidade / countVoltas, 3)

                info['nome_piloto'] = lap['nome_piloto']
                info['voltas_completadas'] = countVoltas
                info['tempo_total_de_prova'] = countTempoTotalDaProva

        infosPiloto.append(info)
    
    return infosPiloto


# Calcula os pilotos mais rápidos
def sortFinalResult(infosPiloto):
    import operator

    infosPiloto.sort(key=operator.itemgetter('tempo_total_de_prova'))

    resultadoFinal = []
    voltas = 4
    count = 1

    # Procura primeiros os pilotos com 4 voltas completas, depois 3, 2 e 1
    while voltas > 0:
        for info in infosPiloto:
            if int(info['voltas_completadas']) == voltas:
                info['posicao'] = count
                resultadoFinal.append(info)
                count += 1
        voltas -= 1
    
    return resultadoFinal

# Através do resultado final retorna a melhor volta da corrida
def getMelhorVoltaDaCorrida(resultadoFinal):
    import datetime

    melhorVolta = {}
    melhorVolta['tempo'] = datetime.timedelta()
    melhorVolta['piloto'] = ''

    for piloto in resultadoFinal:
        if not melhorVolta['tempo']:
            melhorVolta['tempo'] = piloto['melhor_volta']
            melhorVolta['piloto'] = piloto['nome_piloto']
        else:
            if piloto['melhor_volta'] < melhorVolta['tempo']:
                melhorVolta['tempo'] = piloto['melhor_volta']
                melhorVolta['piloto'] = piloto['nome_piloto']
    
     
    return melhorVolta

# Executa as chamadas das funções recebendo a string inicial de log e retornando o resultado final em stop mode
def getFinalResultStop(inputlog):
    splittedLog = splitInput(inputlog)
    laps = getLaps(splittedLog)
    finalInfos = generateFinalInfosStop(laps)
    resultadoFinal = sortFinalResult(finalInfos)

    return resultadoFinal

# Executa as chamadas das funções recebendo a string inicial de log e retornando o resultado final em keep running mode
def getFinalResultKeepRunning(inputlog):
    splittedLog = splitInput(inputlog)
    laps = getLaps(splittedLog)
    listCodPiloto = getCodPiloto(laps)
    finalInfos = generateFinalInfosKeepRunning(laps, listCodPiloto)
    resultadoFinal = sortFinalResult(finalInfos)

    return resultadoFinal
