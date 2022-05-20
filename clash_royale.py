import android_auto_play_opencv as am
import random

adbpath = 'C:\\Users\\manab\\platform-tools\\'

def main():
    aapo = am.AapoManager(adbpath)

    #aapo.start('com.supercell.clashroyale/com.supercell.titan.GameApp')
    #aapo.sleep(10)

    cards_x  = [350 , 550 , 750 , 950 ]
    cards_y  = [2104, 2104, 2104, 2104]
    stages_x = [197 , 408 , 477 , 387 ]
    stages_y = [1656, 1674, 1603, 1505]

    upper_left   = [35  , 350 ]
    upper_right  = [1000, 350 ]
    lower_left   = [35  , 1700]
    lower_right  = [1000, 1700]
    left_bridge  = [210 , 1150]
    right_bridge = [855 , 1150]
    left_enemy   = [122, 527  ]
    right_enemy  = [855, 1100 ]

    template_path = 'C:\\Users\\manab\\github_\\auto_play\\template'
    swipe_ms = 300

    for i in range(100):
        print(i)
        # パーティ
        aapo.touchPos(760, 1575)
        aapo.sleep(3)
        # 1対1エンタメ
        aapo.touchPos(780, 1626)
        aapo.sleep(10)

        while True:
            aapo.screencap()
            res, x, y = aapo.chkImg2(template_path + '\\miner.jpg')
            if res:
                aapo.swipeTouchPos(x, y, left_enemy[0], left_enemy[1], swipe_ms)
                continue

            res, x, y = aapo.chkImg2(template_path + '\\rocket_gunner.jpg')
            if res:
                aapo.swipeTouchPos(x, y, lower_left[0], lower_left[1], swipe_ms)
                continue

            res, x, y = aapo.chkImg2(template_path + '\\balloon.jpg')
            if res:
                aapo.swipeTouchPos(x, y, 35, 1100, swipe_ms)
                continue

            res, x, y = aapo.chkImg2(template_path + '\\knight.jpg')
            if res:
                aapo.swipeTouchPos(x, y, right_bridge[0], right_bridge[1], swipe_ms)
                continue

            res, x, y = aapo.chkImg2(template_path + '\\skelton_dragon.jpg')
            if res:
                aapo.swipeTouchPos(x, y, lower_right[0], lower_right[1], swipe_ms)
                continue

            res, x, y = aapo.chkImg2(template_path + '\\royale_hog.jpg')
            if res:
                aapo.swipeTouchPos(x, y, right_bridge[0], right_bridge[1], swipe_ms)
                continue

            r = random.randint(0, 3)
            d = random.randint(0, 30)
            aapo.swipeTouchPos(cards_x[r], cards_y[r], stages_x[r]+d, stages_y[r]+d, swipe_ms)

            # 試合終了
            if aapo.chkImg(template_path + '\\stage_ok.jpg'):
                aapo.touchImg(template_path + '\\stage_ok.jpg')
                break

            aapo.sleep(1)

        aapo.sleep(10)

    aapo.end('com.supercell.clashroyale')


if __name__ == '__main__':
    main()


"""
    card1 : 350, 2104
    card2 : 550, 2104
    card3 : 750, 2104
    card4 : 950, 2104

    stage_upper_left  : 55  , 350
    stage_upper_right : 1000, 350
    stage_lower_left  : 55  , 1700
    stage_lower_right : 1000, 1700
"""
