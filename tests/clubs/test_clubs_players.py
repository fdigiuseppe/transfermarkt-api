import pytest
from fastapi import HTTPException

from app.services.clubs.players import TransfermarktClubPlayers


def test_clubs_players_id_0():
    tfmkt = TransfermarktClubPlayers(club_id="0")

    with pytest.raises(HTTPException):
        tfmkt.get_club_players()


def test_clubs_players_id_210_season_2017():
    tfmkt = TransfermarktClubPlayers(club_id="210", season_id="2017")
    result = tfmkt.get_club_players()

    expected = {
        "id": "210",
        "clubName": "Grêmio Foot-Ball Porto Alegrense",
        "seasonYear": "2017",
        "players": [
            {
                "id": "52313",
                "name": "Marcelo Grohe",
                "position": "Goalkeeper",
                "dateOfBirth": "Jan 13, 1987",
                "age": "31",
                "nationality": ["Brazil", "Italy"],
                "currentClub": "Ittihad Club",
                "height": "1,88m",
                "foot": "right",
                "joinedOn": "Jan 1, 2004",
                "signedFrom": "Grêmio FBPA U20",
                "contract": "Jun 30, 2024",
                "marketValue": "€4.00m",
            },
            {
                "id": "67886",
                "name": "Paulo Victor",
                "position": "Goalkeeper",
                "dateOfBirth": "Jan 12, 1987",
                "age": "31",
                "nationality": ["Brazil", "Italy"],
                "currentClub": "Al-Ettifaq FC",
                "height": "1,87m",
                "foot": "left",
                "joinedOn": "Jul 13, 2017",
                "signedFrom": "CR Flamengo",
                "contract": "Jun 30, 2025",
                "marketValue": "€900k",
            },
            {
                "id": "95747",
                "name": "Bruno Grassi",
                "position": "Goalkeeper",
                "dateOfBirth": "Mar 5, 1987",
                "age": "31",
                "nationality": ["Brazil", "Italy"],
                "currentClub": "Al-Ain FC",
                "height": "1,92m",
                "foot": "right",
                "joinedOn": "Apr 23, 2015",
                "signedFrom": "EC Cruzeiro",
                "contract": "Jun 30, 2024",
                "marketValue": "€100k",
            },
            {
                "id": "288415",
                "name": "Léo Jardim",
                "position": "Goalkeeper",
                "dateOfBirth": "Mar 20, 1995",
                "age": "23",
                "nationality": ["Brazil", "Italy"],
                "currentClub": "Clube de Regatas Vasco da Gama",
                "height": "1,88m",
                "foot": "right",
                "joinedOn": "Jan 1, 2015",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "Dec 31, 2025",
                "marketValue": "€100k",
            },
            {
                "id": "555016",
                "name": "Brenno",
                "position": "Goalkeeper",
                "dateOfBirth": "Apr 1, 1999",
                "age": "19",
                "nationality": ["Brazil"],
                "currentClub": "Grêmio Foot-Ball Porto Alegrense",
                "height": "1,90m",
                "foot": "right",
                "joinedOn": "Jan 1, 2019",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "Dec 31, 2024",
                "marketValue": "-",
            },
            {
                "id": "32568",
                "name": "Pedro Geromel",
                "position": "Centre-Back",
                "dateOfBirth": "Sep 21, 1985",
                "age": "32",
                "nationality": ["Brazil", "Italy"],
                "currentClub": "Grêmio Foot-Ball Porto Alegrense",
                "height": "1,90m",
                "foot": "right",
                "joinedOn": "Jan 1, 2016",
                "signedFrom": "1.FC Köln",
                "contract": "Dec 31, 2023",
                "marketValue": "€5.00m",
            },
            {
                "id": "145400",
                "name": "Walter Kannemann",
                "position": "Centre-Back",
                "dateOfBirth": "Mar 14, 1991",
                "age": "27",
                "nationality": ["Argentina", "Italy"],
                "currentClub": "Grêmio Foot-Ball Porto Alegrense",
                "height": "1,84m",
                "foot": "left",
                "joinedOn": "Jul 15, 2016",
                "signedFrom": "Atlas Guadalajara",
                "contract": "Dec 31, 2023",
                "marketValue": "€2.50m",
            },
            {
                "id": "52844",
                "name": "Marcelo Oliveira",
                "position": "Centre-Back",
                "dateOfBirth": "Mar 29, 1987",
                "age": "31",
                "nationality": ["Brazil"],
                "currentClub": "Retired",
                "height": "1,84m",
                "foot": "left",
                "joinedOn": "Jan 1, 2015",
                "signedFrom": "Cruzeiro Esporte Clube",
                "contract": "-",
                "marketValue": "€1.00m",
            },
            {
                "id": "80499",
                "name": "Paulo Miranda",
                "position": "Centre-Back",
                "dateOfBirth": "Aug 16, 1988",
                "age": "29",
                "nationality": ["Brazil"],
                "currentClub": "Without Club",
                "height": "1,84m",
                "foot": "right",
                "joinedOn": "Jan 5, 2018",
                "signedFrom": ": Ablöse €800k",
                "contract": "-",
                "marketValue": "€1.00m",
            },
            {
                "id": "256453",
                "name": "Bressan",
                "position": "Centre-Back",
                "dateOfBirth": "Jan 15, 1993",
                "age": "25",
                "nationality": ["Brazil", "Italy"],
                "currentClub": "Nantong Zhiyun",
                "height": "1,85m",
                "foot": "right",
                "joinedOn": "Jan 1, 2013",
                "signedFrom": "Esporte Clube Juventude",
                "contract": "Dec 31, 2024",
                "marketValue": "€1.00m",
            },
            {
                "id": "292152",
                "name": "Rafael Thyere",
                "position": "Centre-Back",
                "dateOfBirth": "May 17, 1993",
                "age": "25",
                "nationality": ["Brazil"],
                "currentClub": "Sport Club do Recife",
                "height": "1,90m",
                "foot": "right",
                "joinedOn": "Oct 1, 2013",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "Dec 31, 2024",
                "marketValue": "€700k",
            },
            {
                "id": "445101",
                "name": "Rodrigues",
                "position": "Centre-Back",
                "dateOfBirth": "Oct 10, 1997",
                "age": "20",
                "nationality": ["Brazil"],
                "currentClub": "Grêmio Foot-Ball Porto Alegrense",
                "height": "1,88m",
                "foot": "right",
                "joinedOn": "Aug 9, 2019",
                "joined": "Returned after loan spell with San Jose Earthquakes; date: Aug 2, 2023; fee: End of loan",
                "signedFrom": "ABC Futebol Clube (RN)",
                "contract": "Dec 31, 2024",
                "marketValue": "€200k",
            },
            {
                "id": "216071",
                "name": "Gabriel",
                "position": "Centre-Back",
                "dateOfBirth": "Feb 28, 1989",
                "age": "29",
                "nationality": ["Brazil"],
                "currentClub": "Without Club",
                "height": "1,91m",
                "foot": "right",
                "joinedOn": "Jan 1, 2015",
                "signedFrom": "CE Lajeadense",
                "contract": "-",
                "marketValue": "€100k",
                "status": "Knee Surgery - Return unknown",
            },
            {
                "id": "68679",
                "name": "Bruno Rodrigo",
                "position": "Centre-Back",
                "dateOfBirth": "Apr 12, 1985",
                "age": "33",
                "nationality": ["Brazil"],
                "currentClub": "Retired",
                "height": "1,86m",
                "foot": "right",
                "joinedOn": "Mar 8, 2017",
                "signedFrom": "Without Club",
                "contract": "-",
                "marketValue": "-",
            },
            {
                "id": "476366",
                "name": "Denilson",
                "position": "Centre-Back",
                "dateOfBirth": "Apr 18, 1995",
                "age": "23",
                "nationality": ["Brazil"],
                "currentClub": "Clube Náutico Capibaribe",
                "height": "1,87m",
                "foot": "right",
                "joinedOn": "-",
                "contract": "-",
                "marketValue": "-",
            },
            {
                "id": "539183",
                "name": "Anderson",
                "position": "Centre-Back",
                "dateOfBirth": "Mar 2, 1995",
                "age": "23",
                "nationality": ["Brazil"],
                "currentClub": "FC Vizela",
                "height": "1,86m",
                "foot": "right",
                "joinedOn": "-",
                "contract": "Jun 30, 2024",
                "marketValue": "-",
            },
            {
                "id": "555015",
                "name": "Ruan Tressoldi",
                "position": "Centre-Back",
                "dateOfBirth": "Jun 7, 1999",
                "age": "19",
                "nationality": ["Brazil"],
                "currentClub": "US Sassuolo",
                "height": "1,87m",
                "foot": "right",
                "joinedOn": "Aug 12, 2021",
                "signedFrom": "US Sassuolo",
                "contract": "Jun 30, 2026",
                "marketValue": "-",
            },
            {
                "id": "555634",
                "name": "Derlan",
                "position": "Centre-Back",
                "dateOfBirth": "Feb 3, 1996",
                "age": "22",
                "nationality": ["Brazil"],
                "currentClub": "Oita Trinita",
                "height": "1,87m",
                "foot": "left",
                "joinedOn": "-",
                "contract": "Jan 31, 2025",
                "marketValue": "-",
            },
            {
                "id": "689524",
                "name": "Mendonça",
                "position": "Centre-Back",
                "dateOfBirth": "Aug 15, 1995",
                "age": "22",
                "nationality": ["Brazil"],
                "currentClub": "EC Democrata",
                "height": "1,94m",
                "foot": "left",
                "joinedOn": "-",
                "contract": "-",
                "marketValue": "-",
            },
            {
                "id": "182216",
                "name": "Bruno Cortez",
                "position": "Left-Back",
                "dateOfBirth": "Mar 11, 1987",
                "age": "31",
                "nationality": ["Brazil"],
                "currentClub": "Avaí FC",
                "height": "1,79m",
                "foot": "left",
                "joinedOn": "Jan 30, 2017",
                "signedFrom": "São Paulo Futebol Clube",
                "contract": "Nov 30, 2023",
                "marketValue": "€1.75m",
            },
            {
                "id": "406676",
                "name": "Juninho Capixaba",
                "position": "Left-Back",
                "dateOfBirth": "Jul 6, 1997",
                "age": "20",
                "nationality": ["Brazil"],
                "currentClub": "Red Bull Bragantino",
                "height": "1,76m",
                "foot": "left",
                "joinedOn": "May 17, 2019",
                "signedFrom": "Sport Club Corinthians Paulista",
                "contract": "Dec 31, 2026",
                "marketValue": "€900k",
            },
            {
                "id": "322781",
                "name": "Breno Lorran",
                "position": "Left-Back",
                "dateOfBirth": "Mar 6, 1995",
                "age": "23",
                "nationality": ["Brazil"],
                "currentClub": "Without Club",
                "height": "1,74m",
                "foot": "left",
                "joinedOn": "Jul 1, 2013",
                "signedFrom": "Red Bull Brasil (SP)",
                "contract": "-",
                "marketValue": "€600k",
            },
            {
                "id": "552548",
                "name": "Guilherme Guedes",
                "position": "Left-Back",
                "dateOfBirth": "May 18, 1999",
                "age": "19",
                "nationality": ["Brazil"],
                "currentClub": "Ypiranga FC",
                "height": "1,77m",
                "foot": "left",
                "joinedOn": "Jan 1, 2020",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "Nov 30, 2023",
                "marketValue": "-",
            },
            {
                "id": "75083",
                "name": "Edílson",
                "position": "Right-Back",
                "dateOfBirth": "Jul 27, 1986",
                "age": "31",
                "nationality": ["Brazil"],
                "currentClub": "Without Club",
                "height": "1,77m",
                "foot": "right",
                "joinedOn": "Apr 1, 2022",
                "signedFrom": "Avaí FC",
                "contract": "-",
                "marketValue": "€1.50m",
            },
            {
                "id": "177845",
                "name": "Madson",
                "position": "Right-Back",
                "dateOfBirth": "Jan 13, 1992",
                "age": "26",
                "nationality": ["Brazil"],
                "currentClub": "Club Athletico Paranaense",
                "height": "1,82m",
                "foot": "right",
                "joinedOn": "Jan 1, 2018",
                "signedFrom": "Clube de Regatas Vasco da Gama",
                "contract": "Dec 31, 2024",
                "marketValue": "€1.25m",
            },
            {
                "id": "29368",
                "name": "Léo Moura",
                "position": "Right-Back",
                "dateOfBirth": "Oct 23, 1978",
                "age": "39",
                "nationality": ["Brazil"],
                "currentClub": "Retired",
                "height": "1,76m",
                "foot": "right",
                "joinedOn": "Jan 16, 2017",
                "signedFrom": "Santa Cruz Futebol Clube (PE)",
                "contract": "-",
                "marketValue": "€500k",
            },
            {
                "id": "347016",
                "name": "Léo Gomes",
                "position": "Right-Back",
                "dateOfBirth": "Mar 30, 1996",
                "age": "22",
                "nationality": ["Brazil"],
                "currentClub": "Without Club",
                "height": "1,78m",
                "foot": "right",
                "joinedOn": "Jan 16, 2017",
                "signedFrom": "Boa EC",
                "contract": "-",
                "marketValue": "€200k",
            },
            {
                "id": "555012",
                "name": "Felipe Albuquerque",
                "position": "Right-Back",
                "dateOfBirth": "Sep 27, 1999",
                "age": "18",
                "nationality": ["Brazil"],
                "currentClub": "Associação Chapecoense de Futebol",
                "height": "1,74m",
                "foot": "right",
                "joinedOn": "-",
                "contract": "Nov 30, 2023",
                "marketValue": "-",
            },
            {
                "id": "366948",
                "name": "Jailson",
                "position": "Defensive Midfield",
                "dateOfBirth": "Sep 7, 1995",
                "age": "22",
                "nationality": ["Brazil"],
                "currentClub": "Sociedade Esportiva Palmeiras",
                "height": "1,87m",
                "foot": "right",
                "joinedOn": "-",
                "contract": "Dec 31, 2023",
                "marketValue": "€2.50m",
            },
            {
                "id": "435186",
                "name": "Michel",
                "position": "Defensive Midfield",
                "dateOfBirth": "Mar 22, 1990",
                "age": "28",
                "nationality": ["Brazil"],
                "currentClub": "Without Club",
                "height": "1,75m",
                "foot": "both",
                "joinedOn": "Jan 1, 2018",
                "signedFrom": "Grêmio Novorizontino",
                "contract": "-",
                "marketValue": "€1.50m",
            },
            {
                "id": "346705",
                "name": "Balbino",
                "position": "Defensive Midfield",
                "dateOfBirth": "Jan 19, 1997",
                "age": "21",
                "nationality": ["Brazil"],
                "currentClub": "Real Noroeste CFC",
                "height": "1,82m",
                "foot": "left",
                "joinedOn": "-",
                "contract": "-",
                "marketValue": "€100k",
            },
            {
                "id": "376867",
                "name": "Moisés Gaúcho",
                "position": "Defensive Midfield",
                "dateOfBirth": "Sep 24, 1994",
                "age": "23",
                "nationality": ["Brazil"],
                "currentClub": "Londrina Esporte Clube (PR)",
                "height": "1,81m",
                "foot": "right",
                "joinedOn": "-",
                "contract": "Dec 31, 2023",
                "marketValue": "€100k",
            },
            {
                "id": "405727",
                "name": "Kaio",
                "position": "Defensive Midfield",
                "dateOfBirth": "Mar 18, 1995",
                "age": "23",
                "nationality": ["Brazil"],
                "currentClub": "Associação Chapecoense de Futebol",
                "height": "1,73m",
                "foot": "right",
                "joinedOn": "Jan 1, 2016",
                "signedFrom": "Grêmio FBPA U20",
                "contract": "Dec 31, 2023",
                "marketValue": "€100k",
            },
            {
                "id": "520629",
                "name": "Filipe Machado",
                "position": "Defensive Midfield",
                "dateOfBirth": "Jan 20, 1996",
                "age": "22",
                "nationality": ["Brazil"],
                "currentClub": "Cruzeiro Esporte Clube",
                "height": "1,74m",
                "foot": "right",
                "joinedOn": "-",
                "contract": "Dec 31, 2024",
                "marketValue": "€50k",
            },
            {
                "id": "643282",
                "name": "Rodrigo Ancheta",
                "position": "Defensive Midfield",
                "dateOfBirth": "Jan 2, 1997",
                "age": "21",
                "nationality": ["Uruguay", "Brazil"],
                "currentClub": "Independente EC",
                "height": "1,85m",
                "foot": "right",
                "joinedOn": "-",
                "contract": "-",
                "marketValue": "-",
            },
            {
                "id": "362842",
                "name": "Arthur Melo",
                "position": "Central Midfield",
                "dateOfBirth": "Aug 12, 1996",
                "age": "21",
                "nationality": ["Brazil"],
                "currentClub": "ACF Fiorentina",
                "height": "1,72m",
                "foot": "right",
                "joinedOn": "Jan 1, 2017",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "Jun 30, 2024",
                "marketValue": "€30.00m",
            },
            {
                "id": "258070",
                "name": "Ramiro",
                "position": "Central Midfield",
                "dateOfBirth": "May 22, 1993",
                "age": "25",
                "nationality": ["Brazil", "Italy"],
                "currentClub": "Cruzeiro Esporte Clube",
                "height": "1,69m",
                "foot": "right",
                "joinedOn": "Jan 1, 2013",
                "signedFrom": "Esporte Clube Juventude",
                "contract": "Dec 31, 2024",
                "marketValue": "€5.00m",
                "status": "Cruciate Ligament Surgery - Return unknown",
            },
            {
                "id": "229736",
                "name": "Alisson",
                "position": "Central Midfield",
                "dateOfBirth": "Jun 25, 1993",
                "age": "25",
                "nationality": ["Brazil"],
                "currentClub": "São Paulo Futebol Clube",
                "height": "1,74m",
                "foot": "right",
                "joinedOn": "Jan 1, 2018",
                "signedFrom": "Cruzeiro Esporte Clube",
                "contract": "Dec 31, 2024",
                "marketValue": "€2.50m",
            },
            {
                "id": "17663",
                "name": "Cícero",
                "position": "Central Midfield",
                "dateOfBirth": "Aug 26, 1984",
                "age": "33",
                "nationality": ["Brazil"],
                "currentClub": "Retired",
                "height": "1,81m",
                "foot": "left",
                "joinedOn": "Sep 29, 2017",
                "signedFrom": "Fluminense Football Club",
                "contract": "-",
                "marketValue": "€2.00m",
            },
            {
                "id": "50047",
                "name": "Maicon",
                "position": "Central Midfield",
                "dateOfBirth": "Sep 14, 1985",
                "age": "32",
                "nationality": ["Brazil"],
                "currentClub": "Without Club",
                "height": "1,84m",
                "foot": "right",
                "joinedOn": "Aug 30, 2021",
                "signedFrom": "São Paulo Futebol Clube",
                "contract": "-",
                "marketValue": "€1.75m",
            },
            {
                "id": "392487",
                "name": "Thaciano",
                "position": "Central Midfield",
                "dateOfBirth": "May 12, 1995",
                "age": "23",
                "nationality": ["Brazil"],
                "currentClub": "Esporte Clube Bahia",
                "height": "1,82m",
                "foot": "right",
                "joinedOn": "Jul 1, 2019",
                "signedFrom": "Boa EC",
                "contract": "Dec 31, 2025",
                "marketValue": "€200k",
            },
            {
                "id": "552549",
                "name": "Matheus Henrique",
                "position": "Central Midfield",
                "dateOfBirth": "Dec 19, 1997",
                "age": "20",
                "nationality": ["Brazil"],
                "currentClub": "US Sassuolo",
                "height": "1,75m",
                "foot": "right",
                "joinedOn": "Sep 27, 2018",
                "signedFrom": "AD São Caetano (SP)",
                "contract": "Jun 30, 2026",
                "marketValue": "€50k",
            },
            {
                "id": "313106",
                "name": "Luan",
                "position": "Attacking Midfield",
                "dateOfBirth": "Mar 27, 1993",
                "age": "25",
                "nationality": ["Brazil"],
                "currentClub": "Grêmio Foot-Ball Porto Alegrense",
                "height": "1,80m",
                "foot": "right",
                "joinedOn": "Jul 27, 2023",
                "joined": "Joined from Sport Club Corinthians Paulista; date: Jul 27, 2023; fee: free transfer",
                "signedFrom": "Sport Club Corinthians Paulista",
                "contract": "Dec 31, 2023",
                "marketValue": "€20.00m",
            },
            {
                "id": "34332",
                "name": "Douglas",
                "position": "Attacking Midfield",
                "dateOfBirth": "Feb 18, 1982",
                "age": "36",
                "nationality": ["Brazil"],
                "currentClub": "Retired",
                "height": "1,76m",
                "foot": "left",
                "joinedOn": "Jan 24, 2017",
                "signedFrom": "Atlético Monte Azul (SP)",
                "contract": "-",
                "marketValue": "€600k",
            },
            {
                "id": "351738",
                "name": "Lincoln",
                "position": "Attacking Midfield",
                "dateOfBirth": "Nov 7, 1998",
                "age": "19",
                "nationality": ["Brazil"],
                "currentClub": "Fenerbahce",
                "height": "1,78m",
                "foot": "left",
                "joinedOn": "Feb 1, 2015",
                "signedFrom": "Grêmio FBPA U20",
                "contract": "Jun 30, 2026",
                "marketValue": "€500k",
                "status": "No eligibility -  - UEFA Europa Conference League Qualifiers",
            },
            {
                "id": "387611",
                "name": "Lima",
                "position": "Attacking Midfield",
                "dateOfBirth": "Jun 11, 1996",
                "age": "22",
                "nationality": ["Brazil"],
                "currentClub": "Fluminense Football Club",
                "height": "1,81m",
                "foot": "right",
                "joinedOn": "-",
                "contract": "Dec 31, 2025",
                "marketValue": "€400k",
            },
            {
                "id": "561214",
                "name": "Thonny  Anderson",
                "position": "Attacking Midfield",
                "dateOfBirth": "Dec 27, 1997",
                "age": "20",
                "nationality": ["Brazil"],
                "currentClub": "ABC Futebol Clube (RN)",
                "height": "1,84m",
                "foot": "left",
                "joinedOn": "Jan 3, 2019",
                "signedFrom": "Cruzeiro Esporte Clube",
                "contract": "Nov 30, 2023",
                "marketValue": "€400k",
            },
            {
                "id": "405726",
                "name": "Felipe Tontini",
                "position": "Attacking Midfield",
                "dateOfBirth": "Jul 16, 1995",
                "age": "22",
                "nationality": ["Brazil"],
                "currentClub": "Operário Ferroviário Esporte Clube (PR)",
                "height": "1,83m",
                "foot": "both",
                "joinedOn": "-",
                "contract": "-",
                "marketValue": "€200k",
            },
            {
                "id": "351903",
                "name": "Jean Pyerre",
                "position": "Attacking Midfield",
                "dateOfBirth": "May 7, 1998",
                "age": "20",
                "nationality": ["Brazil"],
                "currentClub": "Without Club",
                "height": "1,83m",
                "foot": "right",
                "joinedOn": "Jul 16, 2018",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "-",
                "marketValue": "-",
            },
            {
                "id": "529646",
                "name": "Patrick",
                "position": "Attacking Midfield",
                "dateOfBirth": "Nov 23, 1998",
                "age": "19",
                "nationality": ["Brazil"],
                "currentClub": "Grêmio Esportivo Brasil (RS)",
                "height": "1,75m",
                "foot": "left",
                "joinedOn": "May 26, 2019",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "Dec 31, 2023",
                "marketValue": "-",
            },
            {
                "id": "627099",
                "name": "Isaque",
                "position": "Attacking Midfield",
                "dateOfBirth": "Apr 22, 1997",
                "age": "21",
                "nationality": ["Brazil"],
                "currentClub": "Guarani Futebol Clube (SP)",
                "height": "1,78m",
                "foot": "right",
                "joinedOn": "Jan 1, 2020",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "Dec 31, 2023",
                "marketValue": "-",
            },
            {
                "id": "321239",
                "name": "Everton",
                "position": "Left Winger",
                "dateOfBirth": "Mar 22, 1996",
                "age": "22",
                "nationality": ["Brazil"],
                "currentClub": "CR Flamengo",
                "height": "1,74m",
                "foot": "right",
                "joinedOn": "Jan 1, 2014",
                "signedFrom": "Fortaleza Esporte Clube",
                "contract": "Jun 30, 2026",
                "marketValue": "€7.00m",
            },
            {
                "id": "76902",
                "name": "Fernandinho",
                "position": "Left Winger",
                "dateOfBirth": "Nov 25, 1985",
                "age": "32",
                "nationality": ["Brazil"],
                "currentClub": "Retrô FC Brasil",
                "height": "1,73m",
                "foot": "left",
                "joinedOn": "Jul 10, 2014",
                "signedFrom": "Al-Jazira (Abu Dhabi)",
                "contract": "Nov 30, 2023",
                "marketValue": "€1.20m",
            },
            {
                "id": "54183",
                "name": "Maicosuel",
                "position": "Left Winger",
                "dateOfBirth": "Jun 16, 1986",
                "age": "32",
                "nationality": ["Brazil"],
                "currentClub": "Retired",
                "height": "m",
                "foot": "N/A",
                "joinedOn": "Feb 8, 2018",
                "signedFrom": "São Paulo Futebol Clube",
                "contract": "-",
                "marketValue": "€1.00m",
            },
            {
                "id": "552547",
                "name": "Lucas Poletto",
                "position": "Left Winger",
                "dateOfBirth": "Mar 29, 1995",
                "age": "23",
                "nationality": ["Brazil", "Italy"],
                "currentClub": "Brusque Futebol Clube (SC)",
                "height": "1,81m",
                "foot": "right",
                "joinedOn": "Jan 1, 2018",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "Nov 30, 2023",
                "marketValue": "€50k",
            },
            {
                "id": "520636",
                "name": "Dionathã",
                "position": "Left Winger",
                "dateOfBirth": "Jan 24, 1998",
                "age": "20",
                "nationality": ["Brazil"],
                "currentClub": "EC Novo Hamburgo",
                "height": "1,74m",
                "foot": "both",
                "joinedOn": "Jan 1, 2018",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "-",
                "marketValue": "-",
            },
            {
                "id": "520662",
                "name": "Pepê",
                "position": "Left Winger",
                "dateOfBirth": "Feb 24, 1997",
                "age": "21",
                "nationality": ["Brazil", "Italy"],
                "currentClub": "FC Porto",
                "height": "1,75m",
                "foot": "right",
                "joinedOn": "May 1, 2017",
                "signedFrom": "Grêmio FBPA U20",
                "contract": "Jun 30, 2027",
                "marketValue": "-",
            },
            {
                "id": "74758",
                "name": "Marinho",
                "position": "Right Winger",
                "dateOfBirth": "May 29, 1990",
                "age": "28",
                "nationality": ["Brazil"],
                "currentClub": "Fortaleza Esporte Clube",
                "height": "1,69m",
                "foot": "left",
                "joinedOn": "Jun 30, 2018",
                "signedFrom": "Changchun Yatai",
                "contract": "Dec 31, 2025",
                "marketValue": "€1.20m",
            },
            {
                "id": "393839",
                "name": "Léo Tilica",
                "position": "Right Winger",
                "dateOfBirth": "Apr 20, 1995",
                "age": "23",
                "nationality": ["Brazil"],
                "currentClub": "Al-Najma SC",
                "height": "1,72m",
                "foot": "right",
                "joinedOn": "-",
                "contract": "Jun 18, 2024",
                "marketValue": "€100k",
            },
            {
                "id": "553470",
                "name": "Vico",
                "position": "Right Winger",
                "dateOfBirth": "Dec 3, 1996",
                "age": "21",
                "nationality": ["Brazil"],
                "currentClub": "Mirassol Futebol Clube (SP)",
                "height": "1,74m",
                "foot": "left",
                "joinedOn": "-",
                "contract": "Nov 30, 2023",
                "marketValue": "€50k",
            },
            {
                "id": "104509",
                "name": "André Felipe",
                "position": "Centre-Forward",
                "dateOfBirth": "Sep 27, 1990",
                "age": "27",
                "nationality": ["Brazil"],
                "currentClub": "Associação Atlética Ponte Preta",
                "height": "1,84m",
                "foot": "right",
                "joinedOn": "Feb 22, 2019",
                "signedFrom": "Sport Club do Recife",
                "contract": "Nov 30, 2023",
                "marketValue": "€3.50m",
            },
            {
                "id": "58516",
                "name": "Lucas Barrios",
                "position": "Centre-Forward",
                "dateOfBirth": "Nov 13, 1984",
                "age": "33",
                "nationality": ["Paraguay", "Argentina"],
                "currentClub": "Sportivo Luqueño",
                "height": "1,89m",
                "foot": "right",
                "joinedOn": "Feb 24, 2017",
                "signedFrom": "Sociedade Esportiva Palmeiras",
                "contract": "-",
                "marketValue": "€1.75m",
            },
            {
                "id": "195004",
                "name": "Hernane",
                "position": "Centre-Forward",
                "dateOfBirth": "Apr 8, 1986",
                "age": "32",
                "nationality": ["Brazil"],
                "currentClub": "Brasiliense FC",
                "height": "1,83m",
                "foot": "right",
                "joinedOn": "Feb 22, 2018",
                "signedFrom": "Esporte Clube Bahia",
                "contract": "-",
                "marketValue": "€1.50m",
            },
            {
                "id": "80815",
                "name": "Jael",
                "position": "Centre-Forward",
                "dateOfBirth": "Oct 30, 1988",
                "age": "29",
                "nationality": ["Brazil"],
                "currentClub": "Clube Náutico Capibaribe",
                "height": "1,86m",
                "foot": "right",
                "joinedOn": "Jan 18, 2017",
                "signedFrom": "Joinville Esporte Clube (SC)",
                "contract": "-",
                "marketValue": "€800k",
            },
            {
                "id": "203136",
                "name": "Yuri Mamute",
                "position": "Centre-Forward",
                "dateOfBirth": "May 7, 1995",
                "age": "23",
                "nationality": ["Brazil"],
                "currentClub": "Hai Phong FC",
                "height": "1,80m",
                "foot": "right",
                "joinedOn": "Jan 1, 2013",
                "signedFrom": "Grêmio Foot-Ball Porto Alegrense B (-2022)",
                "contract": "-",
                "marketValue": "€600k",
            },
            {
                "id": "379877",
                "name": "Luis Henrique",
                "position": "Centre-Forward",
                "dateOfBirth": "Mar 17, 1998",
                "age": "20",
                "nationality": ["Brazil", "Italy"],
                "currentClub": "Without Club",
                "height": "1,84m",
                "foot": "right",
                "joinedOn": "-",
                "contract": "-",
                "marketValue": "€400k",
            },
        ],
    }

    assert result == expected