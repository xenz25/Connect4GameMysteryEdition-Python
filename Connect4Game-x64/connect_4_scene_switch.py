
class SCENE():
    def __init__(self):
        self.from_inside = False
        self.from_outside = False
        self.from_ingame_access = False
        self.from_home_access = False
        self.scene = 'LOGO'
        self.END = True
        self.__previous_scene = self.scene
        self.HOW_TO_PLAY_IS_SELECTED = False


    def get_SCENE(self):
        return self.scene

    def save_previous_SCENE(self):
        self.__previous_scene = self.get_SCENE()
        print('previous scene:',self.__previous_scene)

    def get_previous_SCENE(self):
        return self.__previous_scene

    def create_scene(self,scene):
        self.save_previous_SCENE()
        self.scene = scene


scenes = SCENE()

if __name__ == '__main__':
    print(scenes.get_SCENE())
