screen intro_loki:
    add "intro_loki" xalign 0.0 yalign 0.0

screen intro_herc:
    add "intro_herc" xalign 0.0 yalign 0.0

screen intro_dr:
    add "intro_dr" xalign 0.0 yalign 0.0

screen intro_loki_am:
    add "intro_loki_am" xalign 0.0 yalign 0.0

screen intro_herc_am:
    add "intro_herc_am" xalign 0.0 yalign 0.0

screen intro_dr_am:
    add "intro_dr_am" xalign 0.0 yalign 0.0

screen intro_am:
    add "intro_am" xalign 0.0 yalign 0.0

screen alt_day0_charsel:
    tag menu
    modal False
    imagemap:
        ground "intro_transparent"
        hotspot ((0, 0, 635, 1080)):
            hovered [Show("intro_loki", transition=Dissolve(0.5))]
            unhovered [Hide("intro_loki", transition=Dissolve(1.0))]
            action [Hide("intro_loki", transition=Dissolve(0.5)), SetVariable("loki", True), Jump("alt_day0_char")]
        hotspot ((635, 0, 652, 1080)):
            hovered [Show("intro_herc", transition=Dissolve(0.5))]
            unhovered [Hide("intro_herc", transition=Dissolve(1.0))]
            action [Hide("intro_herc", transition=Dissolve(0.5)), SetVariable("herc", True), Jump("alt_day0_char")]
        hotspot ((1287, 0, 634, 1080)):
            hovered [Show("intro_dr", transition=Dissolve(0.5))]
            unhovered [Hide("intro_dr", transition=Dissolve(1.0))]
            action [Hide("intro_dr", transition=Dissolve(0.5)), SetVariable("dr", True), Jump("alt_day0_char")]

screen alt_day0_charsel_am:
    tag menu
    modal False
    imagemap:
        ground "intro_transparent"
        hotspot ((0, 0, 498, 1080)):
            hovered [Show("intro_loki_am", transition=Dissolve(0.5))]
            unhovered [Hide("intro_loki_am", transition=Dissolve(1.0))]
            action [Hide("intro_loki_am", transition=Dissolve(0.5)), SetVariable("loki", True), Jump("alt_day0_char")]
        hotspot ((498, 0, 498, 1080)):
            hovered [Show("intro_herc_am", transition=Dissolve(0.5))]
            unhovered [Hide("intro_herc_am", transition=Dissolve(1.0))]
            action [Hide("intro_herc_am", transition=Dissolve(0.5)), SetVariable("herc", True), Jump("alt_day0_char")]
        hotspot ((996, 0, 464, 1080)):
            hovered [Show("intro_dr_am", transition=Dissolve(0.5))]
            unhovered [Hide("intro_dr_am", transition=Dissolve(1.0))]
            action [Hide("intro_dr_am", transition=Dissolve(0.5)), SetVariable("dr", True), Jump("alt_day0_char")]
        hotspot ((1458, 0, 462, 1080)):
            hovered [Show("intro_am", transition=Dissolve(0.5))]
            unhovered [Hide("intro_am", transition=Dissolve(1.0))]
            action [Hide("intro_am", transition=Dissolve(0.5)), Jump("alt_day0_char")]

screen alt_movie_screen:
    add Movie(size=(1920, 1080))  # Отображение фильма в заданном размере.
    on "show" action Play("movie", movieplaying, loop=False)  # Запуск фильма.
    on "hide" action Stop("movie")  # Остановка фильма при скрытии экрана.

    timer 0.1 repeat True action If(
        movielength > 0.0,
        true=(SetVariable('movielength', movielength - 0.1)),
        false=(Return(0))
    )  # Таймер, уменьшающий переменную movielength.

    textbutton "Пропустить":
        action Return(0)  # Прерывание фильма и скрытие экрана.
        sensitive (not renpy.get_screen("say"))  # Доступность кнопки, если нет другого текста.
        align (.95, .95)
        text_style "sdl_page_text"  # Применение стиля текста.
        style "sdl_page_text"
        at hoverable_visibility

transform hoverable_visibility:
    on show:
        linear 1.0 alpha 0.0
    on hover:
        alpha 1.0
    on idle:
        linear 1.0 alpha 0.0

python early:
    renpy_version_int = renpy.version_tuple[0]*100000+renpy.version_tuple[1]*10000+renpy.version_tuple[2]*1000+renpy.version_tuple[3]

init python:
    def define_res_7dl():
        for file in renpy.list_files():
            #Картинки
            if file.startswith((default_7dl_path+"Pics/bg/")) and file.endswith((".jpg")):
                renpy.image(("bg "+str(file)[len(default_7dl_path)+8:-4]), file)
            elif file.startswith((default_7dl_path+"Pics/cg/")) and file.endswith((".jpg")):
                renpy.image(("cg "+str(file)[len(default_7dl_path)+8:-4]), file)
            elif file.startswith((default_7dl_path+"Pics/gui/tournament/")) and file.endswith((".jpg", ".png")):
                renpy.image((str(file)[len(default_7dl_path)+20:-4]), file)
            elif file.startswith((default_7dl_path+"Pics/gui/intro/")) and file.endswith((".jpg", ".png")):
                renpy.image((str(file)[len(default_7dl_path)+15:-4]), file)
            elif file.startswith((default_7dl_path+"Pics/gui/laptop/")) and file.endswith((".jpg", ".png")):
                renpy.image((str(file)[len(default_7dl_path)+16:-4]), file)
            elif file.startswith((default_7dl_path+"Pics/gui/acm/")) and file.endswith((".jpg", ".png")):
                renpy.image((str(file)[len(default_7dl_path)+13:-4]), file)
            #Звуки
            elif file.startswith((default_7dl_path+"Sound/ambience/")) and file.endswith((".ogg")):
                ambience_7dl[(str(file)[len(default_7dl_path)+24:-8])] = file
            elif file.startswith((default_7dl_path+"Sound/music/")) and file.endswith((".ogg")):
                music_7dl[(str(file)[len(default_7dl_path)+12:-8])] = file
            elif file.startswith((default_7dl_path+"Sound/sfx/")) and file.endswith((".ogg")):
                sfx_7dl[(str(file)[len(default_7dl_path)+10:-8])] = file
            #Старая Дорога
            elif 'Old_Road' in file:
                if '.ogg' in file:
                    name = str(re.findall(r'.+Old_Road.+/(.+?)\.ogg', file))
                    globals()[name[3:-2]] = file
                elif 'bg_' in file:
                    name = str(re.findall(r'.+Old_Road.+/bg_(.+?)\.jpg', file))
                    renpy.image(("bg "+name[3:-2]), file)
                elif 'cg_' in file:
                    name = str(re.findall(r'.+Old_Road.+/cg_(.+?)\.jpg', file))
                    renpy.image(("cg "+name[3:-2]), file)
                elif '.jpg' or '.png' in file:
                    name = str(re.findall(r'.+Old_Road.+/(.+?)\..+', file))
                    renpy.image((name[3:-2]), file)

init:
    $ ambience_7dl = {}
    $ music_7dl = {}
    $ sfx_7dl = {}

    $ define_res_7dl()

    transform fleft:
        xalign 0.16
        xanchor 0.5

    transform left:
        xalign 0.28
        xanchor 0.5

    transform cleft:
        xalign 0.355
        xanchor 0.5

    transform center:
        xalign 0.5

    transform cright:
        xalign 0.645
        xanchor 0.5

    transform right:
        xalign 0.72
        xanchor 0.5

    transform fright:
        xalign 0.84
        xanchor 0.5

    transform voy_left:
        xalign 0.0
        xanchor 0.5

    transform voy_right:
        xalign 1.0
        xanchor 0.5

    transform zenterright:
        xalign 0.5 zoom 1.0
        linear 0.4 zoom 1.02 xalign 0.7

    transform enterright:
        xalign 0.5 zoom 1.02
        linear 0.6 zoom 1.05 xalign 0.9

    transform zenterleft:
        xalign 0.5 zoom 1.0
        linear 0.4 zoom 1.02 xalign 0.3

    transform enterleft: # по левую
        xalign 0.5 zoom 1.02
        linear 0.6 zoom 1.05 xalign 0.1

    transform zentercenter: # для открывающихся дверей
        xalign 0.5 zoom 1.0
        linear 0.8 zoom 1.05 xalign 0.5

    transform zentercenter2: # для открывающихся дверей
        xalign 0.5 zoom 1.0 subpixel True
        linear 20.0 zoom 1.5 xalign 0.5

    transform zexitcenter: # отдаляющий эффект от центра
        xalign 0.5 zoom 1.05 subpixel True
        linear 0.8 zoom 1.0 xalign 0.5

    transform zexitcenter2: # отдаляющий эффект от центра
        xalign 0.5 zoom 1.5
        linear 20 zoom 1.0 xalign 0.5

    transform zexitright: # отдалаюящий эффект от левого края к центру
        xalign 0.7 zoom 1.05
        linear 0.8 zoom 1.0 xalign 0.5

    transform zexitleft: # отдаляющий эффект от правого края к центру
        xalign 0.3 zoom 1.05
        linear 0.8 zoom 1.0 xalign 0.5

    transform bottotop: # для показа вертикальных артов в галерее
        pos (0,int(-706/sdl_gall_vert_ratio))
        linear round(5.6/sdl_gall_vert_ratio, 1) pos (0,0)
        linear round(1.12/sdl_gall_vert_ratio, 1) pos (0,int(-112/sdl_gall_vert_ratio))

    transform big_gallery: # для показа 8к артов в галерее
        pos (0,0)
        xalign 0.5 yalign 0.5
        zoom 0.25

    transform middle_gallery: # для показа 4к артов в галерее
        pos (0,0)
        xalign 0.5 yalign 0.5
        zoom 0.38

    transform normal_gallery: # для показа артов в галерее
        pos (0,0)

    # основной салют
    transform salute_main_black(salute):
        "sal_black"
        choice 15:
            0.2
        choice:
            "sal_splash" with dspq
            0.2
            salute with dspr
            "sal_black" with dsps
            6.0
        repeat

    transform salute_main(salute):
        "sal_black"
        choice 15:
            0.2
        choice:
            "sal_splash"
            0.2
            choice:
                salute with dspr
                "sal_black" with dsps
                6.0
            choice:
                salute with dspr
                "sal_black" with dissolve
                6.0
        repeat

    # вторичный салют
    transform salute_second_black(salute):
        "sal_black"
        choice 15:
            0.2
        choice:
            #"sal_splash" with dspq
            0.2
            salute with dspr
            "sal_black" with dsps
            6.0
        repeat

    transform salute_second(salute):
        "sal_black"
        choice 15:
            0.2
        choice:
            #"sal_splash" with dspq
            0.2
            choice:
                salute with dspr
                "sal_black" with dsps
                6.0
            choice:
                salute with dspr
                "sal_black" with dissolve
                6.0
        repeat

    transform walking:
        block:
            zoom 1.05 xcenter 0.5 ycenter 0.5
        block:
            ease 0.5 xoffset 0 yoffset 0
            ease 0.5 xoffset 10 yoffset 20
            ease 0.5 xoffset 0 yoffset 0
            ease 0.5 xoffset -10 yoffset 20
        repeat

    transform running:
        block:
            zoom 1.1 xcenter 0.5 ycenter 0.5
        block:
            ease 0.2 xoffset 0 yoffset 0
            ease 0.2 xoffset 25 yoffset 50
            ease 0.2 xoffset 0 yoffset 0
            ease 0.2 xoffset -25 yoffset 50
        repeat

    transform fast_running:
        pos (0,0)
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (5,5)
        pos (0,0)
        linear 0.1 pos (0,-5)
        linear 0.1 pos (0,5)
        repeat

    transform fast_running2:
        block:
            zoom 1.1 xcenter 0.5 ycenter 0.5
        block:
            ease 0.1 xoffset 0 yoffset 0
            ease 0.1 xoffset 12 yoffset 25
            ease 0.1 xoffset 0 yoffset 0
            ease 0.1 xoffset -12 yoffset 25
        repeat
    transform eminluv_drop:
        rotate_pad False
        easeout 1.7 ypos 0.8 rotate 90

    # прочие трансформы
    transform sdl_transform1:
        pos (400,150)

    transform sdl_transform2:
        xalign .5 yalign .5 zoom 1.0
        linear 1.0 xalign .6 yalign .4 zoom 1.1

    transform sdl_transform3:
        xalign .5 yalign .5 zoom 1.0
        linear 2 rotate -15

    transform sdl_transform4:
        xalign .5 yalign .5 zoom 1.0 rotate -15
        ease 1 rotate 15

    transform sdl_transform5:
        xalign .5 yalign .5 zoom 1.0
        ease 0.5 yalign 1 zoom 1.3

    transform sdl_transform6:
        zoom 1.0 xalign 0.5 yalign 0.4
        linear 6.0 zoom 2.0 xalign 0.5 yalign 0.4

    transform sdl_transform7:
        xalign 0.5 yalign 0.5 zoom 1.25
        linear 10 zoom 1.0 xalign 0.5 yalign 0.5

    transform sdl_transform8:
        xalign .5 yalign .5 zoom 1.0
        linear 2 rotate 15

    transform sdl_transform9:
        xalign .5 yalign .5 zoom 1.0
        linear 1.0 xalign .7 yalign .3 zoom 1.25

    transform sdl_transform10:
        xalign .5
        easeout 2.0 xalign .9

    transform sdl_transform11:
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        repeat

    transform sdl_transform12:
        zoom 1.13
        ease .8 zoom 1.0

    transform sdl_transform13:
        xalign .5 yalign .6 zoom 1.0
        linear .3 xalign .5 yalign .55 zoom 1.05
        linear .3 xalign .55 yalign .6 zoom 1.1

    transform sdl_transform14:
        xalign .55 yalign .6 zoom 1.1
        linear .3 xalign .55 yalign .55 zoom 1.15
        linear .3 xalign .4 yalign .6 zoom 1.2

    transform sdl_transform15:
        xalign .6 yalign .4 zoom 1.0
        linear .3 xalign .55 yalign .55 zoom 1.05
        linear .3 xalign .6 yalign .6 zoom 1.1

    transform sdl_transform16:
        xalign .5 yalign .6 zoom 1.2
        linear .3 xalign .55 yalign .55 zoom 1.25
        linear .3 xalign .6 yalign .6 zoom 1.3

    transform sdl_transform17:
        yalign .5 zoom 1.0
        easein .3 zoom 1.15 yalign .7

    transform sdl_transform18:
        yalign .7 zoom 1.15
        easeout .6 zoom 1.3 yalign .4

    transform sdl_transform19:
        zoom 1.3
        linear .6 zoom 1.15

    transform sdl_transform20:
        linear 1.0 zoom 1.3 xcenter 0.65

    transform sdl_transform21:
        pos (0,0)
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (5,5)
        pos (0,0)
        linear 0.1 pos (0,-5)
        linear 0.1 pos (0,5)
        repeat (12)

    transform sdl_transform22:
        zoom 2.0 xalign .8 yalign .1
        linear 4.0 zoom 1.0 xalign .5 yalign .5

    transform sdl_transform23:
        subpixel True
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.25
        alignaround (.5, .5)
        linear 3.0 yalign 1.0 clockwise circles 1 zoom 1.02

    transform sdl_transform24:
        zoom 0.4

    transform veryclose:
        zoom 1.5
        yalign 0.0
        yoffset -275

    transform mt_slide_down:
        align(0.72, 0.0)
        linear 0.5 pos(0.5, 0.15)
        linear 0.5 pos(0.28, 0.25)
        linear 2.0 pos(0.28, 0.5)

    transform mt_shaking_hard:
        linear 1.0 xpos 0.72
        linear 0.1 xpos 0.725
        linear 0.05 xpos 0.715
        linear 0.1 xpos 0.725
        linear 0.05 xpos 0.72
        linear 0.025 xpos 0.725
        linear 0.1 xpos 0.715
        linear 0.075 xpos 0.725
        linear 1.5 xpos 0.72
        linear 4.0 xpos 0.72
        repeat

    transform ba_sit_down_unfzdv:
        parallel:
            ease 1.5 ypos 1.15
        parallel:
            ease 1.0 zoom 1.05
            ease 0.75 zoom 1.0

    transform ba_stand_up_unfzdv:
        parallel:
            ease 1.0 ypos 1.0
        parallel:
            ease 0.5 zoom 1.05
            ease 0.75 zoom 1.0

    transform sit_down_7dl:
        parallel:
            ease 1.5 ypos 0.15
        parallel:
            ease 1.0 zoom 1.05
            ease 0.75 zoom 1.0

    transform stand_up_7dl:
        parallel:
            ease 1.0 ypos 0.0
        parallel:
            ease 0.5 zoom 1.05
            ease 0.75 zoom 1.0

    transform sitting_7dl:
        ypos 0.15

    transform sitting_closely_7dl:
        ypos 1.15

    transform awakening_7dl(imgn): # трансформ пробуждения, позаимствованный из БКРР
        contains:
            ImageReference(imgn)
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.5))
            truecenter
            alpha 0.9
            zoom 1.05
            ease 5.0 alpha 0.0 zoom 1.0
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.5))
            truecenter
            alpha 0.9
            zoom 1.075
            ease 5.0 alpha 0.0 zoom 1.0

    transform flinch: # вздрагивание
        linear 0.05 yoffset -2
        linear 0.05 yoffset +2

    transform jumpscared: # испуганный подпрыг
        linear 0.1 yoffset -20
        linear 0.1 yoffset +20

    if renpy_version_int >= 740000:
        transform sepia_s:
            matrixcolor (TintMatrix(Color(rgb=(1.0, .94, .76))) * SaturationMatrix(0.15))
    else:
        transform sepia_s:
            pass

