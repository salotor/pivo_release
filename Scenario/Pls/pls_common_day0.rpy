label alt_day0_prologue:
    $ renpy.pause(2)
    $ prolog_time()
    scene black
    play music music_list["drown"] fadein 3
    $ plthr = u"Выбор"
    $ alt_chapter0()
    with fade
    show spill_red with dspr
    $ renpy.pause(2)
    show spill_gray with dspr
    with dissolve2
    $ renpy.pause(3)
    scene black with fade2
    show alt_credits "Я с трудом вспоминаю, \n с чего всё началось…" with dissolve2:
        pos (200,540)
    with dissolve2
    $ renpy.block_rollback()
    if persistent.me_neu_loki_true and persistent.me_neu_dr_true and persistent.me_neu_herc_true:
        call screen alt_day0_charsel_am
    else:
        call screen alt_day0_charsel

label alt_day0_char:
    $ renpy.block_rollback()
    if herc:
        $ plthr = u"Герк"
        play sound sfx_7dl["mpbt"] fadein 0
        if persistent.me_neu_loki_true and persistent.me_neu_dr_true and persistent.me_neu_herc_true:
            scene intro_herc_am with dissolve
        else:
            scene intro_herc with dissolve

    elif loki:
        $ plthr = u"Локи"
        play sound sfx_punch_medium
        if persistent.me_neu_loki_true and persistent.me_neu_dr_true and persistent.me_neu_herc_true:
            scene intro_loki_am with dissolve
        else:
            scene intro_loki with dissolve

    elif dr:
        $ plthr = u"Дрищ"
        play sound sfx_wind_gust
        if persistent.me_neu_loki_true and persistent.me_neu_dr_true and persistent.me_neu_herc_true:
            scene intro_dr_am with dissolve
        else:
            scene intro_dr with dissolve

    else:
        $ plthr = u"Мажор"
        play sound sfx_7dl["role_am"]
        scene intro_am_pi with dissolve2
        $ renpy.pause(4)
        $ renpy.music.set_volume(0.5, delay=0, channel='sound')
        play sound sfx_7dl["glass_break"]
        show intro_am_hldr
        $ renpy.pause(2)
        $ renpy.music.set_volume(1.0, delay=0, channel='sound')

    $ renpy.pause(1)
    $ alt_chapter0()

    if herc:
        play sound sfx_7dl["role_herc"]
    elif loki:
        play sound sfx_7dl["role_loki"]
    elif dr:
        play sound sfx_7dl["role_drisch"]

    $ renpy.pause(4)
    with fade2
    $ routetag = "prologue"
    scene black with fade
    show alt_credits "ПРЕДУПРЕЖДЕНИЕ\nВсе совпадения персонажей и характеров\nс реально существующими людьми\nсчитать злой волей автора" with dissolve2:
        pos (200,540)
    $ renpy.pause(4)
    $ prolog_time()

    if herc:
        call alt_day0_start_h
    elif loki:
        call alt_day0_start_l
    elif dr:
        call alt_day0_start_d
    else:
        call alt_day0_start_am

label alt_day0_start:
    if alt_day_catapult:
        return

    $ plthr_temp = plthr
    $ plthr = u"Ролик"
    if renpy_version_int >= 740000:
        $ renpy.music.play(music_7dl["cheap_lighters"], channel='music', loop=True, relative_volume=0)
    $ movielength = 123.9
    $ movieplaying = default_7dl_path+"Pics/gui/intro/opening.webm"
    call screen alt_movie_screen with dissolve
    stop music
    $ plthr = plthr_temp

    if not (herc or loki or dr):
        jump alt_day1_me_7dl_start
    else:
        jump alt_day1_start