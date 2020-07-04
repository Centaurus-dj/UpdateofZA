label mini_jeux1:
$ niveau = 3
init python:

    class PongDisplayable(renpy.Displayable):

        def __init__(self):

            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            self.PADDLE_WIDTH = 12
            self.PADDLE_HEIGHT = 95
            self.PADDLE_X = 240
            self.BALL_WIDTH = 20
            self.BALL_HEIGHT = 20
            self.COURT_TOP = 129
            self.COURT_BOTTOM = 650

            # Some displayables we use.
            self.paddle = Solid("#ffffff", xsize=self.PADDLE_WIDTH, ysize=self.PADDLE_HEIGHT)
            self.ball = Solid("#ffffff", xsize=self.BALL_WIDTH, ysize=self.BALL_HEIGHT)

            # If the ball is stuck to the paddle.
            self.stuck = True

            # The positions of the two paddles.
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery

            # The speed of the computer.
            self.computerspeed = 490.0

            # The position, delta-position, and the speed of the
            # ball.
            self.bx = self.PADDLE_X + self.PADDLE_WIDTH + 10
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            self.bspeed = 600.0

            # The time of the past render-frame.
            self.oldst = None

            # The winner.
            self.winner = None

        def visit(self):
            return [ self.paddle, self.ball ]

        # Recomputes the position of the ball, handles bounces, and
        # draws the screen.
        def render(self, width, height, st, at):

            # The Render object we'll be drawing into.
            r = renpy.Render(width, height)

            # Figure out the time elapsed since the previous frame.
            if self.oldst is None:
                self.oldst = st

            dtime = st - self.oldst
            self.oldst = st

            # Figure out where we want to move the ball to.
            speed = dtime * self.bspeed
            oldbx = self.bx

            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed

            # Move the computer's paddle. It wants to go to self.by, but
            # may be limited by it's speed limit.
            cspeed = self.computerspeed * dtime
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

            # Handle bounces.

            # Bounce off of top.
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play(audio.pong_beep, channel=0)

            # Bounce off bottom.
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy

                if not self.stuck:
                    renpy.sound.play(audio.pong_beep, channel=0)

            # This draws a paddle, and checks for bounces.
            def paddle(px, py, hotside):

                # Render the paddle image. We give it an 800x600 area
                # to render into, knowing that images will render smaller.
                # (This isn't the case with all displayables. Solid, Frame,
                # and Fixed will expand to fill the space allotted.)
                # We also pass in st and at.
                pi = renpy.render(self.paddle, width, height, st, at)

                # renpy.render returns a Render object, which we can
                # blit to the Render we're making.
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                    hit = False

                    if oldbx >= hotside >= self.bx:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True

                    elif oldbx <= hotside <= self.bx:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True

                    if hit:
                        renpy.sound.play(audio.pong_boop, channel=1)
                        self.bspeed *= 1.10

            # Draw the two paddles.
            paddle(self.PADDLE_X, self.playery, self.PADDLE_X + self.PADDLE_WIDTH)
            paddle(width - self.PADDLE_X - self.PADDLE_WIDTH, self.computery, width - self.PADDLE_X - self.PADDLE_WIDTH)

            # Draw the ball.
            ball = renpy.render(self.ball, width, height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                          int(self.by - self.BALL_HEIGHT / 2)))

            # Check for a winner.
            if self.bx < -50:
                self.winner = "programmeur"

                # Needed to ensure that event is called, noticing
                # the winner.
                renpy.timeout(0)

            elif self.bx > width + 50:
                self.winner = "joueur"
                renpy.timeout(0)

            # Ask that we be re-rendered ASAP, so we can show the next
            # frame.
            renpy.redraw(self, 0)

            # Return the Render object.
            return r

        # Handles events.
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

screen pong():

    default pong = PongDisplayable()

    add "bg pong field"

    add pong

    text _("joueur"):
        xpos 240
        xanchor 0.5
        ypos 25
        size 40

    text _("Programmeur"):
        xpos (1280 - 240)
        xanchor 0.5
        ypos 25
        size 40

    if pong.stuck:
        text _("Cliquez pour commencer"):
            xalign 0.5
            ypos 50
            size 40
label play_pongtown1:

    window hide  # Hide the window and  quick menu while in pong
    $ quick_menu = False

    call screen pong

    $ quick_menu = True
    window show
hide zya
show prog at right


if _return == "programmeur":

    a "J'ai gagné !"
    return
else:

    a "Tu as gagné !!"
    $ pongcorrect = True
    return















































































################################################################################
###                           PUZZLE                                         ###
################################################################################






































