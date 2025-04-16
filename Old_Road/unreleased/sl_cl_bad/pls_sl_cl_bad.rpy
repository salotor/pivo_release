label alt_day6_sl_cl_narcomania:
    $ sdl_local_vars = [sdl_var_e_d0_char]
    call screen sdl_replay_vars(sdl_local_vars)
    $ alt_vars_screen(sdl_local_vars)
    $ alt_char_set(cur_char)

    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    call alt_day6_sl_cl_home
    pause(1)
    call alt_day6_sl_cl_intellect
    pause(1)
    if alt_day6_sl_cl_int == 2:
        $ routetag = "sltrue"
        $ alt_chapter(7, u"Славя. Фантазм.")
        call alt_day7_sl_cl_fear
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        call alt_day7_sl_cl_1996
        pause(1)
        if alt_day6_sl_cl_int == 3:
            $ sdl_stories_return()
        else:
            call alt_day7_sl_cl_int_bad
            pause(1)
    else:
        call alt_day7_sl_cl_int_bad
        pause(1)
    $ sdl_stories_return()
