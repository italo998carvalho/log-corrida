inputLog = """
23:49:08.277      038 – F.MASSA                           1     1:02.852            44,275
23:49:10.858      033 – R.BARRICHELLO                     1	    1:04.352            43,243
23:49:11.075      002 – K.RAIKKONEN                       1     1:04.108            43,408
23:49:12.667      023 – M.WEBBER                          1	    1:04.414            43,202
23:49:30.976      015 – F.ALONSO                          1	    1:18.456		    35,47
23:50:11.447      038 – F.MASSA                           2	    1:03.170            44,053
23:50:14.860      033 – R.BARRICHELLO                     2	    1:04.002            43,48
23:50:15.057      002 – K.RAIKKONEN                       2     1:03.982            43,493
23:50:17.472      023 – M.WEBBER                          2	    1:04.805            42,941
23:50:37.987      015 – F.ALONSO                          2	    1:07.011            41,528
23:51:14.216      038 – F.MASSA                           3	    1:02.769            44,334
23:51:18.576      033 – R.BARRICHELLO                     3	    1:03.716            43,675
23:51:19.044      002 – K.RAIKKONEN                       3	    1:03.987            43,49
23:51:21.759      023 – M.WEBBER                          3	    1:04.287            43,287
23:51:46.691      015 – F.ALONSO                          3	    1:08.704            40,504
23:52:01.796      011 – S.VETTEL                          1	    3:31.315            13,169
23:52:17.003      038 – F.MASSA                           4	    1:02.787            44,321
23:52:22.586      033 – R.BARRICHELLO                     4	    1:04.010            43,474
23:52:22.120      002 – K.RAIKKONEN                       4     1:03.076            44,118
23:52:25.975      023 – M.WEBBER                          4	    1:04.216            43,335
23:53:06.741      015 – F.ALONSO                          4	    1:20.050            34,763
23:53:39.660      011 – S.VETTEL                          2	    1:37.864            28,435
23:54:57.757      011 – S.VETTEL                          3	    1:18.097            35,633
"""

# ========================================================================================
# ============================= MOCKED RESULTS FOR TESTS =================================
# ========================================================================================

testLog = """
23:49:08.277      038 – F.MASSA                           1     1:02.852            44,275
23:49:10.858      033 – R.BARRICHELLO                     1	    1:04.352            43,243
23:50:11.447      038 – F.MASSA                           2	    1:03.170            44,053
23:50:14.860      033 – R.BARRICHELLO                     2	    1:04.002            43,48
23:51:14.216      038 – F.MASSA                           3	    1:02.769            44,334
23:51:18.576      033 – R.BARRICHELLO                     3	    1:03.716            43,675
23:52:17.003      038 – F.MASSA                           4	    1:02.787            44,321
23:52:22.586      033 – R.BARRICHELLO                     4	    1:04.010            43,474
"""

brokenTestLog = [
    "23:49:08.277 038 – F.MASSA 1 1:02.852 44,275"
]

splittedInput = ['\n23:49:08.277', '038', '–', 'F.MASSA', '1', '1:02.852', 
        '44,275\n23:49:10.858', '033', '–', 'R.BARRICHELLO', '1\t', '1:04.352', 
        '43,243\n23:50:11.447', '038', '–', 'F.MASSA', '2\t', '1:03.170', 
        '44,053\n23:50:14.860', '033', '–', 'R.BARRICHELLO', '2\t', '1:04.002', 
        '43,48\n23:51:14.216', '038', '–', 'F.MASSA', '3\t', '1:02.769', 
        '44,334\n23:51:18.576', '033', '–', 'R.BARRICHELLO', '3\t', '1:03.716', 
        '43,675\n23:52:17.003', '038', '–', 'F.MASSA', '4\t', '1:02.787', 
        '44,321\n23:52:22.586', '033', '–', 'R.BARRICHELLO', '4\t', '1:04.010', '43,474\n'
]

