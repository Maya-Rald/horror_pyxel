# The Oblivion Alley
# coding: UTF-8
import pyxel as px
import math
import random

# タイトル画面


class App():
    start = 0
    step = 0
    on = True

    def __init__(self):
        px.init(120, 70, fps=3)
        px.load("my_resource.pyxres", True, False, True, True)
        self.dead_x = 0  # skelton 初期位置
        self.exit_x = px.width
        px.run(self.update, self.draw)
        self.title()

    def title(self):
        px.cls(2)
        self.step = 0
        px.text(px.width/6, px.height/3, '"The Oblivion Alley"', 7)
        px.text(px.width/8, px.height/3*2, 'Press SPACEBAR to start', 0)
        if px.btn(px.KEY_SPACE):
            self.start = 1
            return self.start

    # ゲーム画面
    def game_screen(self):
        px.cls(0)
        self.scare_point = [46, 54, 26, 46]  # ビックリシーンs

        # プレイヤー表示（walking）
        if self.step in self.scare_point:
            px.blt(px.width/6, px.height/2, 0, 48, 0, 16, 16, 0)  # ビックリ２
        elif self.step % 2 == 0:
            if self.step >= 46 and self.step <= 51:
                px.blt(px.width/6, px.height/2, 0, 48, 0, 16, 16, 0)  # ビックリ２
            else:
                px.blt(px.width/6, px.height/2, 0, 0, 0, 16, 16, 0)
        else:
            if (self.step >= 46 and self.step <= 51) or self.step == 55:
                px.blt(px.width/6, px.height/2, 0, 32, 0, 16, 16, 0)
            else:
                px.blt(px.width/6, px.height/2, 0, 16, 0, 16, 16, 0)

        # horror 1
        if self.step == 3:
            self.horror_1(0)
        elif self.step == 26:
            self.horror_1(5)

        # horror 2
        if self.step > 20 and self.step < 26:
            self.flash()

        # horror3-1
        if self.step > 40 and self.step < 46:
            self.flash()

        # horror3-2
        if self.step >= 46 and self.step <= 51:
            self.skelton()
        if self.step >= 52 and self.step < 55:
            self.flash()
        if self.step >= 55:
            self.dead_skelton()

        # exit appear
        if self.step >= 90:
            self.exit()

        px.text(110, 3, "{self.step}", 7)    # only for debugging

    def horror_1(self, music_num):  # ホラー演出１・２： BGM
        px.play(0, music_num, loop=True)

    def skelton(self):  # ホラー演出３
        # music
        px.stop()
        px.play(0, 1, loop=True)
        # boss skelton
        px.blt(self.boss_x, px.height/4, 0, 0, 32, 32, 32, 0)
        # bloody skelton
        px.blt(self.blood_x, px.height/2, 0, 16, 16, 16, 16, 0)
        px.blt(self.blood_x+15, px.height/2, 0, 16, 16, 16, 16, 0)

    def dead_skelton(self):
        # dead skelton
        self.red_eye = random.randint(0, 9)
        for i in range(10):
            if i == self.red_eye:
                px.blt(self.dead_x+i*24, px.height/5*3+4, 0, 48, 16, 16, 16, 0)
            else:
                px.blt(self.dead_x+i*24, px.height/5*3+4, 0, 0, 16, 16, 16, 0)

    def option(self):
        px.stop()
        px.text(px.width/3+20, px.height/4, 'Keep going?', 7)
        px.text(px.width/3+21, px.height/4+13, 'YES: Y-key', 7)
        px.text(px.width/3+23, px.height/4+20, 'NO: N-key', 8)
        if px.btnp(px.KEY_Y):
            px.play(0, 2, loop=True)
            self.step += 1
        elif px.btnp(px.KEY_N):
            self.step = -1
            # self.game_over()  #ここに入れるとだめ

    def exit(self):
        px.rect(self.exit_x, px.height/3+4, 16, 24, 7)

    def flash(self):
        px.play(0, 3, loop=False)
        if self.step % 2 == 0:
            px.cls(0)
        else:
            px.cls(8)

    def game_over(self):
        px.cls(8)
        px.text(px.width/3+3, px.height/2, 'Game Over', 0)
        if px.btnp(px.KEY_ENTER):
            self.start = 0

    def congrats(self):
        px.cls(7)
        px.stop()
        px.play(0, 4, loop=False)
        px.text(px.width/3, px.height/5*2, 'Game Clear!', 14)
        px.text(px.width/3-5, px.height/5*3, 'Congratulation', 10)
        self.on = False

    def update(self):
        # スペースが押されたら開始
        if self.start == 0:
            self.title()
        else:
            # horror3-3
            if self.step == 56:
                self.option()
            elif self.step == 108:
                if self.on == True:
                    self.congrats()
            elif self.step == -1:
                self.game_over()
            else:
                self.game_screen()
                # Step カウント：スペースが押された数をカウント
                if px.btn(px.KEY_SPACE):
                    self.step += 1
                    if self.step > 55:
                        self.dead_x -= 5
                    if self.step >= 90:
                        self.exit_x -= 5

        if self.step < 46:
            self.boss_x = px.width/6*5-20
            self.blood_x = px.width/6*2+10

        else:
            self.boss_x -= 0.5
            self.blood_x -= 3

    def draw(self):   # draw()空っぽ
        pass


App()
