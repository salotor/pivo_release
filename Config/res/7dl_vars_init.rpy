#Мод пилится на базе нетленки от АБЦБ - его сюжет и подача мне куда симпатичнее оригинальной стори.
#За что ему огромный респектище и, по возможности, оставлены отсылки на оригинальные правки.
init -1:
    $ alt_release_no = "1.0"
    $ alt_compatible_release_no = ["0.34.a", "0.34.b", "0.35.a", "0.36.a", "0.37.a", "0.38.a", "0.39.a", "0.40", "0.40.1", "0.40.2", "0.41", "0.42", "0.43", "0.44", "0.45", "0.46", "0.47", "0.48", "0.49", "0.50", "0.51", "0.52", "0.53", "0.54", "0.55", "0.56", "0.57", "0.58", "1.0"]
    $ alt_hotfix_no = ""
    $ plthr = u"None"
    $ alt_start_release_no = None

init 2:
    $ mods["scenario__alt_sevendl"] = u"7 Дней Лета: Lost Alpha"
    $ mod_tags["scenario__alt_sevendl"] = ["length:days","gameplay:vn","protagonist:male"]

    $ timeskip_dev = "Рут находится в активной разработке"

    $ alt_credits_text = "{image=logo_7dl}\n\n\n{b}Сценарий{/b}\n\ndialup, Евген, 7дл-кун, abcb\n\n{b}Режиссура сцен{/b}\n\nGr0m, AlzGamer, Ismir, 7дл-кун, still13free, stranburg\n\n{b}Графика{/b}\n\nТэй (shwwma), mono, GoodbyeNona, SkieyWayfarer, Макс Смолев, Narwhal Iv, Kef34, Mannych, FairyApple, nyamaznya, nenkoket, Trojan, NikHaker, rina.jess, childofburningtime27, Касандра, resident_art, Mo~, Эру, Денис Кучер, goozeecat, Таруто Неко, Primary, teromioset, RanKate, LCKR, Katy-Tan, Eve Kel'man, Панельев, Михаил Ломов, Денис Скиба, София «matrox» Харитонова, nell4an, Иван Лебедев\n\n{b}Музыка{/b}\n\nApril Rain, Tym Nyman, DeadPunk, ППВК, Kevin MacLeod, SinkWay, DeepCosmo, телеэкран, seille, Denis Stelmakh и др.\n\n{b}Логика повествования, вычитка сценария{/b}\n\nЕвген, Gr0m, AlzGamer, Sitzileon, Ismir, Salotor, Dantiras, faddeev, Kaiserd3, Alex New, tngeyzer, Kellvan\n\n{b}Код и адаптация{/b}\n\nSalotor — порт сценария в Steam и на Андроид, главное меню, галерея, раздел «Истории», прочие технические решения\n\nKaiserd3 — ачивлист, просмотрщик сцен, музыкальный плеер\n\nSitzileon — рефаб рутов\n\nEldhenn, Kibconj — порт сценария в Steam\n\nLyonyai, drh, Macrosis — перевод на английский язык\n\nBlackMazeGOD — главное меню\n\nNuttyprof, openplace — новая карта лагеря и новый карточный турнир\n\nЛенофаг Простой, Ravsii — стартовые меню\n\n{b}Бета-тест{/b}\n\nAlex New, Corvinus, Kellvan\n\n{b}Товарищи, помогавшие со всем остальным{/b}\n\nМакс Ветров, Drago23, Arlien, Peregarrett, Demiurge-kun, Дельта, KirillZ89, Ленофаг Простой, Ленивый Бегун, Занудный, Serge Domingo, Ravsii, Peregarrett, Chess, shers, polandkyn, alexzen84, traven42, nikolaystorm, Рыжий Тигра, Paul Atrides, Пивной Логист, Уныл, звёздныйэкспресс, btn, Хомячок aka Апрель, Евдокия\n\n{b}Благодарим за предоставленные ресурсы{/b}\n\nРазработчиков модификаций «Саманта», «Булки, кефир и рок-н-ролл», «Двое», «Последнее Лето», «Эти безумные деньки!», «Бесконечное лето: продолжение истории», «Дубликат», «По ту сторону Совёнка», «Сансара», «История одного лагеря», визуальных новелл «HSOOVN», «Katawa Shoujo», «Young Hearts», группу «КПБСА», Дмитрия Мерзлякова, Артёма Болгова, Ивана Лебедева\n\n{b}Команда разработчиков «7 Дней Лета: Lost Alpha»{/b}\n\nAlzGamer, dialup, Gr0m, salotor, Евген\n\n{b}Выражаем благодарность{/b}\n\nКоманде «Soviet Games» за предоставление ресурсов и платформы для творчества\n\n7дл-куну за ранее проделанную работу над модификацией «7 дней лета»\n\nСпасибо всем, кто не был упомянут, но внёс свой вклад, — за то, что помогали и поддерживали!"

    $ alt_donator_list = [[u'mysteriousarchangel', u'Святослав Тюпин', u'Вечный Джун (Ждун)', u'Пивной Логист', u'Степан Ермаков', u'Николай Ерохин', u'Александр Павлов', u'Guron', u'Кит', u'Юрий Назаренко', u'Даниил Полев', u'Shun Akiyama', u'Роман Александров', u'AlzGamer', u'Arrogance', u'Геннадий Сафонкин', u'btn', u'Salieri410', u'Иван Силкин', u'Илья Макарычев', u'_sponez', u'Мужчина', u'I_AM_SHREK', u'Herr_Kruss', u'Дмитрий Ражабалиев', u'Иван Рейнгард', u'Nyanpasa_', u'TheMagicPe4enka', u'Евдокия', u'Илья Соболев', u'Савва Окопный', u'Владимир Якимчук', u'An00b1z', u'Проект TRP M&K', u'AD_god', u'Rogi Vegas', u'Arsulis', u'13th_PILOT', u'Егор из Амбальского Чатика (the_vozhd)', u'Александр Лобанов', u'Нянпаса', u'Иван Кецко', u'Redmoor Goto', u'Атлас', u'Перегонный Куб', u'Адриан Бравцев', u'Woolfy', u'Андрей Шмаков', u'Очередной Mukylllu3', u'Евгений Москвичев', u'Владимир Недужко', u'Обыgun 228', u'Haydar1989', u'Анатолий Сотник', u'Андрей Неткачев', u'Invidious ', u'FarnassesRX', u'Артемий Стрела', u'Мэрт Арслан'], [u'Андрей Цымбалюк', u'Влад Зозуля', u'Иван Усик', u'Максим Шорохов', u'Марк Буревестник', u'Михаил Круглов', u'Рафаэль Мамчич', u'Лекс Мрачный', u'DarkSniper', u'Егор Маркин', u'Foxed', u'Максим Хочу научиться готовить едуф', u'Frostmourne', u'Shytongue', u'Nyanpasa Verflucht', u'prononim', u'Аянами Рей хочу научиться готовить едуф', u'Беларус', u'Лена и Юри спрашивают', u'Kabelka', u'Olexas', u'Petr Janouškovec', u'Tommy Joad', u'Labus', u'Изяслав Макаров', u'Antaniel Inharnity', u'Kidon', u'GoodPeter', u'☕️Чай с молоком🥛', u'Maer', u'Russian Иван', u'ваффелл', u'Эн', u'ShizyMik', u'Dmitry Я Кшка', u'Freetin', u'Prosto_Aleksey', u'Александр Разливаев', u'Фёдор', u'Чумба-Чучумба', u'Legion', u'Александр Майский', u'C0D1 ', u'staffkarp ', u'Арсений', u'Максим Соборников', u'Яков Сивин', u'shwwma', u'Ikadzev', u'Snowfox330', u'AlexrGnus', u'Alexund', u'EoFumi', u'Gamball007', u'Hatsune Aquamarine', u'siniy sahar', u'Егор Ковтун', u'Иванов Кирилл', u'Марат Учиха', u'Никита Назаров', u'Сергей Евтухов', u'Синдзо Абэ', u'Maximka_mecenat', u'Dilea', u'drh', u'maizz', u'Romualdo', u'TheBestWarrior'], [u'Илья Шелихин', u'Salathicc', u'Kivi86', u'Sad Nation', u'1NGO', u'Berkyt', u'Endcru', u'Ermakar', u'Korvin Khazad', u'mahichh♥', u'Mirai no hito', u'Peonur', u'Xopek_1337', u'Абстрактное Лето', u'Александр Полончук', u'Денис Иванов', u'Дмитрий Родоманов', u'Жора', u'Миша Акимцев', u'никита потапович', u'Tom Joad', u'yetaroamzero', u'EwokRus', u'Tom Nguyen', u'Егор Гришмановский', u'Леонид Игнатов', u'Михайло Балаганский', u'Шичков Легенда ', u'Ricardo Gorillas', u'Дима Ягунов', u'Shredrum', u'Alex Lucis Caelum', u'MsFet', u'Vitaly', u'IXIL_x', u'Антон Кулаженков', u'Евген ', u'TDI', u'SoLonely', u'Abuser', u'DanilaV7', u'kresto00', u'Subway7887', u'Лена Тихонова', u'kodopp', u'Stuxi', u'Александр Дейнеко', u'Григорий Бородин', u'Дима Попов', u'Леонид Пономарев', u'Максим Лёвин', u'Никита Павлов', u'Таня Танина', u'Чокер Алёны Повышевой', u'ЭЛИСОФАГ', u'Дед внутри', u'Игорь Крашенинников', u'King Crimson Is Confusing', u'Echoe', u'Aleksey', u'Cú Chulainn', u'Dominion 1859', u'Nerrbrin', u'Sgt Frost', u'Shadence', u'Taunt33', u'Totaldark ', u'Арсений Липатов', u'Вадим Фирюпкин'], [u'Кесарь добрый ', u'Матвей Проскуряков', u'Овчинников Вадим', u'Рома Попека', u'Виктор Резунов', u'Alexandr Gavrikov', u'Broni', u'Faded', u'Mikro4elik', u'Андрей Фадеев', u'Bogdan GG', u'MazNarever', u'Дмитрий Стрыкало', u'Taunt', u'Maslinu4', u'Chuchundra', u'DarkFox', u'Анатоль Курочкин', u'Андрей Васильев', u'Владимир Ищенко', u'Данил Переверзев', u'Сева', u'Сергей Матвеев', u'Levyne', u'hypn0sphere', u'anime girl', u'iailil', u'Борис Тетерин', u'Dean Winchester', u'muhomor41k', u'Quark Rain', u'World Creator892', u'Великая Паймон', u'Олег Нигамаев', u'Секретарь ханжеского отдела ВЛКСМ', u'Mor0v4ik', u'Алексей Иванов', u'Point_man', u'Egor Matveev', u'Генератор Бабла', u'Иван Кутепов', u'Максон', u'Славя не одобряет этот рут', u'Тимофей Масло', u'Чикишев Владислав', u'Аркадий Шестиряков', u'Mak8m', u'Alex Ten', u'Alexander Go', u'Dirty_Senator', u'HikkiNEET', u'Гигачад', u'Максим Шибанов', u'Спасибо СалаторКатя', u'Степан Михеев', u'staffkarp', u'Ilya Timokhin', u'Артём Юран', u'Ilgar Novruzov', u'Nikita Pchelintsev', u'Red cap', u'Robert Langdon', u'Sasha', u'Tengo'], [u"Velg'larn Noamuth", u'Александр Березин', u'Алексей Голачев', u'Анастасия Тихонова', u'Анатолий Правдюк', u'Андрей Бакин', u'Андрей Любимов', u'Андрей Попович', u'Артём Горский', u'Артем Захаров', u'Буф', u'Вячеслав Юшков', u'Григорий Коток', u'Даниил Мясников', u'Даниил Пигин', u'Даниил Чуб', u'Данила Васильев', u'Даня Шляхтич', u'Денис Гумаров', u'Дима Марин', u'Дима Токарев', u'Евгений Зюзин', u'Евгений Обз', u'И тут врывается милицейский бобик', u'Иван Бабич', u'Иван Крузенштейн', u'Иван Пичуев', u'Иван Трубин', u'Кевин Каслана', u'Максим Печков', u'Михаил Осипов', u'Никита Малярчук', u'Олег Луданный', u'Паша Пилипчук', u'Пивожор с 7-летним стажем', u'Сергей Дубровин', u'Серго Зайцев', u'Совёнок 🌸ܓ', u'Старик', u'Тётка', u'Хайдар Стародубцев', u'Хихих', u'Ярослав Старостин', u'Илья Вишняков', u'Никита Мошонкин', u'Энакентий Бест', u'Albert Schiemann', u'alxlsn ', u'Andrey Babenyshev', u'Artur Martos', u'BrightFlame', u'FunT1k', u'Mause', u'Operator FPV', u'Weeldand', u'WK217', u'Александр Фомин', u'Данила Макаров', u'Идиотический'], [u'Мaxim Мusin', u'Михаил Ломакин', u'Михаил Стеблевец', u'Никита Золанов', u'Семён Павлюк', u'Степан Ульянкин', u'Юлькен']]

    #Day - базис
    #Sunset - 94%, 82%, 100%
    #Night - 58%, 67%, 67%
    #Prologue - 84%, 72%, 100%

    $ colors['ai'] = {
    'night': (41, 164, 1, 255),
    'sunset': (67, 201, 2, 255),
    'day': (72, 246, 2, 255),
    'prolog': (60, 177, 2, 255)}
    $ store.names_list.append('ai')
    $ names['ai'] = u'Собеседник'

    $ colors['al'] = {
    'night': (122, 121, 102, 255),
    'sunset': (198, 148, 153, 255),
    'day': (211, 181, 153, 255),
    'prolog': (177, 130, 153, 255)}
    $ store.names_list.append('al')
    $ names['al'] = u'Алька'

    $ colors['am'] = {
    'night': (94, 143, 100, 255),
    'sunset': (152, 175, 149, 255),
    'day': (162, 214, 149, 255),
    'prolog': (136, 154, 149, 255)}
    $ store.names_list.append('am')
    $ names['am'] = u'Я'

    $ colors['ase'] = {
    'night': (137, 44, 44, 255),
    'sunset': (222, 54, 56, 255),
    'day': (236, 66, 66, 255),
    'prolog': (198, 48, 66, 255)}
    $ store.names_list.append('ase')
    $ names['ase'] = u'Алиса'

    $ colors['ba'] = {
    'night': (137, 153, 135, 255),
    'sunset': (223, 188, 201, 255),
    'day': (237, 229, 201, 255),
    'prolog': (199, 165, 201, 255)}
    $ store.names_list.append('ba')
    $ names['ba'] = u'Саныч'

    $ colors['bb'] = {
    'night': (133, 116, 90, 255),
    'sunset': (215, 142, 135, 255),
    'day': (229, 173, 135, 255),
    'prolog': (192, 125, 135, 255)}
    $ store.names_list.append('bb')
    $ names['bb'] = u'Алексей Максимыч'

    $ colors['dn'] = {
    'night': (119, 68, 45, 255),
    'sunset': (193, 84, 67, 255),
    'day': (205, 102, 67, 255),
    'prolog': (172, 73, 67, 255)}
    $ store.names_list.append('dn')
    $ names['dn'] = u'Даня'

    $ colors['dy'] = {
    'night': (192, 192, 192, 255),
    'sunset': (192, 192, 192, 255),
    'day': (56, 90, 107, 255),
    'prolog': (192, 192, 192, 255)}
    $ store.names_list.append('dy')
    $ names['dy'] = u'Динамики'

    $ colors['hg'] = {
    'night': (41, 119, 41, 255),
    'sunset': (60, 170, 60, 255),
    'day': (60, 170, 60, 255),
    'prolog': (60, 170, 60, 255)}
    $ store.names_list.append('hg')
    $ names['hg'] = u'Парень'

    $ colors['ka'] = {
    'night': (137, 82, 85, 255),
    'sunset': (222, 101, 127, 255),
    'day': (236, 123, 127, 255),
    'prolog': (198, 89, 127, 255)}
    $ store.names_list.append('ka')
    $ names['ka'] = u'Катюшка'

    $ colors['kids'] = {
    'night': (235, 120, 131, 255),
    'sunset': (235, 120, 131, 255),
    'day': (235, 120, 131, 255),
    'prolog': (235, 120, 131, 255)}
    $ store.names_list.append('kids')
    $ names['kids'] = u'Дети'

    $ colors['ml'] = {
    'night': (43, 134, 98, 255),
    'sunset': (70, 164, 147, 255),
    'day': (74, 200, 147, 255),
    'prolog': (62, 144, 147, 255)}
    $ store.names_list.append('ml')
    $ names['ml'] = u'Мальчик'

    $ colors['ml2'] = {
    'night': (43, 53, 134, 255),
    'sunset': (70, 65, 200, 255),
    'day': (74, 79, 200, 255),
    'prolog': (62, 57, 200, 255)}
    $ store.names_list.append('ml2')
    $ names['ml2'] = u'Мальчик'

    $ colors['ml3'] = {
    'night': (62, 114, 98, 255),
    'sunset': (101, 139, 147, 255),
    'day': (107, 170, 147, 255),
    'prolog': (90, 122, 147, 255)}
    $ store.names_list.append('ml3')
    $ names['ml3'] = u'Мальчик'

    $ colors['sak'] = {
    'night': (89, 115, 146, 255),
    'sunset': (144, 140, 218, 255),
    'day': (153, 171, 218, 255),
    'prolog': (129, 123, 218, 255)}
    $ store.names_list.append('sak')
    $ names['sak'] = u'Сакишита Чихиро'

    $ colors['tn'] = {
    'night': (125, 111, 62, 255),
    'sunset': (203, 136, 93, 255),
    'day': (216, 166, 93, 255),
    'prolog': (181, 120, 93, 255)}
    $ store.names_list.append('tn')
    $ names['tn'] = u'Тоник'

    $ colors['voice1'] = {
    'night': (159, 8, 73, 255),
    'sunset': (196, 7, 92, 255),
    'day': (255, 136, 192, 255),
    'prolog': (196, 7, 124, 255)}
    $ store.names_list.append('voice1')
    $ names['voice1'] = u'Продавщица'

    $ colors['voices'] = {
    'night': (192, 192, 192, 255),
    'sunset': (192, 192, 192, 255),
    'day': (192, 192, 192, 255),
    'prolog': (192, 192, 192, 255)}
    $ store.names_list.append('voices')
    $ names['voices'] = u'Голоса'

    $ colors['we'] = {
    'night': (67, 23, 111, 255),
    'sunset': (132, 27, 100, 255),
    'day': (252, 15, 192, 255),
    'prolog': (150, 50, 100, 255)}
    $ store.names_list.append('we')
    $ names['we'] = u'Хором'

    $ colors['ve'] = {
    'night': (255, 127, 0, 255),
    'sunset': (255, 127, 0, 255),
    'day': (255, 127, 0, 255),
    'prolog': (255, 127, 0, 255),}
    $ store.names_list.append('ve')
    $ names['ve'] = u'Верка'

    $ colors['mir'] = {
    'night': (85, 107, 47, 255),
    'sunset': (85, 107, 47, 255),
    'day': (85, 107, 47, 255),
    'prolog': (85, 107, 47, 255),}
    $ store.names_list.append('mir')
    $ names['mir'] = u'Миря'

    $ colors['an'] = {
    'night': (133, 116, 90, 255),
    'sunset': (215, 142, 135, 255),
    'day': (229, 173, 135, 255),
    'prolog': (192, 125, 135, 255)}
    $ store.names_list.append('an')
    $ names['an'] = u'Алексей Максимыч'

    $ reload_names()

