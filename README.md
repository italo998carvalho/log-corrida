## Aplicação
Através da entrada do log das voltas de uma corrida contendo as seguintes informações (hora, 
código do piloto, nome do piloto, tempo da volta e velocidade média da volta) esta aplicação calcula
o resultado final da corrida.

###### Exemplo de input:
```bash
23:49:08.277      038 – F.MASSA             1     1:02.852      44,275
23:49:10.858      033 – R.BARRICHELLO       1	  1:04.352      43,243
23:50:11.447      038 – F.MASSA             2	  1:03.170      44,053
23:50:14.860      033 – R.BARRICHELLO       2	  1:04.002      43,48
23:51:14.216      038 – F.MASSA             3	  1:02.769      44,334
23:51:18.576      033 – R.BARRICHELLO       3	  1:03.716      43,675
23:52:17.003      038 – F.MASSA             4	  1:02.787      44,321
23:52:22.586      033 – R.BARRICHELLO       4	  1:04.010      43,474
```

A aplicação possui dois modos de execução, são eles:
#### Stop mode:
Quando o primeiro piloto completa a 4ª volta a corrida é finalizada, os pilotos no meio do caminho não completam a corrida e o resultado final é baseado nas voltas completadas até o momento.

#### Keep running mode:
A corrida continua até todos os pilotos completarem suas voltas, mesmo se já houver um vencedor.

## Execução
O valor de entrada é do tipo string (formato de texto) e está localizado no arquivo src/logs.py na variável chamada inputLog e lá é possível alterar seus valores (sem alterar o formato, posição das informações ou pontuações dos valores).

#### Requisitos
O único requisito é ter o interpretador da linguagem [python](https://www.python.org/downloads/) instalado em sua versão 3 ou superior.

Clone este projeto e acesse sua raíz via terminal.

#### Comandos
###### Executar a aplicação em Stop mode
```bash
python runStop.py
```

###### Executar a aplicação em Keep running mode
```bash
python runKeepRunning.py
```

###### Executar os testes
```bash
python -m unittest test_grid.py
```