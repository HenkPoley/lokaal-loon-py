# Lokaal Loon (in python)

Dit programma zoekt op Funda naar de prijzen van woningen in de omgeving en berekent het bijbehorende inkomen.

# Aannames:

* We willen ervoor zorgen dat onze werknemer minstens in een woning kan wonen (geen dakloosheid of bij ouders, op een studenten kamer)
* We kunnen er niet van uitgaan dat onze werknemer altijd een partner heeft (eenpersoonshuishouden)
* Een minimale woning voor een eenpersoonshuishouden is ofwel een studio (minimaal 1 kamer)
* Ofwel een woning met een woonkamer en een slaapkamer (maximaal 2 kamers)
* Het woonoppervlak per persoon voor huishoudens met kinderen (2+ personen) is 32-36m2
* Dus woningen die veel kleiner zijn dan 2 * 32m2 (64m2) zijn alleen geschikt voor één persoon (1,5x36m2 = 54m2 is een goede bovengrens)
* Een reistijd van meer dan 20 minuten is ongewenst, of hoger loon nodig (op basis van onderzoek)
* Dit komt neer op een maximale afstand van ongeveer 15 km (met de auto) of 20 km (met de trein) of 7 km (met de fiets)
* Een verhuurder wil dat een huurder als bruto maandloon minimaal 3,5x de huurprijs verdient.
* Een verhuurder wil de woning in 240 maanden (20 jaar) afbetalen.

# Enkele percentielen voor heel Nederland in mei 2023

Benodigd inkomen om deze hypotheek te krijgen bij een rente van 4,5%, volgens de financieringslastnormen van de overheid:

- 1,1% = € 135.718 = € 2800
- 10,8% = € 200.677 = € 4200
- 25,5% = € 246.652 = € 4900
- 52,4% = € 301.620 = € 5700
- 75,4% = € 377.955 = € 6700
- 90,1% = € 488.296 = € 8400
- 98,9% = € 811.679 = € 13700

# TODO:

* Verbeteren van de loonschatting op basis van de hypotheek door middel van de inverse van de financieringslastnormen.
* De zoek-configuratie in een array zetten.
* Opgehaalde gegevens in een databaseje opslaan.
* Kaart maken van gevonden gegevens.
* Grafieken plotten.