# Трансформы для календарика
    transform cal_sheet_right_7dl:
        truecenter
        parallel:
            ease 2.5 xpos 1.3 rotate -90
        parallel:
            linear 1.5 ypos 1.2
        parallel:
            ease 1.0 alpha 0.0
    transform cal_sheet_left_7dl:
        truecenter
        parallel:
            ease 2.5 xpos -0.3 rotate 90
        parallel:
            linear 1.5 ypos 1.2
        parallel:
            ease 1.0 alpha 0.0
    transform cal_sheet_cright_7dl:
        truecenter
        parallel:
            ease 2.5 xpos 0.9 rotate -90
        parallel:
            linear 1.5 ypos 1.2
        parallel:
            ease 1.0 alpha 0.0
    transform cal_sheet_cleft_7dl:
        truecenter
        parallel:
            ease 2.5 xpos 0.1 rotate 90
        parallel:
            linear 1.5 ypos 1.2
        parallel:
            ease 1.0 alpha 0.0

# Наши транзиты, с блекджеком и разными цветами.
    $ flash_cyan = Fade(1, 0, 1, color="#1fa")
    $ fade_red = Fade(2, 2, 2, color="#f11")
    $ flash2_red = Fade(0.5, 0, 0.5, color="#f11")
    $ flash_pink = Fade(1, 0, 1, color="#e25")
    $ water_splash = Fade(0.5, 0, 0.75, color="#28f")
    # Кристал
    $ diam = ImageDissolve(im.Tile(get_image_7dl("gui/transit/pattern.jpg")), 1.1, 1)
    $ fdiam = ImageDissolve(im.Tile(get_image_7dl("gui/transit/pattern.jpg")), 0.4, 1)
    $ fulldiam = MultipleTransition([False,fdiam,get_image_7dl("screens/digi1.jpg"),fdiam,True])
    # Поворотный переключатель
    $ gopr = ImageDissolve(im.Tile(get_image_7dl("gui/transit/blackout_go.png")), 0.95, 1)
    $ gopr2 = ImageDissolve(im.Tile(get_image_7dl("gui/transit/blackout_go.png")), 1.4, 1)
    $ clock_l = ImageDissolve(im.Tile(get_image_7dl("gui/transit/clock_l.jpg")), 0.95, 1)
    $ joff_l = MultipleTransition([False, clock_l, Solid("#000"), clock_l, True])
    $ clock_r = ImageDissolve(get_image_7dl("gui/transit/clock_r.png"), 2.5, 50, reverse=False)
    $ joff_r = MultipleTransition([False, clock_r, Solid("#000"), clock_r, True])
    # Жалюзи а ля KS
    $ blind_d = ImageDissolve(im.Tile(get_image_7dl("gui/transit/roof_ks.jpg")), 1.3)
    $ blinds_l = ImageDissolve(im.Tile(get_image_7dl("gui/transit/roof_ks2.jpg")), 0.6)
    $ blinds_r = ImageDissolve(im.Tile(get_image_7dl("gui/transit/roof_ks3.jpg")), 0.7)
    $ blinds_ud = ImageDissolve(get_image_7dl("gui/transit/blackout_ud.png"), 0.3)
    $ blind_l = MultipleTransition([False,blinds_l,Solid("#011"),blinds_r,True])
    $ blind_r = MultipleTransition([False,blinds_r,Solid("#011"),blinds_l,True])
    # Разное
    $ touch = ImageDissolve(im.Tile(get_image_7dl("gui/transit/pattern2.jpg")), 0.9, 1)
    $ dspq = Dissolve(0.04, alpha=True)
    $ dsps = Dissolve(3.0, alpha=True)
    $ guess_on = ImageDissolve(get_image_7dl("screens/blackpalm.png"), 0.25, ramplen=256, reverse=True)
    $ guess_off = ImageDissolve(get_image_7dl("screens/blackpalm.png"), 0.3, ramplen=256)