brokenSplittedInput = {'\n23:49:08.277', '038', '–', 'F.MASSA', '1', '1:02.852', 
        '44,275\n23:49:10.858', '033', '–', 'R.BARRICHELLO', '1\t', '1:04.352', 
        '43,243\n23:50:11.447', '038', '–', 'F.MASSA', '2\t', '1:03.170', 
        '44,053\n23:50:14.860', '033', '–', 'R.BARRICHELLO', '2\t', '1:04.002'
}

laps = [
        {'hora': '23:49:08.277', 'cod_piloto': '038', 'nome_piloto': 'F.MASSA', 'n_volta': '1', 'tempo_volta': '1:02.852', 'vel_media_volta': '44,275'}, 
        {'hora': '23:49:10.858', 'cod_piloto': '033', 'nome_piloto': 'R.BARRICHELLO', 'n_volta': '1\t', 'tempo_volta': '1:04.352', 'vel_media_volta': '43,243'}, 
        {'hora': '23:50:11.447', 'cod_piloto': '038', 'nome_piloto': 'F.MASSA', 'n_volta': '2\t', 'tempo_volta': '1:03.170', 'vel_media_volta': '44,053'}, 
        {'hora': '23:50:14.860', 'cod_piloto': '033', 'nome_piloto': 'R.BARRICHELLO', 'n_volta': '2\t', 'tempo_volta': '1:04.002', 'vel_media_volta': '43,48'}, 
        {'hora': '23:51:14.216', 'cod_piloto': '038', 'nome_piloto': 'F.MASSA', 'n_volta': '3\t', 'tempo_volta': '1:02.769', 'vel_media_volta': '44,334'}, 
        {'hora': '23:51:18.576', 'cod_piloto': '033', 'nome_piloto': 'R.BARRICHELLO', 'n_volta': '3\t', 'tempo_volta': '1:03.716', 'vel_media_volta': '43,675'}, 
        {'hora': '23:52:17.003', 'cod_piloto': '038', 'nome_piloto': 'F.MASSA', 'n_volta': '4\t', 'tempo_volta': '1:02.787', 'vel_media_volta': '44,321'}, 
        {'hora': '23:52:22.586', 'cod_piloto': '033', 'nome_piloto': 'R.BARRICHELLO', 'n_volta': '4\t', 'tempo_volta': '1:04.010', 'vel_media_volta': '43,474'}
    ]

brokenLaps = [
        {'hora': '23:49:08.277', 'cod_piloto': '038', 'nome_piloto': 'F.MASSA', 'n_volta': '1', 'tempo_volta': '1:02', 'vel_media_volta': '44,275'}, 
        {'hora': '23:49:10.858', 'cod_piloto': '033', 'nome_piloto': 'R.BARRICHELLO', 'n_volta': '1\t', 'tempo_volta': '1:04', 'vel_media_volta': '43,243'}, 
        {'hora': '23:50:11.447', 'cod_piloto': '038', 'nome_piloto': 'F.MASSA', 'n_volta': '2\t', 'tempo_volta': '1:03', 'vel_media_volta': '44,053'}, 
        {'hora': '23:50:14.860', 'cod_piloto': '033', 'nome_piloto': 'R.BARRICHELLO', 'n_volta': '2\t', 'tempo_volta': '1:04', 'vel_media_volta': '43,48'}, 
        {'hora': '23:51:14.216', 'cod_piloto': '038', 'nome_piloto': 'F.MASSA', 'n_volta': '3\t', 'tempo_volta': '1:02', 'vel_media_volta': '44,334'}, 
        {'hora': '23:51:18.576', 'cod_piloto': '033', 'nome_piloto': 'R.BARRICHELLO', 'n_volta': '3\t', 'tempo_volta': '1:03', 'vel_media_volta': '43,675'}, 
        {'hora': '23:52:17.003', 'cod_piloto': '038', 'nome_piloto': 'F.MASSA', 'n_volta': '4\t', 'tempo_volta': '1:02', 'vel_media_volta': '44,321'}, 
        {'hora': '23:52:22.586', 'cod_piloto': '033', 'nome_piloto': 'R.BARRICHELLO', 'n_volta': '4\t', 'tempo_volta': '1:04', 'vel_media_volta': '43,474'}]

