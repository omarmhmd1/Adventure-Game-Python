# استيراد وحدة الوقت لإنشاء تأخير
import time
# استيراد وحدة عشوائية
import random

# دالة للطباعة ثم النوم
def print_pause(text):
    print(text)
    time.sleep(2)

# -------------------------------------------------------

# دالة تأخذ اختيار اللاعب
def take_the_choice():
    choice = input("اضغط (1 أو 2) : ")
    while choice not in ["1", "2"]:
        choice = input("من فضلك، اضغط (1 أو 2) : ")
    return choice

# دالة تسأل اللاعب إذا كان يريد اللعب مرة أخرى
def ask_play_again():
    try_again = input("هل تريد اللعب مرة أخرى [نعم/لا] : ")
    while try_again.lower() not in ["نعم", "لا"]:
        try_again = input("من فضلك أدخل [نعم/لا] : ")
    return try_again.lower()

# دالة تعرض رسالة نهاية اللعبة
def game_over():
    state = False
    print("شكراً لك، نأمل أنك استمتعت بها.")
    return state

# -------------------------------------------------------

# دالة تبدأ اللعبة
def describe_what_happen():
    # طباعة الترحيب والوصف
    print_pause("\nمرحباً بك في عالم المغامرات - مغامرة الفضاء!\n")
    print_pause("أثناء وجودك في مركز حماية الأرض ضد الكائنات الفضائية")
    print_pause("تلقيت رسالة تقول: أن الفضائيين يخططون")
    print_pause("لاحتلال الأرض عن طريق اختراع مدفع يعمل بالطاقة الليزرية.")
    print_pause("بمجرد أن يكتمل هذا المخطط،")
    print_pause("سيتم توجيه مدفع الليزر")
    print_pause("نحو الأرض، وفي لحظة،")
    print_pause("ستتحول الكوكب إلى رماد")
    print_pause("ثم، قلت لنفسك:\n")
    # عرض الخيارات للاعب
    print_pause("1- هل سأواجههم وأهزمهم؟")
    print_pause("2- هل سأترك المهمة لشخص آخر مع فريقه؟")
    return take_the_choice()

# دالة إذا اختار اللاعب إنقاذ العالم والذهاب لمهاجمة الفضائيين
def choose_saving_world(color_of_first_planet, color_of_second_planet):
    print_pause("هذا صحيح! دعونا نركب مركبة فضائية تتحرك بسرعة كبيرة")
    print_pause("أثناء ذهابك إلى الفضائيين، رأيت كوكبين،")
    print_pause(f"الأول كان {color_of_first_planet},")
    print_pause(f"والآخر كان {color_of_second_planet}, يا إلهي!")
    print_pause("بدأ الفضائيون في مهاجمتنا باستخدام الدفاعات بالليزر.")
    print_pause("ماذا أفعل؟")

# دالة إذا اختار اللاعب ترك المهمة لشخص آخر وفريقه وكانت المحاولات صفر
def decision_staying_tries_zero():
    print_pause("قررت أن تبقى وتترك المهمة لشخص آخر وفريقه")
    print_pause("لكن الشخص الآخر لم ينجح في المهمة!")
    print_pause("يا إلهي! أطلق الفضائيون شعاع ليزر والأرض ستتحول إلى رماد..")
    print_pause("لقد خسرت!")
    return ask_play_again()

# دالة إذا اختار اللاعب ترك المهمة لشخص آخر وفريقه وكانت المحاولات غير صفر
def decision_staying_tries_not_zero():
    print_pause("قررت أن تبقى وتترك المهمة لشخص آخر")
    print_pause("لكن الشخص الآخر لم ينجح في المهمة!")
    print_pause("لكن هناك فرصة أخرى قبل أن يطلق الفضائيون")
    print_pause("شعاع الليزر والأرض ستتحول إلى رماد..")
    print_pause("1- هل سأواجههم وأهزمهم؟")
    print_pause("2- هل سأترك المهمة لشخص آخر مع فريقه؟")
    return take_the_choice()

# -------------------------------------------------------

