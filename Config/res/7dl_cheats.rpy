﻿init 2:
    $ sdl_cheat_string = ""

    image sdl_cheat_terminal_icon = get_image_7dl("gui/menu_elem/misc/cheat_terminal_icon.png")

init python:
    # Обрабатываем символ
    def sdl_cheat_read_char(char):
        # Добавляем новый символ
        global sdl_cheat_string
        sdl_cheat_string += char

        # Проверяем, корректна ли введённая последовательность
        cheat_string_correct = False
        for code in sdl_cheat_code_to_handler:
            if code.startswith(sdl_cheat_string):
                cheat_string_correct = True
                break
        # Если нет - прерываем ввод чит-кода
        if not cheat_string_correct:
            sdl_cheat_string = ""
            renpy.hide_screen("sdl_cheat_reader")
            return

        # Если код полностью введён - вызываем обработчик
        if sdl_cheat_string in sdl_cheat_code_to_handler:
            sdl_cheat_code_to_handler[sdl_cheat_string][0](sdl_cheat_code_to_handler[sdl_cheat_string][1])
            sdl_cheat_string = ""
            renpy.hide_screen("sdl_cheat_reader")
            return

    # Обработчики чит-кодов
    def sdl_cheat_enable_all(name):
        for ch, char in sdl_achv_section_to_routes.items():
            if ch != "va":
                for route in char:
                    for achieve in route.achv_arr:
                        sdl_persistent_inc(achieve.persistent)
        sdl_persistent_inc("alt_cheater")
        renpy.play(sfx_konami_on, channel='sound')

    def sdl_cheat_enable(name):
        for ch, char in sdl_achv_section_to_routes.items():
            if ch == name:
                for route in char:
                    for achieve in route.achv_arr:
                        sdl_persistent_inc(achieve.persistent)
        sdl_persistent_inc("alt_cheater")
        renpy.play(sfx_konami_on, channel='sound')


    def sdl_cheat_disable_all(name):
        for ch, char in sdl_achv_section_to_routes.items():
            for route in char:
                for achieve in route.achv_arr:
                    sdl_persistent_res(achieve.persistent)
        sdl_persistent_res("alt_cheater")
        renpy.play(sfx_konami_off, channel='sound')

    def sdl_cheat_jojo(name):
        if getattr(persistent, "jojo_reference_7dl"):
            setattr(persistent, "jojo_reference_7dl", False)
            renpy.play(sfx_konami_off, channel='sound')
        else:
            setattr(persistent, "jojo_reference_7dl", True)
            renpy.play(sfx_7dl["jojo"], channel='sound')

    # Словарь чит-кодов
    sdl_cheat_code_to_handler = {
        "7dl4people"   : [sdl_cheat_enable_all, ""],
        "justnamiki"   : [sdl_cheat_enable, "mi"],
        "justalice"    : [sdl_cheat_enable, "dv"],
        "justslavya"   : [sdl_cheat_enable, "sl"],
        "justlena"     : [sdl_cheat_enable, "un"],
        "justolga"     : [sdl_cheat_enable, "mt"],
        "justulyana"   : [sdl_cheat_enable, "us"],
        "foreveralone" : [sdl_cheat_enable, "me"],
        "fullreset"    : [sdl_cheat_disable_all, ""],
        "jojoreference": [sdl_cheat_jojo, ""]
    }

screen sdl_cheat_reader:
    tag cheat_reader

    key "0" action Function(sdl_cheat_read_char, '0')
    key "1" action Function(sdl_cheat_read_char, '1')
    key "2" action Function(sdl_cheat_read_char, '2')
    key "3" action Function(sdl_cheat_read_char, '3')
    key "4" action Function(sdl_cheat_read_char, '4')
    key "5" action Function(sdl_cheat_read_char, '5')
    key "6" action Function(sdl_cheat_read_char, '6')
    key "7" action Function(sdl_cheat_read_char, '7')
    key "8" action Function(sdl_cheat_read_char, '8')
    key "9" action Function(sdl_cheat_read_char, '9')
    key "a" action Function(sdl_cheat_read_char, 'a')
    key "b" action Function(sdl_cheat_read_char, 'b')
    key "c" action Function(sdl_cheat_read_char, 'c')
    key "d" action Function(sdl_cheat_read_char, 'd')
    key "e" action Function(sdl_cheat_read_char, 'e')
    key "f" action Function(sdl_cheat_read_char, 'f')
    key "g" action Function(sdl_cheat_read_char, 'g')
    key "h" action Function(sdl_cheat_read_char, 'h')
    key "i" action Function(sdl_cheat_read_char, 'i')
    key "j" action Function(sdl_cheat_read_char, 'j')
    key "k" action Function(sdl_cheat_read_char, 'k')
    key "l" action Function(sdl_cheat_read_char, 'l')
    key "m" action Function(sdl_cheat_read_char, 'm')
    key "n" action Function(sdl_cheat_read_char, 'n')
    key "o" action Function(sdl_cheat_read_char, 'o')
    key "p" action Function(sdl_cheat_read_char, 'p')
    key "q" action Function(sdl_cheat_read_char, 'q')
    key "r" action Function(sdl_cheat_read_char, 'r')
    key "s" action Function(sdl_cheat_read_char, 's')
    key "t" action Function(sdl_cheat_read_char, 't')
    key "u" action Function(sdl_cheat_read_char, 'u')
    key "v" action Function(sdl_cheat_read_char, 'v')
    key "w" action Function(sdl_cheat_read_char, 'w')
    key "x" action Function(sdl_cheat_read_char, 'x')
    key "y" action Function(sdl_cheat_read_char, 'y')
    key "z" action Function(sdl_cheat_read_char, 'z')

    add "sdl_cheat_terminal_icon" pos (1750, 910)

# Ловим наркоманов, нажимающих одновременно "Shift", "+", "~"
init python:
    def sdl_cheat_fiasko():
        sdl_persistent_inc("alt_narcomaniac")

        sdl_persistent_res(random.choice(random.choice(sdl_achv_names)))

        renpy.play(sfx_7dl["fiasko"], channel='sound')

screen sdl_cheat_watcher:
    tag cheat_watcher

    key "~" action [Hide("sdl_cheat_narcomaniac"), Function(sdl_cheat_fiasko), Show("sdl_cheat_narcomaniac")]

screen sdl_cheat_narcomaniac:
    tag cheat_reader

    text "НАРКОМАН [[[persistent.alt_narcomaniac]]!" size 30 color "#FF0000" bold True pos (1450, 1035)

    timer 3.0 action Hide("sdl_cheat_narcomaniac", transition=Dissolve(3.0))
