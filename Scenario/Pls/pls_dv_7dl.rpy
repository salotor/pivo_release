﻿label alt_day4_dv_7dl_start:
    call alt_day4_dv_7dl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Алиса. 7ДЛ. Утро")
    call alt_day4_dv_7dl_begin
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(4, u"Алиса. 7ДЛ. Поход")
    call alt_day4_dv_7dl_forest
    pause(1)
    $ alt_chapter(4, u"Алиса. 7ДЛ. Обед")
    call alt_day4_dv_7dl_dinner
    pause(1)
    $ alt_chapter(4, u"Алиса. 7ДЛ. Тихий час")
    call alt_day4_dv_7dl_silent_hour
    pause(1)
    $ alt_chapter(4, u"Алиса. 7ДЛ. Репетиция")
    call alt_day4_dv_7dl_repetition
    pause(1)
    $ alt_chapter(4, u"Алиса. 7ДЛ. Полдник")
    call alt_day4_dv_7dl_lunch
    pause(1)
    call alt_day4_dv_7dl_help
    pause(1)
    if alt_day4_dv_7dl_help_cs:
        $ alt_chapter(4, u"Алиса. 7ДЛ. Поездка")
        call alt_day4_dv_7dl_roadtrip
        pause(1)
        call alt_day4_dv_7dl_alco
        pause(1)
        call alt_day4_dv_7dl_back_to_camp
    else:
        call alt_day4_dv_7dl_append
        pause(1)
        if alt_day4_dv_7dl_medication == 2:
            call alt_day4_dv_7dl_aidpost
            pause(1)
        else:
            call alt_day4_dv_7dl_mt_aid
            pause(1)
        if alt_day4_dv_7dl_vodka != 2:
            $ persistent.sprite_time = "sunset"
            $ sunset_time()
            $ alt_chapter(4, u"Алиса. 7ДЛ. Ужин")
            call alt_day4_dv_7dl_supper
            pause(1)
            $ persistent.sprite_time = "night"
            $ night_time()
            call alt_day4_dv_7dl_sleeptime
            pause(1)
    jump alt_day5_dv_7dl_start

label alt_day5_dv_7dl_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    if alt_day4_dv_7dl_vodka == 2:
        $ alt_chapter(5, u"Алиса. 7ДЛ. Похмелье")
        call alt_day5_dv_7dl_alco_morning
        pause(1)
        call alt_day5_dv_7dl_begin
        pause(1)
    elif alt_day4_dv_7dl_help_cs:
        $ alt_chapter(5, u"Алиса. 7ДЛ. Возвращение.")
        call alt_day5_dv_7dl_roadtrip
        pause(1)
    else:
        $ alt_chapter(5, u"Алиса. 7ДЛ. Утро.")
        call alt_day5_dv_7dl_begin
        pause(1)
    $ day_time()
    $ alt_chapter(5, u"Алиса. 7ДЛ. Свечка.")
    call alt_day5_dv_7dl_candle
    pause(1)
    $ persistent.sprite_time = "day"
    $ alt_chapter(5, u"Алиса. 7ДЛ. День")
    call alt_day5_dv_7dl_dinner
    pause(1)
    call alt_day5_dv_7dl_silent_hour
    pause(1)
    call alt_day5_dv_7dl_lunch
    pause(1)
    call alt_day5_dv_7dl_repetition
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Алиса. 7ДЛ. Вечер")
    call alt_day5_dv_7dl_supper
    pause(1)
    call alt_day5_dv_7dl_evening
    pause(1)
    $ alt_chapter(5, u"Алиса. 7ДЛ. Костёр")
    call alt_day5_dv_7dl_campfire
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(5, u"Алиса. 7ДЛ. Ночь")
    call alt_day5_dv_7dl_night
    pause(1)
    call alt_day5_dv_7dl_sleeptime
    pause(1)
    jump alt_day6_dv_7dl_start

