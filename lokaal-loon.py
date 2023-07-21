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
    # https://rijksoverheid.bouwbesluit.com/Inhoud/docs/wet/bb2003_nvt/artikelsgewijs/hfd4/afd4-5
    # Daarom zijn er minimum eisen gesteld aan het in het hoofdgedeelte van de woning aanwezige verblijfsgebied. Is het verblijfsgebied van een in een woongebouw gelegen woning kleiner dan 24 m², dan moet het gemeenschappelijk verblijfsgebied waarop die woning is aangewezen ten minste 18 m² zijn.
    woonoppervlakte_min = 24  # 24
    woonoppervlakte_max = 54  # 54 = 1,5 x 36

    # my_dict = {
    #     'filter_location': f'{locatie}',
    #     'autocomplete-identifier': f'{locatie}',
    #     'filter_Straal': f'{reisafstand_max}',
    #     'filter_ZoekType': 'koop',  # 1ste filter_ZoekType
    #     'filter_ZoekType': 'koop',  # 2de  filter_ZoekType
    #     'filter_WijkNaam': 'active',
    #     'filter_KoopprijsVan': '0',
    #     'filter_KoopprijsVan': '',
    #     'filter_KoopprijsTot': f'{prijs_max}',
    #     'filter_KoopprijsTot': '',
    #     'filter_SoortObject': '',
    #     'filter_WoningSoort': 'active',
    #     'filter_WoningType': 'active',
    #     'filter_SoortAppartementId': 'active',
    #     'filter_AppartementType': 'active',
    #     'filter_SoortParkeergelegenheidId': 'active',
    #     'filter_AutoCapaciteitParkeergelegenheid': '',
    #     'filter_IndBouwrijp': '',
    #     'filter_PublicatieDatum': '',
    #     'filter_WoonOppervlakte': '',
    #     'filter_WoonOppervlakte-range-min': f'{woonoppervlakte_min}',
    #     'filter_WoonOppervlakte-range-max': f'{woonoppervlakte_max}',
    #     'filter_PerceelOppervlakte': '',
    #     'filter_PerceelOppervlakte-range-min': '',
    #     'filter_PerceelOppervlakte-range-max': '',
    #     'filter_AantalKamers': '',
    #     'filter_AantalKamers-range-min': '',
    #     'filter_AantalKamers-range-max': '',
    #     'filter_AantalSlaapkamers': '',
    #     'filter_LiggingTuin': 'active',
    #     'filter_Tuinoppervlakte': '',
    #     'filter_BouwPeriodeId': 'active',
    #     'filter_Ligging': 'active',
    #     'filter_BouwvormId': '',
    #     'filter_SoortGarage': 'active',
    #     'filter_AutoCapaciteitGarage': '',
    #     'filter_AanwezigheidVan': 'active',
    #     'filter_Toegankelijkheid': 'active',
    #     'filter_Energielabel': 'active',
    #     'filter_ZoekType': 'koop',  # 3rde filter_ZoekType
    #     'filter_IndicatiePDF': 'active',
    #     'filter_OpenHuizen': '',
    #     'filter_VeilingDatum': '',
    #     'filter_VirtueleOpenHuizen': '',
    #     'sort': 'sorteer-datum_Descending',
    #     'search-map-type-control-top': 'default',
    #     'pagination-page-number-next': '2',
    #     'filter_AantalKamers-range-min': f'{kamers_min}',
    #     'filter_AantalKamers-range-max': f'{kamers_max}'
    # }

    # data = '&'.join(f'{key}={value}' for key, value in my_dict.items())

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

        if abs(huidig_percentage - gewenst_percentage) < ((1.0 / max_totaal_aantal_huizen) / 2.0):
            return prijs_gok

        prijs_gok_oud = prijs_gok
        
        if huidig_percentage > gewenst_percentage:
            max_prijs = prijs_gok
            prijs_gok = (max_prijs + min_prijs) // 2
            if(abs(prijs_gok_oud - prijs_gok) < 500):
                return prijs_gok_oud
        else:
            min_prijs = prijs_gok
            prijs_gok = (max_prijs + min_prijs) // 2
            if(abs(prijs_gok_oud - prijs_gok) < 500):
                return prijs_gok_oud

    return prijs_gok_oud


