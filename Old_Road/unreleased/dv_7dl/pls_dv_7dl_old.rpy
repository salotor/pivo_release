label alt_day3_dv_7dl_old:
    $ sdl_local_vars = [sdl_var_e_d0_char]
    call screen sdl_replay_vars(sdl_local_vars)
    $ alt_vars_screen(sdl_local_vars)
    $ alt_char_set(cur_char)

    $ persistent.sprite_time = "sunset"
    $ sunset_time()

    call alt_day3_dv_reunion_old
    if alt_day_catapult:
        $ sdl_stories_return()
    call alt_day3_dv_stayhere1_old
    $ sdl_stories_return()