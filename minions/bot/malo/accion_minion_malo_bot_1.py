import random
import sqlite3

import pygame
import math


class Accion_minion_malo_bot_1:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.contador_animacion = 0
        self.health = 200  # Barra de vida
        self.max_health = 200  # Barra de vida
        self.vel = 3
        self.path = [(1348, 289), (1348, 292), (1348, 295), (1348, 298), (1348, 301), (1348, 304), (1348, 307),
                     (1348, 310), (1348, 313), (1348, 316), (1348, 319), (1348, 322), (1348, 325), (1348, 328),
                     (1348, 331), (1348, 334), (1348, 337), (1348, 340), (1348, 343), (1348, 346), (1348, 349),
                     (1348, 352), (1348, 355), (1348, 358), (1348, 361), (1348, 364), (1348, 367), (1348, 370),
                     (1348, 373), (1348, 376), (1348, 379), (1348, 382), (1348, 385), (1348, 388), (1348, 391),
                     (1348, 394), (1348, 397), (1348, 400), (1348, 403), (1348, 406), (1348, 409), (1348, 412),
                     (1348, 415), (1348, 418), (1348, 421), (1348, 424), (1348, 427), (1348, 430), (1348, 433),
                     (1348, 436), (1348, 439), (1348, 442), (1348, 445), (1348, 448), (1348, 451), (1348, 454),
                     (1348, 457), (1348, 460), (1348, 463), (1348, 466), (1348, 469), (1348, 472), (1348, 475),
                     (1348, 478), (1348, 481), (1348, 484), (1348, 487), (1348, 490), (1348, 493), (1348, 496),
                     (1348, 499), (1348, 502), (1348, 505), (1348, 508), (1348, 511), (1348, 514), (1348, 517),
                     (1348, 520), (1348, 523), (1348, 526), (1348, 529), (1348, 532), (1348, 535), (1348, 538),
                     (1348, 541), (1348, 544), (1348, 547), (1348, 550), (1348, 553), (1348, 556), (1348, 559),
                     (1348, 562), (1348, 565), (1348, 568), (1348, 571), (1348, 574), (1348, 577), (1348, 580),
                     (1348, 583), (1348, 586), (1348, 589), (1348, 592), (1348, 595), (1348, 598), (1348, 601),
                     (1348, 604), (1348, 607), (1348, 610), (1348, 613), (1348, 616), (1348, 619), (1348, 622),
                     (1348, 625), (1348, 628), (1348, 631), (1348, 634), (1348, 637), (1348, 640), (1348, 643),
                     (1348, 646), (1348, 649), (1348, 652), (1348, 655), (1348, 658), (1348, 661), (1348, 664),
                     (1348, 667), (1348, 670), (1348, 673), (1348, 676), (1348, 679), (1348, 682), (1348, 685),
                     (1348, 688), (1348, 691), (1348, 694), (1348, 697), (1348, 700), (1348, 703), (1348, 706),
                     (1348, 709), (1348, 712), (1348, 715), (1348, 718), (1348, 721), (1348, 724), (1348, 724),
                     (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724),
                     (1345, 727), (1342, 730), (1339, 733), (1336, 736), (1333, 739), (1330, 742), (1327, 745),
                     (1324, 748)]

        self.path1 = [(1348, 289), (1348, 292), (1348, 295), (1348, 298), (1348, 301), (1348, 304), (1348, 307),
                      (1348, 310), (1348, 313), (1348, 316), (1348, 319), (1348, 322), (1348, 325), (1348, 328),
                      (1348, 331), (1348, 334), (1348, 337), (1348, 340), (1348, 343), (1348, 346), (1348, 349),
                      (1348, 352), (1348, 355), (1348, 358), (1348, 361), (1348, 364), (1348, 367), (1348, 370),
                      (1348, 373), (1348, 376), (1348, 379), (1348, 382), (1348, 385), (1348, 388), (1348, 391),
                      (1348, 394), (1348, 397), (1348, 400), (1348, 403), (1348, 406), (1348, 409), (1348, 412),
                      (1348, 415), (1348, 418), (1348, 421), (1348, 424), (1348, 427), (1348, 430), (1348, 433),
                      (1348, 436), (1348, 439), (1348, 442), (1348, 445), (1348, 448), (1348, 451), (1348, 454),
                      (1348, 457), (1348, 460), (1348, 463), (1348, 466), (1348, 469), (1348, 472), (1348, 475),
                      (1348, 478), (1348, 481), (1348, 484), (1348, 487), (1348, 490), (1348, 493), (1348, 496),
                      (1348, 499), (1348, 502), (1348, 505), (1348, 508), (1348, 511), (1348, 514), (1348, 517),
                      (1348, 520), (1348, 523), (1348, 526), (1348, 529), (1348, 532), (1348, 535), (1348, 538),
                      (1348, 541), (1348, 544), (1348, 547), (1348, 550), (1348, 553), (1348, 556), (1348, 559),
                      (1348, 562), (1348, 565), (1348, 568), (1348, 571), (1348, 574), (1348, 577), (1348, 580),
                      (1348, 583), (1348, 586), (1348, 589), (1348, 592), (1348, 595), (1348, 598), (1348, 601),
                      (1348, 604), (1348, 607), (1348, 610), (1348, 613), (1348, 616), (1348, 619), (1348, 622),
                      (1348, 625), (1348, 628), (1348, 631), (1348, 634), (1348, 637), (1348, 640), (1348, 643),
                      (1348, 646), (1348, 649), (1348, 652), (1348, 655), (1348, 658), (1348, 661), (1348, 664),
                      (1348, 667), (1348, 670), (1348, 673), (1348, 676), (1348, 679), (1348, 682), (1348, 685),
                      (1348, 688), (1348, 691), (1348, 694), (1348, 697), (1348, 700), (1348, 703), (1348, 706),
                      (1348, 709), (1348, 712), (1348, 715), (1348, 718), (1348, 721), (1348, 724), (1348, 724),
                      (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724),
                      (1345, 727), (1342, 730), (1339, 733), (1336, 736), (1333, 739), (1330, 742), (1327, 745),
                      (1324, 748)]
        self.path2v = [(1348, 289), (1348, 292), (1348, 295), (1348, 298), (1348, 301), (1348, 304), (1348, 307),
                       (1348, 310), (1348, 313), (1348, 316), (1348, 319), (1348, 322), (1348, 325), (1348, 328),
                       (1348, 331), (1348, 334), (1348, 337), (1348, 340), (1348, 343), (1348, 346), (1348, 349),
                       (1348, 352), (1348, 355), (1348, 358), (1348, 361), (1348, 364), (1348, 367), (1348, 370),
                       (1348, 373), (1348, 376), (1348, 379), (1348, 382), (1348, 385), (1348, 388), (1348, 391),
                       (1348, 394), (1348, 397), (1348, 400), (1348, 403), (1348, 406), (1348, 409), (1348, 412),
                       (1348, 415), (1348, 418), (1348, 421), (1348, 424), (1348, 427), (1348, 430), (1348, 433),
                       (1348, 436), (1348, 439), (1348, 442), (1348, 445), (1348, 448), (1348, 451), (1348, 454),
                       (1348, 457), (1348, 460), (1348, 463), (1348, 466), (1348, 469), (1348, 472), (1348, 475),
                       (1348, 478), (1348, 481), (1348, 484), (1348, 487), (1348, 490), (1348, 493), (1348, 496),
                       (1348, 499), (1348, 502), (1348, 505), (1348, 508), (1348, 511), (1348, 514), (1348, 517),
                       (1348, 520), (1348, 523), (1348, 526), (1348, 529), (1348, 532), (1348, 535), (1348, 538),
                       (1348, 541), (1348, 544), (1348, 547), (1348, 550), (1348, 553), (1348, 556), (1348, 559),
                       (1348, 562), (1348, 565), (1348, 568), (1348, 571), (1348, 574), (1348, 577), (1348, 580),
                       (1348, 583), (1348, 586), (1348, 589), (1348, 592), (1348, 595), (1348, 598), (1348, 601),
                       (1348, 604), (1348, 607), (1348, 610), (1348, 613), (1348, 616), (1348, 619), (1348, 622),
                       (1348, 625), (1348, 628), (1348, 631), (1348, 634), (1348, 637), (1348, 640), (1348, 643),
                       (1348, 646), (1348, 649), (1348, 652), (1348, 655), (1348, 658), (1348, 661), (1348, 664),
                       (1348, 667), (1348, 670), (1348, 673), (1348, 676), (1348, 679), (1348, 682), (1348, 685),
                       (1348, 688), (1348, 691), (1348, 694), (1348, 697), (1348, 700), (1348, 703), (1348, 706),
                       (1348, 709), (1348, 712), (1348, 715), (1348, 718), (1348, 721), (1348, 724), (1348, 724),
                       (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724),
                       (1345, 727), (1342, 730), (1339, 733), (1336, 736), (1333, 739), (1330, 742), (1327, 745),
                       (1324, 748), (1321, 751), (1318, 754), (1315, 757), (1312, 760), (1309, 763), (1306, 766),
                       (1303, 769), (1300, 772), (1297, 775), (1294, 778), (1291, 781), (1288, 784), (1285, 787),
                       (1282, 790), (1279, 793), (1276, 796), (1273, 799), (1270, 802), (1267, 805), (1264, 808),
                       (1261, 811), (1258, 814), (1255, 817), (1252, 820), (1249, 823), (1246, 826), (1243, 829),
                       (1240, 832), (1237, 835), (1234, 838), (1231, 841), (1228, 844), (1225, 847), (1222, 850),
                       (1219, 853), (1216, 856), (1213, 859), (1213, 859), (1213, 859), (1213, 859), (1213, 859),
                       (1213, 859), (1213, 859), (1213, 859), (1213, 859), (1213, 859), (1213, 859), (1213, 859),
                       (1213, 859), (1213, 859), (1210, 859), (1207, 859), (1204, 859), (1201, 859), (1198, 859),
                       (1195, 859), (1192, 859), (1189, 859), (1186, 859), (1183, 859), (1180, 859), (1177, 859),
                       (1174, 859), (1171, 859), (1168, 859), (1165, 859), (1162, 859), (1159, 859), (1156, 859),
                       (1153, 859), (1150, 859), (1147, 859), (1144, 859), (1141, 859), (1138, 859), (1135, 859),
                       (1132, 859), (1129, 859), (1126, 859), (1123, 859), (1120, 859), (1117, 859), (1114, 859),
                       (1111, 859), (1108, 859), (1105, 859), (1102, 859), (1099, 859), (1096, 859), (1093, 859),
                       (1090, 859), (1087, 859), (1084, 859), (1081, 859), (1078, 859), (1075, 859), (1072, 859),
                       (1069, 859), (1066, 859), (1063, 859), (1060, 859), (1057, 859), (1054, 859), (1051, 859),
                       (1048, 859), (1045, 859), (1042, 859), (1039, 859), (1036, 859), (1033, 859), (1030, 859),
                       (1027, 859), (1024, 859), (1021, 859), (1018, 859), (1015, 859), (1012, 859), (1009, 859),
                       (1006, 859), (1003, 859), (1000, 859), (997, 859), (994, 859), (991, 859)]
        self.path3v = [(1348, 289), (1348, 292), (1348, 295), (1348, 298), (1348, 301), (1348, 304), (1348, 307),
                       (1348, 310), (1348, 313), (1348, 316), (1348, 319), (1348, 322), (1348, 325), (1348, 328),
                       (1348, 331), (1348, 334), (1348, 337), (1348, 340), (1348, 343), (1348, 346), (1348, 349),
                       (1348, 352), (1348, 355), (1348, 358), (1348, 361), (1348, 364), (1348, 367), (1348, 370),
                       (1348, 373), (1348, 376), (1348, 379), (1348, 382), (1348, 385), (1348, 388), (1348, 391),
                       (1348, 394), (1348, 397), (1348, 400), (1348, 403), (1348, 406), (1348, 409), (1348, 412),
                       (1348, 415), (1348, 418), (1348, 421), (1348, 424), (1348, 427), (1348, 430), (1348, 433),
                       (1348, 436), (1348, 439), (1348, 442), (1348, 445), (1348, 448), (1348, 451), (1348, 454),
                       (1348, 457), (1348, 460), (1348, 463), (1348, 466), (1348, 469), (1348, 472), (1348, 475),
                       (1348, 478), (1348, 481), (1348, 484), (1348, 487), (1348, 490), (1348, 493), (1348, 496),
                       (1348, 499), (1348, 502), (1348, 505), (1348, 508), (1348, 511), (1348, 514), (1348, 517),
                       (1348, 520), (1348, 523), (1348, 526), (1348, 529), (1348, 532), (1348, 535), (1348, 538),
                       (1348, 541), (1348, 544), (1348, 547), (1348, 550), (1348, 553), (1348, 556), (1348, 559),
                       (1348, 562), (1348, 565), (1348, 568), (1348, 571), (1348, 574), (1348, 577), (1348, 580),
                       (1348, 583), (1348, 586), (1348, 589), (1348, 592), (1348, 595), (1348, 598), (1348, 601),
                       (1348, 604), (1348, 607), (1348, 610), (1348, 613), (1348, 616), (1348, 619), (1348, 622),
                       (1348, 625), (1348, 628), (1348, 631), (1348, 634), (1348, 637), (1348, 640), (1348, 643),
                       (1348, 646), (1348, 649), (1348, 652), (1348, 655), (1348, 658), (1348, 661), (1348, 664),
                       (1348, 667), (1348, 670), (1348, 673), (1348, 676), (1348, 679), (1348, 682), (1348, 685),
                       (1348, 688), (1348, 691), (1348, 694), (1348, 697), (1348, 700), (1348, 703), (1348, 706),
                       (1348, 709), (1348, 712), (1348, 715), (1348, 718), (1348, 721), (1348, 724), (1348, 724),
                       (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724), (1348, 724),
                       (1345, 727), (1342, 730), (1339, 733), (1336, 736), (1333, 739), (1330, 742), (1327, 745),
                       (1324, 748), (1321, 751), (1318, 754), (1315, 757), (1312, 760), (1309, 763), (1306, 766),
                       (1303, 769), (1300, 772), (1297, 775), (1294, 778), (1291, 781), (1288, 784), (1285, 787),
                       (1282, 790), (1279, 793), (1276, 796), (1273, 799), (1270, 802), (1267, 805), (1264, 808),
                       (1261, 811), (1258, 814), (1255, 817), (1252, 820), (1249, 823), (1246, 826), (1243, 829),
                       (1240, 832), (1237, 835), (1234, 838), (1231, 841), (1228, 844), (1225, 847), (1222, 850),
                       (1219, 853), (1216, 856), (1213, 859), (1213, 859), (1213, 859), (1213, 859), (1213, 859),
                       (1213, 859), (1213, 859), (1213, 859), (1213, 859), (1213, 859), (1213, 859), (1213, 859),
                       (1213, 859), (1213, 859), (1210, 859), (1207, 859), (1204, 859), (1201, 859), (1198, 859),
                       (1195, 859), (1192, 859), (1189, 859), (1186, 859), (1183, 859), (1180, 859), (1177, 859),
                       (1174, 859), (1171, 859), (1168, 859), (1165, 859), (1162, 859), (1159, 859), (1156, 859),
                       (1153, 859), (1150, 859), (1147, 859), (1144, 859), (1141, 859), (1138, 859), (1135, 859),
                       (1132, 859), (1129, 859), (1126, 859), (1123, 859), (1120, 859), (1117, 859), (1114, 859),
                       (1111, 859), (1108, 859), (1105, 859), (1102, 859), (1099, 859), (1096, 859), (1093, 859),
                       (1090, 859), (1087, 859), (1084, 859), (1081, 859), (1078, 859), (1075, 859), (1072, 859),
                       (1069, 859), (1066, 859), (1063, 859), (1060, 859), (1057, 859), (1054, 859), (1051, 859),
                       (1048, 859), (1045, 859), (1042, 859), (1039, 859), (1036, 859), (1033, 859), (1030, 859),
                       (1027, 859), (1024, 859), (1021, 859), (1018, 859), (1015, 859), (1012, 859), (1009, 859),
                       (1006, 859), (1003, 859), (1000, 859), (997, 859), (994, 859), (991, 859), (988, 859),
                       (985, 859), (982, 859), (979, 859), (976, 859), (973, 859), (970, 859), (967, 859), (964, 859),
                       (961, 859), (958, 859), (955, 859), (952, 859), (949, 859), (946, 859), (943, 859), (940, 859),
                       (937, 859), (934, 859), (931, 859), (928, 859), (925, 859), (922, 859), (919, 859), (916, 859),
                       (913, 859), (910, 859), (907, 859), (904, 859), (901, 859), (898, 859), (895, 859), (892, 859),
                       (889, 859), (886, 859), (883, 859), (880, 859), (877, 859), (874, 859), (871, 859), (868, 859),
                       (865, 859), (862, 859), (859, 859), (856, 859), (853, 859), (850, 859), (847, 859), (844, 859),
                       (841, 859), (838, 859), (835, 859), (832, 859), (829, 859), (826, 859), (823, 859), (820, 859),
                       (817, 859), (814, 859), (811, 859), (808, 859), (805, 859), (802, 859), (799, 859), (796, 859)]
        self.path2d = [(1348, 289), (1348, 292), (1348, 295), (1348, 298), (1348, 301), (1348, 304), (1348, 307),
                       (1348, 310), (1348, 313), (1348, 316), (1348, 319), (1348, 322), (1348, 325), (1348, 328),
                       (1348, 331), (1348, 334), (1348, 337), (1348, 340), (1348, 343), (1348, 346), (1348, 349),
                       (1348, 352), (1348, 355), (1348, 358), (1348, 361), (1348, 364), (1348, 367), (1348, 370),
                       (1348, 373), (1348, 376), (1348, 379), (1348, 382), (1348, 385), (1348, 388), (1348, 391),
                       (1348, 394), (1348, 397), (1348, 400), (1348, 403), (1348, 406), (1348, 409), (1348, 412),
                       (1348, 415), (1348, 418), (1348, 421), (1348, 424), (1348, 427), (1348, 430), (1348, 433),
                       (1348, 436), (1348, 439), (1348, 442), (1348, 445), (1348, 448), (1348, 451), (1348, 454),
                       (1348, 457), (1348, 460), (1348, 463), (1348, 466), (1348, 469), (1348, 472), (1348, 475),
                       (1348, 478), (1348, 481), (1348, 484)]
        self.path3d = [(1348, 289), (1348, 292), (1348, 295), (1348, 298), (1348, 301), (1348, 304)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.cont_mover = 0
        self.dist_mover = 0

        self.nombre = ""
        self.estado = False
        self.torre_bot_1_derecha = 1
        self.torre_bot_2_derecha = 1
        self.torre_bot_1_izquierda = 1
        self.torre_bot_2_izquierda = 1

    def draw(self, win):
        self.nombre = self.id
        """
        DIBUJA A LOS ENEMIGOS CON LAS IMAGENES ESTABLECIDAS
        :param win: SURFACE
        """
        if self.estado:

            # ---
            conexion = sqlite3.connect('../datos.db')
            cursor = conexion.cursor()

            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_1_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_1_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_1_derecha = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_2_derecha
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_2_derecha"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_2_derecha = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_1_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_1_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_1_izquierda = r[0]
            # SELECT A LA BASE DE DATOS PARA VER ESTADO DE torre_bot_2_izquierda
            cursor.execute('SELECT estado FROM torres WHERE nombre = "torre_bot_2_izquierda"')
            resul = cursor.fetchall()
            for r in resul:
                self.torre_bot_2_izquierda = r[0]
            conexion.close()
            # ---

            """#CAMBIAR - Esto va fuera es para poder manipular el estado de las torres
            self.torre_bot_1_derecha = 1
            self.torre_bot_2_derecha = 1
            self.torre_bot_1_izquierda = 1
            self.torre_bot_2_izquierda = 1
            #-------"""

            # SELECCIONAR LAS IMAGENES SEGUN EL ESTADO DE LA PARTIDA
            if self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1324 and self.y == 748:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1348 and self.y == 724:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1348 and self.y >= 724:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1324 and self.y == 748:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1348 and self.y == 724:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1348 and self.y >= 724:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 1")
                # SELECCIONADOR DE IMAGENES EN FASE 1
                if self.x == 1324 and self.y == 748:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1348 and self.y == 724:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1348 and self.y >= 724:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2V")
                # SELECCIONADOR DE IMAGENES EN FASE 2 VICTORIA
                if self.x == 991 and self.y == 859 or self.x == 1213 and self.y == 859:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1348 and self.y == 724:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1348 and self.y >= 724:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 796 and self.y == 859 or self.x == 1213 and self.y == 859:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1348 and self.y == 724:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1348 and self.y >= 724:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3V")
                # SELECCIONADOR DE IMAGENES EN FASE 3 VICTORIA
                if self.x == 796 and self.y == 859 or self.x == 1213 and self.y == 859:
                    self.img = self.imgs3[self.contador_animacion]
                else:
                    if self.x == 1348 and self.y == 724:
                        self.img = self.imgs4[self.contador_animacion]
                    else:
                        if self.x <= 1348 and self.y >= 724:
                            self.img = self.imgs2[self.contador_animacion]
                        else:
                            self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2D")
                # SELECCIONADOR DE IMAGENES EN FASE 2 DERROTA
                if self.x == 1348 and self.y == 484:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 1348 and self.y == 304:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3D")
                # SELECCIONADOR DE IMAGENES EN FASE 3 DERROTA
                if self.x == 1348 and self.y == 304:
                    self.img = self.imgs4[self.contador_animacion]
                else:
                    self.img = self.imgs[self.contador_animacion]

            self.contador_animacion += 1
            # ESTE IF REINICIARA EL CONTADOR DE ANIMACIONES PAR A SIMULAR EL MOVIMIENTO DE LA IMGANES
            if self.contador_animacion >= len(self.imgs):
                self.contador_animacion = 0

            if self.health > 0:
                win.blit(self.img, (self.x, self.y))
            else:
                win.blit(self.img, (10000, 10000))
                self.health = 0
                self.path_pos = 0
            # if

            self.mover()
            if self.health > 0:
                self.draw_health_bar(win)

    def colision(self, X, Y):
        """
        DETECTA QUE EL SUBDITO RECIBA UNA COLISION
        :param x: INT
        :param y: INT
        :return: BOOLEAN
        """
        # ESTE IF COMPROBARA MEDIANTE LAS POSICIONES EN EL EJE SI HAN GOLPEADO AL SUBDITO
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def mover(self):
        """
        MUEVE AL SUBDITO
        :return: NADA
        """
        # SELECCIONAR EL PATH SEGUN EL ESTADO DE LA PARTIDA
        if self.health > 0:
            if self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                self.path = self.path1
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 1")
                self.path = self.path1
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 1")
                self.path = self.path1
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2V")
                self.path = self.path2v
            elif self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3V")
                self.path = self.path3v
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and not self.torre_bot_2_izquierda:
                print("FASE 3V")
                self.path = self.path3v
            elif not self.torre_bot_1_derecha and self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 2D")
                self.path = self.path2d
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3D")
                self.path = self.path3d
            elif not self.torre_bot_1_derecha and not self.torre_bot_2_derecha and not self.torre_bot_1_izquierda and self.torre_bot_2_izquierda:
                print("FASE 3D")
                self.path = self.path3d

        # TODA ESTA MIERDA ES PARA CALCULAR EL MOVIMIENTO ENTRE PUNTOS MEDIANTE EL TEOREMA DE PITAGORAS(VECTORES)
        if self.health <= 0:
            self.path_pos = 0
            print("he muerto")

        x1, y1 = self.path[self.path_pos]
        # print(self.path[self.path_pos], self.nombre)
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (672, 147)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.cont_mover += 1
        dirn = (x2 - x1, y2 - y1)

        mover_x, mover_y = (self.x + dirn[0] * self.cont_mover, self.y + dirn[1] * self.cont_mover)
        self.dis += math.sqrt((mover_x - x1) ** 2 + (mover_y - y1) ** 2)

        # VA AL SIGUIENTE PUNTO
        if self.dis >= move_dis:
            self.dis = 0
            self.cont_mover = 0
            """self.path_pos += 1
            if self.path_pos >= len(self.path):
                print(self.path_pos)
                return False"""
            # self.path_pos=0
            # self.path_pos += 1
            if self.path_pos < len(self.path) - 1:
                self.path_pos += 1
            else:
                return False

        if self.health > 0:  # SOLUCION a que el minion muera y dejen de atacar todos
            self.x = mover_x
            self.y = mover_y
        return True

    def hit(self):
        """
        DEVUELVE SI EL SUBDITO HA SIDO GOLPEADO Y LE RESTA VIDA
        :return: BOOLEAN
        """
        dmg = random.choice(range(0, 3))
        # dmg = 10
        self.health -= dmg
        if self.health <= 0:
            self.path_pos = 0
            self.health = 0

    def draw_health_bar(self, win):  # Barra de vida
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """

        length = 25
        move_by = length / self.max_health
        health_bar = round(move_by * self.health)

        pygame.draw.rect(win, (255, 0, 0), (self.x + 5, self.y - 5, length, 5), 0)
        pygame.draw.rect(win, (158, 18, 228), (self.x + 5, self.y - 5, health_bar, 5), 0)

    """
    Si el estado esta en True quiere decir que el minion se va a dibujar
    Si el estado esta en False quiere decir que el minion no se va a dibujar
    """

    def estado_partida(self):
        if self.estado:
            self.estado = False
        else:
            self.estado = True
            self.contador_animacion = 0
            self.health = 200  # Barra de vida
            self.x = self.path[0][0]
            self.y = self.path[0][1]
            self.dis = 0
            self.path_pos = 0
            self.cont_mover = 0
            self.dist_mover = 0
