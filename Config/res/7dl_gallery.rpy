init 9999 python:
    # Список всех фонов. Сначала идёт основное изображение. Далее по порядку (опционально): оригинальный ли это фон (True/False), доп. варианты фона (в квадратных скобках).
    sdl_gall_bgs_list = [
        sdl_gall_bg(img="bus_stop", orig=False, add_img=["ext_bus_stop_summer_7dl"]),
        sdl_gall_bg(img="ext_adductius_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_admins_day_7dl", orig=True, add_img=["ext_admins_night_7dl", "ext_admins_rain_7dl"]),
        sdl_gall_bg(img="ext_aidpost_day", orig=False, add_img=["ext_aidpost_night", "ext_aidpost_rain_7dl", "ext_aidpost_sunset_7dl", "ext_aidpost_night_light_7dl"]),
        sdl_gall_bg(img="ext_alley_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_backdoor_day_7dl", orig=True, add_img=["ext_backdoor_night_7dl", "ext_backdoor_sunset_7dl"]),
        sdl_gall_bg(img="ext_backroad_day_7dl", orig=True, add_img=["ext_backroad_sunset_7dl","ext_backroad_night_7dl"]),
        sdl_gall_bg(img="ext_backstage_alt_day_7dl", orig=False, add_img=["ext_backstage_alt_night_7dl"]),
        sdl_gall_bg(img="ext_bathhouse_day_7dl", orig=False, add_img=["ext_bathhouse_night"]),
        sdl_gall_bg(img="ext_beach2_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_beach_day", orig=False, add_img=["ext_beach_night", "ext_beach_sunset"]),
        sdl_gall_bg(img="ext_beach_water_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_boathouse_alt2_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_boathouse_alt_day_7dl", orig=True, add_img=["ext_boathouse_alt_night_7dl"]),
        sdl_gall_bg(img="ext_boathouse_day", orig=False, add_img=["ext_boathouse_night", "ext_boathouse_rain_7dl", "ext_boathouse_sunset_7dl"]),
        sdl_gall_bg(img="ext_bus", orig=False, add_img=["ext_no_bus", "ext_no_bus_night", "ext_no_bus_sunset","ext_bus_snow_7dl"]),
        sdl_gall_bg(img="ext_bus2_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_bush_sunset_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_busstop_dust_7dl", orig=True, add_img=["ext_busstop_sun_7dl"]),
        sdl_gall_bg(img="ext_camp_entrance_day", orig=False, add_img=["ext_camp_entrance_night", "ext_camp_entrance_sunset_7dl", "ext_entrance_night_clear_7dl", "ext_entrance_night_clear_closed_7dl", "ext_entrance_winter_7dl", "ext_entrance_fantasm_winter_7dl"]),
        sdl_gall_bg(img="ext_childhouse_day_7dl", orig=True, add_img=["ext_childhouse_winter_7dl"]),
        sdl_gall_bg(img="ext_city_night2_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_city_night_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_clubs_day", orig=False, add_img=["ext_clubs_night", "ext_clubs_rain_7dl", "ext_clubs_sunset_7dl", "ext_clubs_winter_day_7dl"]),
        sdl_gall_bg(img="ext_coulisses_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_countryside_day_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_dining_hall_away_day", orig=False, add_img=["ext_dining_hall_away_night", "ext_dining_hall_away_rain_7dl", "ext_dining_hall_away_sunset"]),
        sdl_gall_bg(img="ext_dining_hall_backroad_day_7dl", orig=False, add_img=["ext_dining_hall_backroad_night_7dl"]),
        sdl_gall_bg(img="ext_dining_hall_near_day", orig=False, add_img=["ext_dining_hall_near_night", "ext_dining_hall_near_rain_7dl", "ext_dining_hall_near_sunset"]),
        sdl_gall_bg(img="ext_dv_hideout_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_earth_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_emptiness_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_gostinka_day_7dl", orig=True, add_img=["ext_gostinka_night_7dl"]),
        sdl_gall_bg(img="ext_hospital2_away_day_7dl", orig=True, add_img=["ext_hospital2_away_night_7dl"]),
        sdl_gall_bg(img="ext_house_of_dv_day", orig=False, add_img=["ext_house_of_dv_night"]),
        sdl_gall_bg(img="ext_house_of_el_day_7dl", orig=False, add_img=["ext_house_of_el_night_7dl", "ext_house_of_el_night2_7dl"]),
        sdl_gall_bg(img="ext_house_of_mt_day", orig=False, add_img=["ext_house_of_mt_night", "ext_house_of_mt_night_without_light", "ext_house_of_mt_rain_7dl", "ext_house_of_mt_sunset"]),
        sdl_gall_bg(img="ext_house_of_sl_day", orig=False, add_img=["ext_house_of_sl_night_7dl"]),
        sdl_gall_bg(img="ext_house_of_un_day", orig=False, add_img=["ext_house_of_un_day_with_un_7dl", "ext_house_of_un_night_7dl", "ext_house_of_un_rain_7dl", "ext_house_of_un_sunset_7dl"]),
        sdl_gall_bg(img="ext_houses_day", orig=False, add_img=["ext_houses_night_7dl", "ext_houses_rainy_day_7dl", "ext_houses_sunset", "ext_houses_snowy_day_7dl", "ext_houses_winter_day_7dl"]),
        sdl_gall_bg(img="ext_island_day", orig=False, add_img=["ext_island_night"]),
        sdl_gall_bg(img="ext_japan_graveyard_rain_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_khruschevka_day_7dl", orig=True, add_img=["ext_khruschevka_night_7dl", "ext_khruschevka_rain_7dl", "ext_khruschevka_sunset_7dl", "ext_khruschevka_winter_7dl"]),
        sdl_gall_bg(img="ext_lake_day_7dl", orig=True, add_img=["ext_lake_night_7dl", "ext_lake_night_px_7dl", "ext_lake_sunset_7dl"]),
        sdl_gall_bg(img="ext_library_day", orig=False, add_img=["ext_library_night", "ext_library_sunset_7dl"]),
        sdl_gall_bg(img="ext_lost_city_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_main_building_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_musclub_day", orig=False, add_img=["ext_musclub_night_7dl", "ext_musclub_rain_7dl", "ext_musclub_snowy_day_7dl", "ext_musclub_sunset_7dl"]),
        sdl_gall_bg(img="ext_musclub_verandah_day_7dl", orig=False, add_img=["ext_musclub_verandah_night_7dl"]),
        sdl_gall_bg(img="ext_mv2_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_night_sky_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_old_building_day_7dl", orig=False, add_img=["ext_old_building_day_rainy_7dl", "ext_old_building_night", "ext_old_building_night_moonlight"]),
        sdl_gall_bg(img="ext_old_road_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_path2_day", orig=False, add_img=["ext_path2_night", "ext_path2_rain_7dl", "ext_path2_sunset_7dl"]),
        sdl_gall_bg(img="ext_path_day", orig=False, add_img=["ext_path_night", "ext_path_rain_7dl", "ext_path_sunset"]),
        sdl_gall_bg(img="ext_playground_day", orig=False, add_img=["ext_playground_night", "ext_playground_sunset_7dl"]),
        sdl_gall_bg(img="ext_polyana_day", orig=False, add_img=["ext_polyana_night", "ext_polyana_sunset"]),
        sdl_gall_bg(img="ext_railbridge_sunset_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_road2_night_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_road_day", orig=False, add_img=["ext_road_night2", "ext_road_sunset_7dl", "ext_road_winter_7dl"]),
        sdl_gall_bg(img="ext_road_night", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_roof_city_night_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_sandpit_day_7dl", orig=True, add_img=["ext_sandpit_night_7dl"]),
        sdl_gall_bg(img="ext_seashore_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_shower_day_7dl", orig=True, add_img=["ext_shower_night_7dl"]),
        sdl_gall_bg(img="ext_sky2_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_sky_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_sky_sunset_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_smolensky_graveyard_day_7dl", orig=True, add_img=["ext_smolensky_graveyard_winter_7dl", "ext_smolensky_graveyard_winter_day_7dl"]),
        sdl_gall_bg(img="ext_square2_day_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_square_day", orig=False, add_img=["ext_square_day_party_7dl", "ext_square_night", "ext_square_night_party", "ext_square_night_party2", "ext_square_rain_day_7dl", "ext_square_sunset", "ext_square_sunset3_7dl"]),
        sdl_gall_bg(img="ext_stage_big_day_7dl", orig=False, add_img=["ext_stage_big_clear_day_7dl", "ext_stage_big_night", "ext_stage_big_sunset_7dl"]),
        sdl_gall_bg(img="ext_stage_normal_day", orig=False, add_img=["ext_stage_normal_clear_7dl", "ext_stage_normal_night"]),
        sdl_gall_bg(img="ext_stairs_day_7dl", orig=False, add_img=["ext_stairs_night_7dl", "ext_stairs_sunset_7dl"]),
        sdl_gall_bg(img="ext_stand3_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_street_night_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_suare_winter_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_tennis_court_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_townscape_ph2_day_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_townscape_ph_day_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_tree_house_7dl", orig=True, add_img=["ext_tree_house_sunset_7dl"]),
        sdl_gall_bg(img="ext_tribune_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_un_hideout_day_7dl", orig=True, add_img=["ext_un_hideout_night_7dl", "ext_un_hideout_sunset_7dl", "ext_un_hideout_eva_7dl"]),
        sdl_gall_bg(img="ext_underwater_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_us_lake_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_valun_day_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_volley_court_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_warehouse2_day_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_warehouse_day_7dl", orig=False, add_img=["ext_warehouse_blurry_7dl", "ext_warehouse_night_7dl", "ext_warehouse_rain_day_7dl", "ext_warehouse_sunset_7dl"]),
        sdl_gall_bg(img="ext_washstand2_day", orig=False, add_img=["ext_washstand2_sunset_7dl"]),
        sdl_gall_bg(img="ext_washstand_day", orig=False, add_img=["ext_washstand_night_7dl", "ext_washstand_rain_7dl", "ext_washstand_sunset_7dl"]),
        sdl_gall_bg(img="ext_winter_night_7dl", orig=True, add_img=["ext_winter_night_rotate_7dl"]),
        sdl_gall_bg(img="ext_winterpark_7dl", orig=True, add_img=[]),

        sdl_gall_bg(img="int_access2_day_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_access_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_admin_boxes_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_admins_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_aidpost_day", orig=False, add_img=["int_aidpost_day_apple", "int_aidpost_night", "int_aidpost_no_light_night_7dl", "int_aidpost_sunset_7dl"]),
        sdl_gall_bg(img="int_attic2_day_7dl", orig=False, add_img=["int_attic2_night_7dl"]),
        sdl_gall_bg(img="int_attic_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_bar_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_bus", orig=False, add_img=["int_bus_black", "int_bus_night", "int_bus_people_day", "int_bus_people_night", "int_bus_warp_7dl","int_bus_snow_7dl"]),
        sdl_gall_bg(img="int_bus_flood_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_caffee_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_catacomb_door_fullbright_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_catacombs_entrance", orig=False, add_img=[]),
        sdl_gall_bg(img="int_catacombs_hole", orig=False, add_img=[]),
        sdl_gall_bg(img="int_catacombs_living", orig=False, add_img=[]),
        sdl_gall_bg(img="int_chief_office_day_7dl", orig=True, add_img=["int_chief_office_rain_7dl"]),
        sdl_gall_bg(img="int_childhouse_corridor_7dl", orig=True, add_img=["int_hospital_corridor_7dl"]),
        sdl_gall_bg(img="int_childhouse_room_day_7dl", orig=True, add_img=["int_childhouse_room_night_7dl"]),
        sdl_gall_bg(img="int_church_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_clubs_dj_7dl", orig=True, add_img=["int_clubs_dj_nolight_7dl"]),
        sdl_gall_bg(img="int_clubs_male2_night", orig=False, add_img=["int_clubs_male2_night_nolight", "int_warehouse2_day_7dl"]),
        sdl_gall_bg(img="int_clubs_male_day", orig=False, add_img=["int_clubs_male_night_7dl", "int_clubs_male_night_candle_7dl", "int_clubs_male_rain_7dl", "int_clubs_male_rain_clean_table_7dl", "int_clubs_male_sunset"]),
        sdl_gall_bg(img="int_coaching_room_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_concert_room_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_coupe_day_7dl", orig=True, add_img=["int_coupe_night_7dl"]),
        sdl_gall_bg(img="int_dining_hall_day", orig=False, add_img=["int_dining_hall_night", "int_dining_hall_people_day", "int_dining_hall_people_rain_7dl", "int_dining_hall_people_sunset_7dl", "int_dining_hall_people_sunset_pp_7dl", "int_dining_hall_rain_7dl", "int_dining_hall_sunset"]),
        sdl_gall_bg(img="int_dv_radioroom_day_7dl", orig=False, add_img=["int_dv_radioroom_night_7dl"]),
        sdl_gall_bg(img="int_dv_room_7dl", orig=False, add_img=["int_dv_room_night_7dl"]),
        sdl_gall_bg(img="int_editorial_day_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_excalator2_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_excalator_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_extra_house_day_7dl", orig=False, add_img=["int_extra_house_night_7dl", "int_extra_house_nolight_7dl", "int_extra_house_rain_7dl", "int_extra_house_sunset_7dl"]),
        sdl_gall_bg(img="int_future_airliner_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_future_office_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_home_lift_7dl", orig=True, add_img=["int_future_lift_7dl"]),
        sdl_gall_bg(img="int_hospital_corridor2_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_hospital_hall_day_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_house_of_dv_day", orig=False, add_img=["int_house_of_dv_night", "int_house_of_dv_night_no_light_7dl"]),
        sdl_gall_bg(img="int_house_of_el_day_7dl", orig=False, add_img=["int_house_of_el_sunset_7dl", "int_house_of_el_night_7dl", "int_house_of_el_night2_7dl"]),
        sdl_gall_bg(img="int_house_of_mt_day", orig=False, add_img=["int_house_of_mt_backpack_day", "int_house_of_mt_backpack_sunset", "int_house_of_mt_night", "int_house_of_mt_night2", "int_house_of_mt_noitem_day_7dl", "int_house_of_mt_noitem_night", "int_house_of_mt_sunset"]),
        sdl_gall_bg(img="int_house_of_sl_day", orig=False, add_img=[]),
        sdl_gall_bg(img="int_house_of_un_day", orig=False, add_img=["int_house_of_un_night"]),
        sdl_gall_bg(img="int_kitchen_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_liaz", orig=False, add_img=["int_liaz_city_7dl", "int_liaz_summer_day_7dl"]),
        sdl_gall_bg(img="int_library_day", orig=False, add_img=["int_library_night", "int_library_night2", "int_library_rain_7dl"]),
        sdl_gall_bg(img="int_looney_bin_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_looney_bin_nightmare_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_metrostation_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_mine", orig=False, add_img=["int_mine_water_7dl"]),
        sdl_gall_bg(img="int_mine_coalface", orig=False, add_img=[]),
        sdl_gall_bg(img="int_mine_crossroad", orig=False, add_img=[]),
        sdl_gall_bg(img="int_mine_door", orig=False, add_img=[]),
        sdl_gall_bg(img="int_mine_exit_day_7dl", orig=False, add_img=["int_mine_exit_night_light"]),
        sdl_gall_bg(img="int_mine_halt", orig=False, add_img=[]),
        sdl_gall_bg(img="int_mine_halt_left_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_mine_heart_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_mine_room", orig=False, add_img=[]),
        sdl_gall_bg(img="int_mine_room2_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_mt_sam_room_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_mt_sam_room_away_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_mt_sam_room_close_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_musclub_day", orig=False, add_img=["int_musclub_night_nolight_7dl", "int_musclub_rain_7dl", "int_musclub_sunset_7dl"]),
        sdl_gall_bg(img="int_old_building_cab_day_7dl", orig=False, add_img=["int_old_building_cab_night_7dl"]),
        sdl_gall_bg(img="int_old_building_day_7dl", orig=False, add_img=["int_old_building_night"]),
        sdl_gall_bg(img="int_opened_door_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_potato_storage_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_refinery_day_7dl", orig=True, add_img=["int_refinery_night_7dl"]),
        sdl_gall_bg(img="int_school_corridor_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_semen_bath_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_semen_kitchen_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_semen_room_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_semen_room_alt_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_sporthall_day_7dl", orig=True, add_img=["int_sporthall_night_7dl"]),
        sdl_gall_bg(img="int_staircase_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_store_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_toilet_night_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_train_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="int_tree_house_7dl", orig=True, add_img=["int_tree_house_sunset_7dl"]),
        sdl_gall_bg(img="int_un_exhibition_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_un_stud_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_us_frontdoor_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_us_kitchen_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_us_livingroom_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_wagon_day_7dl", orig=True, add_img=["int_wagon_sunset_7dl"]),
        sdl_gall_bg(img="int_ward2_sunset_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_ward_day_7dl", orig=False, add_img=["int_ward_sunset_7dl"]),
        sdl_gall_bg(img="int_wardrobe2_7dl", orig=True, add_img=["int_wardrobe2_mirror_7dl"]),
        sdl_gall_bg(img="int_wardrobe_7dl", orig=True, add_img=["int_wardrobe_mirror_7dl"]),
        sdl_gall_bg(img="int_warehouse3_day_7dl", orig=True, add_img=["int_warehouse3_night_7dl"]),
        sdl_gall_bg(img="int_warehouse_day_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="intro_xx", orig=False, add_img=["int_intro_liaz_7dl"]),
        sdl_gall_bg(img="semen_room", orig=False, add_img=["int_semen_room_clean_7dl", "int_semen_room_half_clean_7dl", "int_semen_room2_7dl","int_semen_room_day_7dl"]),
        sdl_gall_bg(img="semen_room_window", orig=False, add_img=["int_semen_room_window_day_7dl", "int_semen_room_window_day_summer_7dl","int_semen_room_window_dawn_7dl"]),
        sdl_gall_bg(img="ext_dining_hall_back_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_london_lane_night_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_london_street_night_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_london_busstop_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_ledoviy_hall_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_cottage_room_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_cottage_room2_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="int_airport_day_7dl", orig=False, add_img=[]),
        sdl_gall_bg(img="ext_park_sunset_7dl", orig=True, add_img=[]),
        sdl_gall_bg(img="ext_moonlight_7dl", orig=False, add_img=[])
        ]

    # Список всех артов. Сначала идёт основное изображение. Далее по порядку (опционально): список персонажей на арте (в квадратных скобках), оригинальный ли это арт (True/False), показан ли на арте 18+ cumтент (True/False), вертикальный ли арт (соотношение сторон в виде числа/False), доп. варианты арта (в квадратных скобках).
    sdl_gall_arts_list = [
        sdl_gall_art(img="d0_me_loki_park_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d1_me_end_of_day_7dl", girls=["me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d1_food_normal", girls=[""], orig=False, hent=False, vert=False, add_img=["d1_food_skolop"]),
        sdl_gall_art(img="d1_grasshopper", girls=["us","un"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d1_me_mirror_casual2_7dl", girls=["me"], orig=False, hent=False, vert=False, add_img=["d3_me_mirror_bordo_7dl", "d3_me_mirror_pioneer_7dl", "d7_me_mirror_casual_7dl"]),
        sdl_gall_art(img="d1_mi_bus_7dl", girls=["mi"], orig=True, hent=False, vert=False, add_img=["d1_mi_bus2_7dl", "d1_mi_bus3_7dl"]),
        sdl_gall_art(img="d1_mi_dv_bus_7dl", girls=["mi","dv"], orig=True, hent=False, vert=False, add_img=["d1_mi_dv_bus2_7dl"]),
        sdl_gall_art(img="d1_sl_dinner_smile_7dl", girls=["sl","me"], orig=False, hent=False, vert=False, add_img=["d1_sl_dinner_bunny_7dl", "d1_sl_dinner_sad_7dl", "d1_sl_dinner_bunny1_7dl", "d1_sl_dinner_sad1_7dl", "d1_sl_dinner_smile1_7dl", "d1_sl_dinner_smile2_7dl", "d1_sl_dinner_sad2_7dl"]),
        sdl_gall_art(img="d1_un_book_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=["d1_un_book0_7dl"]),
        sdl_gall_art(img="d1_uv_2", girls=["uv"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d2_2ch_beach", girls=["dv"], orig=False, hent=False, vert=0.56, add_img=[]),
        sdl_gall_art(img="d2_dv_boat_day_7dl", girls=["dv","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d2_us_boat_day_7dl", girls=["us","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_me_boat_night_7dl", girls=["me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_un_boat_night_7dl", girls=["un","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_mi_boat_day_7dl", girls=["mi","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_lineup_with_mi_7dl", girls=["mt","dv","mz","sl","el"], orig=False, hent=False, vert=False, add_img=["d2_lineup", "d4_lineup_no_un_7dl", "d4_lineup_no_un_us_7dl"]),
        sdl_gall_art(img="d2_mi_polaroid_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d2_micu_lib", girls=["mz"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d2_miku_piano", girls=["mi"], orig=False, hent=True, vert=False, add_img=["d2_miku_piano2"]),
        sdl_gall_art(img="d2_mt_resort_7dl", girls=["mt","me"], orig=True, hent=False, vert=False, add_img=["d2_mt_resort_night_7dl"]),
        sdl_gall_art(img="d2_mt_undressed_7dl", girls=["mt"], orig=False, hent=True, vert=False, add_img=["d2_mt_undressed_2_7dl"]),
        sdl_gall_art(img="d2_slavya_forest", girls=["sl"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d2_sovenok", girls=["un","me"], orig=False, hent=False, vert=False, add_img=["d2_un_owlet_pioneer_7dl"]),
        sdl_gall_art(img="d2_un_kissing_7dl", girls=["un","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d2_un_knees_7dl", girls=["un","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d2_un_knees1_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=["d2_un_knees2_7dl", "d2_un_knees3_7dl", "d2_un_knees4_7dl", "d2_un_knees5_7dl"]),
        sdl_gall_art(img="d2_us_soccer_sunset_7dl", girls=["us"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d2_us_trainhop_7dl", girls=["us"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d2_water_dan", girls=["dv","me"], orig=False, hent=False, vert=False, add_img=["d2_water_dan_night_7dl"]),
        sdl_gall_art(img="d3_disco", girls=["el","us","mt","sl","sh"], orig=False, hent=False, vert=False, add_img=["d3_disco_no_un_7dl"]),
        sdl_gall_art(img="d7_dv_alice_dj_7dl", girls=["dv"], orig=True, hent=False, vert=False, add_img=["d3_dv_alice_dj80_7dl"]),
        sdl_gall_art(img="d3_dv_kiss_7dl", girls=["dv","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d3_dv_scene_1", girls=["dv","me"], orig=False, hent=False, vert=False, add_img=["d3_dv_scene_2"]),
        sdl_gall_art(img="d3_me_fag_room_7dl", girls=["me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d3_mi_dance_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=["d3_mi_dance_bordo_7dl"]),
        sdl_gall_art(img="d3_mt_dance_7dl", girls=["mt","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d3_potato_1_7dl", girls=["us","me"], orig=False, hent=False, vert=False, add_img=["d3_potato_2_7dl"]),
        sdl_gall_art(img="d3_sl_bath_unplaited_7dl", girls=["sl"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d3_sl_dance", girls=["sl","me"], orig=False, hent=False, vert=False, add_img=["d3_sl_dance_bordo_7dl", "d6_sl_dance_pioneer_7dl"]),
        sdl_gall_art(img="d6_dv_dance_pioneer_7dl", girls=["dv","me"], orig=False, hent=False, vert=False, add_img=["d6_dv_dance_bordo_7dl"]),
        sdl_gall_art(img="d3_un_dance", girls=["un","me"], orig=False, hent=False, vert=False, add_img=["d3_un_dance_bordo_7dl", "d6_un_dance_pioneer_7dl"]),
        sdl_gall_art(img="d3_un_dance2_7dl", girls=["un","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_ka_dance_7dl", girls=["ka","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d3_sl_evening", girls=["sl","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d3_un_forest", girls=["un","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d3_us_library_3", girls=["us","me"], orig=False, hent=False, vert=False, add_img=["d3_us_library_4", "d4_us_morning"]),
        sdl_gall_art(img="d3_ussr_catched", girls=["us"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_sl_un_catac_7dl", girls=["sl","un"], orig=False, hent=False, vert=False, add_img=["d4_catac", "d4_sl_catac_7dl"]),
        sdl_gall_art(img="d4_cs_car_day_cs_7dl", girls=["cs","ba"], orig=True, hent=False, vert=False, add_img=["d4_cs_car_open_7dl", "d4_cs_car_dark_7dl", "d4_cs_car_day_ba_gl_7dl", "d4_cs_car_day_cs_coat_7dl", "d4_cs_car_night_cs_7dl"]),
        sdl_gall_art(img="d4_dv_falls_7dl", girls=["dv","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_un_falls_7dl", girls=["un","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_mi_dv_concert_7dl", girls=["mi","dv"], orig=True, hent=False, vert=False, add_img=["d4_dv_concert_7dl", "d3_dv_guitar_7dl"]),
        sdl_gall_art(img="d4_dv_mt", girls=["dv","mt","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_el_wash", girls=["el"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_dv", girls=["dv","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_un_camping_7dl", girls=["un","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_un_reject_7dl", girls=["un"], orig=False, hent=False, vert=False, add_img=["d5_un_pixies_7dl"]),
        sdl_gall_art(img="d4_hatch_night_7dl", girls=[""], orig=True, hent=False, vert=False, add_img=["d4_hatch_night_open_7dl"]),
        sdl_gall_art(img="d4_mi_moon_dancing_7dl", girls=["mi"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_mi_falls_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=["d4_mi_falls2_7dl"]),
        sdl_gall_art(img="d4_mi_guitar", girls=["mi"], orig=False, hent=False, vert=False, add_img=["d4_mi_guitar_club_7dl", "d4_mi_guitar_moon_7dl"]),
        sdl_gall_art(img="d4_mi_hedgehod_night_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=["d4_mi_hedgehod_day_7dl"]),
        sdl_gall_art(img="d4_kandji_7dl", girls=[""], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_mi_sup_7dl", girls=["mi"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_sh_met_7dl", girls=["sh","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_sl_lookup_7dl", girls=["sl"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_sl_lookup2_7dl", girls=["sl"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_mt_board_7dl", girls=["mt"], orig=True, hent=False, vert=False, add_img=["d4_mt_board_7dl mt_normal", "d4_mt_board_7dl mt_normal2", "d4_mt_board_7dl mt_dontlike", "d4_mt_board_7dl mt_grin", "d4_mt_board_7dl mt_laugh", "d4_mt_board_7dl mt_smile", "d4_mt_board_7dl mt_smile2", "d4_mt_board_7dl mt_smile3"]),
        sdl_gall_art(img="d4_us_stardust_7dl", girls=["us"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d4_volley_rage_7dl", girls=["un","ba","mt"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_cake", girls=["dv","us","mt","un","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_cs", girls=["cs"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d5_dv_argue", girls=["dv","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_dv_arm_7dl", girls=["dv","me"], orig=True, hent=False, vert=False, add_img=["d5_dv_arm_jojo_7dl"]),
        sdl_gall_art(img="d5_dream_7dl", girls=[""], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_dv_island", girls=["dv","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_dv_sleep_7dl", girls=["dv"], orig=True, hent=False, vert=False, add_img=["d5_dv_sleep2_7dl"]),
        sdl_gall_art(img="d5_dv_sleep_together_7dl", girls=["dv","me"], orig=True, hent=False, vert=False, add_img=["d5_dv_sleep_together2_7dl", "d5_dv_sleep_together3_7dl"]),
        sdl_gall_art(img="d5_alisa_7dl", girls=[""], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_mt_redress_7dl", girls=["mt"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d5_rainy_idle_7dl", girls=[""], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_sl_bed_7dl", girls=["sl"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_un_bed_7dl", girls=["un"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mt_bed_7dl", girls=["mt"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_sl_bench_day_7dl", girls=["sl","me"], orig=True, hent=False, vert=False, add_img=["d5_sl_bench_neutral_7dl", "d5_sl_bench_night_7dl"]),
        sdl_gall_art(img="d5_sl_hugs_7dl", girls=["sl", "mi", "me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_sl_kissing_7dl", girls=["sl","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_sl_moon_7dl", girls=["sl"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d5_sl_piano_1_7dl", girls=["sl"], orig=True, hent=False, vert=False, add_img=["d5_sl_piano_2_7dl", "d5_sl_piano_3_7dl", "d5_sl_piano_4_7dl", "d5_sl_piano_5_7dl"]),
        sdl_gall_art(img="d5_sl_mines_7dl", girls=["sl"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_snark_7dl", girls=[""], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_square_sl_lead_7dl", girls=["sh","dv","us","un","mz","me","mt","sl"], orig=True, hent=False, vert=False, add_img=["d5_square_me_lead_7dl", "d5_square_us_lead_7dl"]),
        sdl_gall_art(img="d5_sl_swimming_7dl", girls=["sl"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d5_un_carrier_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_un_film_7dl", girls=["un","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_us_old_photo_7dl", girls=["us"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_thousand_twinkles_7dl", girls=[""], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_twinkle_1_7dl", girls=[""], orig=True, hent=False, vert=False, add_img=["d5_twinkle_2_7dl", "d5_twinkle_3_7dl", "d5_twinkle_4_7dl", "d5_twinkle_5_7dl", "d5_twinkle_6_7dl"]),
        sdl_gall_art(img="d5_un_island", girls=["un","me"], orig=False, hent=False, vert=False, add_img=["d5_un_island_dress_7dl"]),
        sdl_gall_art(img="d5_un_sleep", girls=["un","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_us_ghost", girls=["us","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_us_kiss_dress_7dl", girls=["us","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_us_rendezvous_7dl", girls=["us","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_us_sneakpeak_7dl", girls=["us"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d5_us_sneakpeak2_7dl", girls=["me","us"], orig=True, hent=False, vert=False, add_img=["d5_us_sneakpeak2_2_7dl", "d5_us_sneakpeak2_3_7dl", "d5_us_sneakpeak2_4_7dl"]),
        sdl_gall_art(img="d5_me_snch_run_7dl", girls=["me","ba"], orig=True, hent=False, vert=False, add_img=["d5_me_snch_run2_7dl", "d6_me_run_7dl", "d6_me_run2_7dl"]),
        sdl_gall_art(img="d6_disco2_7dl", girls=["un","us","dv","sl","mt"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_dv_hentai_7dl", girls=["dv","me"], orig=True, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d6_dv_hentai2_7dl", girls=["dv","me"], orig=True, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d6_mi_farewell_7dl", girls=["mi"], orig=False, hent=False, vert=False, add_img=["d6_mi_cya_7dl"]),
        sdl_gall_art(img="d6_mi_departure_7dl", girls=["mi"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_mi_hugs_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_mi_leaving_7dl", girls=["mi"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_mi_morning_7dl", girls=["mi"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d6_mi_salute_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=["d6_mi_salute2_7dl"]),
        sdl_gall_art(img="d6_mi_swimming_7dl", girls=["mi"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d6_mi_grass_7dl", girls=["mi","me"], orig=False, hent=False, vert=1.3, add_img=[]),
        sdl_gall_art(img="d6_mt_salute_7dl", girls=["mt","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_sl_clean_7dl", girls=["sl"], orig=True, hent=False, vert=False, add_img=["d6_sl_clean_dress_7dl", "d6_sl_clean_dress2_7dl"]),
        sdl_gall_art(img="d6_sl_hentai_2_7dl", girls=["sl"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d6_puppy_7dl", girls=[""], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_sl_swim_7dl", girls=["sl"], orig=False, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d6_sl_zettai_7dl", girls=["sl"], orig=True, hent=False, vert=1.3, add_img=[]),
        sdl_gall_art(img="d6_un_evening_0_7dl", girls=["un"], orig=False, hent=False, vert=False, add_img=["d6_un_evening_0_1_7dl", "d6_un_evening_0_2_7dl", "d6_un_evening_2", "d6_un_evening_3_7dl"]),
        sdl_gall_art(img="d6_faceless_hands_7dl", girls=[""], orig=True, hent=False, vert=False, add_img=["d6_faceless_hands2_7dl"]),
        sdl_gall_art(img="d6_un_death_7dl", girls=["un"], orig=True, hent=True, vert=False, add_img=[]),
        sdl_gall_art(img="d6_un_violence_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=["d6_un_violence2_7dl"]),
        sdl_gall_art(img="d6_us_normal_dance_7dl", girls=["us","me"], orig=True, hent=False, vert=False, add_img=["d6_us_zluka_dance_7dl", "d6_us_surprise_dance_7dl", "d6_us_upset_dance_7dl", "d6_us_smile_dance_7dl", "d6_us_genki_dance_7dl", "d6_us_shy_dance_7dl"]),
        sdl_gall_art(img="d6_us_ghost_7dl", girls=["us","me"], orig=True, hent=False, vert=False, add_img=["d6_us_ghost_hole_7dl", "d6_us_photo_7dl", "d6_us_photo_torn_7dl"]),
        sdl_gall_art(img="d6_us_kiss_7dl", girls=["us","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_us_kiss2_7dl", girls=["us","dn"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_me_cyberfish_7dl", girls=["me","sh","el"], orig=True, hent=False, vert=False, add_img=["d6_me_cyberfish_7dl el_cf_surp semen_cf_normal sh_cf_bore", "d6_me_cyberfish2_7dl el_cf_surp2 semen_cf_surp sh_cf_surp", "d6_me_cyberfish_7dl el_cf_happy semen_cf_surp sh_cf_smile", "d6_me_cyberfish_7dl el_cf_sad semen_cf_normal sh_cf_poker", "d6_me_cyberfish_7dl el_cf_sorrow semen_cf_normal sh_cf_poker", "d6_me_cyberfish_7dl el_cf_smile semen_cf_normal sh_cf_poker", "d6_me_cyberfish_7dl el_cf_smile2 semen_cf_normal sh_cf_smile", "d6_me_cyberfish_7dl el_cf_normal semen_cf_normal sh_cf_poker", "d6_me_cyberfish_7dl el_cf_surp3 semen_cf_normal sh_cf_surp", "d6_me_cyberfish_7dl el_cf_smile3 semen_cf_normal sh_cf_bore"]),
        sdl_gall_art(img="d6_am_aquasemen_7dl", girls=["am"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_bus_night_7dl", girls=[""], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_dv_addic_7dl", girls=["dv","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_dv_child_7dl", girls=["dv","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_dv_come_with_me_1_7dl", girls=["dv"], orig=True, hent=False, vert=False, add_img=["d7_dv_come_with_me_2_7dl"]),
        sdl_gall_art(img="d7_dv_epilogue_kiss_7dl", girls=["dv","me"], orig=True, hent=False, vert=False, add_img=["d7_dv_epilogue_kiss2_7dl", "d7_dv_epilogue_kiss3_7dl"]),
        sdl_gall_art(img="d7_dv_epilogue_bus_7dl", girls=["dv","me"], orig=True, hent=False, vert=False, add_img=["d7_dv_epilogue_bus2_7dl"]),
        sdl_gall_art(img="d7_me_epilogue_bus_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_epilogue_7dl"]),
        sdl_gall_art(img="d7_mi_epilogue_bus_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=["d7_mi_epilogue_bus2_7dl"]),
        sdl_gall_art(img="d7_mt_epilogue_bus_7dl", girls=["mt","me"], orig=True, hent=False, vert=False, add_img=["d7_mt_epilogue_bus2_7dl", "d7_mt_epilogue_bus3_7dl"]),
        sdl_gall_art(img="d7_sl_epilogue_bus_7dl", girls=["sl","me"], orig=True, hent=False, vert=False, add_img=["d7_sl_epilogue_bus2_7dl"]),
        sdl_gall_art(img="d7_un_epilogue_bus_7dl", girls=["un","me"], orig=True, hent=False, vert=False, add_img=["d7_un_epilogue_bus2_7dl"]),
        sdl_gall_art(img="d7_us_epilogue_bus_7dl", girls=["us","me"], orig=True, hent=False, vert=False, add_img=["d7_us_epilogue_bus2_7dl", "d7_us_epilogue_bus3_7dl"]),
        sdl_gall_art(img="d7_dv_hugs_7dl", girls=["dv","me"], orig=True, hent=False, vert=False, add_img=["d7_dv_hugs2_7dl", "d7_dv_hugs3_7dl", "d7_dv_hugs4_7dl"]),
        sdl_gall_art(img="d7_dv_loki_exc_7dl", girls=["dv"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_dv_looney_7dl", girls=["dv","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_dv_noir_7dl", girls=["dv"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_dv_rf_reject_gray_7dl dv_normal", girls=["dv"], orig=True, hent=False, vert=False, add_img=["cg d7_dv_rf_reject_gray_7dl dv_concent", "cg d7_dv_rf_reject_gray_7dl dv_cry", "cg d7_dv_rf_reject_7dl dv_happy"]),
        sdl_gall_art(img="d7_dv_stars_7dl", girls=["dv"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_frozen_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_looney_7dl", girls=["me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mi_club27_7dl", girls=["mi"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mi_concert2_7dl", girls=["mi"], orig=False, hent=False, vert=False, add_img=["d7_mi_concert_7dl"]),
        sdl_gall_art(img="d7_mi_epilogue_7dl", girls=["mi"], orig=False, hent=False, vert=False, add_img=["d7_mi_epilogue0_7dl"]),
        sdl_gall_art(img="d7_mi_farewell_7dl", girls=["mi"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mi_ghost_7dl", girls=["mi"], orig=True, hent=False, vert=0.71, add_img=[]),
        sdl_gall_art(img="d7_mi_hugs_7dl", girls=["mi"], orig=True, hent=False, vert=0.56, add_img=[]),
        sdl_gall_art(img="d7_mi_stroll_7dl", girls=["mi","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mi_letter_7dl", girls=["mi"], orig=False, hent=False, vert=False, add_img=["d7_mi_letter_rain_7dl", "d7_mi_letter_rain_tears_7dl"]),
        sdl_gall_art(img="d7_mi_lost_7dl", girls=["mi"], orig=True, hent=False, vert=False, add_img=["d7_mi_lost2_7dl"]),
        sdl_gall_art(img="d7_mi_meeting_7dl", girls=["mi"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mi_ramen_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mi_reenter_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mi_sparkle_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=["d7_mi_sparkle_smile_7dl"]),
        sdl_gall_art(img="d7_mi_sunk_7dl", girls=["mi"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mi_fujita_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mt_epilogue_miracle_7dl", girls=["mt"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_mt_old_7dl", girls=["mt","me"], orig=True, hent=False, vert=False, add_img=["d7_mt_old2_7dl", "d7_mt_old3_7dl"]),
        sdl_gall_art(img="d7_sl_hug_7dl", girls=["sl","me"], orig=True, hent=False, vert=False, add_img=["d7_sl_hug2_7dl"]),
        sdl_gall_art(img="d7_un_cry_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=["d7_un_cry2_7dl"]),
        sdl_gall_art(img="d7_un_epilogue_7dl", girls=["un"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_epilogue_fall_7dl", girls=[""], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_un_epilogue_bad_7dl", girls=["un"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_cosmonaut_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_fire_7dl", girls=[""], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_un_firebridge_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=["d7_un_firebridge2_7dl", "d7_un_firebridge3_7dl"]),
        sdl_gall_art(img="d7_un_fireyes_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_un_epilogue_rf_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=["d7_un_epilogue_rf2_7dl"]),
        sdl_gall_art(img="d7_un_reanimation_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_un_suicide", girls=["un"], orig=False, hent=False, vert=1.3, add_img=[]),
        sdl_gall_art(img="d7_un_take_my_hand_7dl", girls=["un","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_us_bedroom_7dl", girls=["us","dn"], orig=True, hent=False, vert=False, add_img=["d7_us_bedroom2_7dl", "d7_us_bedroom3_7dl", "d7_us_bedroom4_7dl"]),
        sdl_gall_art(img="d7_us_pixie_7dl", girls=["us"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="epilogue_un_bad", girls=["me"], orig=False, hent=False, vert=False, add_img=["d7_me_tai_tai_7dl"]),
        sdl_gall_art(img="epilogue_dv_2", girls=[""], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="epilogue_mi_1", girls=["mi","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="epilogue_mi_9", girls=["mi","me"], orig=False, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="epilogue_sl", girls=["sl"], orig=False, hent=False, vert=False, add_img=["epilogue_sl_2"]),
        sdl_gall_art(img="d7_me_arseny_7dl", girls=["am","me"], orig=True, hent=False, vert=False, add_img=["d7_me_semen_7dl", "d7_me_neu_arseny1_7dl", "d7_me_neu_arseny2_7dl", "d7_me_neu_arseny3_7dl", "d7_me_neu_arseny4_7dl"]),
        sdl_gall_art(img="shard_intro_7dl", girls=["am"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_neu_farewell_7dl", girls=["am"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_neu_grave_7dl", girls=["am"], orig=True, hent=False, vert=False, add_img=["d7_me_neu_grave1_7dl", "d7_me_neu_grave2_7dl", "d7_me_neu_grave3_7dl"]),
        sdl_gall_art(img="d7_me_neu_rocall_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_neu_rocall2_7dl", "d7_me_neu_rocall3_7dl"]),
        sdl_gall_art(img="downphone1_7dl", girls=[""], orig=True, hent=False, vert=False, add_img=["downphone2_7dl", "downphone3_7dl", "d7_snowphone_7dl"]),
        sdl_gall_art(img="d7_me_neu_loki_on_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_neu_loki_on2_7dl", "d7_me_neu_loki_on3_7dl"]),
        sdl_gall_art(img="d7_me_jeep_7dl", girls=[""], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_neu_graydoomed_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_herc_hny_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_herc_hny2_7dl","d7_me_herc_hny3_7dl","d7_me_herc_hny4_7dl","d7_me_herc_hny5_7dl"]),
        sdl_gall_art(img="d7_me_loki_cry_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_loki_cry2_7dl"]),
        sdl_gall_art(img="d7_me_loki_trumpet_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_loki_bar_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_loki_bar2_7dl","d7_me_loki_bar3_7dl","d7_me_loki_bar4_7dl"]),
        sdl_gall_art(img="d7_me_loki_skirmish_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_loki_skirmish2_7dl","d7_me_loki_skirmish3_7dl"]),
        sdl_gall_art(img="d6_me_sl_sarafan_7dl", girls=["sl"], orig=True, hent=False, vert=False, add_img=["d6_me_sl_sarafan2_7dl","d6_me_sl_sarafan3_7dl"]),
        sdl_gall_art(img="d7_me_sem_shamp_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_sem_shamp2_7dl",]),
        sdl_gall_art(img="d7_me_un_pirate_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_un_sunsetlife_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=["d7_me_un_sunsetlife2_7dl","d7_me_un_sunsetlife3_7dl","d7_me_un_sunsetlife4_7dl"]),
        sdl_gall_art(img="d7_me_un_rest_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=["d7_me_un_rest2_7dl","d7_me_un_rest3_7dl","d7_me_un_rest4_7dl","d7_me_un_rest5_7dl","d7_me_un_rest6_7dl","d7_me_un_rest7_7dl","d7_me_un_rest8_7dl","d7_me_un_rest9_7dl","d7_me_un_rest10_7dl","d7_me_un_rest11_7dl","d7_me_un_rest12_7dl"]),
        sdl_gall_art(img="d7_me_un_bed_close_eyes_night_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=["d7_me_un_bed_drug_night_7dl","d7_me_un_bed_surprise_night_7dl","d7_me_un_bed_happy_night_7dl","d7_me_un_bed_normal_night_7dl","d7_me_un_bed_smile_night2_7dl","d7_me_un_bed_smile2_night2_7dl","d7_me_un_bed_normal_night2_7dl","d7_me_un_bed_close_eyes_day_7dl","d7_me_un_bed_sleepy_day_7dl","d7_me_un_bed_smile_day_7dl","d7_me_un_bed_smile2_day_7dl","d7_me_un_bed_smile3_day_7dl","d7_me_un_bed_serious_day_7dl","d7_me_un_bed_normal_day_7dl"]),
        sdl_gall_art(img="d7_me_un_bed_night3_normal_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=["d7_me_un_bed_night3_smile_7dl","d7_me_un_bed_night3_cry_smile_7dl","d7_me_un_bed_night3_close_eyes_7dl",]),
        sdl_gall_art(img="d7_un_kiss_7dl", girls=["me","un"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_ri_skype_smile_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_ri_skype_upset_7dl","d7_me_ri_skype_think_7dl","d7_me_ri_skype_sad_7dl","d7_me_ri_skype_wink_7dl"]),
        sdl_gall_art(img="d6_me_ma_herc_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d6_me_ma_herc2_7dl"]),
        sdl_gall_art(img="d7_me_herc_call1_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_herc_call2_7dl","d7_me_herc_call3_7dl","d7_me_herc_call4_7dl","d7_me_herc_call5_7dl","d7_me_herc_call6_7dl"]),
        sdl_gall_art(img="d7_me_herc_walk1_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_herc_walk2_7dl","d7_me_herc_walk3_7dl","d7_me_herc_walk4_7dl","d7_me_herc_walk5_7dl"]),
        sdl_gall_art(img="d7_un_cosmo_eyes_normal_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_un_cosmo_eyes_close_7dl","d7_un_cosmo_eyes_scare1_7dl","d7_un_cosmo_eyes_scare2_7dl","d7_un_cosmo_eyes_smile_7dl","d7_un_cosmo_scare1_7dl","d7_un_cosmo_scare2_7dl","d7_un_cosmo_scare3_7dl"]),
        sdl_gall_art(img="day2_mi_beach1_gal", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=["day2_mi_beach2_gal","day2_mi_beach3_gal"]),
        sdl_gall_art(img="day2_mi_beach4_gal", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d2_us_hideout1_7dl", girls=["us","me"], orig=True, hent=False, vert=False, add_img=["d2_us_hideout2_7dl","d2_us_hideout_alone_7dl"]),
        sdl_gall_art(img="d2_us_hideout_hug_7dl", girls=["us","me"], orig=True, hent=False, vert=False, add_img=["d2_us_hideout_hug2_7dl"]),
        sdl_gall_art(img="d2_us_hideout_7dl", girls=["us","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_sl_hospital_7dl", girls=["sl","me"], orig=True, hent=False, vert=False, add_img=["d7_sl_hospital_corrected_7dl"]),
        sdl_gall_art(img="d7_sl_certificate_7dl", girls=["sl"], orig=True, hent=False, vert=False, add_img=["d7_sl_certificate_corrected_7dl"]),
        sdl_gall_art(img="d3_dv_busted_7dl", girls=["mt","me","dv","mi"], orig=True, hent=False, vert=False, add_img=["d3_dv_busted1_7dl","d3_dv_busted2_7dl","d3_dv_busted3_7dl","d3_dv_busted4_7dl","d3_dv_busted5_7dl","d3_dv_busted6_7dl"]),
        # 0.57
        sdl_gall_art(img="d4_mi_treehouse1_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=["d4_mi_treehouse2_7dl","d4_mi_treehouse3_7dl","d4_mi_treehouse4_7dl","d4_mi_treehouse5_7dl"]),
        sdl_gall_art(img="d6_mt_crying_7dl", girls=["mt"], orig=True, hent=False, vert=False, add_img=["d6_mt_crying2_7dl","d6_mt_crying3_7dl"]),
        sdl_gall_art(img="d7_dv_family_7dl", girls=["dv"], orig=True, hent=False, vert=False, add_img=["d7_dv_family2_7dl","d7_dv_family3_7dl"]),
        sdl_gall_art(img="d4_sl_pontoon1_7dl", girls=["sl","me"], orig=True, hent=False, vert=False, add_img=["d4_sl_pontoon2_7dl","d4_sl_pontoon3_7dl","d4_sl_pontoon4_7dl"]),
        # 0.58
        sdl_gall_art(img="d5_sl_bottle_1_7dl", girls=["sl"], orig=True, hent=False, vert=False, add_img=["d5_sl_bottle_2_7dl"]),
        sdl_gall_art(img="day5_me_buf_alone_smile_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["day5_me_buf_alone_tricky_7dl","day5_me_buf_people_smile_7dl","day5_me_buf_people_tricky_7dl"]),
        sdl_gall_art(img="d4_un_teaparty1_7dl", girls=["me","un","mi"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="un_day4_teaparty21_gal", girls=["me","un","mi"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="un_day4_teaparty3_gal", girls=["me","un","mi"], orig=True, hent=False, vert=False, add_img=["un_day4_teaparty3_bueee_gal"]),
        sdl_gall_art(img="day7_us_fairytale", girls=["me","un","us"], orig=True, hent=False, vert=False, add_img=["day7_us_fairytale2","day7_us_fairytale3"]),
        # 1.0
        sdl_gall_art(img="d5_mi_conv_7dl", girls=["mi","me"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_mi_chibis_beach_7dl", girls=["mi"], orig=True, hent=False, vert=False, add_img=["d6_mi_chibis_concert_7dl","d6_mi_chibis_dance_7dl","d6_mi_chibis_disco_7dl","d6_mi_chibis_ducks_7dl","d6_mi_chibis_volley_7dl"]),
        sdl_gall_art(img="d7_sl_hold_normal", girls=["me","sl"], orig=True, hent=False, vert=False, add_img=["d7_sl_hold_normal2","d7_sl_hold_surprise","d7_sl_kiss_tear","d7_sl_tyama_nyaon","d7_sl_tyama_nyaon_sl_eyes","d7_sl_tyama_nyaon_herk_eyes","d7_sl_tyama_nyaon_tear"]),
        sdl_gall_art(img="d6_me_mt_sitting_normal", girls=["mt"], orig=True, hent=False, vert=False, add_img=["d6_me_mt_sitting_sad_smile","d6_me_mt_diary","d6_me_mt_diary_first_page","d6_me_mt_diary_first_page_listing","d6_me_mt_diary_second_page","d6_me_mt_diary_second_page_listing","d6_me_mt_diary_third_page"]),
        sdl_gall_art(img="d6_me_mt_masks_me_questioning_mt_normal_head1", girls=["me","mt"], orig=True, hent=False, vert=False, add_img=["d6_me_mt_masks_me_questioning_mt_smile_head2","d6_me_mt_masks_me_confuse2_mt_smile_liar_head2","d6_me_mt_masks_me_sad_mt_hands_head2","d6_me_mt_masks_me_surp_mt_normal_head1","d6_me_mt_masks_me_head2_normal_mt_normal_head1"]),
        sdl_gall_art(img="d4_mt_swing_mt_normal", girls=["me","mt"], orig=True, hent=False, vert=False, add_img=["d4_mt_swing_me_mt_sad_smile","d4_mt_swing_me_smile_hand_mt_shy","d4_mt_swing_me_shy_head2_hand_mt_grin","d4_mt_swing_me_shy_head1_mt_grin","d4_mt_swing_me_shy_head1_mt_laugh"]),
        sdl_gall_art(img="d6_me_un_portret_7dl", girls=["un"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d6_un_me_un_sad_surp", girls=["me","un"], orig=True, hent=False, vert=False, add_img=["d6_un_me_un_smile","d6_un_me_un_normal_head_2","d6_un_me_un_normal_head_1","d6_un_me_un_wtf","d6_un_me_un_shocked_head_2","d6_un_me_un_shocked_eyes_head_1"]),
        sdl_gall_art(img="anim_d7_dreamgirl", girls=["uv"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_mt_epilogue_meeting_7dl", girls=["mt"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_mt_bus_me_shy_mt_normal", girls=["mt","me"], orig=True, hent=False, vert=False, add_img=["d7_me_mt_bus_me_shy2_mt_serious","d7_me_mt_bus_me_normal_mt_normal","d7_me_mt_bus_me_normal_mt_laugh","d7_me_mt_bus_me_hand_mt_smile","d7_me_mt_bus_hands_me_shy2_mt_smile"]),
        sdl_gall_art(img="d7_me_bench_close_eyes", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_bench_dontlike","d7_me_bench_think","d7_me_bench_close_open_eyes"]),
        sdl_gall_art(img="d7_me_cave_close_fear_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_cave_close_normal_7dl","d7_me_cave_close_surp_7dl","d7_me_cave_close_surp2_7dl"]),
        sdl_gall_art(img="d7_me_cave1_7dl", girls=["me"], orig=True, hent=False, vert=False, add_img=["d7_me_cave2_7dl","d7_me_cave3_7dl","d7_me_cave4_7dl","d7_me_cave5_7dl","d7_me_cave6_7dl","d7_me_cave7_7dl","d7_me_cave8_7dl","d7_me_cave9_7dl","d7_me_cave_knees_7dl","d7_me_cave_knees_greenlight_7dl"]),
        sdl_gall_art(img="d7_me_us_ps_walk_sad", girls=["us","me"], orig=True, hent=False, vert=False, add_img=["d7_me_us_ps_walk_think","d7_me_us_ps_close_eyes","d7_me_us_ps_stand_wall","d7_me_us_ps_stand_sad","d7_me_us_ps_stand_angry_hand","d7_me_us_ps_stand_sad_wall"]),
        sdl_gall_art(img="d7_me_us_ps_bag", girls=["us"], orig=True, hent=False, vert=False, add_img=[]),
        sdl_gall_art(img="d7_me_trip1_me_normal_uv2_smile", girls=["uv","me"], orig=True, hent=False, vert=False, add_img=["d7_me_trip2_me_close_eyes_uv_dontlike","d7_me_trip3_me_alpha_close_eyes_uv_dontlike","d7_me_trip4_me_alpha_scary_hand_uv_smile"]),
        sdl_gall_art(img="d7_cs_car_day_winter", girls=["cs"], orig=True, hent=False, vert=False, add_img=[])
        ]

    sdl_gall_girls_list = {'mi':[], 'dv':[], 'sl':[], 'un':[], 'mt':[], 'us':[]}
    sdl_gall_girls_list_orig = {'mi':[], 'dv':[], 'sl':[], 'un':[], 'mt':[], 'us':[]}
    for girl in sdl_gall_girls_list:
        for img in sdl_gall_arts_list:
            if girl in img.get_girls():
                sdl_gall_girls_list[girl].append(img)
                if img.get_orig():
                    sdl_gall_girls_list_orig[girl].append(img)

    sdl_gall_arts_list_orig = []
    for img in sdl_gall_arts_list:
        if img.get_orig():
            sdl_gall_arts_list_orig.append(img)

    sdl_gall_bgs_list_orig = []
    for img in sdl_gall_bgs_list:
        if img.get_orig():
            sdl_gall_bgs_list_orig.append(img)

init python:
    class sdl_gall_bg:
        def __init__(self, img, orig=False, add_img=[], vert=False, type="bg "):
            self.img = img
            self.orig = orig
            self.add_img = add_img
            self.vert = vert
            self.type = type

        def get_img(self):
            return self.img

        def get_orig(self):
            return self.orig

        def get_add_img(self):
            return self.add_img

        def get_vert(self):
            return self.vert

        def get_type(self):
            return self.type

    class sdl_gall_art:
        def __init__(self, img, girls=[], orig=False, hent=False, vert=False, add_img=[], type="cg "):
            self.img = img
            self.girls = girls
            self.orig = orig
            self.hent = hent
            self.vert = vert
            self.add_img = add_img
            self.type = type

        def get_img(self):
            return self.img

        def get_girls(self):
            return self.girls

        def get_orig(self):
            return self.orig

        def get_hent(self):
            return self.hent

        def get_vert(self):
            return self.vert

        def get_add_img(self):
            return self.add_img

        def get_type(self):
            return self.type

    def sdl_gal_check_seen(img):
        if renpy.seen_image(img.get_type()+img.get_img()):
            return True
        for i in img.get_add_img():
            if renpy.seen_image(img.get_type()+i):
                return True

    def sdl_gal_set_list():
        global sdl_gall_curr_list
        if sdl_gall_mode == "bgs":
            if sdl_gall_orig:
                sdl_gall_curr_list = sdl_gall_bgs_list_orig
            else:
                sdl_gall_curr_list = sdl_gall_bgs_list
        elif sdl_gall_mode == "arts":
            if sdl_gall_orig:
                sdl_gall_curr_list = sdl_gall_arts_list_orig
            else:
                sdl_gall_curr_list = sdl_gall_arts_list
        elif sdl_gall_mode in sdl_gall_girls_list:
            if sdl_gall_orig:
                sdl_gall_curr_list = sdl_gall_girls_list_orig[sdl_gall_mode]
            else:
                sdl_gall_curr_list = sdl_gall_girls_list[sdl_gall_mode]

    def sdl_gall_progress_calc():
        global sdl_gall_progress
        seen_count = 0.0
        img_count = 0.0
        for img in sdl_gall_bgs_list:
            if sdl_gal_check_seen(img):
                seen_count += 1
            img_count += 1
        for img in sdl_gall_arts_list:
            if sdl_gal_check_seen(img):
                seen_count += 1
            img_count += 1
        ratio = seen_count / img_count * 100
        sdl_gall_progress = round(ratio, 1)

init 1:
    image bg gallery_7dl = get_image_7dl("gui/gallery/gallery_bg.png")
    $ locked_img_7dl = ["gallery_stub_1.png", "gallery_stub_2.png", "gallery_stub_3.png"]

    $ sdl_gall_mode = ""
    $ sdl_gall_page = 1
    $ sdl_gall_page_str = "1"

    $ style.sdl_page_text = Style(style.default)
    $ style.sdl_page_text.font  = get_image_7dl("fonts/a_AvanteLtNr.ttf")
    $ style.sdl_page_text.color = "#ffffff"
    $ style.sdl_page_text.size = 60

    $ sdl_gall_sshow = False
    $ sdl_gall_orig = False
    $ sdl_gall_curr_list = []

screen sdl_gall_main:
    add get_image_7dl("gui/gallery/gallery_bg.png")

    if not sdl_gall_mode == "bgs":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_bgs_%s.png") xalign 0.31 yalign 0.029
            action [SetVariable("sdl_gall_mode", "bgs"), SetVariable("sdl_gall_page", 1), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2)), Show("sdl_gall_bw", transition=Dissolve(0.2)), Show("sdl_gall_fw", transition=Dissolve(0.2)), Show("sdl_gall_sshow", transition=Dissolve(0.2))]
    else:
        add get_image_7dl("gui/gallery/gallery_navig_bgs_hover.png") xalign 0.31 yalign 0.029
    if not sdl_gall_mode == "arts":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_arts_%s.png") xalign 0.733 yalign 0.032
            action [SetVariable("sdl_gall_mode", "arts"), SetVariable("sdl_gall_page", 1), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2)), Show("sdl_gall_bw", transition=Dissolve(0.2)), Show("sdl_gall_fw", transition=Dissolve(0.2)), Show("sdl_gall_sshow", transition=Dissolve(0.2))]
    else:
        add get_image_7dl("gui/gallery/gallery_navig_arts_hover.png") xalign 0.733 yalign 0.032
    if sdl_gall_mode not in ("bgs", "filter"):
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_filter_%s.png") xcenter 0.917 ycenter 0.148
            action [Hide("sdl_gall_sshow", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), SetVariable("sdl_gall_mode", "filter"), SetVariable("sdl_gall_page", 1), Show("sdl_gall_filter", transition=Dissolve(0.2))]
    if sdl_gall_mode == "filter":
        timer 0.01 action [Show("sdl_gall_filter", transition=Dissolve(0.2)), Show("sdl_gall_exit", transition=Dissolve(0.2))]
    else:
        timer 0.01 action [Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2)), Show("sdl_gall_bw", transition=Dissolve(0.2)), Show("sdl_gall_fw", transition=Dissolve(0.2)), Show("sdl_gall_sshow", transition=Dissolve(0.2)), Show("sdl_gall_exit", transition=Dissolve(0.2))]
        if not sdl_gall_orig:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_orig_unch_%s.png") xcenter 0.08 ycenter 0.148
                action [SetVariable("sdl_gall_orig", True), SetVariable("sdl_gall_page", 1), Hide("sdl_gall_photos", transition=Dissolve(0.2)), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2))]
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_orig_ch_%s.png") xcenter 0.08 ycenter 0.148
                action [SetVariable("sdl_gall_orig", False), SetVariable("sdl_gall_page", 1), Hide("sdl_gall_photos", transition=Dissolve(0.2)), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2))]
        text "ОРИГИНАЛЬНЫЕ\nАРТЫ":
            text_align 0.5
            xcenter 0.08
            ycenter 0.23
            color "#fff"
            font get_image_7dl("fonts/a_AvanteLtNr.ttf")
            size 45

    # Панелька плеера
    if sdl_mus_engine.is_active:
        use music_panel_7dl(default_music=music_7dl["more_than_alive"])

screen sdl_gall_exit:
    if sdl_gall_sshow:
        imagebutton:
            if persistent.stream_mode_7dl:
                auto get_image_7dl("gui/gallery/gallery_navig_exit_a_%s.png") xalign 0.029 yalign 0.971
            else:
                auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("sdl_gall_exit", transition=Dissolve(0.2)), Hide("sdl_gall_page_input", transition=Dissolve(0.2)), SetVariable("sdl_gall_sshow", False), Jump("sdl_gall_continue")]
    elif sdl_gall_mode == "filter":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("sdl_gall_filter", transition=Dissolve(0.2)), Hide("sdl_gall_exit", transition=Dissolve(0.2)), Hide("sdl_gall_page_input", transition=Dissolve(0.2)), SetVariable("sdl_gall_mode", ""), SetVariable("sdl_gall_page", 1), Jump("main_menu_7dl")]
    else:
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971
            action [Hide("sdl_gall_photos", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), Hide("sdl_gall_sshow", transition=Dissolve(0.2)), Hide("sdl_gall_exit", transition=Dissolve(0.2)), Hide("sdl_gall_page_input", transition=Dissolve(0.2)), SetVariable("sdl_gall_mode", ""), SetVariable("sdl_gall_page", 1), Jump("main_menu_7dl")]

screen sdl_gall_bw:
    if sdl_gall_page > 1:
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
            action [SetVariable("sdl_gall_page", sdl_gall_page-1), Hide("sdl_gall_photos", transition=Dissolve(0.2)), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2))]

screen sdl_gall_fw:
    if sdl_gall_page < ((len(sdl_gall_curr_list) - 1) // 6 + 1):
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
            action [SetVariable("sdl_gall_page", sdl_gall_page+1), Hide("sdl_gall_photos", transition=Dissolve(0.2)), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2))]

screen sdl_gall_filter:
    tag menu
    $ sdl_gall_filter_imgs = {"mi": ["Мику", "d6_mi_hugs_7dl"], "dv": ["Алиса", "d7_dv_hugs_7dl"], "sl": ["Славя", "d7_sl_hug_7dl"], "un": ["Лена", "d3_un_dance2_7dl"], "mt": ["Ольга", "d2_mt_resort_7dl"], "us": ["Ульяна", "d6_us_normal_dance_7dl"]}
    $ sdl_gall_img_count = 0
    for char in sdl_gall_filter_imgs:
        imagebutton:
            idle get_image_7dl("gui/gallery/arts/"+sdl_gall_filter_imgs[char][1]+"_idle.png") xalign (0.2 + 0.3 * (sdl_gall_img_count % 3)) yalign (0.15 if sdl_gall_img_count < 3 else 0.93)
            action [Hide("sdl_gall_filter", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), SetVariable("sdl_gall_mode", char), SetVariable("sdl_gall_page", 1), Function(sdl_gal_set_list), Show("sdl_gall_photos", transition=Dissolve(0.2)), Show("sdl_gall_bw", transition=Dissolve(0.2)), Show("sdl_gall_fw", transition=Dissolve(0.2))]
        text sdl_gall_filter_imgs[char][0]:
            text_align 0.5
            xcenter (0.26 + 0.24 * (sdl_gall_img_count % 3))
            ycenter (0.45 if sdl_gall_img_count < 3 else 0.91)
            style "replays_textbutton"
            color "#2f059a"
        $ sdl_gall_img_count += 1

screen sdl_gall_sshow:
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_navig_slide_show_%s.png") xcenter 1761 ycenter 280
        action [Hide("sdl_gall_photos", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), Hide("sdl_gall_sshow", transition=Dissolve(0.2)), Jump("sdl_gall_sshow_imgs")]

screen sdl_gall_photos:
    tag menu
    text "ОТКРЫТО\nАРТОВ: [sdl_gall_progress]%":
        text_align 0.5
        xcenter 0.08
        ycenter 0.73
        color "#fff"
        font get_image_7dl("fonts/a_AvanteLtNr.ttf")
        size 45
    $ sdl_gall_img_count = 0
    if sdl_gall_mode == "bgs":
        textbutton str(sdl_gall_page)+" / "+str(((len(sdl_gall_curr_list) - 1) // 6 + 1)):
            action Show("sdl_gall_page_input", transition=Dissolve(0.2))
            text_style "sdl_page_text"
            style "sdl_page_text"
            xalign 0.95
            yalign 0.95
        for img in sdl_gall_curr_list[sdl_gall_page*6-6:sdl_gall_page*6]:
            if sdl_gal_check_seen(img):
                imagebutton:
                    auto get_image_7dl("gui/gallery/bgs/"+img.get_img()+"_%s.png") xalign (0.2 + 0.3 * (sdl_gall_img_count % 3)) yalign (0.15 if sdl_gall_img_count < 3 else 0.93)
                    action [Hide("sdl_gall_photos", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), Hide("sdl_gall_sshow", transition=Dissolve(0.2)), Hide("sdl_gall_exit", transition=Dissolve(0.2)), Call("sdl_gall_show_imgs", img)]
            else:
                add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign (0.2 + 0.3 * (sdl_gall_img_count % 3)) yalign (0.15 if sdl_gall_img_count < 3 else 0.93)
            $ sdl_gall_img_count += 1
    elif (sdl_gall_mode == "arts") or (sdl_gall_mode in sdl_gall_girls_list):
        textbutton str(sdl_gall_page)+" / "+str(((len(sdl_gall_curr_list) - 1) // 6 + 1)):
            action Show("sdl_gall_page_input", transition=Dissolve(0.2))
            text_style "sdl_page_text"
            style "sdl_page_text"
            xalign 0.95
            yalign 0.95
        for img in sdl_gall_curr_list[sdl_gall_page*6-6:sdl_gall_page*6]:
            if sdl_gal_check_seen(img) and (persistent.hentai_graphics_7dl or (not img.get_hent())):
                imagebutton:
                    auto get_image_7dl("gui/gallery/arts/"+img.get_img()+"_%s.png") xalign (0.2 + 0.3 * (sdl_gall_img_count % 3)) yalign (0.15 if sdl_gall_img_count < 3 else 0.93)
                    action [Hide("sdl_gall_photos", transition=Dissolve(0.2)), Hide("sdl_gall_bw", transition=Dissolve(0.2)), Hide("sdl_gall_fw", transition=Dissolve(0.2)), Hide("sdl_gall_sshow", transition=Dissolve(0.2)), Hide("sdl_gall_exit", transition=Dissolve(0.2)), Call("sdl_gall_show_imgs", img)]
            else:
                add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign (0.2 + 0.3 * (sdl_gall_img_count % 3)) yalign (0.15 if sdl_gall_img_count < 3 else 0.93)
            $ sdl_gall_img_count += 1

screen sdl_gall_page_input:
    frame:
        background None
        xcenter 0.92
        ycenter 0.81
        vbox:
            input default sdl_gall_page:
                value VariableInputValue("sdl_gall_page_str")
                allow "0123456789"
                style "sdl_page_text"
                xalign 0.5
            textbutton "OK":
                action [Hide("sdl_gall_page_input", transition=Dissolve(0.2)), SetVariable("sdl_gall_page", int("0"+sdl_gall_page_str))]
                keysym('K_RETURN', 'K_KP_ENTER')
                style "log_button"
                text_style "settings_link"

label sdl_gall_start:
    $ make_names_known_7dl()
    $ sdl_gall_progress_calc()
    if not sdl_mus_engine.is_active:
        play music music_7dl["more_than_alive"] fadein 3
    scene bg gallery_7dl with fade
    $ sdl_gall_mode = "arts"
    $ renpy.block_rollback()
    call screen sdl_gall_main

label sdl_gall_continue:
    scene bg gallery_7dl with dissolve
    $ renpy.block_rollback()
    call screen sdl_gall_main

label sdl_gall_show_imgs(img):
    python:
        if renpy.seen_image(img.get_type()+img.get_img()):
            renpy.scene()
            if img.get_img() == "d7_me_neu_graydoomed_7dl":
                renpy.show(img.get_type()+img.get_img(), at_list=[middle_gallery])
            elif img.get_vert():
                sdl_gall_vert_ratio = img.get_vert()
                renpy.show(img.get_type()+img.get_img(), at_list=[bottotop])
            else:
                renpy.show(img.get_type()+img.get_img(), at_list=[normal_gallery])
            renpy.with_statement(fade)
            renpy.pause()
        if img.get_add_img():
            for i in img.get_add_img():
                if renpy.seen_image(img.get_type()+i):
                    renpy.scene()
                    if img.get_vert():
                        sdl_gall_vert_ratio = img.get_vert()
                        renpy.show(img.get_type()+i, at_list=[bottotop])
                    else:
                        renpy.show(img.get_type()+i, at_list=[normal_gallery])
                    renpy.with_statement(fade)
                    renpy.pause()
        renpy.show("bg black")
    jump sdl_gall_continue

label sdl_gall_sshow_imgs:
    $ sdl_gall_sshow = True
    python:
        if sdl_gall_mode == "arts" or (sdl_gall_mode in sdl_gall_girls_list):
            for img in sdl_gall_curr_list:
                if (renpy.seen_image(img.get_type()+img.get_img())) and (persistent.hentai_graphics_7dl or (not img.get_hent())):
                    renpy.scene()
                    if img.get_img() == "d7_me_neu_graydoomed_7dl":
                        renpy.show(img.get_type()+img.get_img(), at_list=[middle_gallery])
                        renpy.with_statement(fade)
                        if persistent.stream_mode_7dl:
                            renpy.pause(15)
                        else:
                            renpy.pause(4)
                    elif img.get_vert():
                        sdl_gall_vert_ratio = img.get_vert()
                        renpy.show(img.get_type()+img.get_img(), at_list=[bottotop])
                        renpy.with_statement(fade)
                        if persistent.stream_mode_7dl:
                            renpy.pause(15)
                        else:
                            renpy.pause(round(6.72/sdl_gall_vert_ratio, 1))
                    else:
                        renpy.show(img.get_type()+img.get_img(), at_list=[normal_gallery])
                        renpy.with_statement(fade)
                        if persistent.stream_mode_7dl:
                            renpy.pause(15)
                        else:
                            renpy.pause(4)
        elif sdl_gall_mode == "bgs":
            for img in sdl_gall_curr_list:
                if renpy.seen_image(img.get_type()+img.get_img()):
                    renpy.scene()
                    renpy.show(img.get_type()+img.get_img(), at_list=[normal_gallery])
                    renpy.with_statement(fade)
                    if persistent.stream_mode_7dl:
                        renpy.pause(15)
                    else:
                        renpy.pause(4)
    if persistent.stream_mode_7dl:
        jump sdl_gall_sshow_imgs
    else:
        hide screen sdl_gall_exit
        $ sdl_gall_sshow = False
        jump sdl_gall_continue