pilots_code = ['038', '033']

import datetime
finalInfosKeepRunning = [
    {'cod_piloto': '038', 'melhor_volta': datetime.timedelta(0, 62, 769000), 'vel_media': 44.246, 'nome_piloto': 'F.MASSA', 'voltas_completadas': 4, 'tempo_total_de_prova': datetime.timedelta(0, 251, 578000)}, 
    {'cod_piloto': '033', 'melhor_volta': datetime.timedelta(0, 63, 716000), 'vel_media': 43.468, 'nome_piloto': 'R.BARRICHELLO', 'voltas_completadas': 4, 'tempo_total_de_prova': datetime.timedelta(0, 256, 80000)}
]

finalInfosStop = [
    {'tempo_total_de_prova': datetime.timedelta(0, 251, 578000), 'cod_piloto': '038', 'nome_piloto': 'F.MASSA', 'vel_total': 176.983, 'vel_media': 44.246, 'voltas_completadas': '4\t', 'melhor_volta': datetime.timedelta(0, 62, 769000)}, 
    {'tempo_total_de_prova': datetime.timedelta(0, 192, 70000), 'cod_piloto': '033', 'nome_piloto': 'R.BARRICHELLO', 'vel_total': 130.398, 'vel_media': 43.466, 'voltas_completadas': '3\t', 'melhor_volta': datetime.timedelta(0, 63, 716000)}
]


sortedFinalInfos = [
    {'cod_piloto': '038', 'melhor_volta': datetime.timedelta(0, 62, 769000), 'vel_media': 44.246, 'nome_piloto': 'F.MASSA', 'voltas_completadas': 4, 'tempo_total_de_prova': datetime.timedelta(0, 251, 578000), 'posicao': 1}, 
    {'cod_piloto': '033', 'melhor_volta': datetime.timedelta(0, 63, 716000), 'vel_media': 43.468, 'nome_piloto': 'R.BARRICHELLO', 'voltas_completadas': 4, 'tempo_total_de_prova': datetime.timedelta(0, 256, 80000), 'posicao': 2}
]

bestLap = {'tempo': datetime.timedelta(0, 62, 769000), 'piloto': 'F.MASSA'}

finalResultKeepRunning = [
    {'cod_piloto': '038', 'melhor_volta': datetime.timedelta(0, 62, 769000), 'vel_media': 44.246, 'nome_piloto': 'F.MASSA', 'voltas_completadas': 4, 'tempo_total_de_prova': datetime.timedelta(0, 251, 578000), 'posicao': 1}, 
    {'cod_piloto': '033', 'melhor_volta': datetime.timedelta(0, 63, 716000), 'vel_media': 43.468, 'nome_piloto': 'R.BARRICHELLO', 'voltas_completadas': 4, 'tempo_total_de_prova': datetime.timedelta(0, 256, 80000), 'posicao': 2}
]

finalResultStop = [
    {'tempo_total_de_prova': datetime.timedelta(0, 251, 578000), 'cod_piloto': '038', 'nome_piloto': 'F.MASSA', 'vel_total': 176.983, 'vel_media': 44.246, 'voltas_completadas': '4\t', 'melhor_volta': datetime.timedelta(0, 62, 769000), 'posicao': 1}, 
    {'tempo_total_de_prova': datetime.timedelta(0, 192, 70000), 'cod_piloto': '033', 'nome_piloto': 'R.BARRICHELLO', 'vel_total': 130.398, 'vel_media': 43.466, 'voltas_completadas': '3\t', 'melhor_volta': datetime.timedelta(0, 63, 716000), 'posicao': 2}
]