# دالة إذا اختار اللاعب الهبوط على الكوكب الأول
def landing_on_first_planet(monsters):
    print_pause("قررت الهبوط على الكوكب الأول،")
    print_pause(f"ثم رأيت {monsters} يحرسون مبنى الطاقة")
    print_pause("الذي يزود المدفع الليزري بالطاقة")
    print_pause("ماذا تريد أن تفعل؟")
    print_pause("1- أهاجمهم وأفجر مبنى الطاقة")
    print_pause("2- أعود إلى الفضاء حيث وجدنا المكان الآمن")
    return take_the_choice()

# دالة إذا اختار اللاعب الهبوط على الكوكب الثاني
def landing_on_second_planet(found):
    # تحقق إذا كان اللاعب قد ذهب إلى هناك من قبل أم لا
    if found is False:
        print_pause("هبطت بأمان على الكوكب الثاني،")
        print_pause("ثم خرجت من المركبة الفضائية،")
        print_pause("غاضباً لأنك لم تتمكن من هزيمة الفضائيين و")
        print_pause("صدمت قدمك في التراب بغضب.")
        print_pause("إليك المفاجأة! لقد ضربت عن غير قصد")
        print_pause("رافعة تشغيل جهاز")
        print_pause("وظهر مبنى يحتوي على أكثر من")
        print_pause("100 مركبة فضائية آلية تعمل\nواو!")
        print_pause("1- هل ستشغل تلك المركبات الفضائية الآلية؟")
        print_pause("2- أعود إلى الفضاء حيث وجدنا المكان الآمن")
        return take_the_choice()
    else:
        print_pause("ذهبت إلى الكوكب الثاني")
        print_pause("لم تر أي شيء جديد")
        print_pause("رأيت المبنى الذي يحتوي على أكثر من")
        print_pause("100 مركبة فضائية آلية تعمل")
        print_pause("1- هل ستشغل تلك المركبات الفضائية الآلية؟")
        print_pause("2- أعود إلى الفضاء حيث وجدنا المكان الآمن")
        return take_the_choice()

# ------------------------------------------------------

# دالة إذا اختار اللاعب مهاجمة الفضائيين وتفجير مبنى الطاقة
def attack_and_blow_up(power, monster):
    # تحقق من القوة
    if power >= 70:
        print_pause("لقد توجهت نحوهم وذهبت إلى الكوكب الأول")
        print_pause(f"رأيت {monster} حول مبنى الطاقة")
        print_pause("بدأت الهجوم باستخدام مركباتك الفضائية الآلية، رائع، نحن على وشك هزيمتهم،")
        print_pause("لقد فعلناها، هزمنا العدو")
        print_pause("لكن مدفع الليزر ما زال يحتوي على مصدر للطاقة")
        print_pause("لنذهب إلى الكوكب الذي يحتوي")
        print_pause("على مدفع الليزر الكبير والضخم\n")
        return "success"
    elif 25 < power < 70:
        print_pause("بدأت الهجوم عليهم، لكنهم كانوا أقوى منك")
        print_pause("لذلك لم تتمكن من هزيمتهم وهربت إلى مكان آمن على الكوكب")
        print_pause("1- عد مرة أخرى وهاجمهم")
        print_pause("2- أعود إلى الفضاء حيث وجدنا المكان الآمن")
        return take_the_choice()
    elif power <= 25:
        print_pause("بدأت الهجوم، لا، قوة")
        print_pause("مركبتك الفضائية ضعيفة جداً")
        print_pause("يا إلهي، لقد هزموا مركبتك الفضائية وأمسكوا بك،")
        print_pause("لقد خسرت!")
        return ask_play_again()

# -------------------------------------------------------

# دالة تسأل اللاعب أي كوكب سيذهب إليه
def go_to_first_or_second_planet():
    print_pause("ذهبت إلى منطقة آمنة في الفضاء،")
    print_pause("وما زلت ترى نفس الكواكب")
    print_pause("أي كوكب ستذهب إليه؟")
    print_pause("1- الكوكب الأول")
    print_pause("2- الكوكب الثاني")
    return take_the_choice()

