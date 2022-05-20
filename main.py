import android_auto_play_opencv as am
import random
from character import Character
from stage import Stage
from controller import Controller


def main():
    miner         = Character("miner")
    balloon       = Character("balloon")
    knight        = Character("knight")
    rocket_gunner = Character("rocket_gunner")
    giant         = Character()
    dark_prince   = Character()
    gobrin_gang   = Character()
    elct          = Character()

    stage = Stage()

    miner.set_pos(stage.get_left_enemy())
    balloon.set_pos((35, 1100))
    knight.set_pos(stage.get_right_bridge())
    dark_prince.set_pos(stage.get_right_bridge())
    giant.set_pos(stage.get_random_pos())

    specific_char = [miner, balloon, knight, rocket_gunner]

    ctr = Controller('C:\\Users\\manab\\github_\\auto_play\\template')
    # ctr.activate_app()

    for i in range(100):
        ctr.start_1vs1()

        while True:
            ctr.screencap()

            if ctr.may_touch("stage_ok.jpg"):
                break

            for char in specific_char:
                if ctr.may_generate_character(char.get_file_name(), char.get_pos()):
                    break

            # 画像なしの場合、ランダムカード召喚
            card_pos = stage.get_card_pos(random.randint(0, 3))
            ctr.generate_character(card_pos, char.get_pos())

            ctr.sleep(1)


if __name__ == '__main__':
    main()
