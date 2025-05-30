﻿label alt_day3_start:
    call alt_day3_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ prolog_time()
    $ alt_chapter(3, u"Утро")
    call alt_day3_begin
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(3, u"Завтрак")
    call alt_day3_bf
    pause(1)
    if alt_day3_duty:
        call alt_day3_bf_duty
        pause(1)
        call alt_day3_map_prepare
    elif counter_un_fz == 1:
        $ alt_chapter(3, u"Операция «Ы»")
        call alt_day3_morning_un_fz
    elif alt_day3_date == 'un':
        call alt_day3_event_library
    elif alt_day3_date == 'dv':
        call alt_day3_event_estrade
    elif alt_day3_date == 'mi':
        call alt_day3_event_music_club
    else:
        call alt_day3_map_prepare
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(3, u"Обед")
    call alt_day3_dinner
    pause(1)
    if (alt_day2_date == 'dv') and (alt_day3_date == 'dv') and alt_day3_duty:
        call alt_day3_eventAf_music_club1
    elif counter_un_fz == 2:
        $ alt_save_name(3, u"Подготовка к дискотеке")
        call alt_day3_day_un_fz
        if alt_day3_un_fz_work == 'un':
            call alt_day3_day_un_fz_un
        elif alt_day3_un_fz_work == 'sl':
            call alt_day3_day_un_fz_sl
        elif alt_day3_un_fz_work == 'dv':
            call alt_day3_day_un_fz_dv
        pause(1)
    elif counter_un_7dl == 4:
        call alt_day3_eventAf_library1
    else:
        call alt_day3_mapAf_prepare
    pause(1)
    if (counter_dv_7dl == 3):
        call alt_day3_aftermath
        pause(1)
        $ alt_chapter(3, u"Вечер")
        call alt_day3_nightmare
        if alt_day_catapult:
            return
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(3, u"Ужин")
        pause(1)
        call alt_day3_supper1
        pause(1)
        call alt_day3_supper2
    elif (counter_un_fz == 2):
        call alt_day3_aftermath
        pause(1)
        $ persistent.sprite_time = 'sunset'
        $ sunset_time()
        $ alt_chapter(3, u"Вечер")
        call alt_day3_un_fz_dream
        pause(1)
        $ alt_chapter(3, u"Ужин")
        call alt_day3_un_fz_dinner
    else:
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(3, u"Ужин")
        call alt_day3_supper
        pause(1)
        if counter_mi_7dl == 2:
            pass
        else:
            call alt_day3_supper2
    if counter_un_7dl == 6 and alt_day3_un_med_help == 1:
        $ alt_chapter(3, u"Вечер")
        call alt_day3_pre_med_un
        pause(1)
        $ alt_chapter(3, u"Медпункт. Вечер.")
        call alt_day3_med_un
        pause(1)
        call alt_day3_un_cards
        pause(1)
        call alt_day3_post_strip
        pause(1)
        $ alt_save_name(3, u"Отбой")
        call alt_day3_sleeptime
        pause(1)
        jump alt_day3_slots
    else:
        pause(1)
        $ alt_chapter(3, u"Танцы")
        call alt_day3_dance_dance
        pause(1)
        if alt_day3_dj != 'dv':
            call alt_day3_makeup
            pause(1)
            $ persistent.sprite_time = "night"
            $ night_time()
            if (counter_un_fz == 2):
                call alt_day3_un_fz_dance
                pause(1)
                if alt_day3_un_fz_walk:
                    $ alt_save_name(3, u"Прогулка с Леной")
                    call alt_day3_un_fz_evening_walk
                elif alt_day3_un_fz_stories:
                    $ alt_save_name(3, u"Сказка о Дороге")
                    call alt_day3_un_fz_evening_stories
                elif alt_day3_un_fz_neu_transit:
                    call alt_day3_un_fz_dance2
                pause(1)
                $ alt_chapter(3, u"Отбой")
                call alt_day3_un_fz_sleeptime
                pause(1)
                if alt_day3_un_fz_neu_transit:
                    jump alt_day3_router_neutral
                else:
                    jump alt_day3_router_un
            elif (counter_dv_7dl == 3) or (alt_day3_dv_guitar == 2):
                call alt_day3_dv_lf
                pause(1)
                if counter_dv_7dl == 3:
                    call alt_day3_dv_reunion
                    pause(1)
                    if alt_day_catapult:
                        return
                    pause(1)
                    $ persistent.sprite_time = "night"
                    $ night_time()
                    call alt_day3_dv_stayhere1
                    pause(1)
                    $ alt_save_name(3, u"Поход в баню")
                    call alt_day3_bath_voyeur
                    pause(1)
                    $ alt_save_name(3, u"Отбой")
                    call alt_day3_sleeptime
                    pause(1)
                    jump alt_day3_slots
                elif alt_day3_dv_guitar == 3:
                    $ alt_save_name(3, u"Отбой")
                    call alt_day3_sleeptime
                    pause(1)
                    jump alt_day3_slots
        call alt_day3_choose
        pause(1)
        if ((counter_sl_7dl >= 4) or (counter_sl_cl >= 6)) and (alt_day3_dancing1 == 'sl_1') and (lp_sl >= 12):
            if counter_sl_7dl == 5:
                pause(1)
                $ alt_save_name(3, u"Поход в баню")
                call alt_day3_bath_voyeur
                pause(1)
                $ alt_save_name(3, u"Отбой")
                call alt_day3_sleeptime
                pause(1)
                jump alt_day3_slots
            elif counter_sl_cl == 7:
                call alt_day3_technoquest3
                pause(1)
                jump alt_day3_slots

        else:
            call alt_day3_dance_dance2
            pause(1)
            if (alt_day3_dj == 'dv') and (alt_day3_technoquest2 == True):
                $ alt_save_name(3, u"Поход в баню")
                call alt_day3_bath_voyeur
                pause(1)
                $ alt_save_name(3, u"Отбой")
                call alt_day3_sleeptime
                pause(1)
                jump alt_day3_slots
            elif (alt_day3_us_bugs == 1) and (alt_day3_dancing1 != 'un_fz'):
                call alt_day3_mt_scare
                pause(1)
                $ alt_save_name(3, u"Поход в баню")
                call alt_day3_bath_voyeur
                pause(1)
                $ alt_save_name(3, u"Отбой")
                call alt_day3_sleeptime
                pause(1)
                jump alt_day3_slots
            elif alt_day3_technoquest2:
                call alt_day3_technoquest3
                pause(1)
                jump alt_day3_slots
        call alt_day3_choose2
        pause(1)
        if (alt_day3_date == 'mi') and (counter_mi_7dl == 2) and (alt_day3_dancing2 == 'mi_12'):
            call alt_day3_mi_7dl_init
            pause(1)
            jump alt_day4_mi_7dl_start
        elif alt_day3_dancing2 != 'me_2':
            call alt_day3_disco_past_d2
            pause(1)
            $ alt_save_name(3, u"Поход в баню")
            call alt_day3_bath_voyeur
            pause(1)
    $ alt_save_name(3, u"Отбой")
    call alt_day3_sleeptime
    pause(1)
    jump alt_day3_slots