# دالة إذا وصل اللاعب إلى الكوكب الذي يحتوي على المدفع الليزري
def reaches_the_laser_cannon():
    print_pause("رائع، دعنا نذهب للهجوم! أنت والمركبات الفضائية الآلية ذهبتم، لننهزم المدفع")
    print_pause("رأيت المدفع الليزري، كان كبيراً وضخماً")
    print_pause("-لإلحاق الهزيمة بالمدفع، يجب أن تجيب على اللغز-")
    print_pause("قال النظام في المدفع\n")
    print_pause("اللغز: -حلزون يتسلق جداراً عالياً بارتفاع 20 مترًا كل يوم،")
    print_pause("يتسلق مترين أثناء النهار و")
    print_pause("ينزل مترًا في الليل ليتمكن من سحب-\n")
    print_pause("كم من الأيام يحتاج الحلزون ليصل إلى قمة الجدار؟")
    print_pause("1- 20 \n2- 19 \n3- 21 ")
    puzzle_answer = input("اضغط (1 ، 2 أو 3) : ")
    while puzzle_answer not in ["1", "2", "3"]:
        puzzle_answer = input("من فضلك، اضغط (1 ، 2 أو 3) : ")
    return puzzle_answer

# -------------------------------------------------------

# دالة إذا حل اللاعب اللغز
def solve_puzzle():
    print_pause("تمهل، المدفع على وشك الانفجار")
    print_pause("ثلاثة،")
    print_pause("اثنان،")
    print_pause("واحد،")
    print_pause("بوم!")
    print_pause("نعم، فعلناها، أنت منتصر!")

# دالة إذا لم يحل اللاعب اللغز
def not_solve_puzzle():
    print_pause("حل خاطئ، تم إطلاق النار على الأرض")
    print_pause("لا، لقد خسرت!")
    return ask_play_again()

# دالة لزيادة أو تقليل النقاط الإجمالية
def print_total_score(total_score, points):
    total_score += points
    print_pause("\n" + str(points) + " نقاط\n")
    print_pause("إجمالي نقاطك : " + str(total_score))
    return total_score

# -------------------------------------------------------