# Анимы

    image anim_digi:
        get_image_7dl("screens/digi1.jpg")  with Dissolve(1.5)
        pause 1.5
        get_image_7dl("screens/digi2.jpg")  with Dissolve(1.5)
        pause 1.5
        repeat

    image anim_grain: #Смэртельный номер: тянем картинку, делаем прозрачной и запускаем в секвенцию - и всё в коде!
        filmetile(get_image_7dl("screens/alt_noise1.png"))
        pause 0.1
        filmetile(get_image_7dl("screens/alt_noise2.png"))
        pause 0.1
        filmetile(get_image_7dl("screens/alt_noise3.png"))
        pause 0.1
        repeat

    image anim_intro_recall:
        get_image("bg/semen_room.jpg")
        pause 0.1
        get_image("bg/semen_room_window.jpg")
        pause 0.1
        get_image("anim/intro_1.jpg")
        pause 0.1
        get_image("anim/intro_2.jpg")
        pause 0.1
        get_image("anim/intro_3.jpg")
        pause 0.1
        get_image("anim/intro_4.jpg")
        pause 0.1
        get_image("anim/intro_5.jpg")
        pause 0.1
        get_image("anim/intro_6.jpg")
        pause 0.1
        get_image("anim/intro_8.jpg")
        pause 0.1
        get_image("anim/prolog_2.jpg")
        pause 0.1
        get_image("anim/prolog_1.jpg")
        pause 0.1
        get_image("anim/intro_9.jpg")
        pause 0.1
        get_image("anim/intro_10.jpg")
        pause 0.1
        get_image("anim/intro_11.jpg")
        pause 0.1
        get_image("anim/intro_13.jpg")
        pause 0.1
        get_image("bg/intro_xx.jpg")
        pause 0.1
        repeat

    image cg anim_d7_dreamgirl:
        get_image_7dl("cg/dreamgirl/d7_dreamgirl_1_7dl.jpg")
        pause 0.15
        get_image_7dl("cg/dreamgirl/d7_dreamgirl_2_7dl.jpg")
        pause 0.15
        get_image_7dl("cg/dreamgirl/d7_dreamgirl_3_7dl.jpg")
        pause 0.15
        get_image_7dl("cg/dreamgirl/d7_dreamgirl_4_7dl.jpg")

    image anim_square_party:
        get_image("bg/ext_square_night_party.jpg") with Dissolve(.5)
        pause 0.6
        get_image("bg/ext_square_night_party2.jpg") with Dissolve(.5)
        pause 0.6
        repeat

    image anim_square_preparty:
        get_image_7dl("bg/ext_square_sunset3_7dl.jpg") with Dissolve(1.5)
        pause 1.6
        get_image_7dl("bg/ext_square_sunset2_7dl.jpg") with Dissolve(1.5)
        pause 1.4
        repeat

    image uv_bus:
        get_sprite_7dl("custom/uv_alt1_7dl.png")
        pause 0.5
        get_sprite_7dl("custom/uv_alt2_7dl.png")
        pause 0.5
        get_sprite_7dl("custom/uv_alt3_7dl.png")
        pause 0.5
        get_sprite_7dl("custom/uv_alt2_7dl.png")
        pause 0.5
        get_sprite_7dl("custom/uv_alt1_7dl.png")
        pause 0.5

    image anim_underwater:
        get_image_7dl("bg/ext_underwater_7dl.jpg")  with Dissolve(2.0)
        pause 2.0
        get_image_7dl("bg/ext_underwater2_7dl.jpg")  with Dissolve(2.0)
        pause 2.0
        get_image_7dl("bg/ext_underwater3_7dl.jpg")  with Dissolve(2.0)
        pause 2.0
        get_image_7dl("bg/ext_underwater2_7dl.jpg")  with Dissolve(2.0)
        pause 2.0
        get_image_7dl("bg/ext_underwater_7dl.jpg")  with Dissolve(2.0)
        pause 2.0
        repeat

    image anim_un_hideout:
        get_image_7dl("bg/ext_un_hideout_sunset_7dl.jpg")
        get_image_7dl("bg/ext_un_hideout_night_7dl.jpg")  with Dissolve(120.0)
        pause 120.0

    image anim_int_musclub:
        get_image_7dl("bg/int_musclub_sunset_7dl.jpg")
        get_image_7dl("bg/int_musclub_night_nolight_7dl.jpg")  with Dissolve(30.0)
        pause 30.0

    image anim_int_beach:
        get_image("bg/ext_beach_day.jpg")
        get_image("bg/ext_beach_sunset.jpg")  with Dissolve(30.0)
        pause 30.0

    image anim_int_dining_hall_day_cough:
        get_image("bg/int_dining_hall_day.jpg")
        get_image("bg/int_dining_hall_day.jpg") with Move((0, 10), (0, -10), .10, bounce=True, repeat=True, delay=.275*3)
        pause 1.2
        repeat

    #Ну не надо, ну не стукай.
    image punch_to_up = get_image_7dl("gui/punches/punch_to_up_7dl.jpg")

    image punch_to_down = get_image_7dl("gui/punches/punch_to_down_7dl.jpg")

    image punch_to_right = get_image_7dl("gui/punches/punch_to_right_7dl.jpg")

    image punch_to_left = get_image_7dl("gui/punches/punch_to_left_7dl.jpg")

    # Пятнышки.
    image spill_red_left = get_image_7dl("gui/extra_spills/spill_red_left.png")
    image spill_red_up = get_image_7dl("gui/extra_spills/spill_red_up.png")
    image spill_red_down = get_image_7dl("gui/extra_spills/spill_red_down.png")

    image salute = LiveComposite((1920,1080),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh1.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh11.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh2.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh21.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh3.png")),

                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh4.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh41.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh5.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh51.png")),
                                  #(0,0), salute_main(get_image_7dl("screens/salute/spoloh6.png")),
                                  #(0,0), salute_main(get_image_7dl("screens/salute/spoloh61.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh7.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh71.png")),

                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh91.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh9.png")))

    image salute2 = LiveComposite((1920,1080),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh1.png")),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh11.png")),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh2.png")),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh21.png")),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh3.png")),

                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh4.png")),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh41.png")),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh5.png")),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh51.png")),
                                  #(0,0), salute_second(get_image_7dl("screens/salute/spoloh6.png")),
                                  #(0,0), salute_second(get_image_7dl("screens/salute/spoloh61.png")),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh7.png")),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh71.png")),

                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh91.png")),
                                  (0,0), salute_second(get_image_7dl("screens/salute/spoloh9.png")))

    image timer_anim:
        get_sprite_7dl("custom/win_7dl.png")
        0.1 # Задержка
        get_sprite_7dl("custom/win2_7dl.png")
        0.1
        get_sprite_7dl("custom/win3_7dl.png")
        0.1
        repeat # Не убирать

    image ftl_anim:
        get_image_7dl("screens/ftl1.png")
        0.1 # Задержка
        get_image_7dl("screens/ftl2.png")
        0.1
        get_image_7dl("screens/ftl3.png")
        0.1
        repeat # Не убирать

    image un serious dress anim:
        get_sprite_7dl("custom/un_3_dress_serious_1_7dl.png")
        8.0 # Задержка
        get_sprite_7dl("custom/un_3_dress_serious_2_7dl.png")
        0.1
        get_sprite_7dl("custom/un_3_dress_serious_1_7dl.png")
        4.0 # Задержка
        get_sprite_7dl("custom/un_3_dress_serious_2_7dl.png")
        0.15
        get_sprite_7dl("custom/un_3_dress_serious_1_7dl.png")
        7.0 # Задержка
        get_sprite_7dl("custom/un_3_dress_serious_2_7dl.png")
        0.1
        repeat # Не убирать

    image scenery:
        get_image("anim/prolog_2.jpg") with Dissolve(.5)
        pause 2.6
        get_image("anim/prolog_1.jpg") with Dissolve(.5)
        pause 0.6
        repeat

    image scenery2:
        get_image("anim/prolog_2.jpg") with Dissolve(.4)
        pause 2.0
        get_image("anim/prolog_1.jpg") with Dissolve(.4)
        pause 0.4
        repeat

    image scenery3:
        get_image("anim/prolog_2.jpg") with Dissolve(.25)
        pause 1.4
        get_image("anim/prolog_1.jpg") with Dissolve(.25)
        pause 0.25
        repeat

    image fog_7dl:
        contains:
            get_image_7dl("gui/fog/fog1.png")
            alpha 1.0
            ease 2.0 alpha 1.0
            ease 2.0 alpha 1.0
            ease 2.0 alpha 1.0
            repeat
        contains:
            get_image_7dl("gui/fog/fog2.png")
            alpha 0.0
            ease 2.0 alpha 1.0
            ease 2.0 alpha 0.0
            ease 2.0 alpha 0.0
            repeat
        contains:
            get_image_7dl("gui/fog/fog3.png")
            alpha 0.0
            ease 2.0 alpha 0.0
            ease 2.0 alpha 1.0
            ease 2.0 alpha 0.0
            repeat

    image emptiness_7dl:
        contains:
            get_image_7dl("gui/fog/emptiness1.png")
            alpha 1.0
            ease 2.0 alpha 1.0
            ease 2.0 alpha 1.0
            ease 2.0 alpha 1.0
            repeat
        contains:
            get_image_7dl("gui/fog/emptiness2.png")
            alpha 0.0
            ease 2.0 alpha 1.0
            ease 2.0 alpha 0.0
            ease 2.0 alpha 0.0
            repeat
        contains:
            get_image_7dl("gui/fog/emptiness3.png")
            alpha 0.0
            ease 2.0 alpha 0.0
            ease 2.0 alpha 1.0
            ease 2.0 alpha 0.0
            repeat

    image int_bus_7dl = get_image_7dl("gui/fog/int_bus_night_wo_forest.png")
    image int_future_hangar_7dl = get_image_7dl("gui/fog/int_future_hangar_7dl.png")
    if renpy_version_int >= 720000:
        image bg un_hideout_night_blur_7dl = im.Blur(get_image_7dl("bg/ext_un_hideout_night_7dl.jpg"), 3.5)
        image bg ext_city_night_blur_7dl = im.Blur(get_image_7dl("bg/ext_city_night_7dl.jpg"), 3.5)
        image bg ext_winterpark_blur_7dl = im.Blur(get_image_7dl("bg/ext_winterpark_7dl.jpg"), 3.5)
        image cg day7_us_fairytale_white2_7dl = im.Blur(get_image_7dl("cg/us_fairytale/day7_us_fairytale_white_7dl.jpg"), 3.5)
    else:
        image bg un_hideout_night_blur_7dl = get_image_7dl("bg/ext_un_hideout_night_7dl.jpg")
        image bg ext_city_night_blur_7dl = get_image_7dl("bg/ext_city_night_7dl.jpg")
        image bg ext_winterpark_blur_7dl = get_image_7dl("bg/ext_winterpark_7dl.jpg")
        image cg day7_us_fairytale_white2_7dl = get_image_7dl("cg/us_fairytale/day7_us_fairytale_white_7dl.jpg")

#Заставки
    image bg ext_stand3_night_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand3_7dl.jpg"), im.matrix.tint(0.63, 0.78, 0.82))
    image bg ext_stand3_sunset_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand3_7dl.jpg"), im.matrix.tint(0.94, 0.82, 1.0))
    image bg ext_stand3_prolog_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand_pr_7dl.jpg"), im.matrix.tint(0.82, 0.84, 1.0))

#Турнир
    image sal_black = Solid("#00000000")
    image sal_splash = Solid("#FFFFFF10")

# Цикл вспышек для салюта
    image sal_splash2:
        Solid("#f7ae4010") with dspr
        0.3
        Solid("#d6c6a610") with dspr
        0.3
        Solid("#cd4f1910") with dspr
        0.3
        Solid("#9e242210") with dspr
        0.3
        Solid("#bd6a3710") with dspr
        0.3
        Solid("#96820010") with dspr
        0.3
        Solid("#9f000010") with dspr
        0.3
        Solid("#fffeaa10") with dspr
        0.3
        Solid("#bd86bf10") with dspr
        0.3
        Solid("#5c4ba110") with dspr
        0.3
        Solid("#7ee05310") with dspr
        0.3
        Solid("#f1824e10") with dspr
        0.3
        Solid("#fca02c10") with dspr
        0.3
        repeat

#Элементы интерфейса
    image blackout = get_image_7dl("gui/transit/blackout.png")
    image blackout2 = get_image_7dl("gui/transit/blackout2.png")
    image blackout_exh = get_image_7dl("gui/transit/blackout_exh.png")
    image blackout_exh2 = get_image_7dl("gui/transit/blackout_exh2.png")
    image blackout_exh3 = get_image_7dl("gui/transit/blackout_exh3.png")
    image genda_portrait = get_image_7dl("sprites/custom/genda_portrait_7dl.png")
    image gfx bokeh = get_image_7dl("screens/splatter.png")

    image anim_exhausted:
        get_image_7dl("gui/transit/blackout_exh2.png")
        0.03 # Задержка
        get_image_7dl("gui/transit/blackout_exh3.png")
        0.03 # Задержка
        get_image_7dl("gui/transit/blackout_exh2.png")
        0.03 # Задержка
        get_image_7dl("gui/transit/blackout_exh3.png")
        0.03 # Задержка
        get_image_7dl("gui/transit/blackout_exh2.png")
        0.03 # Задержка
        repeat # Не убирать

#ЦГ Ольги в лодке. Лена-ФЗ.
    image cg d4_mt_board_7dl mt_dontlike = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_board/d4_mt_board_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_board/mt_dontlike.png"))

    image cg d4_mt_board_7dl mt_grin = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_board/d4_mt_board_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_board/mt_grin.png"))

    image cg d4_mt_board_7dl mt_normal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_board/d4_mt_board_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_board/mt_normal.png"))

    image cg d4_mt_board_7dl mt_normal2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_board/d4_mt_board_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_board/mt_normal2.png"))

    image cg d4_mt_board_7dl mt_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_board/d4_mt_board_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_board/mt_smile.png"))

    image cg d4_mt_board_7dl mt_smile2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_board/d4_mt_board_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_board/mt_smile2.png"))

    image cg d4_mt_board_7dl mt_smile3 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_board/d4_mt_board_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_board/mt_smile3.png"))

    image cg d4_mt_board_7dl mt_laugh = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_board/d4_mt_board_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_board/mt_laugh.png"))

    image cg d4_mt_board_7dl = ImageReference("cg d4_mt_board_7dl mt_normal")

#Рыбалка в 6 день Сыча.
#DefaultALL
    image cg d6_me_cyberfish_7dl el_cf_normal semen_cf_normal sh_cf_bore = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_bore.png"))

#SurpriseEL
    image cg d6_me_cyberfish_7dl el_cf_surp semen_cf_normal sh_cf_bore = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_surp.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_bore.png"))

#SurpriseALL
    image cg d6_me_cyberfish2_7dl el_cf_surp2 semen_cf_surp sh_cf_surp = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_surp2.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_surp.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_surp.png"))

#HappyEL + SurpSEM + SmileSH
    image cg d6_me_cyberfish_7dl el_cf_happy semen_cf_surp sh_cf_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_happy.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_surp.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_smile.png"))

#SadEL + DefaultSEM + PokerSH
    image cg d6_me_cyberfish_7dl el_cf_sad semen_cf_normal sh_cf_poker = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_sad.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_poker.png"))

#SorrowEL + DefaultSEM + PokerSH
    image cg d6_me_cyberfish_7dl el_cf_sorrow semen_cf_normal sh_cf_poker = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_sorrow.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_poker.png"))

#SadEL + DefaultSEM + BoreSH
    image cg d6_me_cyberfish_7dl el_cf_sad semen_cf_normal sh_cf_bore = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_sad.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_bore.png"))

#SorrowEL + DefaultSEM + BoreSH
    image cg d6_me_cyberfish_7dl el_cf_sorrow semen_cf_normal sh_cf_bore = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_sorrow.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_bore.png"))

#SmileEL + DefaultSEM + PokerSH
    image cg d6_me_cyberfish_7dl el_cf_smile semen_cf_normal sh_cf_poker = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_smile.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_poker.png"))

#SmileEL + SurpSEM + PokerSH
    image cg d6_me_cyberfish_7dl el_cf_smile semen_cf_surp sh_cf_poker = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_smile.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_surp.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_poker.png"))

#SmileEL + DefaultSEM + SurpSH
    image cg d6_me_cyberfish_7dl el_cf_smile semen_cf_normal sh_cf_surp = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_smile.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_surp.png"))

#SmileEL + DefaultSEM + boreSH
    image cg d6_me_cyberfish_7dl el_cf_smile semen_cf_normal sh_cf_bore = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_smile.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_bore.png"))

#SmileEL_SH + DefaultSEM
    image cg d6_me_cyberfish_7dl el_cf_smile2 semen_cf_normal sh_cf_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_smile2.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_smile.png"))

#Smile2EL_SH + DefaultSEM
    image cg d6_me_cyberfish_7dl el_cf_smile2 semen_cf_normal sh_cf_bore = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_smile2.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_bore.png"))

#DefaultEL_SEM + PokerSH
    image cg d6_me_cyberfish_7dl el_cf_normal semen_cf_normal sh_cf_poker = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_poker.png"))

#DefaltEL + SurpSEM + PokerSH
    image cg d6_me_cyberfish_7dl el_cf_normal semen_cf_surp sh_cf_poker = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_surp.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_poker.png"))

#SurpEL_SH + DefailtSEM
    image cg d6_me_cyberfish_7dl el_cf_surp3 semen_cf_normal sh_cf_surp = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_surp3.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_surp.png"))

#Smile3EL + DefailtSEM + BoreSH
    image cg d6_me_cyberfish_7dl el_cf_smile3 semen_cf_normal sh_cf_bore = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/cyber_fish/d6_me_cyberfish_7dl.jpg"),
        (0, 0), get_image_7dl("cg/cyber_fish/el_cf_smile3.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/semen_cf_normal.png"),
        (0, 0), get_image_7dl("cg/cyber_fish/sh_cf_bore.png"))

    image cg d6_me_cyberfish_7dl = ImageReference("cg d6_me_cyberfish_7dl el_cf_normal semen_cf_normal sh_cf_bore")

#alice7dl_rej
    image cg d7_dv_rf_reject_gray_7dl dv_normal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/dv_guitar/d7_dv_rf_reject_gray_7dl.jpg"),
        (0, 0), get_image_7dl("cg/dv_guitar/dv_normal.png"))

    image cg d7_dv_rf_reject_gray_7dl dv_concent = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/dv_guitar/d7_dv_rf_reject_gray_7dl.jpg"),
        (0, 0), get_image_7dl("cg/dv_guitar/dv_concent.png"))

    image cg d7_dv_rf_reject_gray_7dl dv_cry = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/dv_guitar/d7_dv_rf_reject_gray_7dl.jpg"),
        (0, 0), get_image_7dl("cg/dv_guitar/dv_cry.png"))

    image cg d7_dv_rf_reject_7dl dv_happy = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/dv_guitar/d7_dv_rf_reject_7dl.jpg"),
        (0, 0), get_image_7dl("cg/dv_guitar/dv_happy.png"))

