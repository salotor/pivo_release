init -998 python:
    style.button_text_7dl = Style(style.default)
    style.button_text_7dl.color = "#c8ffff"
    style.button_text_7dl.insensitive_color = "#c8c8c8"
    style.button_text_7dl.selected_color = "#ffffc8"
    style.button_text_7dl.text_align = 0.5
    style.button_text_7dl.xalign = 0.5
    style.button_text_7dl.yalign = 0.5
    style.button_text_7dl.ypos = 9
    style.button_text_7dl.xpadding = 6
    style.button_text_7dl.size = 13

    style.button_7dl = Style(style.default)
    style.button_7dl.background = Frame(im.Twocolor("_roundrect/rr6g.png", "#404040", "#404040"), 12, 12)
    style.button_7dl.hover_background = Frame(im.Twocolor("_roundrect/rr6g.png", "#404040", "#404040"), 12, 12)
    style.button_7dl.insensitive_background = Frame(im.Twocolor("_roundrect/rr6g.png", "#404040", "#404040"), 12, 12)
    style.button_7dl.xmargin = 1
    style.button_7dl.xpadding = 6
    style.button_7dl.ymargin = 1
    style.button_7dl.ypadding = 1
    style.button_7dl.ypos = 2

python early:
    def widget_lp_7dl():
        if (not persistent.lp_widget_7dl) or (plthr in [u"None", u"Выбор", u"Достижения", u"Меню", u"Ролик"]):
            return
        else:
            # Роль
            ui.button(clicked=None, style="button_7dl", xpos=0.0, xanchor=0.0, xminimum=120)
            ui.text("%s: %s" % ("Роль", plthr), style="button_text_7dl")

            ui.button(clicked=None, style="button_7dl", xpos=0.16, xanchor=0.0, xminimum=200)
            ui.text("%s" % (save_name), style="button_text_7dl")

            # Особые поинты
            if plthr != u"Мажор":
                ui.button(clicked=None, style="button_7dl", xpos=0.07, xanchor=0.0, xminimum=120)
                if alt_sp > 0:
                    ## Карма | Воля (Славя-Классик)
                    if karma >= 75:
                        ui.text("%s: %d | %s: %d" % ("Карма", karma, "Воля", alt_sp), style="button_text_7dl", size=14, color="#7bacff")
                    else:
                        ui.text("%s: %d | %s: %d" % ("Карма", karma, "Воля", alt_sp), style="button_text_7dl")
                elif (alt_spt > 0) or (alt_hpt > 0):
                    ## Princess | Human (Мику-7дл)
                    if alt_spt >= 7:
                        ui.text("%s: %d | %s: %d" % ("Princess", alt_spt, "Human", alt_hpt), style="button_text_7dl", size=14, color="#ff7bac")
                    elif alt_hpt >= 7:
                        ui.text("%s: %d | %s: %d" % ("Human", alt_hpt, "Princess", alt_spt), style="button_text_7dl", size=14, color="#ac7bff")
                    else:
                        ui.text("%s: %d | %s: %d" % ("Human", alt_hpt, "Princess", alt_spt), style="button_text_7dl")
                else:
                    ## Карма
                    if karma >= 75:
                        ui.text("%s: %d" % ("Карма", karma), style="button_text_7dl", size=14, color="#7bacff")
                    else:
                        ui.text("%s: %d" % ("Карма", karma), style="button_text_7dl")

            # ЛП поинты
            if (routetag == "neu") or ("mt" in routetag) or ("us" in routetag):
                ## Ответы | Ольга | Ульяна
                ui.button(clicked=None, style="button_7dl", xpos=1.0, xanchor=1.0, xminimum=120)
                if counter_us_7dl < 6:
                    ui.text("%s: %d" % ("Ульяна", counter_us_7dl), style="button_text_7dl", color="#f65252")
                else:
                    ui.text("%s: %d" % ("Ульяна", counter_us_7dl), style="button_text_7dl", size=14, color="#ff3200")
                ui.button(clicked=None, style="button_7dl", xpos=0.93, xanchor=1.0, xminimum=120)
                if counter_mt_7dl < 7:
                    ui.text("%s: %d" % ("Ольга", counter_mt_7dl), style="button_text_7dl", color="#f65252")
                else:
                    ui.text("%s: %d" % ("Ольга", counter_mt_7dl), style="button_text_7dl", size=14, color="#00ea32")
                if persistent.alt_binder:
                    ui.button(clicked=None, style="button_7dl", xpos=0.86, xanchor=1.0, xminimum=120)
                    if counter_me_neu_answers < 3:
                        ui.text("%s: %d" % ("Ответы", counter_me_neu_answers), style="button_text_7dl", color="#f65252")
                    else:
                        ui.text("%s: %d" % ("Ответы", counter_me_neu_answers), style="button_text_7dl", size=14, color="#e1dd7d")
            elif ("un7dl" in routetag) and (counter_un_fz == 2):
                ui.button(clicked=None, style="button_7dl", xpos=0.79, xanchor=1.0, xminimum=120)
                ui.text("%s: %d" % ("Лена", counter_un_fz_un_route), style="button_text_7dl", color="#ff55ff")
                ui.button(clicked=None, style="button_7dl", xpos=0.86, xanchor=1.0, xminimum=120)
                ui.text("%s: %d" % ("Алиса", counter_un_fz_dv_fake_date), style="button_text_7dl", color="#FF5300")
                ui.button(clicked=None, style="button_7dl", xpos=0.93, xanchor=1.0, xminimum=120)
                ui.text("%s: %d" % ("Дорога", counter_un_fz_old_road), style="button_text_7dl", color="#ff2222")
                ui.button(clicked=None, style="button_7dl", xpos=1.0, xanchor=1.0, xminimum=120)
                ui.text("%s: %d" % ("Ольга", counter_un_fz_mt_transit), style="button_text_7dl", color="#00ea32")
            elif routetag == "dvdj":
                ui.button(clicked=None, style="button_7dl", xpos=0.86, xanchor=1.0, xminimum=120)
                ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text_7dl", color="#bb8800")
                if secret_dv_dj > 0:
                    ui.button(clicked=None, style="button_7dl", xpos=0.93, xanchor=1.0, xminimum=120)
                    ui.text("%s: %d" % ("Тайна", secret_dv_dj), style="button_text_7dl", color="#00a060")
            elif routetag == "neu_main":
                ### Мику
                ui.button(clicked=None, style="button_7dl", xpos=1.00, xanchor=1.0, xminimum=90)
                if lp_mi < 5:
                    ui.text("%s: %d" % ("Мику", lp_mi), style="button_text_7dl")
                else:
                    ui.text("%s: %d" % ("Мику", lp_mi), style="button_text_7dl", color="#00bbbb")

                ### Алиса
                ui.button(clicked=None, style="button_7dl", xpos=0.95, xanchor=1.0, xminimum=90)
                if lp_dv < 5:
                    ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text_7dl")
                else:
                    ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text_7dl", color="#bb8800")

                ### Славя
                ui.button(clicked=None, style="button_7dl", xpos=0.90, xanchor=1.0, xminimum=90)
                if lp_sl < 5:
                    ui.text("%s: %d" % ("Славя", lp_sl), style="button_text_7dl")
                else:
                    ui.text("%s: %d" % ("Славя", lp_sl), style="button_text_7dl", color="#bbb200")

                ### Лена
                ui.button(clicked=None, style="button_7dl", xpos=0.85, xanchor=1.0, xminimum=90)
                if lp_un < 5:
                    ui.text("%s: %d" % ("Лена", lp_un), style="button_text_7dl")
                else:
                    ui.text("%s: %d" % ("Лена", lp_un), style="button_text_7dl", color="#9f72be")

                ### Ольга
                ui.button(clicked=None, style="button_7dl", xpos=0.80, xanchor=1.0, xminimum=90)
                if counter_mt_7dl < 5:
                    ui.text("%s: %d" % ("Ольга", counter_mt_7dl), style="button_text_7dl")
                else:
                    ui.text("%s: %d" % ("Ольга", counter_mt_7dl), style="button_text_7dl", color="#00ea32")

                ### Ульяна
                ui.button(clicked=None, style="button_7dl", xpos=0.75, xanchor=1.0, xminimum=90)
                if counter_us_7dl < 5:
                    ui.text("%s: %d" % ("Ульяна", counter_us_7dl), style="button_text_7dl")
                else:
                    ui.text("%s: %d" % ("Ульяна", counter_us_7dl), style="button_text_7dl", color="#f65252")

                ### Женя
                ui.button(clicked=None, style="button_7dl", xpos=0.70, xanchor=1.0, xminimum=90)
                if counter_mz_7dl < 3:
                    ui.text("%s: %d" % ("Женя", counter_mz_7dl), style="button_text_7dl")
                else:
                    ui.text("%s: %d" % ("Женя", counter_mz_7dl), style="button_text_7dl", color="#647fc5")
            elif plthr != u"Мажор":
                ## Лена | Славя | Алиса | Мику | Ульяна
                ### Ульяна
                ui.button(clicked=None, style="button_7dl", xpos=1.0, xanchor=1.0, xminimum=120)
                ui.text("%s: %d" % ("Ульяна", lp_us), style="button_text_7dl")

                ### Мику
                ui.button(clicked=None, style="button_7dl", xpos=0.93, xanchor=1.0, xminimum=120)
                if lp_mi < 13:
                    ui.text("%s: %d" % ("Мику", lp_mi), style="button_text_7dl")
                else:
                    if (counter_mi_7dl == 2) and (alt_day2_date == 'mi') and (alt_day3_dancing2 in ('mi_2', 'mi_12')):
                        if (alt_spt >= 8) or ((alt_hpt >= 9) and (lp_mi > 16)):
                            ui.text("%s: %d" % ("Мику-7ДЛ", lp_mi), style="button_text_7dl", size=15, color="#00ffff")
                        else:
                            ui.text("%s: %d" % ("Мику-7ДЛ", lp_mi), style="button_text_7dl", size=14, color="#00bbbb")
                    elif (lp_mi >= 13) and (alt_day3_dj == 'mi'):
                        if lp_mi >= 13:
                            ui.text("%s: %d" % ("Мику-DJ", lp_mi), style="button_text_7dl", size=15, color="#00ffff")
                        else:
                            ui.text("%s: %d" % ("Мику-DJ", lp_mi), style="button_text_7dl", size=14, color="#00bbbb")
                    else:
                        ui.text("%s: %d" % ("Мику", lp_mi), style="button_text_7dl", size=14)

                ### Алиса
                ui.button(clicked=None, style="button_7dl", xpos=0.86, xanchor=1.0, xminimum=120)
                if lp_dv >= 11:
                    if lp_dv < 18:
                        ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text_7dl", size=14, color="#bb8800")
                    else:
                        ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text_7dl", size=15, color="#ffaa00")
                else:
                    ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text_7dl")

                ### Славя
                ui.button(clicked=None, style="button_7dl", xpos=0.79, xanchor=1.0, xminimum=120)
                if (lp_sl < 13) and (counter_sl_cl < 7) and (counter_sl_7dl < 5):
                    ui.text("%s: %d" % ("Славя", lp_sl), style="button_text_7dl")
                else:
                    if counter_sl_cl == 7:
                        if ((lp_sl >= 20) or (alt_sp >= 6)) or ((lp_sl >=20) and (alt_day6_sl_cl_arc == 'sh')):
                            ui.text("%s: %d" % ("Славя-КЛ", lp_sl), style="button_text_7dl", size=15, color="#ffaa00")
                        else:
                            ui.text("%s: %d" % ("Славя-КЛ", lp_sl), style="button_text_7dl", size=14, color="#bbb200")
                    elif counter_sl_7dl == 5:
                        if (lp_sl >= 20) and (karma > 120):
                            ui.text("%s: %d" % ("Славя-7ДЛ", lp_sl), style="button_text_7dl", size=15, color="#ffaa00")
                        elif (lp_sl >= 20):
                            ui.text("%s: %d" % ("Славя-7ДЛ", lp_sl), style="button_text_7dl", size=15, color="#bbb200")
                        else:
                            ui.text("%s: %d" % ("Славя-7ДЛ", lp_sl), style="button_text_7dl", size=14, color="#bbb200")
                    else:
                        ui.text("%s: %d" % ("Славя", lp_sl), style="button_text_7dl", size=14)

                ### Лена
                ui.button(clicked=None, style="button_7dl", xpos=0.72, xanchor=1.0, xminimum=120)
                if lp_un >= 12:
                    if lp_un < 20:
                        ui.text("%s: %d" % ("Лена", lp_un), style="button_text_7dl", size=14, color="#9f72be")
                    else:
                        ui.text("%s: %d" % ("Лена", lp_un), style="button_text_7dl", size=15, color="#d599ff")
                else:
                    ui.text("%s: %d" % ("Лена", lp_un), style="button_text_7dl")

    config.overlay_functions.append(widget_lp_7dl)
