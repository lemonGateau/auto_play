import android_auto_play_opencv as am
from character import Character


class Controller:
    def __init__(self, adb_path, template_dict):
        self.aapo = am.AapoManager(adb_path)

        self.template_dict = template_dict

    def activate_app(self):
        self.aapo.start('com.supercell.clashroyale/com.supercell.titan.GameApp')
        self.sleep(30)

    def start_1vs1(self):
        # パーティ
        self.aapo.touchPos(760, 1550)
        self.sleep(5)
        # 1対1エンタメ
        self.aapo.touchPos(770, 1590)
        self.sleep(5)

    def screencap(self):
        self.aapo.screencap()

    def may_generate_character(self, file_name, to_, swipe_ms=400):
        res, x, y= self.aapo.chkImg2(self.template_dict + "\\" + file_name)
        if res:
            self.generate_character((x, y), to_, swipe_ms)
        return res

    def generate_character(self, from_, to_, swipe_ms=300):
        self.aapo.swipeTouchPos(from_[0], from_[1], to_[0], to_[1], swipe_ms)

    def may_touch(self, file_name):
        path = self.template_dict + "\\" + file_name

        if self.aapo.chkImg(path):
            self.aapo.touchImg(path)
            return True
        return False

    def sleep(self, sec):
        self.aapo.sleep(sec)

    def inactivate_app(self):
        self.aapo.end('com.supercell.clashroyale')