# Танцульки с Ульяной
    # Нормал
    image cg d6_us_normal_dance_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_7dl.jpg"),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_normal_7dl.png"))

    # Щёчки
    image cg d6_us_zluka_dance_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_7dl.jpg"),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_zluka_7dl.png"))

    # Удивление
    image cg d6_us_surprise_dance_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_7dl.jpg"),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_surprise_7dl.png"))

    # Bruh…
    image cg d6_us_upset_dance_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_7dl.jpg"),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_upset_7dl.png"))

    # Улыбка
    image cg d6_us_smile_dance_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_7dl.jpg"),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_smile_7dl.png"))

    # Лыба
    image cg d6_us_genki_dance_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_7dl.jpg"),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_genki_7dl.png"))

    # Смущение
    image cg d6_us_shy_dance_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_7dl.jpg"),
        (0, 0), get_image_7dl("cg/us_dance/d6_us_dance_shy_7dl.png"))

# Симен-космонавт
    image cg d7_un_cosmo_eyes_close_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/d7_un_cosmo.jpg"),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/eyes_close.png"))

    image cg d7_un_cosmo_eyes_normal_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/d7_un_cosmo.jpg"),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/eyes_normal.png"))

    image cg d7_un_cosmo_eyes_scare1_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/d7_un_cosmo.jpg"),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/eyes_scare1.png"))

    image cg d7_un_cosmo_eyes_scare2_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/d7_un_cosmo.jpg"),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/eyes_scare2.png"))

    image cg d7_un_cosmo_eyes_smile_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/d7_un_cosmo.jpg"),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/eyes_smile.png"))

    image cg d7_un_cosmo_scare1_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/d7_un_cosmo.jpg"),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/scare1.png"))

    image cg d7_un_cosmo_scare2_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/d7_un_cosmo.jpg"),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/scare2.png"))

    image cg d7_un_cosmo_scare3_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/d7_un_cosmo.jpg"),
        (0, 0), get_image_7dl("cg/d7_un_cosmo/scare3.png"))

#  Уля тильтуля
    image cg d2_us_hideout_alone_7dl = get_image_7dl("cg/us_set/d2_us_hideout_alone_7dl.jpg")

    image cg d2_us_hideout1_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/us_set/d2_us_hideout_alone_7dl.jpg"),
        (0, 0), get_image_7dl("cg/us_set/d2_us_hideout_p1_7dl.png"))

    image cg d2_us_hideout2_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/us_set/d2_us_hideout_alone_7dl.jpg"),
        (0, 0), get_image_7dl("cg/us_set/d2_us_hideout_p2_7dl.png"))

# Мику колокольчик вместо клитора
    image cg day2_mi_beach1_7dl = get_image_7dl("cg/mi_beach/day2_mi_beach1_7dl.jpg")
    image cg day2_mi_beach2_7dl = get_image_7dl("cg/mi_beach/day2_mi_beach2_7dl.jpg")
    image cg day2_mi_beach3_7dl = get_image_7dl("cg/mi_beach/day2_mi_beach3_7dl.jpg")
    image cg day2_mi_beach4_7dl = get_image_7dl("cg/mi_beach/day2_mi_beach4_7dl.jpg")

    image day2_beach_mi_sad1 = get_image_7dl("cg/mi_beach/mi_sad1.png")
    image day2_beach_mi_normal1 = get_image_7dl("cg/mi_beach/mi_normal1.png")
    image day2_beach_mi_smile1 = get_image_7dl("cg/mi_beach/mi_smile1.png")
    image day2_beach_mi_smilecl1 = get_image_7dl("cg/mi_beach/mi_smilecl1.png")
    image day2_beach_mi_2smile1 = get_image_7dl("cg/mi_beach/mi_2smile1.png")
    image day2_beach_mi_sorrow1 = get_image_7dl("cg/mi_beach/mi_sorrow1.png")

    image day2_beach_me_sad1 = get_image_7dl("cg/mi_beach/me_sad1.png")
    image day2_beach_me_normal1 = get_image_7dl("cg/mi_beach/me_normal1.png")
    image day2_beach_me_smile1 = get_image_7dl("cg/mi_beach/me_smile1.png")

    image day2_beach_mi_cl2 = get_image_7dl("cg/mi_beach/mi_cl2.png")
    image day2_beach_mi_surp2 = get_image_7dl("cg/mi_beach/mi_surp2.png")

    image day2_beach_mi_tears3 = get_image_7dl("cg/mi_beach/mi_tears3.png")
    image day2_beach_mi_angry3 = get_image_7dl("cg/mi_beach/mi_angry3.png")
    image day2_beach_mi_sad3 = get_image_7dl("cg/mi_beach/mi_sad3.png")
    image day2_beach_mi_dontlike3 = get_image_7dl("cg/mi_beach/mi_dontlike3.png")
    image day2_beach_mi_surp3 = get_image_7dl("cg/mi_beach/mi_surp3.png")
    image day2_beach_mi_shy3 = get_image_7dl("cg/mi_beach/mi_shy3.png")
    image day2_beach_mi_normal3 = get_image_7dl("cg/mi_beach/mi_normal3.png")

    image day2_beach_me_sad3 = get_image_7dl("cg/mi_beach/me_sad3.png")
    image day2_beach_me_normal3 = get_image_7dl("cg/mi_beach/me_normal3.png")
    image day2_beach_me_smile3 = get_image_7dl("cg/mi_beach/me_smile3.png")

    image day2_beach_cumihimo4 = get_image_7dl("cg/mi_beach/cumihimo4.png")
    image day2_beach_mi_normal_eye4 = get_image_7dl("cg/mi_beach/mi_normal_eye4.png")
    image day2_beach_mi_surp_eye4 = get_image_7dl("cg/mi_beach/mi_surp_eye4.png")

    image cg day2_mi_beach1_gal  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mi_beach/day2_mi_beach1_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mi_beach/mi_normal1.png"),
        (0, 0), get_image_7dl("cg/mi_beach/me_normal1.png"))

    image cg day2_mi_beach2_gal  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mi_beach/day2_mi_beach2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mi_beach/mi_surp2.png"))

    image cg day2_mi_beach3_gal  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mi_beach/day2_mi_beach3_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mi_beach/mi_normal3.png"),
        (0, 0), get_image_7dl("cg/mi_beach/me_normal3.png"))

    image cg day2_mi_beach4_gal  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mi_beach/day2_mi_beach4_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mi_beach/mi_normal_eye4.png"))

# Пират на костре
    image cg day5_me_buf_7dl = get_image_7dl("cg/me_buf/day5_me_buf_7dl.jpg")
    image cg day5_me_buf2_7dl = get_image_7dl("cg/me_buf/day5_me_buf2_7dl.jpg")

    image day5_me_buf_smile_face_7dl = get_image_7dl("cg/me_buf/day5_me_buf_smile_face_7dl.png")
    image day5_me_buf_tricky_face_7dl = get_image_7dl("cg/me_buf/day5_me_buf_tricky_face_7dl.png")

    image cg day5_me_buf_alone_smile_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_buf/day5_me_buf_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_buf/day5_me_buf_smile_face_7dl.png"))

    image cg day5_me_buf_alone_tricky_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_buf/day5_me_buf_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_buf/day5_me_buf_tricky_face_7dl.png"))

    image cg day5_me_buf_people_smile_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_buf/day5_me_buf2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_buf/day5_me_buf_smile_face_7dl.png"))

    image cg day5_me_buf_people_tricky_7dl  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_buf/day5_me_buf2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_buf/day5_me_buf_tricky_face_7dl.png"))

# Гамовер
    image gameover  = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("gui/intro/gameover1.png"),
        (0, 0), get_image_7dl("gui/intro/gameover2.png"))


# Сыч в тумане
    image d7_me_epilogue_bus2_7dl = get_image_7dl("gui/fog/d7_me_epilogue_bus2_7dl.png")

# Фото Ульяны.
    image cg d6_us_photo_7dl = get_image_7dl("cg/d6_us_photo_7dl.png")
    image cg d6_us_photo_torn_7dl = get_image_7dl("cg/d6_us_photo_torn_7dl.png")

# День сурка для ФЗ.
    image anim_groundhog_day:
        get_image("bg/semen_room.jpg") with Dissolve(1.5)
        0.03
        get_image("bg/bus_stop.jpg") with Dissolve(1.5)
        0.03
        get_image_7dl("bg/int_store_7dl.jpg") with Dissolve(1.5)
        repeat

# Скачки по карте
    image bg map_explain = get_image_7dl("gui/maps/map_explain.jpg")
    image dvsem_el = get_image_7dl("gui/maps/dvsem_el.png")
    image eye_s = get_image_7dl("sprites/custom/eye_s_7dl.png")
# Сотик
    image frame = get_image_7dl("gui/phone/frame.png")
    image frame_sl = get_image_7dl("gui/phone/frame_sl.png")
    image cam_ui = get_image_7dl("gui/phone/cam_ui.png")
    image telephone_fz_7dl = get_image_7dl("sprites/custom/telephone_fz_7dl.png")
    image telephone_dj_7dl = get_image_7dl("sprites/custom/telephone_dj_7dl.png")
    image telephone_mi_7dl = get_image_7dl("sprites/custom/telephone_mi_7dl.png")
    image tapochek_mobile_7dl = get_image_7dl("sprites/custom/tapochek_mobile_7dl.png")
# Пека
    image anim_laptop:
        get_image_7dl("gui/laptop/laptop_prologue.png")
        0.3
        get_image_7dl("gui/laptop/laptop_prologue_weak.png")
        0.25
        get_image_7dl("gui/laptop/laptop_prologue_mid.png")
        0.25
        get_image_7dl("gui/laptop/laptop_prologue_strong.png")
        0.2
        get_image_7dl("gui/laptop/laptop_prologue_mid.png")
        0.25
        get_image_7dl("gui/laptop/laptop_prologue_weak.png")
        0.3
        repeat

# Камень-ножницы-бумага
    image miku_paper = get_image_7dl("gui/rps/miku_paper.png")
    image miku_rock = get_image_7dl("gui/rps/miku_rock.png")
    image miku_scissor = get_image_7dl("gui/rps/miku_scissor.png")
    image sam_paper = get_image_7dl("gui/rps/sam_paper.png")
    image sam_rock = get_image_7dl("gui/rps/sam_rock.png")
    image sam_scissor = get_image_7dl("gui/rps/sam_scissor.png")

# Прочее
    image logo_7dl = get_image_7dl("gui/menu_elem/logo_7dl.png") # Логотип мода

    image dreamgirl_overlay = get_image_7dl("screens/dreamgirl_overlay.png")
    image wet1 = get_image_7dl("screens/wet1.png")
    image volley_fight = get_sprite_7dl("custom/volley_fight_7dl.png")
    image rain_overlay = get_image_7dl("screens/rain_overlay.png")

    image alt_KS_censor = get_image_7dl("screens/alt_KS_censor.png")
    image alt_KS_censor2 = get_image_7dl("screens/alt_KS_censor2.png")
    image alt_blink = get_image_7dl("screens/blink_7dl.png")

# Картинки с использованием прозрачности и прочая спрайтовость
    image dv normal flipped = Transform("dv normal pioneer", xzoom=-1.0)
    image dv normal flipped far = Transform("dv normal pioneer far", xzoom=-1.0)
    image sl normal flipped = Transform("sl normal pioneer", xzoom=-1.0)
    image sl serious flipped = Transform("sl serious pioneer", xzoom=-1.0)
    #image d3_miku_dance_blush flipped = Transform("d3_miku_dance_blush", xzoom=-1.0)
    image uv shade3 sized = Transform("uv shade3", zoom=.4)
    image uv shade4 sized = Transform("uv shade4", zoom=.4)
    image digi_pad = get_sprite_7dl("custom/digi_pad_7dl.png")
    image sl_1_winter2 = get_sprite_7dl("custom/sl_1_winter2_7dl.png")
    image sl3_4_winter1 = get_sprite_7dl("custom/sl3_4_winter1_7dl.png")
    image sl_trench = get_sprite_7dl("custom/sl_trench_7dl.png")
    image sl_trench2 = get_sprite_7dl("custom/sl_trench2_7dl.png")
    image cotocomb_lighter = get_sprite_7dl("custom/cotocomb_lighter_7dl.png")
    image d4_cat_door_frame = get_sprite_7dl("custom/d4_cat_door_frame_7dl.png")
    image d6_miku_cries = get_sprite_7dl("custom/d6_miku_cries_7dl.png")
    image mouth_dull = get_sprite_7dl("custom/mouth_dull_7dl.png")
    image mi_ru = get_sprite_7dl("custom/mi_ru_7dl.png")
    image mt_bus = get_sprite_7dl("custom/mt_bus_7dl.png")
    image sl_bus = get_sprite_7dl("custom/sl_bus_7dl.png")
    image myst_mh = get_sprite_7dl("custom/myst_mh_7dl.png")
    image uvao_d1 = get_sprite_7dl("custom/uvao_d1_7dl.png")
    image dv_mt_7dl = get_sprite_7dl("custom/dv_mt_7dl.png")
    image backpack = get_sprite_7dl("custom/backpack_7dl.png")
    image backpack_tiny = get_sprite_7dl("custom/backpack_tiny_7dl.png")
    image bg int_house_of_mt_backpack_sunset = im.Composite((1920, 1080), (0, 0), "images/bg/int_house_of_mt_sunset.jpg", (0, 0), get_sprite_7dl("custom/backpack_tiny_7dl.png"))
    image bg int_house_of_mt_backpack_day = im.Composite((1920, 1080), (0, 0), "images/bg/int_house_of_mt_day.jpg", (0, 0), get_sprite_7dl("custom/backpack_tiny_7dl.png"))
    image dv_us_volley = get_sprite_7dl("custom/dv_us_volley_7dl.png")
    image ldb_blind = get_image_7dl("sprites/custom/ldb_blind.png")
    image PolaroidFrame_7dl = get_sprite_7dl("custom/PolaroidFrame_7dl.png")
    image un_grasp_7dl = get_sprite_7dl("custom/un_grasp_7dl.png")
    image un_grasp2_7dl = get_sprite_7dl("custom/un_grasp2_7dl.png")
    image un_old normal dress = get_sprite_7dl("custom/un_old_normal_dress_7dl.png")
    image un_so_spiny_7dl = im.MatrixColor(get_sprite_7dl("custom/un_so_spiny_7dl.png"), im.matrix.tint(0.94, 0.82, 1.0))

    image pi normal2 = get_sprite_7dl("custom/pi_normal2.png")
    image pi smile2 = get_sprite_7dl("custom/pi_smile2.png")
    image pi surprise = get_sprite_7dl("custom/pi_surprise.png")
    image bottle_punch = get_sprite_7dl("custom/bottle_punch_7dl.png")
    image par = get_image_7dl("gui/par/par_7dl.png")

