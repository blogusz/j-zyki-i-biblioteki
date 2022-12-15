- Program działa w oparciu o moduł pickle. Dane są przechowywane w odpowiednich plikach z tym rozszerzeniem.
- Konto może założyć zarówno czytelnik jak i pracownik. Zakładam, że nie jest to wielki problem, że pracownikiem może zostać każdy kto tylko zechce.
- Czytelnik posiada imię i nazwisko, hasło wybiera sam. 
  Czytelnik może książki przeglądać, wypożyczać, rezerwować i przedłużać rezerwację, aczkolwiek to ostatnie najwidoczniej nie chce współpracować (po dodaniu funkcji z datami nie działa to najlepiej).
- Pracownik biblioteki ma szereg funkcji pozwalających na zarządzanie systemem. Identyfikator pracownika to dowolny string, hasło tak samo.
- Zarezerwować książkę można, jeżeli nie jest ona już zarezerwowana przez kogoś lub jeżeli jest, ale termin ich rezerwacji minął.
- Wypożyczyć książę można, jeżeli nie jest ona wypożyczona ani zarezerwowana, chyba że to my ją zarezerwowaliśmy.
- Dane z dysku wczytywane są przy odpaleniu maina, a zapisywaniu przy wyjściu przez menu, tzn. opcji [0] Wyjście w logowaniu.
  Dzięki temu, jeżeli w trakcie trwania programu wystąpią jakieś errory, to nic złego nie zapisze się na stałe.
  Można też w razie paniki zatrzymać działanie programu i zacząć działać od nowa.

Czytelnicy zdefiniowani przeze mnie oraz ich dane logowania: 
{'Ala Makota': 'kot', 'Arek Milik': 'gol', 'Michael jackson': 'heehee', 'Taylor Swift': 'sing', 'Pan Mareczek': 'maro'} 
Pracownicy biblioteki i ich dane logowania:
{'2137': '1', '1337': '2', '402606': 'JiBAD'}