label clicker:
    init python:
        # окно игры в центре экрана
        import os
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        # автоматическое объявление изображений
        config.automatic_images_minimum_components = 1
        config.automatic_images = [' ', '_', '/']
        config.automatic_images_strip = ['images']
        # вспышка
        flash  = Fade(.25, 0, .5, color="#fff")
        flash2 = Fade(.25, 0, .5, color="#222")

    # настройки игры:
        # максимальное значение шкалы
        max_points = 100
        # название картинки (без нумерации кадров)
        img_name = "n"
        # первый и последний кадры анимации
        minN = 1
        maxN = 14
        # значение, на которое прибавляется шкала при клике
        # (т.е. сложность игры. 2.0 - очень сложно, 3.0 - легко)
        points_plus = 2.5

    # переменные по умолчанию
        # при желании можно поменять и это значение,
        # чтобы точнее подобрать баланс игры
        points_minus = 1.0
        # допустимое время между кликами или
        # скорость анимации (время между сменой кадров)
        ani_time = .1
        # текущий кадр
        number = 0
        # инкремент кадра (+1/-1)
        plus = 1
        # шкала, которую нужно заполнить
        points = 0
        # недавно был клик
        clicked = True
        # смена кадров анимации, если клик был недавно
        # и перерисовка экрана, чтобы увидеть изменения
        def NextFrameF():
            global points, number, plus, clicked
            # если клик был недавно, то продолжаем анимацию,
            # иначе следующего кадра не будет. пауза
            if clicked:
                # следующий/предыдущий кадр
                number += plus
                # если за пределы числа кадров, то анимация в обратную сторону
                if number > maxN:
                    number = maxN - 1
                    plus = -plus
                if number < minN:
                    number = minN + 1
                    plus = -plus
            # уменьшение шкалы, если давно не было клика
            points -= points_minus
            if points < 0:
                points = 0
            clicked = False
            # перерисовка экрана
            renpy.restart_interaction()
        # функция → action
        NextFrame = renpy.curry(NextFrameF)

    # экран игры
    screen clicker():
        # это чтобы игра не продолжилась по клику мышкой
        modal True
        # сбрасываем настройки игры при появлении экрана
        on "show" action [SetVariable("number", 0), SetVariable("plus", 1), SetVariable("clicked", True)]
        # меняем кадр, если клик был недавно,
        # и проверяем на проигрыш
        timer ani_time repeat True action [NextFrame(), If(points <= 0, true=Return(False), false=NullAction())]
        # картинка с анимацией
        add img_name + str(number)
        # отображаем невидимую кнопку для кликов
        # по нажатию прибавляем шкалу и устанавливаем флаг клика
        button:
            text _(" ")
            xfill True
            yfill True
            background "#00000001"
            # если шкала полная, то конец игры, победа
            action [SetVariable("points", points + points_plus), SetVariable("clicked", True), If(points >= max_points, true=Return(True), false=NullAction())]
        # альтернативное нажатие с клавиатуры
        key "K_SPACE" action [SetVariable("points", points + points_plus), SetVariable("clicked", True), If(points >= max_points, true=Return(True), false=NullAction())]
        # индикатор
        vbar value StaticValue(points, max_points):
            align (0, 0) # положение на экране
            maximum (150, 150) # размеры
            left_bar "heartempty" # пустое сердце
            right_bar "heart" # полное сердце
            thumb None # тут можно поставить разделитель
            thumb_shadow None # и тень

    label starter:
        # всякие ненужные штуки для оформления
        scene expression (img_name + "0")
        pause .5
        show expression Text("Prêt(e) ?!") at truecenter as txt
        with dissolve
        pause
        hide txt
        # начать с 10 очков, чтобы не проиграть сразу же
        $ points = 10

        # ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
        call screen clicker # ←  игра
        # ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑ ↑

        # дальше снова пошли всякие ненужные вещи:
        # показываем результаты игры
        if _return:
            # перематываем анимацию до последнего кадра
            while number < maxN:
                $ number += 1
                scene expression (img_name + str(number))
                $ renpy.pause(ani_time, hard=True)
            scene expression (img_name + str(maxN))
            with flash
            show expression Text("Tu as gagné !") at truecenter as txt
        else:
            # перематываем анимацию до первого кадра
            while number > 1:
                $ number -= 1
                scene expression (img_name + str(number))
                $ renpy.pause(ani_time, hard=True)
            scene expression (img_name + "0")
            with flash2
            show expression Text("Tu as perdu !") at truecenter as txt
        # жесткая пауза на случай, если игрок всё еще лупит по кнопке
        $ renpy.pause(1.0, hard=True)
        hide txt
        with dissolve
        return "minijeux"














































    # Это мини-игра по поиску предметов
    # сохранить этот код в файл game.rpy в корне игры

    # Вызывается примерно так:

    # $ InitGame("bg_room", 5.0, True, (735, 300), "figure1", (640, 226), "figure2", (288, 38), "figure3", (115, 260), "figure4")
    # $ StartGame()

    # где bg_room - имя файла фона без указания расширения .jpg
    # 5.0 - количество секунд на выполнение поиска
    # если <= 0, таймер отключен, взять можно лишь один предмет, он сохранится в oRes
    # (735, 300), "figure1" - координаты и имя файла предмета
    # без расширения .png
    # предметов может быть сколько угодно
    # все фоны и картинки предметов должны быть в папке images
    # в oRes - истина или ложь (уложились в отведенное время или нет) - либо название предмета
    # количество найденных предметов в переменной oLen
    # общее количество предметов в переменной maxLen

    # $ GameAsBG() # показывает экран с картинками в качестве фона, не кликабельного

    # в папке sounds должен лежать звук «click.mp3»
    # либо, если его нет, то нужно закомментировать строку:
    # renpy.play("sounds/click.mp3", channel="sound")

    init python:
        # окно по центру экрана
        import os
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        # автоматическое объявление спрайтов
        config.automatic_images_minimum_components = 1
        config.automatic_images = [' ', '_', '/']
        config.automatic_images_strip = ["images"]
        oXY = []
        oN = []
        oLen = 0
        maxLen = 0
        oBg = ""
        oLast = -1
        oTime = 0.0
        oMaxTime = 5.0
        needTimer = False
        oActive = False
        oRes = False

        # Инициализация игры, размещение предметов на экране
        def InitGame(bg, time, *args):
            global oBg, oXY, oN, oLen, maxLen, oLast, oTime, oMaxTime, oActive, needTimer, oRes
            oXY = []
            oN = []
            oLen = 0
            oBg = bg
            oLast = -1
            oTime = time
            oMaxTime = time
            maxLen = 0
            oActive = True
            oRes = False
            if oTime > 0.0:
                needTimer = True
            for xy, obj_name in zip(args[0::2], args[1::2]):
                oXY.append(xy)
                oN.append(obj_name)
                maxLen += 1

        # Запуск игры
        def StartGame():
            global oActive
            oActive = True
            need = True
            while need:
                renpy.call_screen("game", _layer="master")
                need = oRes == False
                if needTimer and (oTime <= .0):
                    need = False

        # Показать экран игры в виде неактивного фона
        # Уже найденные предметы не будут отображаться
        def GameAsBG():
            global oActive
            oActive = False
            renpy.show_screen("game", _layer="master")

        # Обработчик клика по предмету
        def o_click(i):
            global oLen, oRes
            if i >= 0:
                if oN[i]:
                    temp = oN[i]
                    oN[i] = ""
                    oLen += 1
                    renpy.play("sounds/click.mp3", channel="sound")
                    renpy.restart_interaction()
                    if needTimer:
                        if oLen >= maxLen:
                            oRes = True
                    else:
                        oRes = temp
        oClick = renpy.curry(o_click)

    # Собственно экран игры, запускать из функции StartGame()
    screen jeux():
        modal True
        if oActive and needTimer:
            timer 0.01 repeat True action [SetVariable("oTime", oTime-.01), If(oTime <= .0, true=[Return()])]
        add oBg
        for i in range(0, len(oN)):
            if oN[i]:
                imagebutton:
                    focus_mask True
                    pos(oXY[i])
                    idle oN[i]
                    hover oN[i]
                    # можно продублировать картинки предметов,
                    # назвав их "images/имяпредмета_hover.png"
                    # и высветить их в графическом редакторе
                    # и заменить строку выше на строку ниже
                    # тогда при наведении курсора, они будут подсвечиваться
                    # hover oN[i] + " hover"
                    if oActive:
                        action [oClick(i), Return()]
                    else:
                        action []
        if oActive and needTimer:
            # if oTime > .1:
                # text "[oTime]" align(.1, .1) size 48
            # else:
                # text "0.0" align(.1, .1) size 48
            bar value StaticValue(oTime, oMaxTime):
                align(.5, .001)
                xmaximum 400
                ymaximum 20
                left_bar Frame("slider_left.png", 10, 10)
                right_bar Frame("slider_right.png", 10, 10)
                thumb None
                thumb_shadow None