# Мать Слави
    image slm normal = get_sprite_7dl("custom/slm/slm_normal_7dl.png")
    image slm happy = get_sprite_7dl("custom/slm/slm_happy_7dl.png")
    image slm smile = get_sprite_7dl("custom/slm/slm_smile_7dl.png")
    image slm worry = get_sprite_7dl("custom/slm/slm_worry_7dl.png")

#Красивый Стас
    image sts normal = get_sprite_7dl("custom/sts/sts_normal_7dl.png")
    image sts sad = get_sprite_7dl("custom/sts/sts_sad_7dl.png")
    image sts smile = get_sprite_7dl("custom/sts/sts_smile_7dl.png")
    image sts laugh = get_sprite_7dl("custom/sts/sts_laugh_7dl.png")
    image sts serious = get_sprite_7dl("custom/sts/sts_serious_7dl.png")

# Бабуля Арсения
    image bba normal = get_sprite_7dl("custom/bba/bb_normal_7dl.png")
    image bba sad = get_sprite_7dl("custom/bba/bb_sad_7dl.png")
    image bba smile = get_sprite_7dl("custom/bba/bb_smile_7dl.png")

#Лольга
    image lmt normal = get_sprite_7dl("custom/lmt/lmt_normal_7dl.png")
    image lmt sad = get_sprite_7dl("custom/lmt/lmt_sad_7dl.png")
    image lmt smile = get_sprite_7dl("custom/lmt/lmt_smile_7dl.png")

#Дед

    # Первое тело с smile
    image ded laugh = Composite(
        (1920, 1080),
        (0, 0), get_sprite_7dl("custom/ded/ded_1_body_7dl.png"))

    # Второе тело с laugh
    image ded laugh2 = Composite(
        (1920, 1080),
        (0, 0), get_sprite_7dl("custom/ded/ded_2_body_7dl.png"))

    # Первое тело с smile
    image ded smile = Composite(
            (1920, 1080),
            (0, 0), get_sprite_7dl("custom/ded/ded_1_body_7dl.png"),
            (0, 0), get_sprite_7dl("custom/ded/ded_smile_7dl.png"))

    # Второе тело со smile
    image ded smile2 = Composite(
            (1920, 1080),
            (0, 0), get_sprite_7dl("custom/ded/ded_2_body_7dl.png"),
            (0, 0), get_sprite_7dl("custom/ded/ded_smile_7dl.png"))

    # Первое тело с upset
    image ded upset = Composite(
            (1920, 1080),
            (0, 0), get_sprite_7dl("custom/ded/ded_1_body_7dl.png"),
            (0, 0), get_sprite_7dl("custom/ded/ded_upset_7dl.png"))

    # Второе тело с upset
    image ded upset2 = Composite(
            (1920, 1080),
            (0, 0), get_sprite_7dl("custom/ded/ded_2_body_7dl.png"),
            (0, 0), get_sprite_7dl("custom/ded/ded_upset_7dl.png"))

    # Первое тело с evil
    image ded evil = Composite(
            (1920, 1080),
            (0, 0), get_sprite_7dl("custom/ded/ded_1_body_7dl.png"),
            (0, 0), get_sprite_7dl("custom/ded/ded_evil_7dl.png"))

    # Второе тело с evil
    image ded evil2 = Composite(
            (1920, 1080),
            (0, 0), get_sprite_7dl("custom/ded/ded_2_body_7dl.png"),
            (0, 0), get_sprite_7dl("custom/ded/ded_evil_7dl.png"))

    # Первое тело с wink (подмигивание)
    image ded wink = Composite(
            (1920, 1080),
            (0, 0), get_sprite_7dl("custom/ded/ded_1_body_7dl.png"),
            (0, 0), get_sprite_7dl("custom/ded/ded_wink_7dl.png"))

    # Второе тело с wink (подмигивание)
    image ded wink2 = Composite(
            (1920, 1080),
            (0, 0), get_sprite_7dl("custom/ded/ded_2_body_7dl.png"),
            (0, 0), get_sprite_7dl("custom/ded/ded_wink_7dl.png"))

    # Первое тело с surprise
    image ded surprise = Composite(
            (1920, 1080),
            (0, 0), get_sprite_7dl("custom/ded/ded_1_body_7dl.png"),
            (0, 0), get_sprite_7dl("custom/ded/ded_surprise_7dl.png"))

    # Второе тело с surprise
    image ded surprise2 = Composite(
            (1920, 1080),
            (0, 0), get_sprite_7dl("custom/ded/ded_2_body_7dl.png"),
            (0, 0), get_sprite_7dl("custom/ded/ded_surprise_7dl.png"))

#Семён Анимешник
    image semen_animeshnik_7dl = get_sprite_7dl("custom/semen_animeshnik_7dl.png")

#Грустный Семён (отбытие)
    image semen_mouth_bus_7dl = get_sprite_7dl("custom/semen_mouth_bus_7dl.png")

# Dnd
    image alt_cat_map_wireframe = get_image_7dl("gui/dnd/alt_cat_map_wireframe.png")
    image alt_cat_map = get_image_7dl("gui/dnd/alt_cat_map.png")
    image alt_cat_map_pathfinding = get_image_7dl("gui/dnd/alt_cat_map_pathfinding.png")

# Звучок
    $ sfx_alisa_falls_novoice = "sound/sfx/alisa_falls_novoice.ogg"
    $ sfx_owl = "sound/test.ogg"
    $ sfx_heavy_breathing = "zhenya/sounds/heavy_breathing.ogg"

# Анимации для "Сжигая мосты"
    image cg d7_un_fireyes_7dl:
        get_image_7dl("cg/d7_un_fireyes1_7dl.jpg") with Dissolve(1.2)
        0.8
        get_image_7dl("cg/d7_un_fireyes2_7dl.jpg") with Dissolve(1.2)
        0.8
        repeat

    image cg d7_fire_7dl:
        get_image_7dl("cg/d7_fire2_7dl.jpg") with Dissolve(1.5)
        1.4
        get_image_7dl("cg/d7_fire1_7dl.jpg") with Dissolve(1.5)
        1.4
        repeat

# Лучики для Осколка Арсения
    image sunshine_7dl:
        get_sprite_7dl("custom/sunshine/sunshine1_7dl.png") with Dissolve(1.9)
        1.8
        get_sprite_7dl("custom/sunshine/sunshine2_7dl.png") with Dissolve(1.9)
        1.8
        repeat

#Интро Осколка Арсения
    image shard_intro1_7dl = get_sprite_7dl("custom/shard_anim/shard_intro1_7dl.png")

    image shard_intro2_7dl = get_sprite_7dl("custom/shard_anim/shard_intro2_7dl.png")

    image shard_intro3_7dl = get_sprite_7dl("custom/shard_anim/shard_intro3_7dl.png")

    image shard_intro4_7dl = get_sprite_7dl("custom/shard_anim/shard_intro4_7dl.png")

    image shard_intro5_7dl = get_sprite_7dl("custom/shard_anim/shard_intro5_7dl.png")

    image cg shard_intro_7dl:
        get_sprite_7dl("custom/shard_anim/shard_intro1_7dl.png") with Dissolve(1.5)
        3
        get_sprite_7dl("custom/shard_anim/shard_intro2_7dl.png") with Dissolve(1.5)
        3
        get_sprite_7dl("custom/shard_anim/shard_intro3_7dl.png") with Dissolve(1.5)
        3
        get_sprite_7dl("custom/shard_anim/shard_intro4_7dl.png") with Dissolve(1.5)
        3
        get_sprite_7dl("custom/shard_anim/shard_intro5_7dl.png") with Dissolve(1.5)

# Анимация дождя для ЦГшки
    image gray_rain_anim_7dl:
            get_sprite_7dl("custom/gray_rain/gray_rain_anim1_7dl.png") with dspr
            0.15
            get_sprite_7dl("custom/gray_rain/gray_rain_anim2_7dl.png") with dspr
            0.15
            get_sprite_7dl("custom/gray_rain/gray_rain_anim3_7dl.png") with dspr
            0.15
            repeat

#Застывшая версия
    image gray_rain_stable_7dl = get_sprite_7dl("custom/gray_rain/gray_rain_stable_7dl.png")

#Чёрный фрейм на все случаи жизни
    image blackframe_7dl = get_sprite_7dl("custom/blackframe_7dl.png")

#Падающий телефончик
    image cg downphone1_7dl = get_image_7dl("cg/downphone/downphone1_7dl.jpg")
    image cg downphone2_7dl = get_image_7dl("cg/downphone/downphone2_7dl.jpg")
    image cg downphone3_7dl = get_image_7dl("cg/downphone/downphone3_7dl.jpg")

#Падающий телефончик 2
    image sonyphone_7dl = get_sprite_7dl("custom/sonyphone_7dl.png")

#Кефирный снег
    transform snow_movement_7dl(time, start_pos, x_deviation=0.05, pause_time=0.0, fade_time=1.0):
        truecenter
        ypos -0.25 + 1.5 * start_pos  # стартовая позиция в процентах
        xpos 0.5 - x_deviation + 2 * x_deviation * start_pos  # стартовая девиация
        pause pause_time
        block:
            block:
                alpha 1.0
                parallel:
                    linear (time * (1 - start_pos)) ypos 1.1 xpos (0.5 + x_deviation)
                parallel:
                    pause ((time * (1 - start_pos)) - fade_time)
                    linear fade_time alpha 0.0
            block:
                ypos -0.25
                xpos 0.5 - x_deviation
                alpha 1.0
                linear (time * start_pos) ypos (-0.25 + 1.5 * start_pos) xpos (0.5 - x_deviation + 2 * x_deviation * start_pos)
            repeat
    image bush_frame_7dl = get_image_7dl("gui/Bush/bush_frame.png")

    image snow_layer0_img_7dl = get_image_7dl("gui/snow/0_7dl.png")
    image snow_layer1_img_7dl = get_image_7dl("gui/snow/1_7dl.png")
    image snow_layer2_img_7dl = get_image_7dl("gui/snow/2_7dl.png")
    image snow_layer3_img_7dl = get_image_7dl("gui/snow/3_7dl.png")



    image snow_layer0_anim_7dl:
        contains:
            "snow_layer0_img_7dl"
            snow_movement_7dl(8, 0.0, -0.05)
        contains:
            "snow_layer0_img_7dl"
            snow_movement_7dl(8, 0.25, -0.05)
        contains:
            "snow_layer0_img_7dl"
            snow_movement_7dl(8, 0.5, -0.05)
        contains:
            "snow_layer0_img_7dl"
            snow_movement_7dl(8, 0.75, -0.05)

    image snow_layer1_anim_7dl:
        contains:
            "snow_layer1_img_7dl"
            snow_movement_7dl(10, 0.0, 0.05, pause_time=0.5)
        contains:
            "snow_layer1_img_7dl"
            snow_movement_7dl(10, 0.25, 0.05, pause_time=0.5)
        contains:
            "snow_layer1_img_7dl"
            snow_movement_7dl(10, 0.5, 0.05, pause_time=0.5)
        contains:
            "snow_layer1_img_7dl"
            snow_movement_7dl(10, 0.75, 0.05, pause_time=0.5)

    image snow_layer2_anim_7dl:
        contains:
            "snow_layer2_img_7dl"
            snow_movement_7dl(15, 0.0, -0.05, pause_time=0.07)
        contains:
            "snow_layer2_img_7dl"
            snow_movement_7dl(15, 0.25, -0.05, pause_time=0.07)
        contains:
            "snow_layer2_img_7dl"
            snow_movement_7dl(15, 0.5, -0.05, pause_time=0.07)
        contains:
            "snow_layer2_img_7dl"
            snow_movement_7dl(15, 0.75, -0.05, pause_time=0.07)

    image snow_layer3_anim_7dl:
        contains:
            "snow_layer3_img_7dl"
            snow_movement_7dl(20, 0.0, 0.07)
        contains:
            "snow_layer3_img_7dl"
            snow_movement_7dl(20, 0.25, 0.07)
        contains:
            "snow_layer3_img_7dl"
            snow_movement_7dl(20, 0.5, 0.07)
        contains:
            "snow_layer3_img_7dl"
            snow_movement_7dl(20, 0.75, 0.07)

    image snow_layer0_anim_quick_7dl:
        contains:
            "snow_layer0_img_7dl"
            snow_movement_7dl(3, 0.0, -0.03)
        contains:
            "snow_layer0_img_7dl"
            snow_movement_7dl(3, 0.25, -0.03)
        contains:
            "snow_layer0_img_7dl"
            snow_movement_7dl(3, 0.5, -0.03)
        contains:
            "snow_layer0_img_7dl"
            snow_movement_7dl(3, 0.75, -0.03)

    image snow_layer1_anim_quick_7dl:
        contains:
            "snow_layer1_img_7dl"
            snow_movement_7dl(4, 0.0, 0.05)
        contains:
            "snow_layer1_img_7dl"
            snow_movement_7dl(4, 0.25, 0.05)
        contains:
            "snow_layer1_img_7dl"
            snow_movement_7dl(4, 0.5, 0.05)
        contains:
            "snow_layer1_img_7dl"
            snow_movement_7dl(4, 0.75, 0.05)

    image snow_layer2_anim_quick_7dl:
        contains:
            "snow_layer2_img_7dl"
            snow_movement_7dl(5, 0.0, -0.05)
        contains:
            "snow_layer2_img_7dl"
            snow_movement_7dl(5, 0.25, -0.05)
        contains:
            "snow_layer2_img_7dl"
            snow_movement_7dl(5, 0.5, -0.05)
        contains:
            "snow_layer2_img_7dl"
            snow_movement_7dl(5, 0.75, -0.05)

    image snow_layer3_anim_quick_7dl:
        contains:
            "snow_layer3_img_7dl"
            snow_movement_7dl(5, 0.0, 0.03)
        contains:
            "snow_layer3_img_7dl"
            snow_movement_7dl(5, 0.25, 0.03)
        contains:
            "snow_layer3_img_7dl"
            snow_movement_7dl(5, 0.5, 0.03)
        contains:
            "snow_layer3_img_7dl"
            snow_movement_7dl(5, 0.75, 0.03)


