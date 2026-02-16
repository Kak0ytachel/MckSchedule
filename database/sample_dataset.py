from database.db import Database
from datetime import datetime
from database.db_dataclasses import Group, init_db, Teacher, Classroom, Subject, Lesson, Semester


def load_sample_data(db: Database):
    db._drop_database()
    db._init_database()
    init_db(db)
    # sem1 = 1
    sem1 = Semester("Winter", datetime(2025, 10, 1), datetime(2026, 2, 10), "schedule-semester-winter")
    # sem2 = 2
    sem2 = Semester("Summer", datetime(2026, 2, 16), datetime(2026, 7, 30), "schedule-semester-summer")

    group_1n = Group("1N")
    group_2n = Group("2N")
    group_3n = Group("3N")
    group_4n = Group("4N")
    group_5n = Group("5N")
    group_6n = Group("6N")
    group_1s = Group("1S")
    group_2s = Group("2S")
    group_3s = Group("3S")
    group_4s = Group("4S")
    group_5s = Group("5S")

    subgroup_1n_inz = group_1n.make_subgroup("inz", "1N / inz")
    subgroup_1n_art = group_1n.make_subgroup("art", "1N / art")
    subgroup_1n_arch = group_1n.make_subgroup("arch", "1N / arch")
    subgroup_1n_ekon = group_1n.make_subgroup("ekon", "1N / ekon")

    subgroup_2n_inz = group_2n.make_subgroup("inz", "2N / inz")
    subgroup_2n_art = group_2n.make_subgroup("art", "2N / art")
    subgroup_2n_ekon = group_2n.make_subgroup("ekon", "2N / ekon")

    subgroup_3n_arch = group_3n.make_subgroup("arch", "3N / arch")
    subgroup_3n_ekon = group_3n.make_subgroup("ekon", "3N / ekon")
    subgroup_3n_art = group_3n.make_subgroup("art", "3N / art")

    subgroup_4n_inz = group_4n.make_subgroup("inz", "4N / inz")
    subgroup_4n_ekon = group_4n.make_subgroup("ekon", "4N / ekon")

    subgroup_5n_art = group_5n.make_subgroup("art", "5N / art")
    subgroup_5n_ekon = group_5n.make_subgroup("ekon", "5N / ekon")

    subgroup_6n_inz = group_6n.make_subgroup("inz", "6N / inz")
    subgroup_6n_arch = group_6n.make_subgroup( "arch", "6N / arch")

    subgroup_1s_inz = group_1s.make_subgroup("inz", "1S / inz")
    subgroup_1s_ekon = group_1s.make_subgroup("ekon", "1S / ekon")

    subgroup_2s_inz = group_2s.make_subgroup("inz", "2S / inz")
    subgroup_2s_ekon = group_2s.make_subgroup("ekon", "2S / ekon")

    subgroup_3s_inz = group_3s.make_subgroup("inz", "3S / inz")

    subgroup_4s_ekon = group_4s.make_subgroup("ekon", "4S / ekon")
    subgroup_4s_art = group_4s.make_subgroup("art", "4S / art")
    subgroup_4s_arch = group_4s.make_subgroup("arch", "4S / arch")

    subgroup_5s_ekon = group_5s.make_subgroup("ekon", "5S / ekon")
    subgroup_5s_art = group_5s.make_subgroup("art", "5S / art")
    subgroup_5s_inz = group_5s.make_subgroup("inz", "5S / inz")

    classroom_warszawa = Classroom("warszawa", "Warszawa (07)")
    classroom_wroclaw = Classroom("wroclaw", "Wrocław (08)")
    classroom_krakow = Classroom("krakow", "Kraków (09)")
    classroom_lodz = Classroom("lodz", "Łódź (05)")
    classroom_gdansk = Classroom("gdansk", "Gdańsk (04)")
    classroom_poznan = Classroom("poznan", "Poznań (06)")
    classroom_seminar = Classroom("seminar", "Sała seminaryjna (12)")
    classroom_komp = Classroom("komput", "Sała komputerowa (10)")
    classroom_konfer = Classroom("konfer", "Sała konferencyjna (13)")
    classroom_proj = Classroom("proj", "Sała projektowa (11)")

    teacher_kgr = Teacher("KGR", "Kinga Górecka-Rokita")
    teacher_jk = Teacher("JK", "Justyna Krztoń")
    teacher_eg = Teacher("EG", "Edyta Gałat")
    teacher_jpm = Teacher("JPM", "Joanna Piera-Mitka")
    teacher_tj = Teacher("TJ", "Tomasz Jeleński")

    teacher_ika = Teacher("IKA", "Izabela Kugiel-Abuhasna")
    teacher_wo = Teacher("WO", "Witold Obloza")
    teacher_md = Teacher("MD", "Małgorzata Duraj")
    teacher_an = Teacher("AN", "Artur Niewiarowski")
    teacher_wg = Teacher("WG", "WG (?)")
    teacher_sr = Teacher("SR", "SR (?)")
    teacher_mr = Teacher("MR", "Michalina Rittner")
    teacher_ap = Teacher("AP", "AP (?)")
    teacher_mb = Teacher("MB", "MB (?)")
    teacher_wzt = Teacher("WZT", "WZT (?)")
    teacher_ak = Teacher("AK", "AK (?)")

    teacher_kst = Teacher("KST", "KSt (?)")
    teacher_msz = Teacher("MSZ", "MSZ (?)")

    teacher_ab = Teacher("AB", "AB (?)") # matematyka
    teacher_abar = Teacher("ABAR", "A.Bar. (?)")
    teacher_im = Teacher("IM", "IM (?)")
    teacher_jd = Teacher("JD", "JD (?)")
    teacher_abuk = Teacher("ABUK", "A.Buk. (?)")
    teacher_rb = Teacher("RB", "RB (?)")
    teacher_tk = Teacher("TK", "TK (?)")

    subject_mat_i = Subject("mat-i", "Matematyka inz.")
    subject_fiz = Subject("fiz", "Fizyka inz.")
    subject_inf_i = Subject("inf-i", "Informatyka inz.")
    subject_jn = Subject("jn", "Język naukowy")

    subject_kscz = Subject("kscz", "KSCz")
    subject_gp = Subject("gp", "GP")
    subject_wop = Subject("wop", "WOP")
    subject_konw = Subject("konw", "Konwersatorium")
    subject_dkf = Subject("dkf", "DKF")

    subject_mat_ea = Subject("mat-ea", "Matematyka ekon./arch.")
    subject_fp = Subject("fp", "Film polski")
    subject_sa = Subject("sa", "Słownictwo architektoniczne")
    subject_ha = Subject("ha", "Historia architektury")
    subject_rarch = Subject("rarch", "Rysunek architektoniczny")

    subject_se = Subject("se", "Słownictwo ekonomiczne")
    subject_hs = Subject("hs", "Historia sztuki")
    subject_hk = Subject("hk", "Historia kultury")
    subject_inf_e = Subject("inf-e", "Informatyka ekonomiczna")
    subject_rart = Subject("rart", "Rysunek artystyczny")
    subject_wok = Subject("wok", "Wiedza o kulturze")
    subject_zw = Subject("zw", "Zajęcia warsztatowe")
    subject_ksczwop = Subject("ksczwop", "KSCZWOP")

    subject_pp = Subject("pp", "Podstawy projektowania")
    subject_gehg = Subject("gehg", "Geogragia ekonomiczna / Historia gospodarcza")
    subject_pr = Subject("pr", "Prawo")
    subject_saw = Subject("saw", "Sztuki audiowizualne")
    subject_ch = Subject("ch", "Chemia")
    subject_si = Subject("si", "Słownictwo inżynierskie")
    subject_inf = Subject("inf", "Informatyka")
    subject_bud = Subject("bud", "Budownictwo")
    subject_gi = Subject("gi", "Grafika inżynierska")
    subject_wil = Subject("wil", "WIL")
    subject_tn = Subject("tn", "Tenneessee")
    subject_inf_ech = Subject("inf-ech", "Informatka ekon./chem.")
    # db.subjects_table.add_subject("")

    i = db.lessons_table.add_lesson("mat-i", classroom_warszawa, "WO", 1,
                                      9, 50, 11, 20, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("dkf", classroom_gdansk, "TJ", 1, 18, 0, 20, 15, sem1)
    db.group_lessons_table.add_group_lesson(group_6n, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("wop", classroom_gdansk, "EG", 2, 8, 0, 9, 30, sem1)
    db.group_lessons_table.add_group_lesson(group_6n, i)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_krakow, "KGR", 2,
                                      9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("jn", classroom_lodz, "IKA", 2, 11, 40, 13, 10, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("fiz", classroom_lodz, "MD", 2, 15, 15, 16, 45, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("mat-i", classroom_krakow, "WO", 2, 17, 00, 18, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 3, 8, 15, 9, 45, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("konw", classroom_poznan, "JPM", 3, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "JK", 4, 8, 00, 9, 30, sem1)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 4, 10, 0, 11, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "JK", 4, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_lodz, "KGR", 4, 13, 30, 15, 0, sem1)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("fiz", classroom_lodz, "MD", 4, 17, 00, 18, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_lodz, "JK", 5, 8, 0, 9, 30, sem1)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_krakow, "KGR", 5, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("fp", classroom_gdansk, "TJ", 1, 15, 15, 17, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)
    db.group_lessons_table.add_group_lesson(group_1s, i)
    db.group_lessons_table.add_group_lesson(group_2s, i)

    i = db.lessons_table.add_lesson("fp", classroom_gdansk, "TJ", 3, 15, 15, 17, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i)  # TODO: fix conflicts
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i)  # wtf duplicats
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)

    i = db.lessons_table.add_lesson("fp", classroom_gdansk, "TJ", 3, 18, 0, 20, 15, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_art, i)  # duplicates
    # db.group_lessons_table.add_group_lesson(group_5n, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_ekon, i)
    db.group_lessons_table.add_group_lesson(group_5s, i)

    i = db.lessons_table.add_lesson("ha", classroom_lodz, "EG", 1, 9, 50, 11, 20, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_arch, i)

    i = db.lessons_table.add_lesson("sa", classroom_lodz, "EG", 1, 11, 40, 13, 10, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_arch, i)
    # db.lessons_table.add_lesson("math", 1, "123456", 1, 23, 59, 23, 59)

    i = db.lessons_table.add_lesson("rarch", classroom_konfer, "WG", 2, 15, 15, 18, 15, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_arch, i)

    i = db.lessons_table.add_lesson("mat-ea", classroom_krakow, "WO", 4, 13, 30, 15, 0, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    # db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_???) #TODO add
    db.group_lessons_table.add_group_lesson(subgroup_3n_ekon, i)

    i = db.lessons_table.add_lesson("mat-ea", classroom_krakow, "WO", 4, 15, 15, 16, 45, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)

    i = db.lessons_table.add_lesson("mat-ea", classroom_konfer, "WO", 1, 8, 0, 9, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)

    i = db.lessons_table.add_lesson("kscz", classroom_warszawa, "SR", 1, 8, 0, 9, 30, sem1)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("gp", classroom_wroclaw, "JPM", 1, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("wop", classroom_krakow, "EG", 1, 13, 30, 15, 0, sem1)
    db.group_lessons_table.add_group_lesson(group_2n, i)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("se", classroom_lodz, "IKA", 2, 8, 0, 9, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)

    i = db.lessons_table.add_lesson("gp", classroom_konfer, "JPM", 2, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("mat-ea", classroom_krakow, "WO", 2, 13, 30, 15, 0, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("hs", classroom_krakow, "MR", 3, 8, 0, 9, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)

    i = db.lessons_table.add_lesson("konw", classroom_warszawa, "KGR", 3, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("hk", classroom_gdansk, "MR", 3, 11, 40, 13, 10, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)

    i = db.lessons_table.add_lesson("inf-e", classroom_komp, "AP", 3, 17, 0, 18, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)

    i = db.lessons_table.add_lesson("wok", classroom_lodz, "KGR", 4, 8, 0, 9, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)

    i = db.lessons_table.add_lesson("se", classroom_gdansk, "IKA", 4, 8, 0, 9, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)

    i = db.lessons_table.add_lesson("kscz", classroom_poznan, "SR", 4, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("mat-ea", classroom_krakow, "WO", 4, 13, 30, 15, 0, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)

    i = db.lessons_table.add_lesson("rart", classroom_konfer, "MB", 4, 13, 30, 16, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i)

    i = db.lessons_table.add_lesson("kscz", classroom_proj, "SR", 5, 8, 0, 9, 30, sem1)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("gp", classroom_warszawa, "JPM", 5, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_gdansk, "JK", 1, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("mat-i", classroom_konfer, "WO", 1, 11, 40, 13, 10, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)

    i = db.lessons_table.add_lesson("wop", classroom_gdansk, "EG", 2, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("konw", classroom_gdansk, "EG", 2, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_warszawa, "JK", 2, 13, 30, 15, 0, sem1)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("mat-i", classroom_krakow, "WO", 2, 15, 15, 16, 45, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)

    i = db.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 3, 10, 0 , 11, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_proj, "KGR", 3, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("fiz", classroom_konfer, "MD", 3, 15, 15, 16, 45, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)

    i = db.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 4, 8, 15, 9, 45, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_lodz, "KGR", 4, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("jn", classroom_komp, "IKA", 4, 11, 40, 13, 10, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_inz, i)

    i = db.lessons_table.add_lesson("fiz", classroom_lodz, "MD", 4, 15, 15, 16, 45, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "KGR", 5, 8, 0, 9, 30, sem1)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_lodz, "JK", 5, 13, 30, 15, 0, sem1)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("hk", classroom_krakow, "MR", 1, 8, 0, 9, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_art, i)

    i = db.lessons_table.add_lesson("gp", classroom_proj, "KGR", 2, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("wok", classroom_lodz, "KGR", 3, 8, 0, 9, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_art, i)

    i = db.lessons_table.add_lesson("se", classroom_gdansk, "IKA", 3, 8, 0, 9, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_ekon, i)

    i = db.lessons_table.add_lesson("kscz", classroom_lodz, "IKA", 3, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_lodz, "IKA", 3, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("inf-e", classroom_komp, "AP", 3, 15, 15, 16, 45, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_ekon, i)

    i = db.lessons_table.add_lesson("hs", classroom_proj, "MR", 4, 8, 0, 9, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_art, i)

    i = db.lessons_table.add_lesson("konw", classroom_konfer, "MR", 4, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("gp", classroom_lodz, "KGR", 4, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("se", classroom_gdansk, "IKA", 5, 8, 0, 9, 30, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_ekon, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "KGR", 5, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_gdansk, "IKA", 5, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_gdansk, "JK", 1, 8, 0, 9, 30, sem1)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("zw", classroom_poznan, "WZT", 1, 9, 50, 11, 20, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)


    i = db.lessons_table.add_lesson("zw", classroom_poznan, "WZT", 1, 11, 40, 13, 10, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)

    i = db.lessons_table.add_lesson("konw", classroom_komp, "MR", 2, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("gp", classroom_komp, "MR", 2, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "MR", 3, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_krakow, "JK", 4, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("gp", classroom_warszawa, "MR", 4, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("rart", classroom_konfer, "MB", 4, 16, 45, 19, 45, sem1)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_art, i)

    i = db.lessons_table.add_lesson("kscz", classroom_lodz, "JK", 5, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("gp", classroom_wroclaw, "JPM", 1, 13, 30, 15, 0, sem1)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    i = db.lessons_table.add_lesson("ksczwop", classroom_krakow, "AK", 2, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    i = db.lessons_table.add_lesson("ksczwop", classroom_krakow, "AK", 2, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    i = db.lessons_table.add_lesson("ksczwop", classroom_wroclaw, "AK", 3, 9, 50, 11, 20, sem1)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    i = db.lessons_table.add_lesson("ksczwop", classroom_wroclaw, "AK", 3, 11, 40, 13, 10, sem1)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    i = db.lessons_table.add_lesson("gp", classroom_lodz, "JPM", 3, 13, 30, 15, 0, sem1)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    #
    # sem2
    #

    i = db.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 1, 8, 15, 9, 45, sem2)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("mat-i", classroom_konfer, "WO", 1, 11, 40, 13, 10, sem2)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("mat-i", classroom_konfer, "WO", 2, 9, 50, 13, 20, sem2)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "JK", 2, 13, 30, 15, 0, sem2)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 3, 8, 15, 9, 45, sem2)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("kscz", classroom_komp, "KGR", 3, 9, 50, 11, 20, sem2)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("wop", classroom_gdansk, "EG", 3, 11, 40, 13, 10, sem2)
    db.group_lessons_table.add_group_lesson(group_6n, i)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("fiz", classroom_lodz, "MD", 3, 17, 00, 18, 30, sem2)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("kscz", classroom_krakow, "KGR", 4, 8, 00, 9, 30, sem2)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("jn", classroom_gdansk, "IKA", 4, 9, 50, 11, 20, sem2)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("fiz", classroom_lodz, "MD", 4, 15, 15, 16, 45, sem2)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_proj, "JK", 5, 8, 00, 9, 30, sem2)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("konw", classroom_warszawa, "JPM", 5, 9, 50, 11, 20, sem2)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_warszawa, "KGR", 5, 11, 40, 13, 10, sem2)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("gp", classroom_proj, "JK", 5, 13, 30, 15, 00, sem2)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    Lesson(subject_gp, classroom_warszawa, teacher_jpm, 1, 9, 50, 11, 20, sem2).add_group(group_2n)
    Lesson(subject_kscz, classroom_warszawa, teacher_jk, 1, 11, 40, 13, 10, sem2).add_group(group_3n)
    Lesson(subject_ksczwop, classroom_wroclaw, teacher_kst, 1, 9, 50, 11, 20, sem2).add_group(group_1s)
    Lesson(subject_gp, classroom_wroclaw, teacher_kst, 1, 11, 40, 13, 10, sem2).add_group(group_3s)
    Lesson(subject_gp, classroom_krakow, teacher_kst, 1, 8, 00, 9, 30, sem2).add_group(group_5s)
    Lesson(subject_gp, classroom_krakow, teacher_mr, 1, 9, 50, 11, 20, sem2).add_group(group_3n)
    Lesson(subject_gp, classroom_krakow, teacher_msz, 1, 11, 40, 13, 10, sem2).add_group(group_2s)
    Lesson(subject_konw, classroom_krakow, teacher_msz, 1, 13, 30, 15, 00, sem2).add_group(group_2n)

    Lesson(subject_ksczwop, classroom_lodz, teacher_msz, 1, 9, 50, 11, 20, sem2).add_group(group_3s)
    Lesson(subject_gp, classroom_lodz, teacher_jpm, 1, 11, 40, 13, 10, sem2).add_group(group_1s)
    Lesson(subject_ksczwop, classroom_gdansk, teacher_sr, 1, 8, 00, 9, 30, sem2).add_group(group_2s)
    Lesson(subject_ksczwop, classroom_gdansk, teacher_sr, 1, 9, 50, 11, 20, sem2).add_group(group_2s)
    Lesson(subject_kscz, classroom_gdansk, teacher_sr, 1, 11, 40, 13, 10, sem2).add_group(group_4s)
    Lesson(subject_kscz, classroom_gdansk, teacher_sr, 1, 13, 30, 15, 00, sem2).add_group(group_4s)
    Lesson(subject_ksczwop, classroom_proj, teacher_ak, 1, 9, 50, 11, 20, sem2).add_group(group_1n)
    Lesson(subject_ksczwop, classroom_proj, teacher_ak, 1, 11, 40, 13, 10, sem2).add_group(group_1n)
    Lesson(subject_kscz, classroom_proj, teacher_jk, 1, 13, 30, 15, 00, sem2).add_group(group_4n)

    Lesson(subject_gp, classroom_warszawa, teacher_kst, 2, 9, 50, 11, 20, sem2).add_group(group_5s)
    Lesson(subject_gp, classroom_warszawa, teacher_kst, 2, 11, 40, 13, 10, sem2).add_group(group_3s)
    Lesson(subject_ksczwop, classroom_warszawa, teacher_kst, 2, 13, 30, 15, 00, sem2).add_group(group_1s)
    Lesson(subject_ksczwop, classroom_warszawa, teacher_kst, 2, 15, 15, 16, 45, sem2).add_group(group_1s)

    Lesson(subject_kscz, classroom_krakow, teacher_jk, 2, 11, 40, 13, 10, sem2).add_group(group_4n)


    Lesson(subject_gp, classroom_warszawa, teacher_mr, 3, 11, 40, 13, 10, sem2).add_group(group_3n)
    Lesson(subject_konw, classroom_warszawa, teacher_mr, 3, 13, 30, 15, 00, sem2).add_group(group_5n)

    Lesson(subject_kscz, classroom_wroclaw, teacher_sr, 3, 9, 50, 11, 20, sem2).add_group(group_5s)
    Lesson(subject_gp, classroom_wroclaw, teacher_jpm, 3, 11, 40, 13, 10, sem2).add_group(group_2n)
    Lesson(subject_gp, classroom_wroclaw, teacher_jpm, 3, 13, 30, 15, 00, sem2).add_group(group_1n)

    Lesson(subject_ksczwop, classroom_krakow, teacher_ak, 3, 11, 40, 13, 10, sem2).add_group(group_1n)
    Lesson(subject_konw, classroom_lodz, teacher_eg, 3, 9, 50, 11, 20, sem2).add_group(group_4s)
    Lesson(subject_ksczwop, classroom_lodz, teacher_msz, 3, 11, 40, 13, 10, sem2).add_group(group_3s)
    Lesson(subject_gp, classroom_lodz, teacher_msz, 3, 13, 30, 15, 00, sem2).add_group(group_2s)
    Lesson(subject_ksczwop, classroom_gdansk, teacher_msz, 3, 9, 50, 11, 20, sem2).add_group(group_3s)
    Lesson(subject_gp, classroom_poznan, teacher_jpm, 3, 9, 50, 11, 20, sem2).add_group(group_1s)
    Lesson(subject_ksczwop, classroom_konfer, teacher_sr, 3, 11, 40, 13, 10, sem2).add_group(group_2s)
    Lesson(subject_kscz, classroom_proj, teacher_ika, 3, 9, 50, 11, 20, sem2).add_group(group_5n)
    Lesson(subject_kscz, classroom_proj, teacher_sr, 3, 13, 30, 15, 00, sem2).add_group(group_4s)


    Lesson(subject_gp, classroom_warszawa, teacher_msz, 4, 11, 40, 13, 10, sem2).add_group(group_2s)
    Lesson(subject_gp, classroom_warszawa, teacher_kst, 4, 13, 30, 15, 00, sem2).add_group(group_5s)
    Lesson(subject_gp, classroom_wroclaw, teacher_jk, 4, 8, 00, 9, 30, sem2).add_group(group_4s)
    Lesson(subject_ksczwop, classroom_wroclaw, teacher_sr, 4, 9, 50, 11, 20, sem2).add_group(group_2s)
    Lesson(subject_gp, classroom_wroclaw, teacher_jpm, 4, 11, 40, 13, 10, sem2).add_group(group_2n)
    Lesson(subject_kscz, classroom_wroclaw, teacher_sr, 4, 13, 30, 15, 00, sem2).add_group(group_2n)

    Lesson(subject_kscz, classroom_krakow, teacher_jk, 4, 9, 50, 11, 20, sem2).add_group(group_3n)
    Lesson(subject_gp, classroom_krakow, teacher_mr, 4, 11, 40, 13, 10, sem2).add_group(group_3n)
    Lesson(subject_ksczwop, classroom_krakow, teacher_msz, 4, 13, 30, 15, 00, sem2).add_group(group_3s)

    Lesson(subject_gp, classroom_lodz, teacher_kgr, 4, 9, 50, 11, 20, sem2).add_group(group_4n)
    Lesson(subject_gp, classroom_lodz, teacher_kgr, 4, 11, 40, 13, 10, sem2).add_group(group_4n)
    Lesson(subject_gp, classroom_lodz, teacher_kgr, 4, 13, 30, 15, 00, sem2).add_group(group_5n)

    Lesson(subject_kscz, classroom_gdansk, teacher_ika, 4, 11, 40, 13, 10, sem2).add_group(group_5n)
    Lesson(subject_kscz, classroom_gdansk, teacher_jk, 4, 13, 30, 15, 00, sem2).add_group(group_4n)
    Lesson(subject_gp, classroom_poznan, teacher_jpm, 4, 9, 50, 11, 20, sem2).add_group(group_1s)
    Lesson(subject_gp, classroom_poznan, teacher_jk, 4, 11, 40, 13, 10, sem2).add_group(group_4s)

    Lesson(subject_kscz, classroom_komp, teacher_sr, 4, 8, 00, 9, 30, sem2).add_group(group_5s)
    Lesson(subject_ksczwop, classroom_komp, teacher_msz, 4, 9, 50, 11, 20, sem2).add_group(group_3s)
    Lesson(subject_ksczwop, classroom_komp, teacher_kst, 4, 11, 40, 13, 10, sem2).add_group(group_1s)

    Lesson(subject_kscz, classroom_konfer, teacher_sr, 4, 11, 40, 13, 10, sem2).add_group(group_5s)
    Lesson(subject_ksczwop, classroom_proj, teacher_ak, 4, 9, 50, 11, 20, sem2).add_group(group_1n)
    Lesson(subject_ksczwop, classroom_proj, teacher_ak, 4, 11, 40, 13, 10, sem2).add_group(group_1n)
    Lesson(subject_gp, classroom_proj, teacher_jpm, 4, 13, 30, 15, 00, sem2).add_group(group_1n)

    Lesson(subject_kscz, classroom_warszawa, teacher_ika, 5, 8, 00, 9, 30, sem2).add_group(group_5n)
    Lesson(subject_ksczwop, classroom_wroclaw, teacher_sr, 5, 8, 00, 9, 50, sem2).add_group(group_2s)
    Lesson(subject_konw, classroom_wroclaw, teacher_kst, 5, 9, 50, 11, 20, sem2).add_group(group_3n)
    Lesson(subject_konw, classroom_wroclaw, teacher_jpm, 5, 11, 40, 13, 10, sem2).add_group(group_4n)
    Lesson(subject_gp, classroom_wroclaw, teacher_jpm, 5, 13, 30, 15, 00, sem2).add_group(group_1n)

    Lesson(subject_gp, classroom_krakow, teacher_kgr, 5, 8, 00, 9, 30, sem2).add_group(group_4n)
    Lesson(subject_gp, classroom_krakow, teacher_kgr, 5, 9, 50, 11, 20, sem2).add_group(group_5n)
    Lesson(subject_konw, classroom_lodz, teacher_ika, 5, 9, 50, 11, 20, sem2).add_group(group_5s)
    Lesson(subject_gp, classroom_lodz, teacher_kgr, 5, 13, 30, 15, 00, sem2).add_group(group_5n)

    Lesson(subject_ksczwop, classroom_gdansk, teacher_kst, 5, 8, 00, 9, 30, sem2).add_group(group_1s)
    Lesson(subject_kscz, classroom_gdansk, teacher_sr, 5, 9, 50, 11, 20, sem2).add_group(group_2n)
    Lesson(subject_kscz, classroom_gdansk, teacher_sr, 5, 11, 40, 13, 10, sem2).add_group(group_2n)

    Lesson(subject_gp, classroom_konfer, teacher_sr, 5, 11, 40, 13, 10, sem2).add_group(group_3s)
    Lesson(subject_gp, classroom_proj, teacher_jk, 5, 9, 50, 11, 20, sem2).add_group(group_4s)
    Lesson(subject_kscz, classroom_proj, teacher_jk, 5, 11, 40, 13, 10, sem2).add_group(group_3n)

    Lesson(subject_mat_i, classroom_konfer, teacher_ab, 1, 13, 30, 15, 00, sem2).add_subgroup(subgroup_3s_inz).add_subgroup(subgroup_5s_inz)
    Lesson(subject_mat_i, classroom_konfer, teacher_wo, 4, 8, 00, 9, 30, sem2).add_subgroup(subgroup_1n_inz).add_subgroup(subgroup_4n_inz)
    Lesson(subject_mat_i, classroom_konfer, teacher_ab, 4, 17, 00, 18, 30, sem2).add_subgroup(subgroup_1s_inz).add_subgroup(subgroup_2s_inz)
    Lesson(subject_mat_i, classroom_konfer, teacher_wo, 5, 9, 50, 11, 20, sem2).add_subgroup(subgroup_1n_inz).add_subgroup(subgroup_4n_inz)
    Lesson(subject_mat_i, classroom_konfer, teacher_ab, 5, 15, 15, 16, 45, sem2).add_subgroup(subgroup_3s_inz).add_subgroup(subgroup_5s_inz)
    Lesson(subject_mat_i, classroom_konfer, teacher_ab, 5, 17, 00, 18, 30, sem2).add_subgroup(subgroup_1s_inz).add_subgroup(subgroup_2s_inz)

    Lesson(subject_fiz, classroom_lodz, teacher_md, 2, 13, 30, 15, 00, sem2).add_subgroup(subgroup_1n_inz).add_subgroup(subgroup_4n_inz)
    Lesson(subject_fiz, classroom_lodz, teacher_md, 3, 15, 15, 16, 45, sem2).add_subgroup(subgroup_1s_inz).add_subgroup(subgroup_2s_inz)
    Lesson(subject_fiz, classroom_konfer, teacher_md, 3, 13, 30, 15,00, sem2).add_subgroup(subgroup_3s_inz).add_subgroup(subgroup_5s_inz)
    Lesson(subject_fiz, classroom_lodz, teacher_md, 4, 8, 00, 9, 30, sem2).add_subgroup(subgroup_1s_inz).add_subgroup(subgroup_2s_inz)
    Lesson(subject_fiz, classroom_lodz, teacher_md, 4, 17, 00, 18, 30, sem2).add_subgroup(subgroup_1n_inz).add_subgroup(subgroup_4n_inz)
    Lesson(subject_fiz, classroom_lodz, teacher_md, 5, 8, 00, 9, 30, sem2).add_subgroup(subgroup_3s_inz).add_subgroup(subgroup_5s_inz)

    Lesson(subject_inf_i, classroom_komp, teacher_an, 1, 9, 50, 11, 20, sem2).add_subgroup(subgroup_4n_inz).add_subgroup(subgroup_5s_inz)
    Lesson(subject_inf_i, classroom_komp, teacher_an, 2, 8, 15, 9, 45, sem2).add_subgroup(subgroup_4n_inz).add_subgroup(subgroup_5s_inz)


    Lesson(subject_wop, classroom_gdansk, teacher_eg, 3, 13, 30, 15, 00, sem2).add_group(group_2n).add_group(group_3n)
    Lesson(subject_wop, classroom_gdansk, teacher_eg, 3, 15, 15, 16, 45, sem2).add_group(group_4n)
    Lesson(subject_jn, classroom_proj, teacher_ika, 3, 11, 40, 13, 10, sem2).add_subgroup(subgroup_4n_inz).add_subgroup(subgroup_5s_inz)

    Lesson(subject_mat_ea, classroom_konfer, teacher_wo, 1, 8, 00, 9, 30, sem2).add_subgroup(subgroup_1n_arch).add_subgroup(subgroup_2n_ekon).add_subgroup(subgroup_3n_ekon).add_subgroup(subgroup_3n_arch)
    Lesson(subject_mat_ea, classroom_konfer, teacher_wo, 5, 8, 00, 9, 30, sem2).add_subgroup(subgroup_1n_arch).add_subgroup(subgroup_2n_ekon).add_subgroup(subgroup_3n_ekon).add_subgroup(subgroup_3n_arch)

    Lesson(subject_mat_ea, classroom_konfer, teacher_wo, 1, 9, 50, 11, 20, sem2).add_subgroup(subgroup_4n_ekon).add_subgroup(subgroup_5n_ekon).add_subgroup(subgroup_6n_arch)
    Lesson(subject_mat_ea, classroom_konfer, teacher_wo, 2, 8, 00, 9, 30, sem2).add_subgroup(subgroup_4n_ekon).add_subgroup(subgroup_5n_ekon).add_subgroup(subgroup_6n_arch)

    Lesson(subject_sa, classroom_lodz, teacher_eg, 2, 9, 50, 11, 20, sem2).add_subgroup(subgroup_1n_arch).add_subgroup(subgroup_3n_arch).add_subgroup(subgroup_6n_arch).add_subgroup(subgroup_4s_arch)
    Lesson(subject_sa, classroom_lodz, teacher_eg, 2, 11, 40, 13, 10, sem2).add_subgroup(subgroup_1n_arch).add_subgroup(subgroup_3n_arch).add_subgroup(subgroup_6n_arch).add_subgroup(subgroup_4s_arch)

    Lesson(subject_rart, classroom_konfer, teacher_mb, 2, 13, 30, 16, 30, sem2).add_subgroups(subgroup_2n_art, subgroup_5n_art)
    Lesson(subject_rart, classroom_konfer, teacher_mb, 2, 17, 00, 20, 00, sem2).add_subgroups(subgroup_1n_art, subgroup_3n_art, subgroup_4s_art, subgroup_5s_art)
    Lesson(subject_rarch, classroom_konfer, teacher_wg, 3, 15, 15, 18, 15, sem2).add_subgroups(subgroup_1n_arch, subgroup_3n_arch, subgroup_6n_arch, subgroup_4s_arch)

    Lesson(subject_hs, classroom_wroclaw, teacher_mr, 2, 8, 00, 9, 30, sem2).add_subgroups(subgroup_1n_art)
    Lesson(subject_hs, classroom_wroclaw, teacher_mr, 2, 9, 50, 11, 20, sem2).add_subgroups(subgroup_2n_art, subgroup_3n_art)
    Lesson(subject_hs, classroom_proj, teacher_mr, 2, 11, 40, 13, 10, sem2).add_subgroups(subgroup_5n_art, subgroup_4s_art, subgroup_5s_art)
    Lesson(subject_hk, classroom_wroclaw, teacher_mr, 3, 8, 00, 9, 30, sem2).add_subgroups(subgroup_1n_art)
    Lesson(subject_hk, classroom_konfer, teacher_mr, 3, 9, 50, 11, 20, sem2).add_subgroups(subgroup_2n_art, subgroup_3n_art)
    Lesson(subject_hk, classroom_konfer, teacher_mr, 4, 9, 50, 11, 20, sem2).add_subgroups(subgroup_5n_art, subgroup_4s_art, subgroup_5s_art)
    Lesson(subject_pp, classroom_komp, teacher_abar, 4, 17, 00, 18, 30, sem2).add_subgroups(subgroup_1n_art, subgroup_3n_art, subgroup_4s_art, subgroup_5s_art)
    Lesson(subject_pp, classroom_proj, teacher_abar, 4, 18, 45, 20, 15, sem2).add_subgroups(subgroup_2n_art, subgroup_5n_art)
    Lesson(subject_wok, classroom_lodz, teacher_kgr, 2, 8, 00, 9, 30, sem2).add_subgroups(subgroup_5n_art, subgroup_4s_art, subgroup_5s_art) #
    Lesson(subject_wok, classroom_poznan, teacher_kgr, 2, 9, 50, 11, 20, sem2).add_subgroups(subgroup_1n_art)
    Lesson(subject_wok, classroom_poznan, teacher_kgr, 2, 11, 40, 13, 10, sem2).add_subgroups(subgroup_1n_art)
    Lesson(subject_wok, classroom_lodz, teacher_kgr, 3, 8, 00, 9, 30, sem2).add_subgroups(subgroup_2n_art, subgroup_3n_art)

    Lesson(subject_wop, classroom_gdansk, teacher_eg, 2, 13, 30, 15, 00, sem2).add_group(group_4s).add_group(group_5s)

    Lesson(subject_gehg, classroom_gdansk, teacher_ika, 2, 9, 50, 11, 20, sem2).add_subgroups(subgroup_2n_ekon, subgroup_3n_ekon, subgroup_4n_ekon)
    Lesson(subject_gehg, classroom_gdansk, teacher_ika, 2, 11, 40, 13, 10, sem2).add_subgroups(subgroup_5n_ekon, subgroup_4s_ekon, subgroup_5s_ekon)
    Lesson(subject_gehg, classroom_gdansk, teacher_ika, 3, 8, 00, 9, 30, sem2).add_subgroups(subgroup_1n_ekon, subgroup_1s_ekon, subgroup_2s_ekon)
    Lesson(subject_gehg, classroom_lodz, teacher_ika, 5, 11, 40, 12, 25, sem2).add_subgroups(subgroup_1n_ekon, subgroup_1s_ekon, subgroup_2s_ekon)

    Lesson(subject_se, classroom_warszawa, teacher_im, 3, 8, 00, 9, 30, sem2).add_subgroups(subgroup_5n_ekon, subgroup_4s_ekon, subgroup_5s_ekon)
    Lesson(subject_se, classroom_warszawa, teacher_im, 3, 9, 50, 11, 20, sem2).add_subgroups(subgroup_2n_ekon, subgroup_3n_ekon, subgroup_4n_ekon)
    Lesson(subject_se, classroom_warszawa, teacher_im, 4, 8, 00, 9, 30, sem2).add_subgroups(subgroup_2n_ekon, subgroup_3n_ekon, subgroup_4n_ekon)
    Lesson(subject_se, classroom_warszawa, teacher_im, 4, 9, 50, 11, 20, sem2).add_subgroups(subgroup_5n_ekon, subgroup_4s_ekon, subgroup_5s_ekon)
    Lesson(subject_se, classroom_gdansk, teacher_im, 2, 8, 00, 9, 30, sem2).add_subgroups(subgroup_1n_ekon, subgroup_1s_ekon, subgroup_2s_ekon)
    Lesson(subject_se, classroom_gdansk, teacher_ika, 4, 8, 00, 9, 30, sem2).add_subgroups(subgroup_1n_ekon, subgroup_1s_ekon, subgroup_2s_ekon) # TODO wtf why ika

    Lesson(subject_pr, classroom_krakow, teacher_jd, 4, 15, 15, 16, 45, sem2).add_subgroups(subgroup_2n_ekon, subgroup_3n_ekon, subgroup_4n_ekon)
    Lesson(subject_pr, classroom_krakow, teacher_jd, 4, 17, 00, 18, 30, sem2).add_subgroups(subgroup_1n_ekon, subgroup_1s_ekon, subgroup_2s_ekon)
    Lesson(subject_pr, classroom_krakow, teacher_jd, 4, 18, 45, 20, 15, sem2).add_subgroups(subgroup_5n_ekon, subgroup_4s_ekon, subgroup_5s_ekon)

    Lesson(subject_pr, classroom_krakow, teacher_jd, 5, 11, 40, 13, 10, sem2).add_subgroups(subgroup_5n_ekon, subgroup_4s_ekon, subgroup_5s_ekon)
    Lesson(subject_pr, classroom_krakow, teacher_jd, 5, 13, 30, 15, 00, sem2).add_subgroups(subgroup_2n_ekon, subgroup_3n_ekon, subgroup_4n_ekon)
    Lesson(subject_pr, classroom_krakow, teacher_jd, 5, 15, 15, 16, 45, sem2).add_subgroups(subgroup_1n_ekon, subgroup_1s_ekon, subgroup_2s_ekon)

    Lesson(subject_hs, classroom_proj, teacher_mr, 4, 8, 00, 9, 30, sem2).add_subgroups(subgroup_1n_art)
    Lesson(subject_hk, classroom_lodz, teacher_mr, 1, 8, 50, 9, 35, sem2).add_subgroups(subgroup_1n_art, subgroup_2n_art, subgroup_3n_art)

    Lesson(subject_fp, classroom_gdansk, teacher_tj, 2, 15, 15, 17, 30, sem2).add_subgroups(subgroup_2n_ekon, subgroup_3n_ekon, subgroup_4n_ekon)
    Lesson(subject_fp, classroom_gdansk, teacher_tj, 1, 15, 15, 17, 30, sem2).add_subgroups(subgroup_1n_art, subgroup_2n_art, subgroup_3n_art, subgroup_4s_art, subgroup_5s_art)
    Lesson(subject_fp, classroom_gdansk, teacher_tj, 2, 18, 00, 20, 15, sem2).add_group(group_5n).add_subgroups(subgroup_4s_ekon, subgroup_5s_ekon)
    Lesson(subject_dkf, classroom_gdansk, teacher_tj, 1, 18, 00, 20, 15, sem2).add_subgroups(subgroup_1n_art, subgroup_3n_art, subgroup_1n_inz, subgroup_2n_inz, subgroup_4n_inz, subgroup_6n_inz, subgroup_5s_inz)

    Lesson(subject_zw, classroom_poznan, teacher_wzt, 1, 8, 00, 9, 30, sem2).add_subgroups(subgroup_3n_art, subgroup_4s_art)
    Lesson(subject_zw, classroom_poznan, teacher_wzt, 1, 8, 00, 9, 30, sem2).add_subgroups(subgroup_4s_art, subgroup_3n_art)

    Lesson(subject_mat_ea, classroom_konfer, teacher_ab, 1, 15, 15, 16, 45, sem2).add_subgroups(subgroup_1s_ekon, subgroup_2s_ekon, subgroup_4s_ekon, subgroup_4s_arch, subgroup_5s_ekon)
    Lesson(subject_mat_ea, classroom_konfer, teacher_ab, 4, 15, 15, 16, 45, sem2).add_subgroups(subgroup_1s_ekon, subgroup_2s_ekon, subgroup_4s_ekon, subgroup_4s_arch, subgroup_5s_ekon)

    Lesson(subject_si, classroom_krakow, teacher_ak, 2, 8, 00, 9, 30, sem2).add_subgroups(subgroup_1s_inz, subgroup_3s_inz)
    Lesson(subject_si, classroom_krakow, teacher_ak, 2, 9, 50, 11, 20, sem2).add_subgroups(subgroup_1n_inz, subgroup_2s_inz)
    Lesson(subject_si, classroom_krakow, teacher_ak, 3, 8, 00, 9, 30, sem2).add_subgroups(subgroup_1s_inz, subgroup_3s_inz)
    Lesson(subject_si, classroom_krakow, teacher_ak, 3, 9, 50, 11, 20, sem2).add_subgroups(subgroup_1n_inz, subgroup_2s_inz)

    Lesson(subject_ch, classroom_krakow, teacher_abuk, 2, 17, 45, 19, 15, sem2).add_subgroups(subgroup_1s_inz, subgroup_2s_inz, subgroup_3s_inz, subgroup_5s_inz, subgroup_4n_inz) #TODO check if correct
    Lesson(subject_ch, classroom_gdansk, teacher_abuk, 4, 15, 15, 16, 45, sem2).add_subgroups(subgroup_1s_inz, subgroup_2s_inz, subgroup_3s_inz, subgroup_5s_inz, subgroup_4n_inz)

    Lesson(subject_inf, classroom_komp, teacher_ap, 2, 9, 50, 11, 20, sem2).add_subgroups(subgroup_1s_inz, subgroup_3s_inz)
    Lesson(subject_inf, classroom_komp, teacher_ap, 2, 11, 40, 13, 10, sem2).add_subgroups(subgroup_1s_inz, subgroup_2s_inz, subgroup_1n_inz)
    Lesson(subject_inf_ech, classroom_komp, teacher_ap, 4, 9, 50, 11, 20, sem2).add_group(group_1s).add_group(group_2s).add_subgroups(subgroup_1n_ekon)
    Lesson(subject_inf, classroom_komp, teacher_ap, 4, 11, 40, 13, 10, sem2).add_subgroups(subgroup_1s_inz, subgroup_2s_inz, subgroup_1n_inz)
    Lesson(subject_inf, classroom_komp, teacher_ap, 4, 13, 30, 15, 00, sem2).add_subgroups(subgroup_1s_inz, subgroup_3s_inz)

    Lesson(subject_bud, classroom_krakow, teacher_rb, 1, 16, 30, 18, 00, sem2).add_subgroups(subgroup_2s_inz, subgroup_3s_inz, subgroup_4s_arch, subgroup_1n_arch, subgroup_3n_arch, subgroup_6n_arch)
    Lesson(subject_gi, classroom_komp, teacher_tk, 2, 16, 00, 17, 30, sem2).add_subgroups(subgroup_2s_inz, subgroup_3s_inz, subgroup_4s_arch, subgroup_1n_arch, subgroup_3n_arch, subgroup_6n_arch)
    Lesson(subject_wil, classroom_lodz, teacher_eg, 3, 15, 15, 16, 45, sem2)
    Lesson(subject_wil, classroom_proj, teacher_eg, 3, 8, 00, 9, 30, sem2)
    Lesson(subject_saw, classroom_lodz, teacher_mr, 1, 8, 00, 8, 45, sem2).add_subgroups(subgroup_1n_art, subgroup_2n_art, subgroup_3n_art, subgroup_4s_art)
    #TODO

    # Lesson(subject)
    # print("got to subject creation")
    # lesson = Subject("test", "abc")

    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()

    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()