def print_hypotheek_salaris_schatting(huizen_prijs):
    print()
    print(f"Om een minimaal salarisadvies op {gewenst_werknemerscapaciteit_percentage}% niveau "
          f"niveau te bereiken rondom {bedrijfslocatie}, moet geprobeerd worden om € {huizen_prijs} "
          f"te benaderen bij het veld 'maximale hypotheek' (C23) in de Excel sheet "
          f"'Bijlage financieringslastnormen 2023', dat te vinden is op de website van het NIBUD: "
          f"https://www.nibud.nl/onderzoeksrapporten/rapport-advies-financieringslastnormen-2023-2022/")

    # Het eerste eenvoudige stuk in de NIBUD sheet.
    if huizen_prijs <= 81247:
        schatting_jaarlijks_toetsingsinkomen = huizen_prijs / 3.1248

    # a = 0.094985, b = 18361.197
    if (huizen_prijs > 81247) and (huizen_prijs <= 120884):
        schatting_jaarlijks_toetsingsinkomen = 18361 + huizen_prijs * 0.094985

    # Het tweede eenvoudige stuk in de NIBUD sheet.
    if (huizen_prijs > 120884) and (huizen_prijs < 226143):
        schatting_jaarlijks_toetsingsinkomen = huizen_prijs / 4.0295

    # Er zitten rare sprongetjes in, en een kleine kromme in het begin, maar dit de benadering.
    # a = 0.171712, b = 15846.485
    # y = ax + b
    if (huizen_prijs >= 226143) and (huizen_prijs <= 542734):
        schatting_jaarlijks_toetsingsinkomen = 15846 + huizen_prijs * 0.171712

    # Het derde eenvoudige stuk in de NIBUD sheet.
    if (huizen_prijs >= 542734):
        schatting_jaarlijks_toetsingsinkomen = huizen_prijs / 4.9340

    schatting_maandsalaris = schatting_jaarlijks_toetsingsinkomen / 12.0 / 1.06
    schatting_uurloon = schatting_maandsalaris / 173
    print()
    print(f"Een schatting van het maandsalaris dat nodig is voor een werknemer op "
          f"{gewenst_werknemerscapaciteit_percentage}% van de looncurve is bruto "
          f"€ {schatting_maandsalaris :.2f} (uurloon op basis van 40 uur per week " 
          f"€ {schatting_uurloon :.2f}). Het jaarlijkse toetsingsinkomen is dan "
          f"€ {schatting_jaarlijks_toetsingsinkomen :.0f}. Bij een hypotheekrente van 4.5%.")

# TODO: Eigenlijk is dit 1/3rde van het netto loon, en dan omrekenen naar bruto.
def print_huur_salaris_schatting(huizen_prijs):
    loon_bij_huren = huizen_prijs / 240.0 * 3
    schatting_netto_jaarlijks_toetsingsinkomen = loon_bij_huren * 12.0 * 1.06
    print()
    print(f"NB: De berekening hier klopt niet, want huren in Nederland is duurder dan kopen met 100% hypotheek."
          f"Het inkomen om in aanmerking te komen voor een huurwoning, waarbij de verhuurder de woning in "
          f"240 maanden wil afbetalen, en loonstroken van 3 keer de maandelijkse huur verlangt: netto "
          f"€ {loon_bij_huren :.2f} per maand. Het jaarlijkse 'netto toetsingsinkomen' is dan "
          f"€ {schatting_netto_jaarlijks_toetsingsinkomen :.0f} + belasting (TODO)")


huizen_prijs = benader_percentage(
    bedrijfslocatie,
    gewenst_werknemerscapaciteit_percentage)

print_hypotheek_salaris_schatting(huizen_prijs)
#print_huur_salaris_schatting(huizen_prijs)