label scenario__alt_sevendl:
    $ alt_start_release_no = alt_release_no # только если игру начали заново - принимаем номер релиза на старте раным номеру текущего релиза
    $ alt_save_release_no = alt_release_no # записываем номер релиза для системы контроля сохранений
### инициализация карт. Должна выполняться ТОЛЬКО один раз - иначе не работают сохранения
    $ init_map_zones_alt1()
    $ init_map_zones_alt2()
###
    $ alt_interface_on() # включаем кастомные менюшки
    jump main_menu_7dl # переходим к главному меню мода

init 4:
    call alt_vars # вызываем все переменные в init
    if persistent.waifu_7dl:
        $ persistent.list_waifu_7dl.append(persistent.waifu_7dl) # записываем текущий фон в меню в список
    $ persistent.waifu_7dl = False # обнуляем текущий фон в меню

label alt_vars:
    call alt_day0_vars
    call alt_day1_vars
    call alt_day2_cards_tournament_vars
    call alt_day2_vars
    call alt_day3_vars
    call alt_day4_mi_7dl_vars
    call alt_day5_mi_7dl_vars
    call alt_day6_mi_7dl_vars
    call alt_day4_mi_dj_vars
    call alt_day5_mi_dj_vars
    call alt_day6_mi_dj_vars
    call alt_day4_dv_7dl_vars
    call alt_day6_dv_7dl_vars
    call alt_day4_dv_dj_vars
    call alt_day5_dv_dj_vars
    call alt_day6_dv_dj_vars
    call alt_day7_dv_dj_vars
    call alt_day4_sl_7dl_vars
    call alt_day5_sl_7dl_vars
    call alt_day6_sl_7dl_vars
    call alt_day7_sl_7dl_vars
    call alt_day4_sl_cl_vars
    call alt_day5_sl_cl_vars
    call alt_day6_sl_cl_vars
    call alt_day7_sl_cl_vars
    call alt_day4_un_7dl_vars
    call alt_day5_un_7dl_vars
    call alt_day6_un_7dl_vars
    call alt_day7_un_7dl_vars
    call alt_day4_un_fz_vars
    call alt_day5_un_fz_vars
    call alt_day6_un_fz_vars
    call alt_day6_mt_7dl_vars
    call alt_day7_mt_7dl_vars
    call alt_day6_us_7dl_vars
    call alt_day7_us_7dl_vars
    call alt_day4_me_neu_vars
    call alt_day5_me_neu_vars
    call alt_day6_me_neu_vars
    call alt_day7_me_neu_vars
    call alt_day1_me_7dl_vars
    call alt_day2_me_7dl_vars
    call alt_day3_me_7dl_vars
    call alt_day4_me_7dl_vars
    call alt_day5_me_7dl_vars
    call alt_day6_me_7dl_vars
    call alt_day7_me_7dl_vars
    return

