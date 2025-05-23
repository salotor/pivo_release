﻿label alt_septim_prologue_old:
    $ plthr = u"Септим"
    play music music_7dl["nap_one"] fadein 3
    pause(4)
    $ night_time()
    scene bg ext_entrance_night_clear_closed_7dl
    with dissolve2
    "Я закрываю глаза и снова вижу этот сон."
    "Здесь пахнет полынью и забытыми сожалениями."
    "Когда тебе холодно, ты можешь вернуться сюда и отогреться в тёплой летней ночи."
    "Здесь живёт семья ежей и одна очень красивая девушка, не помнящая, кто она и откуда."
    "Мне всегда так интересно болтать с ней."
    play ambience ambience_camp_center_night fadein 3
    "Она рассказывает самые интересные вещи на свете."
    "Про людей, которые нашли друг друга."
    "Про людей, которые ещё ищут."
    "Как будто есть на свете такое правило, согласно которому вы всё равно однажды встретитесь."
    "Особенно, если рядом с вами места, звучащие одинаково."
    "Это будто бы вешки, проложенные кем-то очень неравнодушным, помогающие вам в поисках."
    "Она называет имя этого неравнодушного, но я никак не могу его запомнить."
    show uv normal with dspr
    dreamgirl "Снова пришёл?"
    "Я молча кивнул."
    dreamgirl "Тебе всегда рады здесь.{w} Хотя ты всё равно снова уйдёшь."
    "Я виновато улыбнулся."
    dreamgirl "Ты нужен здесь."
    am "И там тоже."
    show uv upset with dspr
    dreamgirl "А там — нет. {w}Да и они тебе, если на то пошло."
    am "И что ты предлагаешь? {w}Остаться здесь?"
    dreamgirl "Нет. Пошли лучше со мной?"
    am "Я не могу, там люди, которые мне дороги."
    show uv smile with dspr
    dreamgirl "Дороги?"
    am "Да, ближе их у меня никого…"
    with fade
    "Декорации за спиной девушки сместились, вспыхнул яркий свет, а когда я проморгался…"
    show cg d1_uv_bus_7dl
    pause(.1)
    scene cg d5_alisa_7dl
    show blackout_exh3
    with flash
    "Я поперхнулся вдохом."
    "Из ниоткуда на меня улыбались глаза детской мечты."
    "Девочки с неземным взглядом, девочки, которая улыбалась так, как никто и никогда не мог."
    "Алисы Селезнёвой."
    dreamgirl "А я?.. Дорога?"
    "Не той, постаревшей заживо Наташи Гусевой, променявшей будущее на биологию, а логично и естественно развивавшейся звёздочки, что в детстве общалась с крокодилами и охотилась на космопиратов."
    "Но сейчас отличие было разительным."
    "Потому что улыбка была другая. {w}Не для каких-то абстрактных кинозрителей."
    "И глаза встретились с глазами — так как это никогда не удавалось мне ни в «алисиане», ни в «лиловом шаре»…"
    "И не было это выдумками или наведённой иллюзией, я-то знаю своё подсознание: оно вечно хромает в деталях."
    "Нет, это было всё то же наивно-детское платье авторства футуристов восьмидесятых, но пошитое уже под фигуру взрослой девушки, всё тот же бездонный прогляд с искорками."
    scene
    $ renpy.show("cg d5_alisa_7dl", what = Dawn("cg d5_alisa_7dl"))
    show blackout_exh3
    with diam
    "Не-Алиса сделала шаг навстречу, улыбнулась ещё раз и стрельнула глазами."
    "Я поперхнулся ещё раз."
    "Рассмеявшись, она обняла меня и прижалась изо всех сил."
    am "Так же нельзя!.."
    dreamgirl "Кто запретил?"
    "Её тело немного подрагивало, но она не отстранялась, видимо, не желая отпускать меня раньше времени."
    "А потом провела запрещённый приём:"
    "Немного покраснев, она прикрыла глаза и протянула знакомым таким и до безумия реальным голосом:"
    dreamgirl "Сеееень?.."
    "Она была настоящая."
    "Я почувстовал, будто проваливаюсь в какую-то бездонную яму, с тёмными трепещущими краями, состоящую из единого восторга."
    "А уж что чувствовало тело…"
    $ prolog_time()
    stop ambience fadeout 6
    scene anim prolog_3
    with flash
    play sound sfx_7dl["wakeup"] fadein 0
    "Я резко вскочил в кровати, весь покрытый липкой ледяной испариной."
    "Сердце колотилось в горле как оглашенное, а руки ощутимо дрожали."
    scene bg int_semen_room_clean_7dl
    with fade
    "Ноги подкашивало, пока я пытался встать с дивана, пока прошёл кажущееся бесконечным расстояние в несколько метров и, колотя зубами о стеклянный край чашки, пил воду."
    "Потом долго пытался успокоить запаленное дыхание."
    me "Что за дела?.."
    "Я своими руками вручил несносной девчонке самые главные козыри, самые важные ключи от себя."
    "И от того страшно было ложиться спать."
    "Я знал, что стоит лишь мне смежить веки, изъявить желание…"
    "Только вот нечестно это было, совсем нечестно."
    scene anim prologue_monitor_1
    with dissolve
    "Всё это замечательное место, куда я убегал от проблем и вымороженной отстранённости окружающих…"
    "Как сквозь новокаиновую блокаду, как сквозь вату."
    "Лишь теперь я был по-настоящему выведен из равновесия."
    "Где-то в дальних уголках папочки с загрузками был и старый добрый DVD-rip с сериалом из моего детства."
    "Наушники, чай на столе."
    "Play."
    "Моё крохотное место, куда никому не было хода, оказалось просто летней ночью возле каких-то ворот."
    "Просто семейством ёжиков, ворующих из туеска ягоды."
    "Просто приходящей в гости девушкой без прошлого."
    stop music fadeout 6
    "А вот так и не ставшая двадцатилетней мечта детства…"
    scene bg ext_khruschevka_sunset_7dl
    play ambience ambience_7dl["night_city"] fadein 6
    play music music_7dl["fyrsta"] fadein 3
    "Я успел посмотреть три серии, так и не притронувшись к чаю."
    "Я смотрел мимо экрана, наблюдая не столько за творящимся действом, сколько за изменениями внутри себя."
    "Я задавал себе один простой вопрос:"
    am "А своей ли жизнью я живу?"
    "И не находил ответа."
    "Потому что не от хорошей же жизни человек создаёт такое вот прибежище?"
    "Потом зазвонил будильник, и я, мгновенно собравшись, выскочил на улицу."
    "Мне жутко было находиться дома."
    "Бытует мнение — мол, происходящее снаружи или люди, находящиеся снаружи, могут причинить вам боль и страдания."
    "Что чем ближе вы человека подпускаете, тем больше боли он может вам причинить."
    "Вот только это не так."
    "В своих неудачах и боли вы виноваты только сами."
    "Это вы, никто другой, наделяете окружение такой властью."
    "И кто теперь виноват?"
    "Кто?"
    with fade
    "Уж точно не Рандом."
    "И не родители, которые не спросили вашего согласия — стоит ли являться именно вам на свет."
    "И, разумеется, не Голливуд, воспитывающий в вас любовь и надежду на лучшее, навязывающий какие-то глупые стереотипы."
    "В этом виноваты только вы сами."
    "Вот и всё."
    "Да, быть может, немного переоценённые ожидания."
    "Идеальное поведение человека с пониженным болевым порогом — это ночь, пьяные посиделки накоротке с монитором да пустые сообщение ВК самому себе."
    "Никого никогда никуда не пускать."
    "Так проще. {w}Безопаснее."
    scene cg d6_mi_grass_7dl
    show prologue_dream
    with fade
    "Этому учит и детство. Безоблачное и яркое?"
    "Как бы не так."
    "Нет, если бы оно было, это детство…"
    "Но нет."
    "Одно время у меня была даже теория о том, что дети совершенно иначе воспринимают мир."
    "Они видят его ярко-вымытым, обладают особым зрением, позволяющим в упор не видеть припорошенности пылью, игнорировать патину времени."
    "Дети живут в мире, раскрашенном самыми лучшими карандашами."
    scene bg ext_khruschevka_sunset_7dl
    with dissolve
    "Но что, если вы свой яркий период размотали на попытки просто выжить?"
    "Что, если людей, способных воспитать в вас {i}причину{/i}, попросту никогда не было?"
    "Вы понимаете, что это неправильно, но ничего не можете с этим сделать."
    "Вам срочно необходимо взрослеть, чтобы жить."
    "Даже если кто-то варит вам манную кашу и проверяет отметки в школе, но никогда не спрашивает, о чём вы думаете, что чувствуете."
    "Вы разделены LCD-экраном, временем, недостатком сил."
    "А может, «вас» — как таковых — и не было никогда?"
    "Потому и самые яркие детские воспоминания — это бег наперегонки по кучам листьев, поездки на «колбасе» и броски капитошек вниз с крыши четырнадцатиэтажки."
    "И, конечно, долгие зарубы в компьютерных клубах."
    "Не счастливый смех, объятья и ощущение причастности к чему-то большему, чем сам — а отращивание клыков и бронированной шкуры."
    "Самое странное в этих воспоминаниях — это неспособность вспомнить лица тех, кто был рядом."
    "Лица друзей."
    "Людей, в которых можно было бы поверить."
    "Людей, которыми можно было бы гордиться."
    scene bg ext_khruschevka_day_7dl
    with dissolve
    "Только бесконечный пасмурный день в глазах — отражением бесконечного пасмурного неба."
    "Когда приходит время расставаться, вы делаете это без сожалений."
    "Потому что неродные и были."
    "Я говорю только о себе, но сколько историй я слышал — как под копирку."
    "Люди, живущие чужими годами, чувствующие себя везде не на месте."
    "С убийственной самоиронией называющие себя «человек-косяк», потому что ни одно дело не способны сделать самостоятельно, не напортачив в итоге."
    "Им страшно, и мне — тоже."
    "Потому что я не могу совершить решительный поступок: знаю, чем всё закончится."
    "Все приятели канули в никуда, когда я сделал свой первый взрослый выбор — основываясь единственно на совести и голой логике."
    "Я не мог подвести одного человека, который для меня что-то значил."
    "Себя."
    "Тем удивительнее, что этот выбор вёл к человеку, ставшему моей опорой. {w}Моей семьёй."
    "Путь к запоздалому детству, которого у меня никогда не было."
    "Только вот поезд туда не ходит, а пробирающихся окольными тропами уничтожают пограничники."
    "Так и случилось со мной."
    scene bg ext_khruschevka_rain_7dl
    with fade
    "У меня всегда хорошо получалось шевелить мышкой, но не очень — шевелить мозгами."
    "Особенно в общении с людьми."
    "Потому простреливать головы из рейлгана всегда получалось как-то лучше, чем доносить в головы собственные мысли."
    "Потому я и отказался от затеи кому-то что-то донести."
    "Шевелил себе мышкой и имел с этого небольшую копеечку."
    "А потом влюбился, и…"
    "Я никогда не думал, что история рывка в неизвестность закончится вот так:"
    voice "Тебе не двадцать лет. {w}Что мне надо будет отвечать дочери, когда она спрашивает, кем работает её папа? В игрушки играет?"
    "Играет."
    with fade
    "Видимо, тогда всё и покатилось под откос."
    "У меня есть некоторое образование, хотя, конечно, не чета моей ненаглядной."
    "Я неплохо умею делать мебель."
    "Вот только её изготовление требуют совсем других навыков, а не молниеносной реакции и точности с контролем."
    "Пришлось выбирать — или дело всей жизни, или…"
    "Деньги."
    "Которых у меня на тот момент было мало."
    "Так что вместо тренировки к отборочным я отправился на собеседование."
    "И вышел на работу."
    "Здесь всё началось."
    stop music fadeout 5
    with fade
    play music music_7dl["wonderful_faraway"] fadein 3
    "Первая ласточка началась во время беременности."
    "Проголливудченный насквозь мальчик ждал, что всё будет как в фильмах: девушка сообщает, что скоро их станет больше, муж захлёбывается от счастья, подхватывает на руки и кружит её по комнате."
    "Это же логично, правда? {w}Люди имеют право на счастье, право знать, что всё будет хорошо."
    "Мальчик так долго ждал этот момент, так предвкушал…"
    "Чтобы однажды утром, проснувшись, открыть блог супруги и прочитать там какую-то гадость."
    "И только таким, максимально извращённым способом узнать, что стал отцом."
    "Не мог спросить? Не мог.{w} Хотел."
    "Но, уставший, бежал с работы, остановившись лишь у ларька, чтобы купить бесценной своей её любимую шоколадку."
    "Уснул в душе, а оттуда перебрался уже только когда в двери забарабанили."
    "Плохой я, плохой."
    with fade
    "Впрочем, после предложения руки и сердца через смс это даже ожидаемо."
    "Я никак не мог набраться смелости, чтобы спросить вслух, потому и отправил сообщение."
    "Дурак, конечно."
    "Но тенденция складывается… если однажды станет совсем кисло — она и разведётся со мной через вайбер или скайп."
    "По-детски."
    "Так что не был я ребёнком, и взрослым тоже не стал."
    "Отняли у меня это право."
    with fade
    "И то и дело попрекают этим."
    "Мол, ты не мужик, не глава семьи."
    "Именно так."
    "Я тридцатилетний мальчик, который не сумел найти своего Тайлера и вовремя получить по морде."
    "А мне хочется просто лечь и всё забыть."
    "Просто отключиться и больше никогда не приходить в себя."
    with fade
    "Чтобы не было больше никогда ни хрущёвки этой, не безысходности, которой сопровождалось каждое пробуждение."
    "Не было никогда мелкой, спящей у меня на груди."
    "Не было никогда…"
    with fade
    "В моём возрасте очень просто сдать позиции, если перестать тренироваться."
    "Уж я-то это знаю."
    "Так что когда на одном из матчей я внезапно оказался в середине доски почёта, не удивился даже."
    "Я работал, а не шёл к мечте."
    "Ведь за мечту деньги не платят."
    scene bg int_excalator_7dl
    with dissolve
    "В кармане зажужжал телефон, я включил экран."
    "«На следующую неделю ничего не планируй! У нас первенство по СНГ на носу, понял? Так что плюй на всё и собирайся в Москву!»"
    th "Плюй на всё…"
    th "Да как?"
    scene bg int_excalator_7dl
    with dissolve
    th "Дома четыре бабы — в гости заглянула мама и сестра моей благоверной."
    th "И я вот так уйду?"
    th "А на работе вал заказов, и деньги, вроде, не самые большие, но стабильные…"
    "Я задумался…"
    stop music fadeout 6
    scene anim intro_3
    with dissolve
    "Теперь пустые пальцы печатают трезвый текст — как записку, что оставляют самоубийцы перед прыжком в окно."
    "{i}Я сделал свой выбор несколько месяцев назад, а значит, ни о чём не жалею.{/i}"
    "Только вот моя записка не предсмертная."
    "А преджизненная."
    "{i}Прощай, всё, что составляло меня как личность, прощай, всё, что мне недодали.{/i}"
    "{i}Я никого ни в чём не обвиняю.{/i}"
    "{i}Просто надеялось на то, что всё сложится как-то иначе?..{/i}"
    "{i}Я не знаю.{/i}"
    "{i}Я отказался от сборов, перевёл былой смысл в глупое хобби, которое тоже не продлится долго.{/i}"
    "{i}Тем более, на работе так устаёшь, какие уж тут стрелялки.{/i}"
    "Теперь я только ходил по сайтам, где раньше мог видеть своё имя, смотрел за соревнованиями — но уже со скамьи болельщиков."
    "{i}Я чувствую, как живу не своей жизнью, доставшейся мне обносками с плеча какого-то неудачника, но ничего с этим сделать не могу.{/i}"
    "{i}Да вижу глупые сны про лето.{/i}"
    th "Единственная моя отрада."
    "{i}Просто в ещё одних глазах потухла искра, ещё один заживо стареющий человек.{/i}"
    "{i}Но я всё понимаю. {w}Нужны деньги.{/i}"
    "{i}А они не упадут просто так к ногам.{/i}"
    scene anim intro_5
    with fade
    th "Надо работать…"
    scene anim intro_6
    with fade
    th "Работать…"
    scene anim intro_6
    with fade
    play sound sfx_intro_bus_stop_sigh
    "{i}Я готов подставляться, кости ломать, постоянно терпеть…{/i}"
    "Ни разу ни с кем не приходилось ругаться по вайберу?"
    "Впечатление — то ещё."
    "И, как любое текстовое общение, требует отвечать абсолютно на каждую реплику, какой бы вздорной она ни была."
    "Я. Уделяю. Мало. Времени. Семье."
    "{i}Хочется забиться в угол и сидеть там, пока всё не пройдёт.{/i}"
    "{i}Я не знаю других способов решения проблем.{/i}"
    "{i}А на улице снова зима.{/i}"
    with fade
    "Хотя будь на моём месте «настоящий мужик», каким кличут его бабы из моей семьи, он бы что-нибудь сделал."
    "Например, тем же вечером, в чём однажды появился — осенних ботинках и сером «пилоте» — вышел из дома и набрал телефон менеджера."
    "Попросил бы одолжить денег на билет до столицы и пригреть на время."
    "Тем более, я видел: новая-старая дисциплина привлекает всё новых и новых инвесторов, глупые стрелялки из детства превращается в хорошо оплачиваемое шоу."
    "Особенно, для тех, что однажды уже гремели и купались в лучах славы."
    "Им же нужен такой, да?"
    scene bg int_semen_room_7dl
    with dissolve
    "Дома меня встретили ледяным презрительным молчанием."
    "Не впервой, старый способ воспитания."
    "Игнорировать, молчать и презирать."
    th "Рандом всеблагой, как же меня всё это достало…"
    "Я в молчании съел холодный ужин, помыл за собой тарелки и, отправился за компьютер."
    "И вот я здесь."
    scene anim prologue_monitor_4
    with fade
    "{i}Даже если у тебя не осталось ничего, ты можешь сбежать в пустоту.{/i}"
    "{i}А я сбегаю… в жизнь.{/i}"
    "{i}Ту, что мне положена.{/i}"
    "Я сохранил текст на рабочем столе, запаролил компьютер и отправился на боковую."
    "У меня всё ещё остались мои сны."
    $ night_time()
    play ambience ambience_camp_center_night fadein 3
    stop music fadeout 3
    "Потому я улыбнулся, когда серый потолок моей квартиры сменился старыми знакомыми."
    "Стальными воротами, выкрашенными шаровой краской."
    play music music_7dl["too_quiet"] fadein 3
    "И совёнком у притолоки."
    $ renpy.show("bg ext_entrance_night_clear_closed_7dl", what = D3_intro("bg ext_entrance_night_clear_closed_7dl"))
    show owl :
        pos (931, 88)
    show prologue_dream
    with fdiam
    "Лето."
    "Только моё, куда нет пути ни моим старым приятелям, ни моим новым женщинам."
    "Только моё место."
    "Ворота всегда были закрыты, но пятачок перед ними был в моём полном распоряжении."
    "Я ложился в траву и смотрел в ночное небо, напитываясь спокойствием и умиротворением."
    "Я никому не был нужен, и никто не был нужен мне."
    "Зато…"
    scene bg ext_entrance_night_clear_closed_7dl
    show blackout_exh3
    show uvao_d1 at left
    show prologue_dream
    dreamgirl "Привет."
    am "Привет. {w}Только без этих твоих выкрутасов, ладно?"
    "Девушка улыбнулась, по-кошачьи потягиваясь."
    dreamgirl "Ты сегодня странный."
    am "Человек вообще вещь в себе."
    dreamgirl "Обычно ты болтаешь. {w}Спрашиваешь. Разглядываешь меня."
    am "Знаешь… {w}Я передумал."
    dreamgirl "Снова превратиться?"
    am "Нет. Я решил… Я пойду с тобой."
    dreamgirl "Правда? Сейчас?"
    "Я улыбнулся и кивнул."
    dreamgirl "Ну, наконец-то!"
    play sound sfx_7dl["gate_open"]
    pause(1)
    scene bg ext_entrance_night_clear_7dl
    show uvao_d1 at left
    with dissolve2
    dreamgirl "Тогда пошли."
    "Приключение длиной в жизнь начинается с первого шага."
    "Надо просто сделать этот шаг."
    "Вернуться на самое начало и, воспользовавшись всем моим опытом и знаниями…"
    "Пере-понять всё с самого начала."
    stop music fadeout 2
    stop ambience fadeout 2
    pause(1)
    $ sdl_stories_return()