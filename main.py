import android_auto_play_opencv as am
import random
from character import Character
from stage import Stage
from controller import Controller


def main():
    stage = Stage()

    # miner         = Character("miner")
    # rocket_gunner = Character("rocket_gunner")

    # miner.set_pos(stage.get_left_enemy())
    # balloon.set_pos((35, 1100))
    # knight.set_pos(stage.get_right_bridge())

    # specific_chars = [miner, knight, rocket_gunner]

    adb_path = 'C:\\Program Files\\Nox\\bin\\'
    template_dict = 'C:\\Users\\manab\\github_\\auto_play\\template'
    ctr = Controller(adb_path, template_dict)

    # ctr.activate_app()

    for i in range(150):
        print(i)
        ctr.sleep(10)
        ctr.start_1vs1()

        ctr.screencap()
        ctr.may_touch("stage_ok.jpg")   # 勝っても報酬はもらえません

        while True:
            ctr.sleep(1)
            ctr.screencap()

            if ctr.may_touch("stage_ok.jpg"):
                break

            """
            for char in specific_chars:
                if ctr.may_generate_character(char.get_file_name(), char.get_pos()):
                    break
            """

            # 画像なしの場合、ランダムカード召喚
            r = random.randint(0, 3)
            card_pos = stage.get_card_pos(r)
            ctr.generate_character(card_pos, stage.get_random_pos())

            card_pos = stage.get_card_pos(r+1)
            ctr.generate_character(card_pos, stage.get_random_pos())

if __name__ == '__main__':
    main()
