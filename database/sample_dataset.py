from database.db import Database


def load_sample_data(db: Database):
    db._drop_database()
    db._init_database()

    group_1n = db.groups_table.add_group("1N")
    group_2n = db.groups_table.add_group("2N")
    group_3n = db.groups_table.add_group("3N")
    group_4n = db.groups_table.add_group("4N")
    group_5n = db.groups_table.add_group("5N")
    group_6n = db.groups_table.add_group("6N")
    group_1s = db.groups_table.add_group("1S")
    group_2s = db.groups_table.add_group("2S")
    group_3s = db.groups_table.add_group("3S")
    group_4s = db.groups_table.add_group("4S")
    group_5s = db.groups_table.add_group("5S")

    subgroup_1n_inz = db.subgroups_table.add_subgroup(group_1n, "inz", "1N / inz")
    subgroup_1n_art = db.subgroups_table.add_subgroup(group_1n, "art", "1N / art")
    subgroup_1n_arch = db.subgroups_table.add_subgroup(group_1n, "arch", "1N / arch")

    subgroup_2n_inz = db.subgroups_table.add_subgroup(group_2n, "inz", "2N / inz")
    subgroup_2n_art = db.subgroups_table.add_subgroup(group_2n, "art", "2N / art")
    subgroup_2n_ekon = db.subgroups_table.add_subgroup(group_2n, "ekon", "2N / ekon")

    subgroup_3n_arch = db.subgroups_table.add_subgroup(group_3n, "arch", "3N / arch")
    subgroup_3n_ekon = db.subgroups_table.add_subgroup(group_3n, "ekon", "3N / ekon")
    subgroup_3n_art = db.subgroups_table.add_subgroup(group_3n, "art", "3N / art")

    subgroup_4n_inz = db.subgroups_table.add_subgroup(group_4n, "inz", "4N / inz")
    subgroup_4n_ekon = db.subgroups_table.add_subgroup(group_4n, "ekon", "4N / ekon")

    subgroup_5n_art = db.subgroups_table.add_subgroup(group_5n, "art", "5N / art")
    subgroup_5n_ekon = db.subgroups_table.add_subgroup(group_5n, "ekon", "5N / ekon")

    subgroup_6n_inz = db.subgroups_table.add_subgroup(group_6n, "inz", "6N / inz")
    subgroup_6n_arch = db.subgroups_table.add_subgroup(group_6n, "arch", "6N / arch")

    subgroup_4s_ekon = db.subgroups_table.add_subgroup(group_4s, "ekon", "4S / ekon")
    subgroup_4s_art = db.subgroups_table.add_subgroup(group_4s, "art", "4S / art")
    subgroup_4s_arch = db.subgroups_table.add_subgroup(group_4s, "arch", "4S / arch")

    subgroup_5s_ekon = db.subgroups_table.add_subgroup(group_5s, "ekon", "5S / ekon")
    subgroup_5s_art = db.subgroups_table.add_subgroup(group_5s, "art", "5S / art")
    subgroup_5s_inz = db.subgroups_table.add_subgroup(group_5s, "inz", "5S / inz")

    classroom_warszawa = db.classrooms_table.add_classroom("warszawa", "Warszawa (07)")
    classroom_wroclaw = db.classrooms_table.add_classroom("wroclaw", "Wrocław (08)")
    classroom_krakow = db.classrooms_table.add_classroom("krakow", "Kraków (09)")
    classroom_lodz = db.classrooms_table.add_classroom("lodz", "Łódź (05)")
    classroom_gdansk = db.classrooms_table.add_classroom("gdansk", "Gdańsk (04)")
    classroom_poznan = db.classrooms_table.add_classroom("poznan", "Poznań (06)")
    classroom_seminar = db.classrooms_table.add_classroom("seminar", "Sała seminaryjna (12)")
    classroom_komp = db.classrooms_table.add_classroom("komput", "Sała komputerowa (10)")
    classroom_konfer = db.classrooms_table.add_classroom("konfer", "Sała konferencyjna (13)")
    classroom_proj = db.classrooms_table.add_classroom("proj", "Sała projektowa (11)")

    db.teachers_table.add_teacher("KGR", "Kinga Górecka-Rokita")
    db.teachers_table.add_teacher("JK", "Justyna Krztoń")
    db.teachers_table.add_teacher("EG", "Edyta Gałat")
    db.teachers_table.add_teacher("JPM", "Joanna Piera-Mitka")
    db.teachers_table.add_teacher("TJ", "Tomasz Jeleński")

    db.teachers_table.add_teacher("IKA", "Izabela Kugiel-Abuhasna")
    db.teachers_table.add_teacher("WO", "Witold Obloza")
    db.teachers_table.add_teacher("MD", "Małgorzata Duraj")
    db.teachers_table.add_teacher("AN", "Artur Niewiarowski")
    db.teachers_table.add_teacher("WG", "WG (?)")
    db.teachers_table.add_teacher("SR", "SR (?)")
    db.teachers_table.add_teacher("MR", "MR (?)")
    db.teachers_table.add_teacher("AP", "AP (?)")
    db.teachers_table.add_teacher("MB", "MB (?)")
    db.teachers_table.add_teacher("WZT", "WZT (?)")
    db.teachers_table.add_teacher("AK", "AK (?)")

    db.subjects_table.add_subject("mat-i", "Matematyka inz.")
    db.subjects_table.add_subject("fiz", "Fizyka inz.")
    db.subjects_table.add_subject("inf-i", "Informatyka inz.")
    db.subjects_table.add_subject("jn", "Język naukowy")

    db.subjects_table.add_subject("kscz", "KSCz")
    db.subjects_table.add_subject("gp", "GP")
    db.subjects_table.add_subject("wop", "WOP")
    db.subjects_table.add_subject("konw", "Konwersatorium")
    db.subjects_table.add_subject("dkf", "DKF")

    db.subjects_table.add_subject("mat-ea", "Matematyka ekon./arch.")
    db.subjects_table.add_subject("fp", "Film polski")
    db.subjects_table.add_subject("sa", "Słownictwo architektoniczne")
    db.subjects_table.add_subject("ha", "Historia architektury")
    db.subjects_table.add_subject("rarch", "Rysunek architektoniczny")

    db.subjects_table.add_subject("se", "Słownictwo ekonomiczne")
    db.subjects_table.add_subject("hs", "Historia sztuki")
    db.subjects_table.add_subject("hk", "Historia kultury")
    db.subjects_table.add_subject("inf-e", "Informatyka ekonomiczna")
    db.subjects_table.add_subject("rart", "Rysunek artystyczny")
    db.subjects_table.add_subject("wok", "WOK")
    db.subjects_table.add_subject("zw", "Zajęcia warsztatowe")
    db.subjects_table.add_subject("ksczwop", "KSCZWOP")

    # db.subjects_table.add_subject("")

    i = db.lessons_table.add_lesson("mat-i", classroom_warszawa, "WO", 1,
                                      9, 50, 11, 20)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("dkf", classroom_gdansk, "TJ", 1, 18, 0, 20, 15)
    db.group_lessons_table.add_group_lesson(group_6n, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("wop", classroom_gdansk, "EG", 2, 8, 0, 9, 30)
    db.group_lessons_table.add_group_lesson(group_6n, i)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_krakow, "KGR", 2,
                                      9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("jn", classroom_lodz, "IKA", 2, 11, 40, 13, 10)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("fiz", classroom_lodz, "MD", 2, 15, 15, 16, 45)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("mat-i", classroom_krakow, "WO", 2, 17, 00, 18, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 3, 8, 15, 9, 45)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("konw", classroom_poznan, "JPM", 3, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "JK", 4, 8, 00, 9, 30)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 4, 10, 0, 11, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "JK", 4, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_lodz, "KGR", 4, 13, 30, 15, 0)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("fiz", classroom_lodz, "MD", 4, 17, 00, 18, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_lodz, "JK", 5, 8, 0, 9, 30)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_krakow, "KGR", 5, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_6n, i)

    i = db.lessons_table.add_lesson("fp", classroom_gdansk, "TJ", 1, 15, 15, 17, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)
    db.group_lessons_table.add_group_lesson(group_1s, i)
    db.group_lessons_table.add_group_lesson(group_2s, i)

    i = db.lessons_table.add_lesson("fp", classroom_gdansk, "TJ", 3, 15, 15, 17, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i)  # TODO: fix conflicts
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i)  # wtf duplicats
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)

    i = db.lessons_table.add_lesson("fp", classroom_gdansk, "TJ", 3, 18, 0, 20, 15)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_art, i)  # duplicates
    # db.group_lessons_table.add_group_lesson(group_5n, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_ekon, i)
    db.group_lessons_table.add_group_lesson(group_5s, i)

    i = db.lessons_table.add_lesson("ha", classroom_lodz, "EG", 1, 9, 50, 11, 20)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_arch, i)

    i = db.lessons_table.add_lesson("sa", classroom_lodz, "EG", 1, 11, 40, 13, 10)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_arch, i)
    # db.lessons_table.add_lesson("math", 1, "123456", 1, 23, 59, 23, 59)

    i = db.lessons_table.add_lesson("rarch", classroom_konfer, "WG", 2, 15, 15, 18, 15)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_arch, i)

    i = db.lessons_table.add_lesson("mat-ea", classroom_krakow, "WO", 4, 13, 30, 15, 0)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    # db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_???) #TODO add
    db.group_lessons_table.add_group_lesson(subgroup_3n_ekon, i)

    i = db.lessons_table.add_lesson("mat-ea", classroom_krakow, "WO", 4, 15, 15, 16, 45)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)

    i = db.lessons_table.add_lesson("mat-ea", classroom_konfer, "WO", 1, 8, 0, 9, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_6n_arch, i)

    i = db.lessons_table.add_lesson("kscz", classroom_warszawa, "SR", 1, 8, 0, 9, 30)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("gp", classroom_wroclaw, "JPM", 1, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("wop", classroom_krakow, "EG", 1, 13, 30, 15, 0)
    db.group_lessons_table.add_group_lesson(group_2n, i)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("se", classroom_lodz, "IKA", 2, 8, 0, 9, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)

    i = db.lessons_table.add_lesson("gp", classroom_konfer, "JPM", 2, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("mat-ea", classroom_krakow, "WO", 2, 13, 30, 15, 0)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("hs", classroom_krakow, "MR", 3, 8, 0, 9, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)

    i = db.lessons_table.add_lesson("konw", classroom_warszawa, "KGR", 3, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("hk", classroom_gdansk, "MR", 3, 11, 40, 13, 10)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)

    i = db.lessons_table.add_lesson("inf-e", classroom_komp, "AP", 3, 17, 0, 18, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)

    i = db.lessons_table.add_lesson("wok", classroom_lodz, "KGR", 4, 8, 0, 9, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)

    i = db.lessons_table.add_lesson("se", classroom_gdansk, "IKA", 4, 8, 0, 9, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_ekon, i)

    i = db.lessons_table.add_lesson("kscz", classroom_poznan, "SR", 4, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("mat-ea", classroom_krakow, "WO", 4, 13, 30, 15, 0)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_arch, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_ekon, i)

    i = db.lessons_table.add_lesson("rart", classroom_konfer, "MB", 4, 13, 30, 16, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_2n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i)

    i = db.lessons_table.add_lesson("kscz", classroom_proj, "SR", 5, 8, 0, 9, 30)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("gp", classroom_warszawa, "JPM", 5, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_2n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_gdansk, "JK", 1, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("mat-i", classroom_konfer, "WO", 1, 11, 40, 13, 10)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)

    i = db.lessons_table.add_lesson("wop", classroom_gdansk, "EG", 2, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("konw", classroom_gdansk, "EG", 2, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_warszawa, "JK", 2, 13, 30, 15, 0)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("mat-i", classroom_krakow, "WO", 2, 15, 15, 16, 45)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)

    i = db.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 3, 10, 0 , 11, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_proj, "KGR", 3, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("fiz", classroom_konfer, "MD", 3, 15, 15, 16, 45)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)

    i = db.lessons_table.add_lesson("inf-i", classroom_komp, "AN", 4, 8, 15, 9, 45)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_lodz, "KGR", 4, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("jn", classroom_komp, "IKA", 4, 11, 40, 13, 10)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_inz, i)

    i = db.lessons_table.add_lesson("fiz", classroom_lodz, "MD", 4, 15, 15, 16, 45)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4n_inz, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_inz, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "KGR", 5, 8, 0, 9, 30)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_lodz, "JK", 5, 13, 30, 15, 0)
    db.group_lessons_table.add_group_lesson(group_4n, i)

    i = db.lessons_table.add_lesson("hk", classroom_krakow, "MR", 1, 8, 0, 9, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_art, i)

    i = db.lessons_table.add_lesson("gp", classroom_proj, "KGR", 2, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("wok", classroom_lodz, "KGR", 3, 8, 0, 9, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_art, i)

    i = db.lessons_table.add_lesson("se", classroom_gdansk, "IKA", 3, 8, 0, 9, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_ekon, i)

    i = db.lessons_table.add_lesson("kscz", classroom_lodz, "IKA", 3, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_lodz, "IKA", 3, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("inf-e", classroom_komp, "AP", 3, 15, 15, 16, 45)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_ekon, i)

    i = db.lessons_table.add_lesson("hs", classroom_proj, "MR", 4, 8, 0, 9, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_art, i)

    i = db.lessons_table.add_lesson("konw", classroom_konfer, "MR", 4, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("gp", classroom_lodz, "KGR", 4, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("se", classroom_gdansk, "IKA", 5, 8, 0, 9, 30)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5n_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_ekon, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_ekon, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "KGR", 5, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_gdansk, "IKA", 5, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_5n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_gdansk, "JK", 1, 8, 0, 9, 30)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("zw", classroom_poznan, "WZT", 1, 9, 50, 11, 20)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)


    i = db.lessons_table.add_lesson("zw", classroom_poznan, "WZT", 1, 11, 40, 13, 10)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)

    i = db.lessons_table.add_lesson("konw", classroom_komp, "MR", 2, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("gp", classroom_komp, "MR", 2, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("gp", classroom_krakow, "MR", 3, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("kscz", classroom_krakow, "JK", 4, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("gp", classroom_warszawa, "MR", 4, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("rart", classroom_konfer, "MB", 4, 16, 45, 19, 45)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_1n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_3n_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_4s_art, i)
    db.subgroup_lessons_table.add_subgroup_lesson(subgroup_5s_art, i)

    i = db.lessons_table.add_lesson("kscz", classroom_lodz, "JK", 5, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_3n, i)

    i = db.lessons_table.add_lesson("gp", classroom_wroclaw, "JPM", 1, 13, 30, 15, 0)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    i = db.lessons_table.add_lesson("ksczwop", classroom_krakow, "AK", 2, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    i = db.lessons_table.add_lesson("ksczwop", classroom_krakow, "AK", 2, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    i = db.lessons_table.add_lesson("ksczwop", classroom_wroclaw, "AK", 3, 9, 50, 11, 20)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    i = db.lessons_table.add_lesson("ksczwop", classroom_wroclaw, "AK", 3, 11, 40, 13, 10)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    i = db.lessons_table.add_lesson("gp", classroom_lodz, "JPM", 3, 13, 30, 15, 0)
    db.group_lessons_table.add_group_lesson(group_1n, i)

    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()
    #
    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()
    #
    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()
    #
    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()
    #
    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()
    #
    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()
    #
    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()

    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()

    # i = db.lessons_table.add_lesson()
    # db.subgroup_lessons_table.add_subgroup_lesson()
    # db.group_lessons_table.add_group_lesson()