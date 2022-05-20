import android_auto_play_opencv as am
from character import Character


class Controller:
    def __init__(self, template_dict):
        self.aapo = am.AapoManager('C:\\Users\\manab\\platform-tools\\')
        self.template_dict = template_dict

    def activate_app(self):
        self.aapo.start('com.supercell.clashroyale/com.supercell.titan.GameApp')
        self.sleep(10)

    def start_1vs1(self):
        # パーティ
        self.aapo.touchPos(760, 1575)
        self.sleep(3)
        # 1対1エンタメ
        self.aapo.touchPos(780, 1626)
        self.sleep(10)

    def screencap(self):
        self.aapo.screencap()

    def may_generate_character(self, file_name, to_, swipe_ms=300):
        res, from_= self.aapo.chkImg2(self.template_dict + "\\" + file_name)
        if res:
            self.generate_character(from_, to_, swipe_ms)
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