label alt_day0_vars:
    $ lp_mi = 0
    $ lp_sl = 0
    $ lp_un = 0
    $ lp_us = 0
    $ lp_dv = 0
    $ karma = 0
    $ alt_sp = 0
    $ alt_spt = 0
    $ alt_hpt = 0
    $ dr = False
    $ herc = False
    $ loki = False

    $ routetag = "prologue"
    $ alt_day_catapult = False
    $ alt_replay_on = False
    $ alt_selector = False
    $ role_bg = "intro_ground"
    $ alt_binder_update()

    return

label alt_day1_vars:
    $ counter_mi_7dl = 0 # Счётчик рута (Мику-7дл)
    $ counter_dv_7dl = 0 # Счётчик рута (Алиса-7дл)
    $ counter_sl_7dl = 0 # Счётчик рута (Славя-7дл)
    $ counter_sl_cl = 0  # Счётчик рута (Славя-Классик)
    $ counter_un_7dl = 0 # Счётчик рута (Лена-7дл)
    $ counter_un_cl = 0  # Счётчик рута (Лена-Классик)
    $ counter_un_fz = 0  # Счётчик рута (Лена-ФЗ)
    $ counter_un_fz_un_route = 0     # Лена-ФЗ. Счётчик подрута Лены
    $ counter_un_fz_old_road = 0     # Лена-ФЗ. Счётчик Дороги
    $ counter_un_fz_dv_fake_date = 0 # Лена-ФЗ. Счётчик свиданий с Двачевской
    $ counter_un_fz_mt_transit = 0   # Лена-ФЗ. Счётчик ивентов для транзита на Ольгу. Для транзита должно быть три.
    $ counter_un_fz_dream_un = 0     # Лена-ФЗ. Счётчик снов про Лену.
    $ counter_un_fz_dream_road = 0   # Лена-ФЗ. Счётчик снов про Дорогу.
    $ secret_dv_dj = 0               # Алиса-ДЖ. Счётчик тайны Алисы
    $ list_slavya_7dl = []
    $ alt_day1_cofront_sl_dv = 0
    $ alt_day1_el_followed = False
    $ alt_day1_sl_ignored = False
    $ alt_day1_sl_keys_took = 0
    $ alt_day1_sl_met = False
    $ alt_day1_un = 0
    $ alt_day1_us_shotted = False
    $ alt_day1_un_talk = False #подошел к лене и рассказал анекдот от шамы
    # Переменные кошкорута
    $ alt_day1_chase_uvao = False
    $ alt_day1_genda_investigation = False
    return

