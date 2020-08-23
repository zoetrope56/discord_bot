import random

class Game():
    def __init__(self):
        self.bullet = random.randint(1,6)
        self.fire = random.randint(1,6)
        self.response = str()
        self.cylinder = list()
    
    def init_bullet(self):
        self.bullet = random.randint(1,6)
    
    def init_fire(self):
        self.fire = random.randint(1,6)
    
    def init_cylinder(self):
        self.cylinder = list()
    
    def action(self):
        # 중복발사 방지
        while self.fire in self.cylinder:
            self.init_fire()
        
        # 발사 위치는 총알이 들어있는 위치와 같은가?
        if self.fire == self.bullet:
            self.response = 'Boom!\n-사망-\n게임에서 탈락하셨습니다.'
            self.init_cylinder()
            self.init_bullet()
        else:
            self.cylinder.append(self.fire)
            self.response = 'click!\n-생존-\n다음 플레이어를 기다려주세요.\n확률 1/'+str(6-len(self.cylinder))

        return self.response
