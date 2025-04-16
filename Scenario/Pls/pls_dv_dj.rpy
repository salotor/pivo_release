label alt_day4_dv_dj_start:
    call alt_day4_dv_dj_vars
    $ alt_pause(.1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Алиса. DJ. Утро")
    call alt_day4_dv_dj_morning
    $ alt_pause(1)
    $ alt_save_name(4, u"Алиса. DJ. Завтрак")
    call alt_day4_dv_dj_breakfast
    $ alt_pause(1)
    $ alt_chapter(4, u"Алиса. DJ. Освобождение рыжей!")
    call alt_day4_dv_dj_alise_free
    $ alt_pause(1)
    $ alt_save_name(4, u"Алиса. DJ. Рыжий ураган")
    call alt_day4_dv_dj_radio_event
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_save_name(4, u"Алиса. DJ. Обед")
    call alt_day4_dv_dj_lunch
    $ alt_pause(1)
    $ alt_chapter(4, u"Алиса. DJ. Тихий час")
    call alt_day4_dv_dj_silent_hour
    $ alt_pause(1)
    $ alt_save_name(4, u"Алиса. DJ. Полдник")
    call alt_day4_dv_dj_afternoon
    $ alt_pause(1)
    $ alt_save_name(4, u"Алиса. DJ. Концерт")
    call alt_day4_dv_dj_concert
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Алиса. DJ. Ужин")
    call alt_day4_dv_dj_dinner
    $ alt_pause(1)
    $ alt_save_name(4, u"Алиса. DJ. Поиски Ульяны")
    call alt_day4_dv_dj_us_search
    $ alt_pause(1)
    $ persistent.sprite_time = 'night'
    $ night_time()
    $ alt_save_name(4, u"Алиса. DJ. Свидание на пляже")
    call alt_day4_dv_dj_date_on_the_beach
    $ alt_pause(1)
    $ alt_chapter(4, u"Алиса. DJ. Отбой")
    call alt_day4_dv_dj_sleeptime
    $ alt_pause(1)
    jump alt_day5_dv_dj_begin

label alt_day5_dv_dj_begin:
    call alt_day5_dv_dj_vars
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Алиса. DJ. Утро")
    call alt_day5_dv_dj_morning
    $ alt_pause(1)
    $ alt_save_name(5, u"Алиса. DJ. Завтрак")
    call alt_day5_dv_dj_breakfast
    $ alt_pause(1)
    $ alt_chapter(5, u"Алиса. DJ. 2ch-FM")
    call alt_day5_dv_dj_dvachcast
    $ alt_pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(5, u"Алиса. DJ. Обед")
    call alt_day5_dv_dj_lunch
    $ alt_pause(1)
    $ alt_save_name(5, u"Алиса. DJ. Тихий час")
    call alt_day5_dv_dj_map_siesta
    $ alt_pause(1)
    $ alt_save_name(5, u"Алиса. DJ. Полдник")
    call alt_day5_dv_dj_afternoon
    $ alt_pause(1)
    $ alt_save_name(5, u"Алиса. DJ. Радиоэфир")
    call alt_day5_dv_dj_radio_broadcast
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Алиса. DJ. Ужин")
    call alt_day5_dv_dj_dinner
    $ alt_pause(1)
    $ alt_save_name(5, u"Алиса. DJ. Костёр")
    call alt_day5_dv_dj_campfire
    $ alt_pause(1)
    $ persistent.sprite_time = 'night'
    $ night_time()
    $ alt_save_name(5, u"Алиса. DJ. Отбой")
    call alt_day5_dv_dj_sleeptime
    $ alt_pause(1)
    jump alt_day6_dv_dj_begin

label alt_day6_dv_dj_begin:
    call alt_day6_dv_dj_vars
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Алиса. DJ. Пробуждение")
    call alt_day6_dv_dj_morning
    $ alt_pause(1)
    $ alt_save_name(6, u"Алиса. DJ. Завтрак")
    call alt_day6_dv_dj_breakfast
    $ alt_pause(1)
    $ alt_chapter(6, u"Алиса. DJ. Радиоэфир")
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day6_dv_dj_broadcast
    $ alt_pause(1)
    $ alt_save_name(6, u"Алиса. DJ. Обед")
    call alt_day6_dv_dj_lunch
    $ alt_pause(1)
    $ alt_save_name(6, u"Алиса. DJ. Тихий час")
    call alt_day6_dv_dj_siesta
    if alt_day6_dv_dj_quest == 0:
        call alt_day6_dv_dj_quest_garlands
    elif alt_day6_dv_dj_quest == 1:
        call alt_day6_dv_dj_quest_newspapers
    elif alt_day6_dv_dj_quest == 2:
        call alt_day6_dv_dj_quest_warehouse
    elif alt_day6_dv_dj_quest == 3:
        call alt_day6_dv_dj_quest_costumes
    else:
        call alt_day6_dv_dj_quest_slacker
    $ alt_pause(1)
    call alt_day6_dv_dj_afternoon
    $ alt_pause(1)
    $ alt_chapter(6, u"Алиса. DJ. Концерт")
    call alt_day6_dv_dj_concert
    $ alt_pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Алиса. DJ. Ужин")
    call alt_day6_dv_dj_dinner
    $ alt_pause(1)
 
    if secret_dv_dj == 3:
        $ alt_dv_dj_ends = 'true'
    elif (lp_dv >= 20):
        $ alt_dv_dj_ends = 'good'
    elif (lp_dv >= 16 and karma >= 75):
        $ alt_dv_dj_ends = 'rej'
    elif (lp_dv >= 16 and karma < 75):
        $ alt_dv_dj_ends = 'neu'
    else:
        $ alt_dv_dj_ends = 'bad'
    $ alt_save_name(6, u"Алиса. DJ. Вечер")
    call alt_day6_dv_dj_no_dance
    $ alt_pause(1)
    $ persistent.sprite_time = 'night'
    $ night_time()
    $ alt_save_name(6, u"Алиса. DJ. Разговор по душам")
    if alt_dv_dj_ends == 'true':
        call alt_day6_dv_dj_un_night_true
        if lp_dv < 16:
            return
    elif alt_dv_dj_ends == 'good':
        call alt_day6_dv_dj_un_night_good
    elif alt_dv_dj_ends == 'bad':
        if loki:
            call alt_day6_dv_dj_un_night_loki_bad
        else:
            call alt_day6_dv_dj_un_night_bad
    else:
        call alt_day6_dv_dj_un_night_neu
    $ alt_pause(1)
    $ alt_chapter(6, u"Алиса. DJ. Отбой")
    if alt_dv_dj_ends == 'true' or alt_dv_dj_ends == 'good':
        call alt_day6_dv_dj_sleeptime
    else:
        call alt_day6_dv_dj_sleeptime2
    $ alt_pause(1)
    jump alt_day7_dv_dj_begin

label alt_day7_dv_dj_begin:
    call alt_day7_dv_dj_vars
    $ alt_pause(1)
    $ alt_save_name(7, u"Алиса. DJ. Сон")
    if alt_dv_dj_ends == 'true':
        call alt_day7_dv_dj_dream_true
        $ alt_pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(7, u"Алиса. DJ. Утро")
        call alt_day7_dv_dj_morning_good
        $ alt_save_name(7, u"Алиса. DJ. Точки над Ё")
        call alt_day7_dv_dj_points_true
        $ routetag = "dvdjtrue"
    elif alt_dv_dj_ends == 'good':
        call alt_day7_dv_dj_dream_good
        $ alt_pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(7, u"Алиса. DJ. Утро")
        call alt_day7_dv_dj_morning_good
        $ alt_save_name(7, u"Алиса. DJ. Точки над Ё")
        call alt_day7_dv_dj_points_good
        $ routetag = "dvdjgood"
    else:
        call alt_day7_dv_dj_dream_bad
        $ alt_pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(7, u"Алиса. DJ. Утро")
        if alt_dv_dj_ends == 'bad':
            call alt_day7_dv_dj_morning_bad
            $ routetag = "dvdjbad"
        else:
            call alt_day7_dv_dj_morning_neu
            $ routetag = "dvdjneu"
        $ alt_save_name(7, u"Алиса. DJ. Точки над Ё")
        call alt_day7_dv_dj_points_bad
    $ alt_pause(1)
    $ alt_save_name(7, u"Алиса. DJ. Отбытие")
    call alt_day7_dv_dj_departure
    $ alt_pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    $ alt_chapter(7, u"Алиса. DJ. Эпилог")
    if alt_dv_dj_ends == 'bad':
        call alt_day7_dv_dj_bad
    elif alt_dv_dj_ends == 'neu':
        call alt_day7_dv_dj_neu
    elif alt_dv_dj_ends == 'rej':
        call alt_day7_dv_dj_rej
    elif alt_dv_dj_ends == 'good':
        call alt_day7_dv_dj_good
    elif alt_dv_dj_ends == 'exc':
        if herc:
            call alt_day7_dv_dj_herc_exc
        elif loki:
            call alt_day7_dv_dj_loki_exc
        else:
            call alt_day7_dv_dj_dr_exc
    else:
        call alt_day7_dv_dj_true
    return