label alt_day2_vars:
    $ list_clubs_7dl = []        # список клубов, которые не вычеркнули из бегунка
    $ list_joined_clubs_7dl = [] # список клубов, в которые записались
    $ list_voyage_7dl = []       # список посещённых при обходе мест
    $ alt_day2_bf = ''
    $ alt_day2_convoy = ''
    $ alt_day2_date = ''
    $ alt_day2_cake = False
    $ alt_day2_minijack = False
    $ alt_day2_dv_ultim = 0
    $ alt_day2_dv_chased = False
    $ alt_day2_dv_dinner = False
    $ alt_day2_dv_us_house_visited = False
    $ alt_day2_mi_dinner = False #1: обед с Мику; 2: выбор "А ты одна там постоянно сидишь?", необходим для транзита Ульяны.
    $ alt_day2_mi_kumuhimo = 0
    $ alt_day2_mi_met = False
    $ alt_day2_mi_date = 0
    $ alt_day2_mi_snap = False
    $ alt_day2_mt_help = False
    $ alt_day2_sh_met = False
    $ alt_day2_sl_chased = False
    $ alt_day2_un_rej_convoy = False
    $ alt_day2_us_dubstep = False
    $ alt_day2_us_shenan = False
    $ alt_day2_us_escape = False
    $ alt_day2_us_cake = 0
    $ alt_day2_walk = 0
    $ alt_day2_beach_seen = False
    $ alt_day3_duty = False
    # Турнир
    $ alt_day2_gamblers_result['dv'] = 0
    $ alt_day2_gamblers_result['me'] = 0
    $ alt_day2_gamblers_result['mi'] = 0
    $ alt_day2_gamblers_result['un'] = 0
    $ alt_day2_gamblers_result['us'] = 0
    $ alt_my_rival_1_tour = []
    $ alt_my_rival_semifinal = []
    $ alt_my_rival_final = []
    $ alt_my_rival_1_tour.take = ''
    $ alt_my_rival_semifinal.take = ''
    $ alt_my_rival_final.take = ''
    $ alt_result_dv_1_tour = 0
    $ alt_result_dv_semifinal = 0
    return

