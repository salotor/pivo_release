init:
    $ alt_timer = 10

# Ачивки
    image acm_logo_va_victim:
        default_7dl_path + "Old_Road/unreleased/dv_7dl/acm_logo_va_victim_1.png"
        0.2
        default_7dl_path + "Old_Road/unreleased/dv_7dl/acm_logo_va_victim_2.png"
        0.2
        default_7dl_path + "Old_Road/unreleased/dv_7dl/acm_logo_va_victim_3.png"
        0.2
        repeat

screen alt_timer:
    add "timer_anim" xalign 0.5 yalign 0.5
    key "7" action [Hide("alt_timer"), Return()]
    text "ВЕРНУТЬСЯ В ЛАГЕРЬ! (--->7<---)" align (0.5, 0.8) color "#FF0000"
    timer 2.0 action [Hide("alt_timer"), SetVariable("alt_day_catapult", True), Return()]