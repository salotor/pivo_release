label alt_day1_me_7dl_start:
    call alt_day1_me_7dl_vars
    $ routetag = "final"
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(1, u"Семён. Пробуждение")
    call alt_day1_me_7dl_bus_start
    pause(1)
    $ alt_chapter(1, u"Семён. Экскурсия")
    call alt_day1_me_7dl_meeting
    pause(1)
    $ alt_save_name(1, u"Семён. 1988")
    call alt_day1_me_7dl_memory1
    pause(1)
    $ alt_save_name(1, u"Семён. Роковая встреча")
    call alt_day1_me_7dl_lena
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(1, u"Семён. Ужин")
    call alt_day1_me_7dl_supper
    pause(1)
    $ alt_save_name(1, u"Семён. Музыкальный клуб")
    call alt_day1_me_7dl_music_club
    pause(1)
    $ alt_save_name(1, u"Семён. 1988")
    call alt_day1_me_7dl_memory2
    pause(1)
    $ alt_save_name(1, u"Семён. Отбой")
    call alt_day1_me_7dl_sleep
    pause(1)
    jump alt_day2_me_7dl_start

label alt_day2_me_7dl_start:
    call alt_day2_me_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(2, u"Семён. Утро")
    call alt_day2_me_7dl_begin
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_save_name(2, u"Семён. 1987")
    call alt_day2_me_7dl_memory1
    pause(1)
    $ alt_save_name(2, u"Семён. Утро")
    call alt_day2_me_7dl_begin_continue
    pause(1)
    $ alt_chapter(2, u"Семён. Завтрак")
    call alt_day2_me_7dl_breakfast
    pause(1)
    $ alt_save_name(2, u"Семён. Обход лагеря")
    call alt_day2_me_7dl_bypass
    pause(1)
    $ alt_save_name(2, u"Семён. 1987")
    call alt_day2_me_7dl_memory2
    pause(1)
    $ alt_save_name(2, u"Семён. Обход лагеря")
    call alt_day2_me_7dl_bypass_continue
    pause(1)
    $ alt_chapter(2, u"Семён. Обед")
    call alt_day2_me_7dl_dinner
    pause(1)
    $ alt_save_name(2, u"Семён. Тихий час")
    call alt_day2_me_7dl_silent_hour
    pause(1)
    $ alt_save_name(2, u"Семён. Полдник")
    call alt_day2_me_7dl_lunch
    pause(1)
    $ alt_chapter(2, u"Семён. Пляжный \nэпизод")
    call alt_day2_me_7dl_beach
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(2, u"Семён. Ужин")
    call alt_day2_me_7dl_supper
    pause(1)
    $ alt_save_name(2, u"Семён. 1986")
    call alt_day2_me_7dl_memory3
    pause(1)
    $ alt_save_name(2, u"Семён. Ужин")
    call alt_day2_me_7dl_supper_continue
    pause(1)
    $ alt_chapter(2, u"Семён. Тяжёлый разговор")
    call alt_day2_me_7dl_mt_talk
    pause(1)
    call alt_day2_me_7dl_dv_talk
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    if alt_day2_me_7dl_us_talk:
        $ alt_save_name(2, u"Семён. Цена")
        call alt_day2_me_7dl_us_trace
    else:
        $ alt_save_name(2, u"Семён. Обратно в лагерь")
        call alt_day2_me_7dl_camp
    pause(1)
    $ alt_save_name(2, u"Семён. Отбой")
    call alt_day2_me_7dl_sleep
    pause(3)
    jump alt_day3_me_7dl_start
    return