label alt_day3_vars:
    $ alt_day3_date = ''
    $ alt_day3_dv_dj_fale = False #Алиса-ДЖ. Фейл вербовки
    $ alt_day3_mi_dj_fale = False #Мика-ДЖ. Фейл вербовки
    $ alt_day3_dj = ''
    $ alt_day3_dancing1 = ''
    $ alt_day3_dancing2 = '' # = 'me_2' - танец C Ольгой
    $ alt_day3_technoquest0 = False
    $ alt_day3_technoquest1 = 0
    $ alt_day3_technoquest2 = False
    $ alt_day3_mi_rejected = False
    $ alt_day3_mi_invited = False
    $ alt_day3_mi_7dl_donor = 0
    $ alt_day3_dv_guitar = 0
    $ alt_day3_sl_invite = False
    $ alt_day3_sl_bath_voy = False
    $ alt_day3_un_med_help = 0
    $ alt_day3_un_strip_pool_sp = 5
    $ alt_day3_un_strip_pool_un = 5
    $ alt_day3_us_bugs = 0
    $ alt_day3_un_fz_work = ''           # Лена-ФЗ. Украшал площадь со Славей/Леной/Алисой.
    $ alt_day3_un_fz_walk = False        # Лена-ФЗ. Флаг прогулки.
    $ alt_day3_un_fz_stories = False     # Лена-ФЗ. Флаг историй.
    $ alt_day3_un_fz_neu_transit = False # Лена-ФЗ. Транзит на сыча.
    $ alt_day3_timer_jump = 0
    $ alt_day3_timer_range = 0
    $ alt_day3_us_invite = False
    $ alt_day3_uvao_spotted = False
    return