label alt_day3_slots:
   scene scenery with dissolve
   $ alt_spt = 0
   $ alt_hpt = 0
   jump alt_day3_router_dv

label alt_day3_router_dv:
    if (counter_dv_7dl == 4) or (alt_day3_dj == 'dv' and alt_day3_dancing2 != 'dv_2'):
        "Поворочавшись, я улыбнулся посетившей мои сны Алисе."
        if lp_dv >= 11:
            "Мне снилась Алиса…"
            if counter_dv_7dl == 4:
                $ routetag = "dv7dl"
                jump alt_day4_dv_7dl_start
            elif (alt_day3_dj == 'dv' and alt_day3_dancing2 != 'dv_2'):
                $ routetag = "dvdj"
                jump alt_day4_dv_dj_start
        else:
            jump alt_day3_router_un
    else:
        jump alt_day3_router_un

label alt_day3_router_un:
    if (lp_un >= 12) or (lp_un >= 11 and (counter_sl_7dl >= 1)):
        "Мне снилась Лена…"
    if (counter_un_7dl == 6) and (lp_un >= 13):
        $ routetag = "un7dl"
        jump alt_day4_un_7dl_start
    elif (counter_un_fz == 2):
        $ routetag = "un7dl"
        jump alt_day4_un_fz_start_new
    else:
        jump alt_day3_router_mi

label alt_day3_router_mi:
    if (lp_mi >= 13) and (alt_day3_dj == 'mi'):
        "Мне снилась Мику…"
        "Правда, не очень долго."
        $ routetag = "mi7dl"
        jump alt_day4_mi_dj_start
    else:
        jump alt_day3_router_sl

label alt_day3_router_sl:
    if lp_sl >= 13:
        "Мне снилась Славя…"
        if counter_sl_7dl == 5:
            jump alt_day4_sl_7dl_start
        elif counter_sl_cl == 7:
            $ routetag = "sl"
            jump alt_day4_sl_cl_start
    else:
        jump alt_day3_router_neutral

label alt_day3_router_neutral:
    jump alt_day4_me_neu_start
