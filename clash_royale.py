import android_auto_play_opencv as am

adbpath = 'C:\\Users\\manab\\platform-tools\\'

def main():
    aapo = am.AapoManager(adbpath)

    aapo.start('com.supercell.clashroyale/com.supercell.titan.GameApp')
    aapo.sleep(15)

    cards_x  = [ 350 , 550 , 750 , 950 ]
    cards_y  = [ 2104, 2104, 2104, 2104]
    stages_x = [ 197 , 408 , 677 , 987 ]
    stages_y = [ 1356, 1374, 1203, 1305]

    
    for i in range(1, 25):
        # パーティ
        aapo.touchPos(760, 1575)
        aapo.sleep(3)
        # 1対1エンタメ
        aapo.touchPos(780, 1626)
        aapo.sleep(10)

        j = 0
        while True:
            aapo.screencap()
            if aapo.chkImg('C:\\Users\\manab\\github_\\auto_play\\template\\stage_ok.jpg'):
                aapo.touchImg('C:\\Users\\manab\\github_\\auto_play\\template\\stage_ok.jpg')
                break

            r = j%4
            j += 1
            aapo.swipeTouchPos(cards_x[r], cards_y[r], stages_x[r]+j, stages_y[r]+j, 300)
            aapo.sleep(r)

        aapo.sleep(10)

    aapo.end('com.supercell.clashroyale')


if __name__ == '__main__':
    main()


"""
    カード1 : 350, 2104
    カード2 : 550, 2104
    カード3 : 750, 2104
    カード4 : 950, 2104
"""