label alt_day3_me_7dl_start:
    call alt_day3_me_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(3, u"Семён. Утро")
    call alt_day3_me_7dl_begin
    pause(1)
    $ alt_save_name(3, u"Семён. 1986")
    call alt_day3_me_7dl_memory1
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_save_name(3, u"Семён. Утро")
    call alt_day3_me_7dl_begin_continue
    pause(1)
    $ alt_chapter(3, u"Семён. Завтрак")
    call alt_day3_me_7dl_breakfast
    pause(1)
    $ alt_save_name(3, u"Семён. День")
    call alt_day3_me_7dl_day
    pause(1)
    $ alt_chapter(3, u"Семён. Обед")
    call alt_day3_me_7dl_dinner
    pause(1)
    $ alt_save_name(3, u"Семён. Тихий час")
    call alt_day3_me_7dl_silent_hour
    pause(1)
    $ alt_chapter(3, u"Семён. Вечер")
    call alt_day3_me_7dl_evening
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_save_name(3, u"Семён. Ужин")
    call alt_day3_me_7dl_supper
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(3, u"Семён. Дискотека")
    call alt_day3_me_7dl_disco
    pause(1)
    $ alt_save_name(3, u"Семён. 1987")
    call alt_day3_me_7dl_memory2
    pause(1)
    $ alt_save_name(3, u"Семён. Дискотека")
    call alt_day3_me_7dl_disco_continue
    pause(1)
    $ alt_save_name(3, u"Семён. Отбой")
    call alt_day3_me_7dl_sleep
    pause(1)

label alt_day4_me_7dl_start:
    call alt_day4_me_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Семён. Утро")
    call alt_day4_me_7dl_begin
    pause(1)
    $ alt_chapter(4, u"Семён. Завтрак")
    call alt_day4_me_7dl_breakfast
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_save_name(4, u"Семён. День")
    call alt_day4_me_7dl_day
    pause(1)
    $ alt_chapter(4, u"Семён. Обед")
    call alt_day4_me_7dl_dinner
    pause(1)
    $ alt_save_name(4, u"Семён. Тихий час")
    call alt_day4_me_7dl_silent_hour
    pause(1)
    $ alt_save_name(4, u"Семён. Полдник")
    call alt_day4_me_7dl_lunch
    pause(1)
    $ alt_chapter(4, u"Семён. Концерт")
    call alt_day4_me_7dl_concert
    pause(1)

    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_save_name(4, u"Семён. Ужин")
    call alt_day4_me_7dl_supper
    pause(1)

    $ alt_chapter(4, u"Семён. Вечер")
    call alt_day4_me_7dl_evening
    pause(1)
    if alt_day4_me_7dl_mi_date:
        $ alt_save_name(4, u"Семён. Призвание")
        call alt_day4_me_7dl_mi_treehouse
    else:
        $ alt_save_name(4, u"Семён. Обратно в лагерь")
        call alt_day4_me_7dl_mz_checkers
    pause(1)
    $ alt_save_name(4, u"Семён. Отбой")
    call alt_day4_me_7dl_sleep
    pause(1)
    jump alt_day5_me_7dl_start

label alt_day5_me_7dl_start:
    call alt_day5_me_7dl_vars
    $ persistent.sprite_time = "night"
    $ sunset_time()
    $ alt_chapter(5, u"Семён. Утро")
    call alt_day5_me_7dl_begin
    $ persistent.sprite_time = "sunset"
    pause(1)
    $ alt_save_name(5, u"Семён. Завтрак")
    call alt_day5_me_7dl_breakfast
    pause(1)
    $ alt_chapter(5, u"Семён. Свечка")
    $ persistent.sprite_time = "night"
    call alt_day5_me_7dl_cndl
    pause(1)
    $ alt_chapter(5, u"Семён. Обед")
    $ persistent.sprite_time = "sunset"
    call alt_day5_me_7dl_dinner
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_save_name(5, u"Семён. День")
    call alt_day5_me_7dl_day
    pause(1)
    $ alt_save_name(5, u"Семён. Шпионские игры")
    call alt_day5_me_7dl_spy_games
    pause(1)
    $ alt_save_name(5, u"Семён. Ужин")
    call alt_day5_me_7dl_supper
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Семён. Поход")
    call alt_day5_me_7dl_campfire
    pause(1)
    $ alt_chapter(5, u"Семён. Отбой")
    call alt_day5_me_7dl_sleep
    pause(1)
    jump alt_day6_me_7dl_start