# Леночка в постели
# Дневная
    # Закрытые глаза
    image cg d7_me_un_bed_close_eyes_day_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_emo1_7dl.png"))
    # Сонная
    image cg d7_me_un_bed_sleepy_day_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_emo2_7dl.png"))
    # Улыбка
    image cg d7_me_un_bed_smile_day_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_emo3_7dl.png"))
    # Улыбка 2
    image cg d7_me_un_bed_smile2_day_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_emo4_7dl.png"))
    # Улыбка 3
    image cg d7_me_un_bed_smile3_day_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_emo5_7dl.png"))
    # Серьёзная
    image cg d7_me_un_bed_serious_day_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_emo6_7dl.png"))
    # Нормал
    image cg d7_me_un_bed_normal_day_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_day_emo7_7dl.png"))

# Ночная 1
    # Закрытые глаза
    image cg d7_me_un_bed_close_eyes_night_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo1_7dl.png"))
    # Наркотрип
    image cg d7_me_un_bed_drug_night_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo2_7dl.png"))
    # Удивление
    image cg d7_me_un_bed_surprise_night_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo3_7dl.png") )
    # Счастливая
    image cg d7_me_un_bed_happy_night_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo4_7dl.png"))
    # Улыбка
    # image cg d7_me_un_bed_smile_night_7dl = Composite(
        # (1920, 1080),
        # (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_7dl.jpg"),
        # (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo5_7dl.png"))
    # Улыбка 2
    # image cg d7_me_un_bed_smile2_night_7dl = Composite(
        # (1920, 1080),
        # (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_7dl.jpg"),
        # (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo6_7dl.png"))
    # Улыбка 3
    # image cg d7_me_un_bed_smile3_night_7dl = Composite(
        # (1920, 1080),
        # (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_7dl.jpg"),
        # (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo10_7dl.png"))
    # Серьёзная
    # image cg d7_me_un_bed_serous_night_7dl = Composite(
        # (1920, 1080),
        # (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_7dl.jpg"),
        # (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo11_7dl.png"))
    # Нормал
    image cg d7_me_un_bed_normal_night_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo12_7dl.png"))
# Ночная 2 (шкатулка)
    # Улыбка
    image cg d7_me_un_bed_smile_night2_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo7_7dl.png"))
    # Улыбка 2
    image cg d7_me_un_bed_smile2_night2_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo10_7dl.png"))
    # Нормал
    image cg d7_me_un_bed_normal_night2_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo12_7dl.png"))
# Ночная 3
    #Нормал
    image cg d7_me_un_bed_night3_normal_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night3_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo13_7dl.png"))
    # Улыбка
    image cg d7_me_un_bed_night3_smile_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night3_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo14_7dl.png"))
    # Плачущая улыбка
    image cg d7_me_un_bed_night3_cry_smile_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night3_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo15_7dl.png"))
    # Закрытые
    image cg d7_me_un_bed_night3_close_eyes_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night3_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_bed/d7_me_un_bed_night_emo16_7dl.png"))
    # Эффект слёз
    image d7_me_un_bed_night3_cry_effect_7dl = get_image_7dl("cg/un_bed/d7_me_un_bed_night3_cry_effect_7dl.png")

# Эффект салюта для ночной 3
    image anim_un_kiss_7dl:
        get_image_7dl("cg/un_bed/un_kiss_salute1_7dl.png") with Dissolve(.35)
        pause 0.4
        get_image_7dl("cg/un_bed/un_kiss_salute2_7dl.png") with Dissolve(.35)
        pause 0.4
        get_image_7dl("cg/un_bed/un_kiss_salute3_7dl.png") with Dissolve(.35)
        pause 0.4
        get_image_7dl("cg/un_bed/un_kiss_salute4_7dl.png") with Dissolve(.35)
        pause 0.4
        get_image_7dl("cg/un_bed/un_kiss_salute5_7dl.png") with Dissolve(.35)
        pause 0.4
        repeat
# Поцелуй
    image cg d7_un_kiss_7dl:
        get_image_7dl("cg/un_kiss/d7_un_kiss1_7dl.jpg") with Dissolve(.35)
        pause 0.4
        get_image_7dl("cg/un_kiss/d7_un_kiss2_7dl.jpg") with Dissolve(.35)
        pause 0.4
        get_image_7dl("cg/un_kiss/d7_un_kiss3_7dl.jpg") with Dissolve(.35)
        pause 0.4
        get_image_7dl("cg/un_kiss/d7_un_kiss4_7dl.jpg") with Dissolve(.35)
        pause 0.4
        get_image_7dl("cg/un_kiss/d7_un_kiss5_7dl.jpg") with Dissolve(.35)
        pause 0.4
        get_image_7dl("cg/un_kiss/d7_un_kiss6_7dl.jpg") with Dissolve(.35)
        pause 0.4
        repeat



# Величайший таймскип в истории пива
    image calendar_7dl = get_image_7dl("gui/calendar/calendar_7dl.png")
    image calendar_mar_7dl = get_image_7dl("gui/calendar/march_21_7dl.png")
    image calendar_apr_7dl = get_image_7dl("gui/calendar/april_13_7dl.png")
    image calendar_may_7dl = get_image_7dl("gui/calendar/may_30_7dl.png")
    image calendar_jun_7dl = get_image_7dl("gui/calendar/june_28_7dl.png")
    image calendar_jul_7dl = get_image_7dl("gui/calendar/july_18_7dl.png")
    image calendar_aug_7dl = get_image_7dl("gui/calendar/august_7_7dl.png")
    image calendar_sep_7dl = get_image_7dl("gui/calendar/september_4_7dl.png")
    image calendar_oct_7dl = get_image_7dl("gui/calendar/october_31_7dl.png")
    image calendar_nov_7dl = get_image_7dl("gui/calendar/november_21_7dl.png")
    image calendar_dec1_7dl = get_image_7dl("gui/calendar/december_1_7dl.png")
    image calendar_dec5_7dl = get_image_7dl("gui/calendar/december_5_7dl.png")
    image calendar_dec8_7dl = get_image_7dl("gui/calendar/december_8_7dl.png")
    image calendar_dec15_7dl = get_image_7dl("gui/calendar/december_15_7dl.png")
    image calendar_dec28_7dl = get_image_7dl("gui/calendar/december_28_7dl.png")
    image calendar_jan_7dl = get_image_7dl("gui/calendar/january_12_7dl.png")
    image calendar_feb_7dl = get_image_7dl("gui/calendar/february_24_7dl.png")

# Лучшая японочка лета
    image cg d7_me_ri_skype_smile_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/rioko/d7_me_ri_skype_7dl.jpg"),
        (0, 0), get_image_7dl("cg/rioko/ri_emo1_7dl.png"))
    image cg d7_me_ri_skype_upset_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/rioko/d7_me_ri_skype_7dl.jpg"),
        (0, 0), get_image_7dl("cg/rioko/ri_emo2_7dl.png"))
    image cg d7_me_ri_skype_think_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/rioko/d7_me_ri_skype_7dl.jpg"),
        (0, 0), get_image_7dl("cg/rioko/ri_emo3_7dl.png"))
    image cg d7_me_ri_skype_sad_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/rioko/d7_me_ri_skype_7dl.jpg"),
        (0, 0), get_image_7dl("cg/rioko/ri_emo4_7dl.png"))
    image cg d7_me_ri_skype_wink_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/rioko/d7_me_ri_skype_7dl.jpg"),
        (0, 0), get_image_7dl("cg/rioko/ri_emo5_7dl.png"))

# Лучшая мамка лета
    # анимка лучей
    image d6_me_ma_ray_7dl:
        get_image_7dl("cg/me_ma/ma_ray1_7dl.png") with Dissolve(1.8)
        pause 1.5
        get_image_7dl("cg/me_ma/ma_ray2_7dl.png") with Dissolve(1.8)
        pause 1.5
        repeat
    image cg d6_me_ma_herc_7dl:
        get_image_7dl("cg/me_ma/me_ma3_7dl.jpg") with Dissolve(.60)
        pause 0.55
        get_image_7dl("cg/me_ma/me_ma1_7dl.jpg") with Dissolve(.62)
        pause 0.55
        get_image_7dl("cg/me_ma/me_ma2_7dl.jpg") with Dissolve(.62)
        pause 0.55
        get_image_7dl("cg/me_ma/me_ma1_7dl.jpg") with Dissolve(.60)
        pause 0.55
        repeat

    image cg d6_me_ma_herc2_7dl:
        get_image_7dl("cg/me_ma/me_ma4_7dl.jpg") with Dissolve(.60)
        pause 0.55
        get_image_7dl("cg/me_ma/me_ma5_7dl.jpg") with Dissolve(.62)
        pause 0.55
        get_image_7dl("cg/me_ma/me_ma6_7dl.jpg") with Dissolve(.60)
        pause 0.55
        get_image_7dl("cg/me_ma/me_ma5_7dl.jpg") with Dissolve(.60)
        pause 0.55
        repeat

