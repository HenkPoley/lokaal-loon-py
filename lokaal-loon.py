#!/usr/bin/env python3

import requests


# bedrijfslocatie = f'heel-Nederland'
# bedrijfslocatie = f'amsterdam'
bedrijfslocatie = f'amsterdam/straat-piet-heinkade'

# Hoe wil je in de markt staan. Hoe bekwaam wil je dat je werknemers zijn?

# NB: Woningprijzen in Nederland stijgen vanaf 10% tot 70% van de markt vrij lineair.
# Onder de 8-10% bevinden zich waarschijnlijk de minder aantrekkelijke woningen.
# Boven de 70% zijn waarschijnlijk de woningen van het kaliber waar mensen veel geld voor willen betalen.

# Een percentage lager dan 10% betekent effectief dat je daklozen voor je wilt laten werken.
# In dit prijssegment vind je meestal serviceflats voor ouderen, en bouwvallige kluswoningen.
# gewenst_werknemerscapaciteit_percentage = 10
# Het midden van het 10% tot 70% segment:
gewenst_werknemerscapaciteit_percentage = 40
# gewenst_werknemerscapaciteit_percentage = 70
# Boven dit punt wijkt de verhouding tussen percentage en woningprijs af van lineair.


def check_funda(kamers_min=1, kamers_max=2, prijs_max=999999, locatie='heel-Nederland', reisafstand_max=15):
    cookies = {

    }

    headers = {
        'authority': 'www.funda.nl',
        'accept': '*/*',
        'accept-language': 'en-NL,en;q=0.9,nl-NL;q=0.8,nl;q=0.7,en-US;q=0.6,de;q=0.5,ru;q=0.4,it;q=0.3',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://www.funda.nl',
        'referer': f'https://www.funda.nl/koop/{locatie}/sorteer-datum-af/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    # filter_AantalKamers-range-min: 1
    # filter_AantalKamers-range-max: 2
    woonoppervlakte_min = 36  # 39
    woonoppervlakte_max = 54  # 50
    data = f'filter_location={locatie}&autocomplete-identifier={locatie}&filter_Straal={reisafstand_max}&filter_ZoekType=koop&filter_ZoekType=koop&filter_WijkNaam=active&filter_KoopprijsVan=0&filter_KoopprijsVan=&filter_KoopprijsTot={prijs_max}&filter_KoopprijsTot=&filter_SoortObject=&filter_WoningSoort=active&filter_WoningType=active&filter_SoortAppartementId=active&filter_AppartementType=active&filter_SoortParkeergelegenheidId=active&filter_AutoCapaciteitParkeergelegenheid=&filter_IndBouwrijp=&filter_PublicatieDatum=&filter_WoonOppervlakte=&filter_WoonOppervlakte-range-min={woonoppervlakte_min}&filter_WoonOppervlakte-range-max={woonoppervlakte_max}&filter_PerceelOppervlakte=&filter_PerceelOppervlakte-range-min=&filter_PerceelOppervlakte-range-max=&filter_AantalKamers=&filter_AantalKamers-range-min=&filter_AantalKamers-range-max=&filter_AantalSlaapkamers=&filter_LiggingTuin=active&filter_Tuinoppervlakte=&filter_BouwPeriodeId=active&filter_Ligging=active&filter_BouwvormId=&filter_SoortGarage=active&filter_AutoCapaciteitGarage=&filter_AanwezigheidVan=active&filter_Toegankelijkheid=active&filter_Energielabel=active&filter_ZoekType=koop&filter_IndicatiePDF=active&filter_OpenHuizen=&filter_VeilingDatum=&filter_VirtueleOpenHuizen=&sort=sorteer-datum_Descending&search-map-type-control-top=default&pagination-page-number-next=2&filter_AantalKamers-range-min={kamers_min}&filter_AantalKamers-range-max={kamers_max}&'

    response = requests.post(f'https://www.funda.nl/koop/{locatie}/beschikbaar/sorteer-datum-af/',
                             cookies=cookies,
                             headers=headers,
                             data=data)

    totaal = response.json()['content']['total']

    totaal_number_string = totaal.split()[0]
    totaal_number = int(totaal_number_string.replace('.', ''))
    return totaal_number


def benader_percentage(locatie='heel-Nederland', gewenst_percentage=50.0):
    min_prijs = 1_920 * 12 * 4  # 4 jaarsalarissen bij minimumloon in 2023
    prijs_gok = 300_000         # Dicht bij de 50% in 2023
    max_prijs = 2_503_952 * 2   # Twee keer de 99.99% in 2023
    # max_prijs = 4_391_830     # 99.999% in 2023

    max_totaal_aantal_huizen = check_funda(1, 2, max_prijs, locatie)
    print(f"Gevonden aantal huizen van dit type: {max_totaal_aantal_huizen}")
    print()

    for i in range(20):
        aantal_huizen = check_funda(1, 2, prijs_gok, locatie)
        huidig_percentage = aantal_huizen / max_totaal_aantal_huizen * 100
        print(
            f"{i+1}: min: {min_prijs} prijs_gok: € {prijs_gok} max: {max_prijs} aantal_huizen: {aantal_huizen} percentage: {huidig_percentage :.1f}%")

        if abs(huidig_percentage - gewenst_percentage) < 0.1:
            return prijs_gok

        min_plus_max_prijs = (max_prijs + min_prijs)
        if huidig_percentage > gewenst_percentage:
            max_prijs = prijs_gok
            prijs_gok = min_plus_max_prijs // 2
        else:
            min_prijs = prijs_gok
            prijs_gok = min_plus_max_prijs // 2

    return prijs_gok


huizen_prijs = benader_percentage(
    bedrijfslocatie,
    gewenst_werknemerscapaciteit_percentage)

print()
print(f"Om een minimaal salarisadvies op {gewenst_werknemerscapaciteit_percentage}% niveau "
      f"niveau te bereiken rondom {bedrijfslocatie}, moet geprobeerd worden om € {huizen_prijs} "
      f"te benaderen bij het veld 'maximale hypotheek' (C23) in de Excel sheet "
      f"'Bijlage financieringslastnormen 2023', dat te vinden is op de website van het NIBUD: "
      f"https://www.nibud.nl/onderzoeksrapporten/rapport-advies-financieringslastnormen-2023-2022/")

# TODO: Dit is een zeer groffe schatting.

groffe_schatting_maandsalaris = huizen_prijs / 12.0 / 4.0
print()
print(f"Een ruwe schatting van het maandsalaris dat nodig is voor een werknemer op "
      f"{gewenst_werknemerscapaciteit_percentage}% van de looncurve, is "
      f"€ {groffe_schatting_maandsalaris :.2f}")

loon_bij_huren = huizen_prijs / 240.0 * 3.5
jaarloon_bij_huren = loon_bij_huren * 12.0 * 1.06
print()
print(f"Het inkomen om in aanmerking te komen voor een huurwoning, waarbij de verhuurder de woning in "
      f"240 maanden wil afbetalen, en loonstroken van 3,5 keer de maandelijkse huur verlangt: bruto "
      f"€ {loon_bij_huren :.2f}, Het jaarlijkse toetsingsinkomen is dan € {jaarloon_bij_huren :.0f}")