label alt_day6_me_7dl_start:
    call alt_day6_me_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Семён. Утро")
    call alt_day6_me_7dl_begin
    $ persistent.sprite_time = "day"
    $ day_time()
    pause(1)
    $ alt_save_name(6, u"Семён. Завтрак")
    call alt_day6_me_7dl_breakfast
    pause(1)
    $ alt_save_name(6, u"Семён. День")
    call alt_day6_me_7dl_day
    pause(1)
    $ alt_chapter(6, u"Семён. Обед")
    call alt_day6_me_7dl_dinner
    pause(1)
    $ alt_save_name(6, u"Семён. Тихий час")
    call alt_day6_me_7dl_silent_hour
    pause(1)
    $ alt_save_name(6, u"Семён. Полдник")
    call alt_day6_me_7dl_lunch
    pause(1)
    $ alt_save_name(6, u"Семён. Воспоминание. 1988")
    call alt_day6_me_7dl_concert
    pause(1)
    if alt_day6_me_7dl_un_guilty:
        $ alt_save_name(6, u"Семён. Смирение")
        call alt_day6_me_7dl_un_talk
    else:
        $ alt_save_name(6, u"Семён. Правда или вызов")
        call alt_day6_me_7dl_true_or_challenge
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_save_name(6, u"Семён. Ужин")
    call alt_day6_me_7dl_supper
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_save_name(6, u"Семён. Дискотека")
    call alt_day6_me_7dl_disco
    pause(1)
    if alt_day6_me_7dl_mt_found:
        $ alt_save_name(6, u"Семён. Маски сброшены")
        call alt_day6_me_7dl_mt_talk
    else:
        $ alt_save_name(6, u"Семён. Король и Королева")
        call alt_day6_me_7dl_king_and_queen
    pause(1)
    $ alt_chapter(6, u"Семён. Отбой")
    call alt_day6_me_7dl_sleeptime
    pause(1)
    if alt_day2_me_7dl_us_talk and alt_day3_me_7dl_dv_wish and alt_day4_me_7dl_mi_date and alt_day5_me_7dl_sl_buf and alt_day6_me_7dl_un_guilty and alt_day6_me_7dl_mt_found:
        $ alt_day7_me_7dl_all_talks = True
    jump alt_day7_me_7dl_start


label alt_day7_me_7dl_start:
    call alt_day7_me_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Семён. Утро")
    call alt_day7_me_7dl_begin
    $ persistent.sprite_time = "day"
    $ day_time()
    pause(1)
    $ alt_save_name(7, u"Семён. Завтрак")
    call alt_day7_me_7dl_breakfast
    pause(1)
    $ alt_save_name(7, u"Семён. День")
    call alt_day7_me_7dl_day
    pause(1)
    if alt_day7_me_7dl_answers:
        $ alt_save_name(7, u"Семён. Там, где всё началось")
        call alt_day7_me_7dl_seeking_answers
        pause(1)
        if alt_day7_me_7dl_ending == 'good':
            $ alt_save_name(7, u"Семён. Сначала")
            call alt_day7_me_7dl_good
            pause(1)
            if persistent.me_7dl_neutral and persistent.me_7dl_true and persistent.me_7dl_good:
                $ alt_save_name(7, u"Семён. Сначала?")
                call alt_day7_me_7dl_good_ps
            pause(1)
            return
    else:
        $ alt_save_name(7, u"Семён. Сборы")
        call alt_day7_me_7dl_packing
        pause(1)
    $ alt_save_name(7, u"Семён. Визит к Виоле")
    call alt_day7_me_7dl_cs_visit
    pause(1)
    $ alt_chapter(7, u"Семён. Отъезд")
    call alt_day7_me_7dl_departure
    pause(1)
    if alt_day7_me_7dl_ending == 'true':
        $ alt_save_name(7, u"Семён. Конец")
        call alt_day7_me_7dl_true
    else:
        $ alt_save_name(7, u"Семён. Жизнь?")
        call alt_day7_me_7dl_neutral
        pause(1)
        $ alt_save_name(7, u"Семён. Ещё раз")
        call alt_day7_me_7dl_neutral_ps
    pause(1)
    return