label alt_day6_dv_7dl_start:
    call alt_day6_dv_7dl_vars
    pause(1)
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ alt_chapter(6, u"Алиса. 7ДЛ. Утро")
    call alt_day6_dv_7dl_begin
    pause(1)
    call alt_day6_dv_7dl_mission
    pause(1)
    call alt_day6_dv_7dl_breakfast
    pause(1)
    call alt_day6_dv_7dl_repetition
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Алиса. 7ДЛ. День")
    call alt_day6_dv_7dl_dinner
    pause(1)
    if alt_day6_dv_7dl_route == 'sl':
        call alt_day6_dv_7dl_sl
        pause(1)
        if alt_day6_dv_7dl_sl_help_agree:
            call alt_day6_dv_7dl_sl_help
            pause(1)
        call alt_day6_dv_7dl_sl_help2
        pause(1)
        call alt_day6_dv_7dl_sl_garret
        pause(1)
    elif alt_day6_dv_7dl_route == 'un':
        call alt_day6_dv_7dl_un
        pause(1)
        call alt_day6_dv_7dl_check
        pause(1)
    call alt_day6_dv_7dl_concert
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day6_dv_7dl_supper
    pause(1)
    $ alt_chapter(6, u"Алиса. 7ДЛ. Танцы")
    call alt_day6_dv_7dl_dance
    pause(1)
    if alt_day6_dv_7dl_transit:
        call alt_day6_dv_7dl_catapult
        pause(1)
        if alt_day_catapult:
            return
        call alt_day6_dv_7dl_predance
        pause(1)
        if alt_day6_dv_7dl_route == 'sl':
            call alt_day6_dv_7dl_sl_dancing
            pause(1)
        elif alt_day6_dv_7dl_route == 'un':
            if (dr and (lp_un >= 5) and (lp_dv < 18)):
                call alt_day6_dv_7dl_un_dancing
                pause(1)
            else:
                call alt_day6_dv_7dl_mt_dancing
                pause(1)
    else:
        call alt_day6_dv_7dl_dv_dancing
        pause(1)
        if alt_day1_sl_keys_took in (1, 3) or alt_day4_dv_7dl_extra_key:
            if alt_day6_dv_7dl_route == 'sl':
                if alt_day4_dv_7dl_extra_key:
                    $ alt_day6_dv_7dl_key_hentai = 100
                else:
                    $ alt_day6_dv_7dl_key_hentai = 0
            else:
                $ alt_day6_dv_7dl_key_hentai = 100
        if (alt_day4_dv_7dl_vodka == 1) or alt_day4_dv_7dl_portwine:
            $ alt_day6_dv_7dl_alco_hentai = 10
        if alt_day4_dv_7dl_ba_conv:
            $ alt_day6_dv_7dl_ba_hentai = 1
        $ alt_day6_dv_7dl_hentai = alt_day6_dv_7dl_key_hentai + alt_day6_dv_7dl_alco_hentai + alt_day6_dv_7dl_ba_hentai
        if alt_day6_dv_7dl_hentai == 111:
            if dr:
                $ lp_dv += 4
            else:
                $ lp_dv += 2
            call alt_day6_dv_7dl_love_scene
            pause(1)
        else:
            call alt_day6_dv_7dl_non_love
            pause(1)
    call alt_day6_dv_7dl_sleeptime
    pause(1)
    jump alt_day7_dv_7dl_start

label alt_day7_dv_7dl_start:
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    $ alt_chapter(7, u"Алиса. 7ДЛ. Утро")
    call alt_day7_dv_7dl_begin
    pause(1)
    if alt_day7_dv_7dl_check == 'mt':
        $ routetag = "mt7dl_bad"
    elif (lp_dv >= 16) and (not alt_day6_dv_7dl_transit):
        $ routetag = "dv7dlgood"
    else:
        $ routetag = "dv7dlbad"
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Алиса. 7ДЛ. Отъезд")
    call alt_day7_dv_7dl_router
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if alt_day6_dv_7dl_transit:
        if alt_day6_dv_7dl_dance == 'un':
            call alt_day7_dv_7dl_un
            pause(1)
        elif alt_day6_dv_7dl_dance == 'sl':
            call alt_day7_dv_7dl_sl
            pause(1)
    else:
        if alt_day7_dv_7dl_check == 'mt':
            call alt_day7_dv_7dl_mt
            pause(1)
        else:
            call alt_day7_dv_7dl_dv
            pause(1)
            if alt_day7_dv_7dl_loki_catapult:
                call alt_day7_dv_7dl_loki
                pause(1)
                call alt_day7_dv_7dl_loki_exc
                pause(1)
                return
    call alt_day7_dv_7dl_bus
    pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    $ alt_chapter(7, u"Алиса. 7ДЛ. Эпилог")
    if alt_day7_dv_7dl_check == 'dv_2':
        if karma >= 75:
            if alt_day7_dv_7dl_story_end:
                call alt_day7_dv_7dl_shard
                pause(1)
            else:
                call alt_day7_dv_7dl_good_ussr
                pause(1)
        else:
            call alt_day7_dv_7dl_good_rf
            pause(1)
    elif alt_day7_dv_7dl_check == 'dv_1':
        if karma >= 75:
            call alt_day7_dv_7dl_rej_ussr
            pause(1)
        else:
            call alt_day7_dv_7dl_rej_rf
            pause(1)
    elif alt_day7_dv_7dl_check == 'un':
        call alt_day7_dv_7dl_tran_un
        pause(1)
    else:
        call alt_day7_dv_7dl_bad
        pause(1)
    return