# Телефонный разговор
    # Семён
    image cg d7_me_herc_call1_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_em1_7dl.png"))

    image cg d7_me_herc_call2_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_em1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_nas_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_nas_call_em1_7dl.png"))

    image cg d7_me_herc_call3_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_em1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_nas_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_nas_call_em4_7dl.png"))

    image cg d7_me_herc_call4_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_em1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_nas_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_nas_call_em2_7dl.png"))

    image cg d7_me_herc_call5_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_em1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_nas_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_nas_call_em3_7dl.png"))

    image cg d7_me_herc_call6_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_herc_call_em2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_nas_call_7dl.png"),
        (0, 0), get_image_7dl("cg/me_nas_call/d7_me_nas_call_em3_7dl.png"))

    # Новогоднее ЦГ Герка пнг
    image cg d7_me_herc_hny5_7dl = get_image_7dl("cg/d7_me_herc_hny5_7dl.png")

    # Прогулка Герка и твоей мамаши)))0))
    image cg d7_me_herc_walk1_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/herc_walk/d7_me_herc_walk_7dl.jpg"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_emo1_7dl.png"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_ma_emo1_7dl.png"))

    image cg d7_me_herc_walk2_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/herc_walk/d7_me_herc_walk_7dl.jpg"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_emo1_7dl.png"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_ma_emo3_7dl.png"))

    image cg d7_me_herc_walk3_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/herc_walk/d7_me_herc_walk_7dl.jpg"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_emo2_7dl.png"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_ma_emo2_7dl.png"))

    image cg d7_me_herc_walk4_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/herc_walk/d7_me_herc_walk_7dl.jpg"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_emo2_7dl.png"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_ma_emo2_7dl.png"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_nas_7dl.png"))
    image cg d7_me_herc_walk5_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/herc_walk/d7_me_herc_walk_7dl.jpg"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_emo2_7dl.png"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_ma_emo4_7dl.png"),
        (0, 0), get_image_7dl("cg/herc_walk/herc_walk_nas_7dl.png"))

    #Славя в столовой
    image cg d1_sl_dinner_bunny_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image("cg/d1_sl_dinner.jpg"),
        (0, 0), get_image_7dl("cg/sl_dinner/d1_sl_dinner_bunny_7dl.png"))
    image cg d1_sl_dinner_sad_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image("cg/d1_sl_dinner.jpg"),
        (0, 0), get_image_7dl("cg/sl_dinner/d1_sl_dinner_sad_7dl.png"))
    image cg d1_sl_dinner_smile_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image("cg/d1_sl_dinner.jpg"),
        (0, 0), get_image_7dl("cg/sl_dinner/d1_sl_dinner_smile_7dl.png"))

    image cg d1_sl_dinner_bunny1_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d1_sl_dinner_pi_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_dinner/d1_sl_dinner_bunny_7dl.png"))
    image cg d1_sl_dinner_sad1_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d1_sl_dinner_pi_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_dinner/d1_sl_dinner_sad_7dl.png"))
    image cg d1_sl_dinner_smile1_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d1_sl_dinner_pi_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_dinner/d1_sl_dinner_smile_7dl.png"))

    image cg d1_sl_dinner_smile2_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d1_sl_dinner_day_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_dinner/d1_sl_dinner_smile_day_7dl.png"))

    image cg d1_sl_dinner_sad2_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/d1_sl_dinner_day_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_dinner/d1_sl_dinner_sad_day_7dl.png"))

    #Алиса тырит лифак
    image cg d3_dv_busted_7dl = get_image_7dl("cg/dv_busted/d3_dv_busted_7dl.jpg")

    image cg d3_dv_busted1_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_7dl.jpg"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_handsup_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_horny_7dl.png"))

    image cg d3_dv_busted2_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_7dl.jpg"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_handsup_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_horny_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_mi_panichands_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_mi_panic_7dl.png"))

    image cg d3_dv_busted3_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_7dl.jpg"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_handsup_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_panic_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_mi_panichands_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_mi_panic_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_plus_7dl.png"))

    image cg d3_dv_busted4_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_7dl.jpg"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_handsup_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_panic_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_mi_shyhands_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_mi_shy_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_plus_7dl.png"))

    image cg d3_dv_busted5_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_7dl.jpg"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_handsdown_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_panic_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_mi_runaway_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_plus_7dl.png"))

    image cg d3_dv_busted6_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_7dl.jpg"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_handsdown_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_dv_panic2_7dl.png"),
        (0, 0), get_image_7dl("cg/dv_busted/d3_dv_busted_plus_7dl.png"))

    # Славя отдыхает
    image cg d7_sl_hospital_7dl = get_image_7dl("cg/sl_hospital/d7_sl_hospital_7dl.jpg")

    image cg d7_sl_hospital_corrected_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/sl_hospital/d7_sl_hospital_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_hospital/d7_sl_hospital_corrected_7dl.png"))

    image cg d7_sl_certificate_7dl = get_image_7dl("cg/sl_hospital/d7_sl_certificate_7dl.jpg")

    image cg d7_sl_certificate_corrected_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/sl_hospital/d7_sl_certificate_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_hospital/d7_sl_certificate_corrected_7dl.png"))

    # Славя вайбит
    image cg d4_sl_pontoon1_7dl = get_image_7dl("cg/sl_pontoon/d4_sl_pontoon1_7dl.jpg")
    image cg d4_sl_pontoon2_7dl = get_image_7dl("cg/sl_pontoon/d4_sl_pontoon2_7dl.jpg")
    image cg d4_sl_pontoon3_7dl = get_image_7dl("cg/sl_pontoon/d4_sl_pontoon3_7dl.jpg")
    image cg d4_sl_pontoon4_7dl = get_image_7dl("cg/sl_pontoon/d4_sl_pontoon4_7dl.jpg")


# Гори-гори моя свеча
    image candle_flicker_1 = get_image_7dl("cg/me_candle/candle_flicker_1.png")
    image candle_flicker_2 = get_image_7dl("cg/me_candle/candle_flicker_2.png")
    image candle_flicker_3 = get_image_7dl("cg/me_candle/candle_flicker_3.png")
    image candle_flicker_4 = get_image_7dl("cg/me_candle/candle_flicker_4.png")

    image candle_flickering:
        get_image_7dl("cg/me_candle/candle_flicker_1.png") with Dissolve(.5)
        pause 0.5
        get_image_7dl("cg/me_candle/candle_flicker_2.png") with Dissolve(.5)
        pause 0.5
        get_image_7dl("cg/me_candle/candle_flicker_3.png") with Dissolve(.5)
        pause 0.5
        get_image_7dl("cg/me_candle/candle_flicker_4.png") with Dissolve(.5)
        pause 0.5
        get_image_7dl("cg/me_candle/candle_flicker_3.png") with Dissolve(.5)
        pause 0.5
        get_image_7dl("cg/me_candle/candle_flicker_2.png") with Dissolve(.5)
        pause 0.5
        repeat

#Леначка в хламину
    image cg un_day4_teaparty21_gal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty21_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty21_semenhead2_7dl.png"),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty21_semenhead2_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty21_mikuhead2_7dl.png"),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty21_mikuhead2_cute3_7dl.png"),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty21_lenahead1_horny_7dl.png"))

    image un_day4_teaparty21_7dl = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_7dl.jpg")
    image un_day4_teaparty22_7dl = get_image_7dl("cg/un_teaparty/un_day4_teaparty22_7dl.jpg")
    image teaparty21_lenaarm2 = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_lenaarm2_7dl.png")
    image teaparty21_lenahead1_horny = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_lenahead1_horny_7dl.png")
    image teaparty21_lenahead1_shy = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_lenahead1_shy_7dl.png")
    image teaparty21_lenahead1_shy2 = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_lenahead1_shy2_7dl.png")
    image teaparty21_lenahead2 = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_lenahead2_7dl.png")
    image teaparty21_lenahead2_grin = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_lenahead2_grin_7dl.png")
    image teaparty21_lenahead2_sad = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_lenahead2_sad_7dl.png")
    image teaparty21_mikuhead1_grin = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_mikuhead1_grin_7dl.png")
    image teaparty21_mikuhead1_normal = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_mikuhead1_normal_7dl.png")
    image teaparty21_mikuhead2_cute = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_mikuhead2_cute_7dl.png")
    image teaparty21_mikuhead2_cute2 = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_mikuhead2_cute2_7dl.png")
    image teaparty21_mikuhead2_cute3 = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_mikuhead2_cute3_7dl.png")
    image teaparty21_questionmark = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_questionmark_7dl.png")
    image teaparty21_semenhead1_angry = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_semenhead1_angry_7dl.png")
    image teaparty21_semenhead1_surp = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_semenhead1_surp_7dl.png")
    image teaparty21_mikuhead1_semenhead2 = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_semenhead2_7dl.png")
    image teaparty21_semenhead2_surp = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_semenhead2_surp_7dl.png")
    image teaparty21_semenhead2_normal = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_semenhead2_normal_7dl.png")
    image teaparty21_mikuhead2 = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_mikuhead2_7dl.png")
    image teaparty21_semenhead2 = get_image_7dl("cg/un_teaparty/un_day4_teaparty21_semenhead2_7dl.png")

#Леначке плохо
    image cg un_day4_teaparty3_gal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty3_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty3_withmi_7dl.png"),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty3_migrin_7dl.png"),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty3_unface_7dl.png"))

    image cg un_day4_teaparty3_bueee_gal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty3_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_teaparty/un_day4_teaparty3_bueee_7dl.png"))

    image un_day4_teaparty3 = get_image_7dl("cg/un_teaparty/un_day4_teaparty3_7dl.jpg")
    image teaparty3_alone = get_image_7dl("cg/un_teaparty/un_day4_teaparty3_alone_7dl.png")
    image teaparty3_bueee = get_image_7dl("cg/un_teaparty/un_day4_teaparty3_bueee_7dl.png")
    image teaparty3_migrin = get_image_7dl("cg/un_teaparty/un_day4_teaparty3_migrin_7dl.png")
    image teaparty3_mismile = get_image_7dl("cg/un_teaparty/un_day4_teaparty3_mismile_7dl.png")
    image teaparty3_withmi = get_image_7dl("cg/un_teaparty/un_day4_teaparty3_withmi_7dl.png")
    image teaparty3_unface = get_image_7dl("cg/un_teaparty/un_day4_teaparty3_unface_7dl.png")

#Симен памирац
    image cg day7_us_fairytale3 = get_image_7dl("cg/us_fairytale/day7_us_fairytale3_7dl.jpg")
    image cg day7_us_fairytale2 = get_image_7dl("cg/us_fairytale/day7_us_fairytale2_7dl.jpg")
    image cg day7_us_fairytale = get_image_7dl("cg/us_fairytale/day7_us_fairytale1_7dl.jpg")
    image cg day7_us_fairytale_white = get_image_7dl("cg/us_fairytale/day7_us_fairytale_white_7dl.jpg")

#Не виноватая я
    image cg d6_un_me_un_sad_surp = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head1_sad_surprise_7dl.png"))

    image cg d6_un_me_un_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_smile_7dl.png"))

    image cg d6_un_me_un_normal_head_2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_normal_7dl.png"))

    image cg d6_un_me_un_normal_head_1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head1_normal_7dl.png"))

    image cg d6_un_me_un_questioned = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head1_questioned_7dl.png"))

    image cg d6_un_me_un_wtf = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head1_wtf_7dl.png"))

    image cg d6_un_me_un_sad_head_1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head1_sad_7dl.png"))

    image cg d6_un_me_un_sad_head_2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_sad_7dl.png"))

    image cg d6_un_me_un_shocked_head_2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_shocked_7dl.png"))

    image cg d6_un_me_un_shy = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head1_shy_7dl.png"))

    image cg d6_un_me_un_shocked_head_1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head1_shocked_7dl.png"))

    image cg d6_un_me_un_shocked_eyes_head_1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head1_shocked_eyes_7dl.png"))

    image cg d6_un_me_un_susp_head_2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_susp_7dl.png"))

    image cg d6_un_me_un_normal_eyes_head_2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_7dl.jpg"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/un_me_beach/d6_un_me_beach_head2_normal_eyes_7dl.png"))

# Дневничок, чтобы ты заплакала

    image cg d6_me_mt_diary = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_blur_mt_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_7dl.png"))

    image cg d6_me_mt_diary_first_page = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_blur_mt_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_first_page_7dl.png"))

    image cg d6_me_mt_diary_first_page_listing = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_blur_mt_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_listing1_7dl.png"))

    image cg d6_me_mt_diary_second_page = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_blur_mt_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_second_page_7dl.png"))

    image cg d6_me_mt_diary_second_page_listing = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_blur_mt_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_listing2_7dl.png"))

    image cg d6_me_mt_diary_third_page = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_blur_mt_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_diary/d6_me_mt_diary_third_page_7dl.png"))

# Ольга скрипит

    image cg d6_me_mt_sitting_normal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_sitting/d6_me_mt_sitting_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_sitting/d6_me_mt_sitting_normal_7dl.png"))

    image cg d6_me_mt_sitting_sad_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_sitting/d6_me_mt_sitting_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_sitting/d6_me_mt_sitting_sad_smile_7dl.png"))

# Тяма и Няон

    image cg d7_sl_hold_normal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_hold_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_hold_normal_7dl.png"))

    image cg d7_sl_hold_normal2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_hold_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_hold_normal2_7dl.png"))

    image cg d7_sl_hold_surprise = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_hold_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_hold_surp_7dl.png"))

    image cg d7_sl_kiss_tear = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_kiss_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_kiss_close_eyes_7dl.png"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_kiss_sunshine_7dl.png"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_kiss_sunshine2_7dl.png"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_tear_7dl.png"))

# Хочешь я в глаза, взгляну в твои глаза...

    image cg d7_sl_tyama_nyaon = get_image_7dl("cg/sl_tyama_neon/d7_sl_eyes_7dl.jpg")

    image cg d7_sl_tyama_nyaon_sl_eyes = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_eyes_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_sl_eyes_7dl.png"))

    image cg d7_sl_tyama_nyaon_herk_eyes = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_eyes_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_sl_eyes_7dl.png"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_herk_eyes_7dl.png"))

    image cg d7_sl_tyama_nyaon_tear = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_eyes_7dl.jpg"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_herk_eyes_7dl.png"),
        (0, 0), get_image_7dl("cg/sl_tyama_neon/d7_sl_eyes_tear_7dl.png"))

# Качельки

    image cg d4_mt_swing_mt_normal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_normal_7dl.png"))

    image cg d4_mt_swing_me_mt_normal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_head1_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_normal_7dl.png"))

    image cg d4_mt_swing_me_mt_sad_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_head1_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_sad_smile_7dl.png"))

    image cg d4_mt_swing_me_mt_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_smile_7dl.png"))

    image cg d4_mt_swing_me_mt_think = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_think_7dl.png"))

    image cg d4_mt_swing_me_mt_think_eyes = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_think_eyes_7dl.png"))

    image cg d4_mt_swing_me_mt_laugh = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_laugh_7dl.png"))

    image cg d4_mt_swing_me_mt_grin = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_grin_7dl.png"))

    image cg d4_mt_swing_me_mt_sad = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_sad_7dl.png"))

    image cg d4_mt_swing_me_smile_hand_mt_sad = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_hand_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_sad_7dl.png"))

    image cg d4_mt_swing_me_smile_hand_mt_shy = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_hand_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_shy_7dl.png"))

    image cg d4_mt_swing_me_scared_hand_mt_shy = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_hand_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_scared_7dl.png"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_shy_7dl.png"))

    image cg d4_mt_swing_me_shy_head2_hand_mt_shy = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_hand_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_shy_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_shy_7dl.png"))

    image cg d4_mt_swing_me_shy_head2_hand_mt_grin = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_hand_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_shy_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_grin_7dl.png"))

    image cg d4_mt_swing_me_shy_head1_mt_grin = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_shy_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_grin_7dl.png"))

    image cg d4_mt_swing_me_shy_head1_mt_laugh = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_head2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_me_shy_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/mt_swing/d4_mt_swing_mt_laugh_7dl.png"))