label alt_day4_mi_7dl_vars:
    $ alt_day4_mi_7dl_bl_save = False
    $ alt_day4_mi_7dl_fireworks = False
    $ alt_day4_mi_7dl_ev_savior = False
    return

label alt_day5_mi_7dl_vars:
    $ alt_day5_mi_7dl_voyeur = False
    $ alt_day5_mi_7dl_kiss = False
    return

label alt_day6_mi_7dl_vars:
    $ alt_day6_mi_7dl_left = False
    return

label alt_day4_mi_dj_vars:
    $ alt_day4_mi_dj_hedg = False
    $ alt_day4_mi_dj_blackmailed = False
    $ alt_day4_mi_dj_sl_repet = False
    $ alt_day4_mi_dj_reasons = False
    $ alt_day4_mi_dj_sl_repet = False
    return

label alt_day5_mi_dj_vars:
    $ list_mi_search_7dl = []
    $ alt_day5_mi_dj_dv_blade = False
    $ alt_day5_mi_dj_voyeur = 0
    $ alt_day5_mi_dj_apology = 0
    $ alt_day5_mi_dj_hentai_done = False
    $ alt_day5_mi_dj_dv_kissing = False
    return

label alt_day6_mi_dj_vars:
    $ alt_day6_mi_dj_sonic_agreed = False
    $ alt_day6_mi_dj_sl_evil = False
    $ alt_day6_mi_dj_dv_evil = False
    $ alt_day6_mi_dj_me_evil = False
    $ alt_day6_mi_dj_feed = ''
    $ alt_day6_mi_dj_un_evil = False
    $ alt_day6_mi_dj_walkman = False
    $ alt_day6_mi_dj_hentai2 = False
    $ alt_day6_mi_dj_catapult = 0
    $ alt_day6_mi_dj_rejected = False
    return

label alt_day4_dv_7dl_vars:
    $ alt_day4_dv_7dl_extra_key = False
    $ alt_day4_dv_7dl_roadtrip = 0
    $ alt_day4_dv_7dl_portwine = False
    $ alt_day4_dv_7dl_vodka = 0
    $ alt_day4_dv_7dl_ba_conv = False
    $ alt_day4_dv_7dl_hentai_done = False
    $ alt_day4_dv_7dl_help_cs = False
    $ alt_day4_dv_7dl_medication = 0
    return

label alt_day6_dv_7dl_vars:
    $ alt_day6_dv_7dl_route = ''
    $ alt_day6_dv_7dl_transit = False
    $ alt_day6_dv_7dl_key = False
    $ alt_day6_dv_7dl_key_hentai = 0
    $ alt_day6_dv_7dl_alco_hentai = 0
    $ alt_day6_dv_7dl_ba_hentai = 0
    $ alt_day6_dv_7dl_hentai = 0
    $ alt_day6_dv_7dl_dance = ''
    $ alt_day6_dv_7dl_escape_convince = False
    $ alt_day6_dv_7dl_sl_help_agree = False
    $ alt_day7_dv_7dl_check = ''
    $ alt_day7_dv_7dl_brace = 0
    $ alt_day7_dv_7dl_loki_catapult = False
    $ alt_day7_dv_7dl_story_end = False
    return

label alt_day4_dv_dj_vars:
    $ alt_day4_dv_dj_un_quarrel = False
    $ alt_day4_dv_dj_radio_scoff = False
    $ alt_day4_dv_dj_un_dv_question = False
    return

label alt_day5_dv_dj_vars:
    $ alt_day5_dv_dj_map = ""    # Флаги карты. dv - был у Алисы. us - помогал Ульяне. un - был в библиотеке mi - был у Мику. cyber - был у кибернетиков.
    $ alt_day5_dv_dj_sl_jeer = 0 # 0 - Выброси из головы. 1 - Прояви воображение. 2 - Сейчас я разберусь.
    return

label alt_day6_dv_dj_vars:
    $ alt_day6_dv_dj_bet = False
    $ alt_day6_dv_dj_quest = 0  # 0 Вешал гирлянды. 1 - Очищал стенд от газет. 2 - Уборка на складе. 3 - Принести костюмы. 4 - Другие поручения.
    $ alt_day6_dv_dj_dv_run = False
    $ alt_dv_dj_ends = ''       # Bad - плохая. Neu/Rej - Нейтрал/Реджект. good - хорошая? True - истинная. Exc - бонусная.
    return

label alt_day7_dv_dj_vars:
    return

label alt_day4_sl_7dl_vars:
    $ alt_day4_sl_7dl_workout = False
    $ alt_day4_sl_7dl_herc_appletree = False
    $ alt_day4_sl_7dl_help1 = False
    $ alt_day4_sl_7dl_herc_rendezvous = False
    return

label alt_day5_sl_7dl_vars:
    $ alt_day5_sl_7dl_workout = False
    $ alt_day5_sl_7dl_defend = False
    $ alt_day5_sl_7dl_herc_sick = False
    $ alt_day5_random_val = 0
    $ alt_day5_sl_7dl_hentai_done = False
    $ alt_day5_sl_7dl_olroad = False
    $ alt_day5_sl_7dl_loki_true = False
    return

