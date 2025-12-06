studenty_matematiki = {"Alice", "okynsev", "zavr", "max"}
studenty_fiziki = {"gnida", "borsh", "sania", "lenia"}
studenty_informatiki = {"max", "okynsev", "borsh", "zavr"}

vse_tri_kursa = studenty_matematiki & studenty_fiziki & studenty_informatiki
print(f"все три курса: {vse_tri_kursa}")

tolko_matematika = studenty_matematiki - studenty_fiziki - studenty_informatiki
tolko_fizika = studenty_fiziki - studenty_matematiki - studenty_informatiki
tolko_informatika = studenty_informatiki - studenty_matematiki - studenty_fiziki

tolko_odin_kurs = tolko_matematika | tolko_fizika | tolko_informatika
print(f"только один курс: {tolko_odin_kurs}")

matematika_no_ne_fizika = studenty_matematiki - studenty_fiziki
print(f"математика но не физика: {matematika_no_ne_fizika}")

vse_studenty = studenty_matematiki | studenty_fiziki | studenty_informatiki
print(f"всего студентов: {len(vse_studenty)}")