# Два шизика спорят, кто из них шизее.



    image cg d6_me_mt_masks_me_questioning_mt_normal_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_up_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_shocked_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_normal_7dl.png"))

    image cg d6_me_mt_masks_me_questioning_mt_smile_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_shocked_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_smile_7dl.png"))

    image cg d6_me_mt_masks_me_confuse_mt_smile_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_fists_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_confuse_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_smile_7dl.png"))

    image cg d6_me_mt_masks_me_confuse2_mt_smile_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_confuse2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_smile_7dl.png"))

    image cg d6_me_mt_masks_me_confuse2_mt_smile_liar_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_liar_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_confuse2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_smile_7dl.png"))

    image cg d6_me_mt_masks_me_think_mt_smile_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_think_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_smile_7dl.png"))

    image cg d6_me_mt_masks_me_surp_mt_smile_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_surp_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_smile_7dl.png"))

    image cg d6_me_mt_masks_me_surp_mt_normal_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_surp_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_normal_7dl.png"))

    image cg d6_me_mt_masks_me_normal_mt_normal_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_normal_7dl.png"))

    image cg d6_me_mt_masks_me_normal_mt_sad_smile_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_sad_smile_7dl.png"))

    image cg d6_me_mt_masks_me_normal_mt_normal_eyes2_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_normal_eyes2_7dl.png"))

    image cg d6_me_mt_masks_me_apolo_mt_normal_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_fists_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_apolo_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_normal_7dl.png"))

    image cg d6_me_mt_masks_me_apolo_mt_surp_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_fists_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_apolo_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_surp_7dl.png"))

    image cg d6_me_mt_masks_me_apolo2_mt_surp_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_apolo2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_surp_7dl.png"))

    image cg d6_me_mt_masks_me_upset_mt_sad_smile_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_upset_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_sad_smile_7dl.png"))

    image cg d6_me_mt_masks_me_sad_mt_sad_smile_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_sad_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_sad_smile_7dl.png"))

    image cg d6_me_mt_masks_me_sad_mt_sad_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_sad_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_sad_7dl.png"))

    image cg d6_me_mt_masks_me_sad_mt_hands_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_tilt_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_sad_7dl.png"))

    image cg d6_me_mt_masks_me_sad_smile_mt_hands_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_tilt_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_sad_smile_7dl.png"))

    image cg d6_me_mt_masks_me_sad_smile_mt_sad_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_sad_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_sad_7dl.png"))

    image cg d6_me_mt_masks_me_sad_smile_mt_sad_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_sad_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_sad_7dl.png"))

    image cg d6_me_mt_masks_me_shocked_mt_normal_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_shocked_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_normal_7dl.png"))


    image cg d6_me_mt_masks_me_deep_think_mt_normal_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_deep_think_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_normal_7dl.png"))

    image cg d6_me_mt_masks_me_upset_mt_normal_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_upset_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_normal_7dl.png"))

    image cg d6_me_mt_masks_me_shy_mt_normal_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_shy_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_normal_7dl.png"))

    image cg d6_me_mt_masks_me_upset_mt_sad_smile_eyes_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_upset_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_sad_smile_eyes_7dl.png"))

    image cg d6_me_mt_masks_me_upset_mt_sad_smile_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_upset_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_sad_smile_7dl.png"))

    image cg d6_me_mt_masks_me_sad_smile_mt_sad_smile_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_sad_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_sad_smile_7dl.png"))

    image cg d6_me_mt_masks_me_head2_normal_mt_normal_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head2_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_normal_7dl.png"))


    image cg d6_me_mt_masks_me_head2_normal_shade_mt_normal_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head2_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_normal_7dl.png"))

    image cg d6_me_mt_masks_me_head2_sad_smile_shade_mt_normal_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head2_sad_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_normal_7dl.png"))

    image cg d6_me_mt_masks_me_head2_sad_smile_shade_mt_grin_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head2_sad_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_grin_7dl.png"))

    image cg d6_me_mt_masks_me_head2_normal_mt_grin_shade_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head2_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_grin_shade_7dl.png"))

    image cg d6_me_mt_masks_me_normal_mt_grin_shade_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_grin_shade_7dl.png"))

    image cg d6_me_mt_masks_me_normal_mt_sad_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_sad_7dl.png"))

    image cg d6_me_mt_masks_me_upset_mt_normal_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_upset_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_normal_7dl.png"))

    image cg d6_me_mt_masks_me_neutral_smile_mt_normal_eyes2_head2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_neutral_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_left_normal_eyes2_7dl.png"))

    image cg d6_me_mt_masks_me_neutral_smile_mt_normal_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_neutral_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_normal_7dl.png"))

    image cg d6_me_mt_masks_me_neutral_smile2_mt_normal_head1 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_hands_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_me_head1_neutral_smile2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_talking/me_mt_masks/d6_me_mt_masks_mt_straight_normal_7dl.png"))

    # Можно!

    image cg d7_me_us_ps_walk_sad = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_walk_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_walk_sad_7dl.png"))

    image cg d7_me_us_ps_walk_think = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_walk_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_walk_think_7dl.png"))

    image cg d7_me_us_ps_walk_think2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_walk_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_walk_think2_7dl.png"))

    image cg d7_me_us_ps_close_eyes = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_walk_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_walk_close_eyes_7dl.png"))

    # Нельзя!

    image cg d7_me_us_ps_stand_wall = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_wall_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_stand_7dl.png"))

    image cg d7_me_us_ps_stand_sad = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_wall_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_stand_7dl.png"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_stand_mirror_sad_7dl.png"))

    image cg d7_me_us_ps_stand_dream = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_wall_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_stand_mirror_dream_7dl.png"))

    image cg d7_me_us_ps_stand_angry = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_wall_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_stand_7dl.png"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_stand_mirror_angry_7dl.png"))

    image cg d7_me_us_ps_stand_angry_hand = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_wall_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_hand_7dl.png"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_stand_mirror_angry_7dl.png"))

    image cg d7_me_us_ps_stand_angry_wall = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_wall_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_stand_mirror_angry_7dl.png"))

    image cg d7_me_us_ps_stand_sad_wall = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_wall_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_us_ps/d7_us_ps_stand_mirror_sad_7dl.png"))

    # Мечта Сани.

    image cg d7_me_mt_bus_me_shy_mt_normal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_shy_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_normal_7dl.png"))

    image cg d7_me_mt_bus_me_shy2_mt_normal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_shy2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_normal_7dl.png"))

    image cg d7_me_mt_bus_me_shy2_mt_normal2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_shy_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_normal2_7dl.png"))

    image cg d7_me_mt_bus_me_shy2_mt_serious = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_shy_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_serious_7dl.png"))

    image cg d7_me_mt_bus_me_normal_mt_normal = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_normal_7dl.png"))

    image cg d7_me_mt_bus_me_normal_mt_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_smile_7dl.png"))

    image cg d7_me_mt_bus_me_normal_mt_laugh = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_laugh_7dl.png"))

    image cg d7_me_mt_bus_me_normal_mt_normal2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_normal_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_normal2_7dl.png"))

    image cg d7_me_mt_bus_me_hand_mt_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_handjob_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_shy2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_smile_7dl.png"))

    image cg d7_me_mt_bus_me_shy2_mt_laugh2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_shy2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_laugh2_7dl.png"))

    image cg d7_me_mt_bus_hands_me_shy2_mt_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_hands_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_me_shy2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_mt_bus/day7_me_mt_bus_mt_smile_7dl.png"))

    # Сидим тута.

    image cg d7_me_bench_dontlike = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_bench/me_day7_bench_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_bench/me_day7_bench_dontlike_7dl.png"))

    image cg d7_me_bench_think = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_bench/me_day7_bench_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_bench/me_day7_bench_think_7dl.png"))

    image cg d7_me_bench_close_eyes = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_bench/me_day7_bench_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_bench/me_day7_bench_close_eyes_7dl.png"))

    image cg d7_me_bench_close_close_eyes = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_bench/me_day7_bench_close_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_bench/me_day7_bench_close_close_eyes_7dl.png"))

    image cg d7_me_bench_close_open_eyes = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_bench/me_day7_bench_close_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_bench/me_day7_bench_close_open_eyes_7dl.png"))

    # Пещерный человек

    #image cg d7_me_cave_knees:
    #    get_image_7dl("cg/me_cave/d7_me_cave_knees_7dl.jpg") with Dissolve(1.5)
    #    1.5
    #    get_image_7dl("cg/me_cave/d7_me_cave_knees_greenlight_7dl.jpg") with Dissolve(1.5)
    #    1.5
    #    repeat

    #image d7_me_cave_greenlight_7dl:
    #    get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png") with Dissolve(1.5)
    #    2.5
    #    "d7_me_cave_greenlight0_7dl" with Dissolve(1.5)
    #    1.5
    #    repeat
    #
    #image d7_me_cave_greenlight0_7dl:
    #    contains:
    #        get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png")
    #        alpha 0.0
    #

    image cg d7_me_cave_close_fear_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_close_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_close_fear_7dl.png"))

    image cg d7_me_cave_close_normal_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_close_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_close_normal_7dl.png"))

    image cg d7_me_cave_close_surp_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_close_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_close_surp_7dl.png"))

    image cg d7_me_cave_close_surp2_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_close_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_close_surp2_7dl.png"))

    image cg d7_me_cave1_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_surp_7dl.png"))

    image cg d7_me_cave2_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_surp_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke0_7dl.png"))

    image cg d7_me_cave3_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_surp_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke0_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke_7dl.png"))

    image cg d7_me_cave4_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_surp_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke0_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory2_7dl.png"))

    image cg d7_me_cave5_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_surp_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke0_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory4_7dl.png"))

    image cg d7_me_cave6_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_surp_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke0_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory4_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory1_7dl.png"))

    image cg d7_me_cave7_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_surp_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke0_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory3_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory4_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory1_7dl.png"))

    image cg d7_me_cave8_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_body_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_surp_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_smoke0_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory3_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory4_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_memory1_7dl.png"))

    image cg d7_me_cave9_7dl = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_greenlight_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_body2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_cave/d7_me_cave_hollow_7dl.png"))

    image cg d7_me_cave_knees_greenlight_7dl = get_image_7dl("cg/me_cave/d7_me_cave_knees_greenlight_7dl.jpg")
    image cg d7_me_cave_knees_7dl = get_image_7dl("cg/me_cave/d7_me_cave_knees_7dl.jpg")


    # Юлька с Мажором

    image cg d7_me_trip1_me_normal_uv2_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv2_together_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_head2_eyes_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_normal_7dl.png"))

    image cg d7_me_trip1_me_normal_uv_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_together_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_head1_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_normal_7dl.png"))

    image cg d7_me_trip1_me_normal_uv_dontlike = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_together_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_head1_dontlike_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_normal_7dl.png"))

    image cg d7_me_trip2_me_close_eyes_uv_dontlike = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_together_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_head1_dontlike_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_head2_close_eyes_7dl.png"))

    image cg d7_me_trip2_me_anxiety_uv_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_together_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_head1_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_anxiety_7dl.png"))

    image cg d7_me_trip2_me_anxiety2_uv_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_together_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_head1_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_anxiety2_7dl.png"))

    image cg d7_me_trip2_me_anxiety21_uv_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv2_together_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_head2_eyes_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_anxiety2_7dl.png"))

    image cg d7_me_trip2_me_anxiety22_uv_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_me2_ghost_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_together_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_head1_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_anxiety2_7dl.png"))

    image cg d7_me_trip2_me_alpha_normal_uv_dontlike = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_me2_ghost_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_together_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_me1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_head1_dontlike_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_normal_7dl.png"))

    image cg d7_me_trip2_me_alpha_normal_uv_dontlike2 = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip2_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_together_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_me1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_head1_dontlike_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_normal_7dl.png"))

    image cg d7_me_trip3_me_alpha_close_eyes_uv_dontlike = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_me1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv1_dontlike_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_head2_close_eyes_7dl.png"))

    image cg d7_me_trip3_me_alpha_scary_uv_dontlike = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_me1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv1_dontlike_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_head2_scary_7dl.png"))



    image cg d7_me_trip4_me_alpha_scary_hand_uv_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip4_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_me2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv1_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_head2_semiclose_eyes_alpha_7dl.png"))

    image cg d7_me_trip5_me_alpha_scary_hand_uv_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip4_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_me2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv1_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_head2_semiclose_eyes_alpha_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip5_7dl.png"))

    image cg d7_me_trip6_me_alpha_scary_hand_uv_smile = Composite(
        (1920, 1080),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip4_7dl.jpg"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv1_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_me2_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip3_uv1_smile_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip_me_head2_semiclose_eyes_alpha_7dl.png"),
        (0, 0), get_image_7dl("cg/me_uv_trip/d7_uv_trip6_7dl.png"))

    image anim_uv_trip_light:
        "cg d7_me_trip4_me_alpha_scary_hand_uv_smile" with Dissolve(1.2)
        pause 1.2
        "cg d7_me_trip5_me_alpha_scary_hand_uv_smile" with Dissolve(1.2)
        pause 1.2
        repeat

    image d7_uv_trip6_7dl = get_image_7dl("cg/me_uv_trip/d7_uv_trip6_7dl.png")