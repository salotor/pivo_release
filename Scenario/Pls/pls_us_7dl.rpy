﻿label alt_day6_us_7dl_start:
    call alt_day6_us_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Ульяна. 7ДЛ. Утро")
    if counter_us_7dl_px == 3:
        call alt_day6_us_7dl_px_begin
    else:
        call alt_day6_us_7dl_begin
    pause(1)
    call alt_day6_us_7dl_exercises
    pause(1)
    if counter_us_7dl_px == 3:
        call alt_day6_us_7dl_px_breakfast
        pause(1)
        call alt_day6_us_7dl_px_carrier
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(6, u"Ульяна. 7ДЛ. День")
        call alt_day6_us_7dl_px_dinner
        pause(1)
        call alt_day6_us_7dl_px_party_un
        pause(1)
        if alt_day6_us_7dl_px_sl_join:
            call alt_day6_us_7dl_px_party_sl
        else:
            call alt_day6_us_7dl_px_far_gate
        pause(1)
        $ alt_chapter(6, u"Ульяна. 7ДЛ. Концерт")
        call alt_day6_us_7dl_concert
        pause(1)
    else:
        call alt_day6_us_7dl_breakfast
        pause(1)
        call alt_day6_us_7dl_separation
        pause(1)
        call alt_day6_us_7dl_helping
        pause(1)
        if alt_day6_us_7dl_mi_friends == 2:
            call alt_day6_us_7dl_preps
        elif alt_day6_us_7dl_sl_friends == 2:
            call alt_day6_us_7dl_warehouse
        else:
            call alt_day6_us_7dl_un_met
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(6, u"Ульяна. 7ДЛ. День")
        call alt_day6_us_7dl_dinner
        pause(1)
        if (alt_day6_us_7dl_mi_friends == 2) or (alt_day6_us_7dl_sl_friends == 2):
            call alt_day6_us_7dl_soundcheck
            pause(1)
            call alt_day6_us_7dl_concert
        else:
            call alt_day6_us_7dl_button
            pause(1)
            call alt_day6_us_7dl_deserter
            pause(1)
            if alt_day6_us_7dl_help:
                call alt_day6_us_7dl_ghost
                pause(1)
                $ alt_chapter(6, u"Ульяна. 7ДЛ. Ррромантика")
                call alt_day6_us_7dl_rendezvous
            else:
                call alt_day6_us_7dl_fiasco
                pause(1)
                $ alt_chapter(6, u"Ульяна. 7ДЛ. Концерт")
                call alt_day6_us_7dl_concert
        pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Ульяна. 7ДЛ. Вечер")
    call alt_day6_us_7dl_supper
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day6_us_7dl_disco_prepare
    pause(1)
    call alt_day6_us_7dl_makeup
    pause(1)
    call alt_day6_us_7dl_disco
    pause(1)
    if counter_us_7dl_px == 3:
        call alt_day6_us_7dl_px_disco
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day6_us_7dl_px_afterwords
        pause(1)
    else:
        if alt_day6_us_7dl_help:
            call alt_day6_us_7dl_us_dancing
        elif alt_day6_us_7dl_un_friends == 2:
            call alt_day6_us_7dl_un_dancing
        elif alt_day6_us_7dl_mi_friends == 2:
            call alt_day6_us_7dl_mi_dancing
        elif alt_day6_us_7dl_sl_friends == 2:
            call alt_day6_us_7dl_sl_dancing
        elif alt_day6_us_7dl_un_friends <= 1:
            call alt_day6_us_7dl_no_dancing
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day6_us_7dl_tea
        pause(1)
    call alt_day6_us_7dl_sleeptime
    pause(1)
    jump alt_day7_us_7dl_start

label alt_day7_us_7dl_start:
    call alt_day7_us_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    if counter_us_7dl_px == 3:
        if alt_day6_us_7dl_px_sl_join:
            $ routetag = "us_7dl_px_good_surp"
        else:
            $ routetag = "us_7dl_px_good"
    else:
        if alt_day6_us_7dl_help:
            $ routetag = "us_7dl_good"
        elif (alt_day6_us_7dl_mi_friends == 3) or (alt_day6_us_7dl_un_friends == 3):
            $ routetag = "us_7dl"
        else:
            $ routetag = "us_7dl_bad"
    $ alt_chapter(7, u"Ульяна. 7ДЛ. Утро")
    call alt_day7_us_7dl_begin
    pause(1)
    call alt_day7_us_7dl_breakfast
    pause(1)
    if counter_us_7dl_px == 3:
        call alt_day7_us_7dl_px_escape
        pause(1)
        if alt_day6_us_7dl_px_sl_join:
            $ persistent.sprite_time = "day"
            $ day_time()
            $ alt_chapter(7, u"Ульяна. 7ДЛ. Автобус")
            call alt_day7_us_7dl_px_bus
            pause(1)
            if alt_day7_us_7dl_px_escaped:
                call alt_day7_us_7dl_px_wastelands
                pause(1)
                $ persistent.sprite_time = "prolog"
                $ prolog_time()
                $ alt_chapter(7, u"Ульяна. 7ДЛ. Сказка")
                call alt_day7_us_7dl_px_true
                return
            else:
                call alt_day7_us_7dl_px_mourning
        else:
            $ persistent.sprite_time = "day"
            $ day_time()
            call alt_day7_us_7dl_px_mourning
        $ persistent.sprite_time = "prolog"
        $ prolog_time()
        $ alt_chapter(7, u"Ульяна. 7ДЛ. Эпилог")
        call alt_day7_us_7dl_px_good
    else:
        if alt_day6_us_7dl_help:
            call alt_day7_us_7dl_photo
            pause(1)
            call alt_day7_us_7dl_treehouse
            pause(1)
            call alt_day7_us_7dl_packing_us
        elif alt_day6_us_7dl_un_friends == 3:
            call alt_day7_us_7dl_packing_un
        elif alt_day6_us_7dl_mi_friends == 3:
            call alt_day7_us_7dl_packing_mi
        else:
            call alt_day7_us_7dl_packing
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(7, u"Ульяна. 7ДЛ. Отъезд")
        call alt_day7_us_7dl_leaving
        $ persistent.sprite_time = "prolog"
        $ prolog_time()
        if alt_day7_us_7dl_story_end:
            call alt_day7_us_7dl_shard
            pause(1)
            return
        if alt_day6_us_7dl_mi_friends == 3:
            call alt_day7_us_7dl_tran_mi
            pause(1)
            return
        $ alt_chapter(7, u"Ульяна. 7ДЛ. Эпилог")
        call alt_day7_us_7dl_wakeup
        if alt_day6_us_7dl_help:
            if persistent.us_7dl_tran_un and persistent.us_7dl_px_good and (counter_us_7dl_px >= 1):
                $ alt_chapter(7, u"Ульяна. Спасибо.")
                call alt_day7_us_7dl_true
            else:
                call alt_day7_us_7dl_good
        elif alt_day6_us_7dl_un_friends == 3:
            call alt_day7_us_7dl_tran_un
        else:
            call alt_day7_us_7dl_bad
    pause(1)
    return