label alt_day6_sl_7dl_vars:
    $ alt_day6_sl_7dl_workout = False
    $ alt_day6_sl_7dl_hentai_done = False
    $ alt_day6_sl_7dl_forgive = False
    $ alt_day6_sl_7dl_square = False
    $ alt_day6_sl_7dl_elcur = False
    return

label alt_day7_sl_7dl_vars:
    $ alt_day7_sl_7dl_workout = False
    $ alt_day7_sl_7dl_loki_park = False
    $ alt_day7_sl_7dl_story_end = False
    return

label alt_day4_sl_cl_vars:
    $ alt_day4_sl_cl_un_rej = False
    $ alt_day4_sl_cl_tut_iz = False
    $ alt_day4_sl_cl_tut_lf = False
    $ alt_day4_sl_cl_lf_solo = 0
    return

label alt_day5_sl_cl_vars:
    $ alt_day5_sl_cl_cs = False
    $ alt_day5_sl_cl_hentai_done = False
    return

label alt_day6_sl_cl_vars:
    $ alt_day6_sl_cl_arc = ''
    $ alt_day6_sl_cl_hentai_done = False
    $ alt_day6_sl_cl_shirt = False
    $ alt_day6_sl_cl_int_end = ''
    $ alt_day6_sl_cl_good = 0
    $ alt_day6_sl_cl_agreed = False
    return

label alt_day7_sl_cl_vars:
    $ list_sl_cl_map_7dl = []
    $ alt_day7_sl_cl_code = False
    return

label alt_day4_un_7dl_vars:
    $ alt_day4_un_7dl_morning_searching = False
    $ alt_day4_un_7dl_ducks = False
    $ alt_day4_un_7dl_ba_alerted = False
    $ alt_day4_un_7dl_calm = ''
    $ alt_day4_un_7dl_dv_us_explosives = False
    $ alt_day4_un_7dl_hen1 = False
    return

label alt_day5_un_7dl_vars:
    $ alt_day5_un_7dl_washing = ''
    return

label alt_day6_un_7dl_vars:
    $ alt_day7_un_7dl_rnm = 0
    $ alt_day6_un_7dl_good_ussr_check = False
    return

label alt_day7_un_7dl_vars:
    $ alt_day7_un_7dl_rej_end = False
    $ alt_day7_un_7dl_shard_end = False
    return

label alt_day4_un_fz_vars:
    $ alt_day4_un_fz_morning_event = '' # Универсальная переменная. Помощь Лене в стенгазете/Сбегаем с Двачевской/Помогаем Ольге.
    $ alt_day4_un_fz_un_evening = ''    # Универсальная переменная. После чаепития гулял с Леной (walk) или повёл спать (sleep).
    $ alt_day4_un_fz_us_run = False       # Побежал за Ульянкой на ужине.
    $ alt_day4_un_fz_old_road = False     # Побывал на Старой Дороге.
    $ alt_day4_un_fz_selfportrait = False # Леночка рисовала автопортрет.
    return

label alt_day5_un_fz_vars:
    $ alt_day5_un_fz_un_run = False       # На свечке побежал за Леночкой.
    $ alt_day5_un_fz_us_breakfast = False # На завтраке сидели с Ульяной.
    $ alt_day5_un_fz_old_camp = False     # Ходил с Леной в старый лагерь.
    return

label alt_day6_un_fz_vars:
    $ alt_day6_un_fz_map1_quest = ''      # Локация пребывания в первом заходе. 'boatstation'/
    $ alt_day6_un_fz_map2_quest = ''      # Локация пребывания во втором заходе.
    $ alt_day6_un_fz_sl_secret = False    # Узнаём про маленькую и пушистую тайну Слави.
    $ alt_day6_un_fz_answer = 0           # 1 - Возразил. 0 - Ушел.
    $ alt_un_fz_ends = ""                 # Определяем концовку Леночки по ФЗ-ветке (fake_date == 3 идёт отдельно, опционально плохая концовка). 1 - g_end. 2 - n_end. 3 - rj_end. 4 - b_end.
    $ alt_day6_un_fz_hentai = False
    return

label alt_day6_mt_7dl_vars:
    $ alt_day6_mt_7dl_cat = False
    return

label alt_day7_mt_7dl_vars:
    $ alt_day7_mt_7dl_pt = 0
    return

label alt_day6_us_7dl_vars:
    $ alt_day6_us_7dl_mi_friends = 0
    $ alt_day6_us_7dl_sl_friends = 0
    $ alt_day6_us_7dl_un_friends = 0
    $ alt_day6_us_7dl_help = False
    $ alt_day6_us_7dl_px_sl_join = False
    return

label alt_day7_us_7dl_vars:
    $ alt_day7_us_7dl_story_end = False
    $ alt_day7_us_7dl_px_escaped = False
    return