# الدالة الرئيسية التي تبدأ اللعبة وتستمر في القصة
def main():
    # اختيار عشوائي للون الكوكب الأول والثاني
    color_of_first_planet = random.choice(["أزرق", "أرجواني", "أزرق-أخضر"])
    color_of_second_planet = random.choice(["أحمر", "برتقالي", "بني"])
    # اختيار عشوائي للوحوش
    monsters = random.choice(["فضائيين", "وحوش أرضية", "مدافع ليزر"])

    # حالة اللعبة
    state_of_game = True
    # عدد المحاولات لإنقاذ العالم
    tries = 3
    # قيمة القوة لهزيمة الوحوش
    power = 50
    # إذا تم العثور على المركبات الفضائية الآلية
    found = False
    # إجمالي النقاط
    total_score = 20

    # إذا تم استدعاء دالة (إنقاذ العالم)
    is_choose_saving_world_function_call = False

    # طباعة الترحيب والوصف
    first_choice = describe_what_happen()
    while state_of_game is True:
        # السيناريو 1 - الحرب مع الفضائيين أو ترك المهمة

        # الاختيار الصحيح - الهجوم
        if first_choice == "1":
            # السيناريو 2 - الهبوط على الكوكب الأول أو الثاني
            # عرض الذهاب إلى المركبة الفضائية وزيادة النقاط مرة واحدة
            if is_choose_saving_world_function_call is False:
                # زيادة النقاط
                total_score = print_total_score(total_score, 15)
                choose_saving_world(color_of_first_planet, color_of_second_planet)

                is_choose_saving_world_function_call = True

            # اختيار الهبوط على الكوكب الأول أو الثاني
            land_on_first_or_second = go_to_first_or_second_planet()

            # الاختيار الصحيح - الهبوط على الكوكب الثاني
            if land_on_first_or_second == "2":
                # زيادة النقاط
                total_score = print_total_score(total_score, 10)

                # السيناريو 3 - تشغيل المركبات الفضائية الآلية أو العودة إلى المنطقة الآمنة
                choice_second_planet = landing_on_second_planet(found)
                found = True

                # الاختيار الصحيح - تشغيل المركبات الفضائية الآلية
                if choice_second_planet == "1":
                    # زيادة النقاط
                    total_score = print_total_score(total_score, 20)

                    # السيناريو 4 - الهجوم وحل اللغز أو عدم حله
                    power += 50
                    attack_and_blow_up(power, monsters)
                    # اختيار اللغز
                    puzzle_answer = reaches_the_laser_cannon()

                    # الإجابة الصحيحة على اللغز
                    if puzzle_answer == "2":
                        solve_puzzle()
                        # زيادة النقاط
                        total_score = print_total_score(total_score, 25)

                        # حل اللغز واللعب مرة أخرى - نعم أو لا
                        play_again = ask_play_again()
                        if play_again.lower() == "نعم":
                            first_choice = describe_what_happen()
                        else:
                            state_of_game = game_over()

                    # الإجابة الخاطئة على اللغز
                    else:
                        # تقليل النقاط
                        total_score = print_total_score(total_score, -10)

                        # عدم حل اللغز واللعب مرة أخرى - نعم أو لا
                        play_again = not_solve_puzzle()

                        if play_again.lower() == "نعم":
                            first_choice = describe_what_happen()
                        else:
                            state_of_game = game_over()

                # الاختيار غير الصحيح - العودة إلى المنطقة الآمنة
                else:
                    # تقليل النقاط
                    total_score = print_total_score(total_score, -5)

                    print_pause("لقد عدت إلى المنطقة الآمنة")
                    continue

            else:
                # تقليل النقاط
                total_score = print_total_score(total_score, -15)

                # السيناريو 5
                # الهجوم على الوحوش أو العودة إلى المنطقة الآمنة
                choice_first_planet = landing_on_first_planet(monsters)

                # الاختيار الصحيح - العودة إلى المنطقة الآمنة
                if choice_first_planet == "2":
                    # زيادة النقاط
                    total_score = print_total_score(total_score, 10)

                    print_pause("قررت العودة إلى")
                    print_pause("المنطقة الآمنة")
                    continue

                # الهجوم على الوحوش - الاختيار غير الصحيح
                else:
                    # تقليل النقاط
                    total_score = print_total_score(total_score, -10)

                    power -= random.choice([15, 5, 10])
                    choice_attack = attack_and_blow_up(power, monsters)

                    # الهجوم على الوحوش حتى يختار اللاعب الهجوم عليهم
                    while choice_attack == "1":
                        # تقليل النقاط
                        total_score = print_total_score(total_score, -10)

                        power -= random.choice([15, 5, 10])
                        choice_attack = attack_and_blow_up(power, monsters)

                        # تحقق من القوة وعرض النقاط
                        if power <= 20:
                            print_pause("إجمالي نقاطك : " + str(total_score))

                    # زيادة النقاط
                    total_score = print_total_score(total_score, 5)

                    # المحاولة مرة أخرى
                    if choice_attack.lower() == "نعم":
                        tries = 3
                        total_score = 20
                        found = False
                        is_choose_saving_world_function_call = False
                        first_choice = describe_what_happen()
                    elif choice_attack.lower() == "لا":
                        state_of_game = game_over()

        # الاختيار غير الصحيح - ترك المهمة
        elif first_choice == "2":

            # تقليل النقاط
            total_score = print_total_score(total_score, -5)

            # المحاولة مرة أخرى
            # إذا كانت المحاولات صفر
            if tries == 0:
                try_again = decision_staying_tries_zero()
                if try_again.lower() == "نعم":
                    tries = 3
                    total_score = 20
                    found = False
                    is_choose_saving_world_function_call = False
                    first_choice = describe_what_happen()
                elif try_again.lower() == "لا":
                    state_of_game = game_over()

            # إذا كانت المحاولات أكبر من صفر
            else:
                tries -= 1
                first_choice = decision_staying_tries_not_zero()



if __name__ == "__main__":
    main()