label alt_day4_me_neu_vars:
    $ counter_me_neu_answers = 0                # Счётчик ответов (Одиночка)
    $ counter_mt_7dl = 0                        # Счётчик рута (Ольга-7дл)
    $ counter_us_7dl = 0                        # Счётчик рута (Ульяна-7дл)
    $ counter_us_7dl_px = 0                     # Счётчик рута (Ульяна-Огоньки)
    $ counter_mz_7dl = 0                        # Счётчик встреч с Женей
    $ alt_day4_me_neu_date = ''                 # Компаньон Семена = 'us' (сушил змею), 'mi', 'mt', 'un'
    $ alt_day4_me_neu_transit = ''              # Транзиты 'un_7dl', 'sl_cl'
    $ alt_day4_me_neu_boat = False              # Выбор "Отдохнуть на пристани" на вечерней карте
    $ alt_day4_me_neu_volley = False            # Флаг воллейбола
    $ alt_day4_me_neu_dv_help = False           # Флаг помощи Алисы
    $ alt_day4_me_neu_mi_songs = False          # Флаг готовки песен с Мику
    $ alt_day4_me_neu_mt_diary = False          # Флаг чтения дневника
    $ alt_day4_me_neu_mt_dream = False          # Флаг сна про новеллы
    $ alt_day4_me_neu_mt_volonteer = False      # Флаг сломанного велика
    $ alt_day4_me_neu_us_backpack = False       # Флаг просмотра содержимого рюкзака
    $ alt_day4_me_neu_us_debt = False           # Был в киберкружке
    $ alt_day4_me_neu_mi_resentment = False     # Затроллил Мику
    $ alt_day4_me_neu_mz_newspaper = False      # Был в библиотеке
    $ alt_day4_me_neu_escape = False            # Флаг побега
    $ alt_day4_me_neu_cs_debt = False           # Карточный долг перед Виолой
    $ alt_day4_me_neu_ba_duty = False           # Был на спорт-кружке
    $ alt_day4_me_neu_mi_club = False           # Был в музклубе
    return

label alt_day5_me_neu_vars:
    $ alt_day5_me_neu_candle = 0                # 1 - перед свечкой заходил в домик; 2 - сразу пошёл на свечку; 3 - помогал с игротекой; 4 - присматривал за гвардией
    $ alt_day5_me_neu_candle_escape = False     # Семён свечку не держал, Семён со свечки убежал
    $ alt_day5_me_neu_candle_stay = False       # Семён свечку подержал
    $ alt_day5_me_neu_potato = False            # Таскаем картошку!
    $ alt_day5_me_neu_sl_voyeur = False         # Подглядываем за Славей
    $ alt_day5_me_neu_mt_voyeur = 0             # 0 - остаёмся помогать Мику, 1 - уходим с Ольгой
    $ alt_day5_me_neu_mt_diary = False          # Читаем дневничок Ольги
    $ alt_day5_me_neu_mt_hentai = False         # Мнём вожатую снаружи и внутри
    $ alt_day5_me_neu_us_stores = False         # Наезжаем на Ольгу за то, что лишила Ульяну ужина
    $ alt_day5_me_neu_us_potato = False         # Отдал Ульяне свою картошку
    $ alt_day5_me_neu_map_points = 0            # Очко неудачи на карте. Собери все три
    $ alt_day5_me_neu_campfire_choise = 0       # 1 - сбежал, 2 - искал ответы, 3 - остался у костра
    $ alt_day5_me_neu_cs_debt2 = False          # Дежурит в медпункте
    $ alt_day5_me_neu_clubs_cyber = False       # Прятал карты вместе с кибернетиками
    $ alt_day5_me_neu_nwsppr = False            # Провёл время за книжкой. Возможно пил чай с Женей
    $ alt_day5_me_neu_sport = False             # Гачимучи с Санычем. Мирного решения не будет
    $ alt_day5_me_neu_map_ivent = ''            # medic - бухал на крыше медпункта, boat - навернулся с лодки и залетел на дежурство, dv - мстил рыжему-бесстыжему,
    $ alt_day5_me_neu_mi_help = False           # Вызвался помочь Мику убрать эстраду
    return

label alt_day6_me_neu_vars:
    $ alt_day6_me_neu_dance_invite = ''         # Приглашение на танцы (dv, mt, us, sl, mi, un)
    $ alt_day6_me_neu_mt_help = False           # Помогаем Ольге
    $ alt_day6_me_neu_dv_revenge = False        # Месть Рыжей
    $ alt_day6_me_neu_walk = False              # Решил прогуляться
    $ alt_day6_me_neu_sl_routh = False          # Приглашение Слави # а оно зачем?
    $ alt_day6_me_neu_map_ivent = ''            # Карта - 'music', 'house'
    $ alt_day6_me_neu_mi_club = False           # Был в музклубе утром
    $ alt_day6_me_neu_nwsppr = ''               # был в стенгазете с Ж или без Ж 'mz', 'no_mz'
    $ alt_day6_me_neu_un_escape = False         # Флаг побега
    $ alt_day6_me_neu_clubs_cyber = False       # Kибернетики
    $ alt_day6_me_neu_cyberfire = False         # Дискач с Кибернетиками
    return

label alt_day7_me_neu_vars:
    $ alt_day7_me_neu_ceremony = False          # Награждение у директора
    $ alt_day7_me_neu_story_end = False         # Осколок
    return

label alt_day1_me_7dl_vars:
    return

label alt_day2_me_7dl_vars:
    $ alt_day2_me_7dl_us_talk = False           # Разговор с Ульяной за жизнь
    return

label alt_day3_me_7dl_vars:
    $ alt_day3_me_7dl_dv_wish = False           # Есть желание для Алисы
    return

label alt_day4_me_7dl_vars:
    $ alt_day4_me_7dl_mi_date = False           # Домик на дереве
    return

label alt_day5_me_7dl_vars:
    $ alt_day5_me_7dl_sl_buf = False            # Живой буф
    return

label alt_day6_me_7dl_vars:
    $ alt_day7_me_7dl_all_talks = False         # Все флаги рута Мажора
    $ alt_day6_me_7dl_un_guilty = False         # Не виноватая я (Лена)
    $ alt_day6_me_7dl_mt_found = False          # Точки над ё с Ольгой
    return

label alt_day7_me_7dl_vars:
    $ alt_day7_me_7dl_answers = False           # Пошёл искать ответы
    $ alt_day7_me_7dl_ending = ''               # Флаг концовки
    return

