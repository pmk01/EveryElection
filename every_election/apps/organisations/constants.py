PARENT_TO_CHILD_AREAS = {
    "DIS": ["DIW"],
    "MTD": ["MTW"],
    "CTY": ["CED"],
    "LBO": ["LBW"],
    "CED": ["CPC"],
    "UTA": ["UTW", "UTE"],
    "NIA": ["NIE"],
    "COI": ["COP"],
    "LGD": ["LGE"],
}
CHILD_TO_PARENT_AREAS = {
    "CED": "CTY",
    "COP": "COI",
    "CPC": "CED",
    "DIW": "DIS",
    "LBW": "LBO",
    "LGE": "LGD",
    "MTW": "MTD",
    "UTE": "UTA",
    "UTW": "UTA",
}

AREAS_WITHOUT_PCCS = ["metropolitan", "city-of-london", "northern-ireland"]


POLICE_AREA_NAME_TO_GSS = {
    "avon-and-somerset": [
        "E10000027",
        "E06000022",
        "E06000023",
        "E06000024",
        "E06000025",
    ],
    "bedfordshire": ["E06000055", "E06000056", "E06000032"],
    "cambridgeshire": ["E10000003", "E06000031"],
    "cheshire": ["E06000049", "E06000050", "E06000006", "E06000007"],
    "cleveland": ["E06000001", "E06000002", "E06000003", "E06000004"],
    "cumbria": ["E10000006"],
    "derbyshire": ["E10000007", "E06000015"],
    "devon-and-cornwall": [
        "E10000008",
        "E06000052",
        "E06000026",
        "E06000027",
        "E06000053",
    ],
    "dorset": ["E10000009", "E06000028", "E06000029"],
    "durham": ["E06000005", "E06000047"],
    "dyfed-powys": ["W06000008", "W06000010", "W06000009", "W06000023"],
    "essex": ["E10000012", "E06000033", "E06000034"],
    "gloucestershire": ["E10000013"],
    "warwickshire": ["E10000031"],
    "greater-manchester": [
        "E08000001",
        "E08000002",
        "E08000003",
        "E08000004",
        "E08000005",
        "E08000006",
        "E08000007",
        "E08000008",
        "E08000009",
        "E08000010",
    ],
    "gwent": ["W06000021", "W06000019", "W06000018", "W06000022", "W06000020"],
    "hampshire": ["E10000014", "E06000046", "E06000044", "E06000045"],
    "hertfordshire": ["E10000015"],
    "humberside": ["E06000011", "E06000012", "E06000013", "E06000010"],
    "kent": ["E10000016", "E06000035"],
    "lancashire": ["E10000017", "E06000008", "E06000009"],
    "leicestershire": ["E10000018", "E06000016", "E06000017"],
    "lincolnshire": ["E10000019"],
    "merseyside": ["E08000011", "E08000012", "E08000014", "E08000015", "E08000013"],
    "norfolk": ["E10000020"],
    "north-wales": [
        "W06000001",
        "W06000002",
        "W06000004",
        "W06000005",
        "W06000003",
        "W06000006",
    ],
    "north-yorkshire": ["E10000023", "E06000014"],
    "northamptonshire": ["E10000021"],
    "northumbria": [
        "E06000057",
        "E08000037",
        "E08000021",
        "E08000022",
        "E08000023",
        "E08000024",
    ],
    "nottinghamshire": ["E10000024", "E06000018"],
    "south-wales": [
        "W06000015",
        "W06000011",
        "W06000013",
        "W06000024",
        "W06000012",
        "W06000016",
        "W06000014",
    ],
    "south-yorkshire": ["E08000016", "E08000017", "E08000018", "E08000019"],
    "staffordshire": ["E10000028", "E06000021"],
    "suffolk": ["E10000029"],
    "surrey": ["E10000030"],
    "sussex": ["E10000011", "E10000032", "E06000043"],
    "thames-valley": [
        "E06000036",
        "E06000038",
        "E06000039",
        "E06000037",
        "E06000040",
        "E06000041",
        "E10000002",
        "E10000025",
        "E06000042",
    ],
    "west-mercia": ["E06000051", "E10000034", "E06000019", "E06000020"],
    "west-midlands": [
        "E08000025",
        "E08000026",
        "E08000027",
        "E08000028",
        "E08000029",
        "E08000030",
        "E08000031",
    ],
    "west-yorkshire": ["E08000032", "E08000033", "E08000034", "E08000035", "E08000036"],
    "wiltshire": ["E06000054", "E06000030"],
}

COMBINED_AUTHORITY_SLUG_TO_GSS = {
    "cambridgeshire-and-peterborough": [
        "E06000031",
        "E10000003",
        "E07000008",
        "E07000011",
        "E07000009",
        "E07000012",
        "E07000010",
    ],
    "greater-manchester-ca": [
        "E08000001",
        "E08000002",
        "E08000003",
        "E08000004",
        "E08000005",
        "E08000006",
        "E08000007",
        "E08000008",
        "E08000009",
        "E08000010",
    ],
    "liverpool-city-ca": [
        "E06000006",
        "E08000011",
        "E08000012",
        "E08000013",
        "E08000014",
        "E08000015",
    ],
    "sheffield-city-ca": ["E08000016", "E08000017", "E08000018", "E08000019"],
    "tees-valley": ["E06000005", "E06000001", "E06000002", "E06000003", "E06000004"],
    "west-midlands": [
        "E08000025",
        "E08000026",
        "E08000027",
        "E08000028",
        "E08000029",
        "E08000030",
        "E08000031",
    ],
    "west-of-england": ["E06000022", "E06000023", "E06000025"],
}


ORG_CURIE_TO_MAPIT_AREA_TYPE = {
    "local-authority-eng:ADU": "DIS",
    "local-authority-eng:ALL": "DIS",
    "local-authority-eng:AMB": "DIS",
    "local-authority-eng:ARU": "DIS",
    "local-authority-eng:ASF": "DIS",
    "local-authority-eng:ASH": "DIS",
    "local-authority-eng:AYL": "DIS",
    "local-authority-eng:BAB": "DIS",
    "local-authority-eng:BAE": "DIS",
    "local-authority-eng:BAI": "DIS",
    "local-authority-eng:BAN": "DIS",
    "local-authority-eng:BAR": "DIS",
    "local-authority-eng:BAS": "UTA",
    "local-authority-eng:BBD": "UTA",
    "local-authority-eng:BDF": "UTA",
    "local-authority-eng:BDG": "LBO",
    "local-authority-eng:BEN": "LBO",
    "local-authority-eng:BEX": "LBO",
    "local-authority-eng:BIR": "MTD",
    "local-authority-eng:BKM": "CTY",
    "local-authority-eng:BLA": "DIS",
    "local-authority-eng:BMH": "UTA",
    "local-authority-eng:BNE": "LBO",
    "local-authority-eng:BNH": "UTA",
    "local-authority-eng:BNS": "MTD",
    "local-authority-eng:BOL": "MTD",
    "local-authority-eng:BOS": "DIS",
    "local-authority-eng:BOT": "DIS",
    "local-authority-eng:BPL": "UTA",
    "local-authority-eng:BRA": "DIS",
    "local-authority-eng:BRC": "UTA",
    "local-authority-eng:BRD": "MTD",
    "local-authority-eng:BRE": "DIS",
    "local-authority-eng:BRM": "DIS",
    "local-authority-eng:BRO": "DIS",
    "local-authority-eng:BRT": "DIS",
    "local-authority-eng:BRW": "DIS",
    "local-authority-eng:BRX": "DIS",
    "local-authority-eng:BRY": "LBO",
    "local-authority-eng:BST": "UTA",
    "local-authority-eng:BUN": "DIS",
    "local-authority-eng:BUR": "MTD",
    "local-authority-eng:CAB": "DIS",
    "local-authority-eng:CAM": "CTY",
    "local-authority-eng:CAN": "DIS",
    "local-authority-eng:CAR": "DIS",
    "local-authority-eng:CAS": "DIS",
    "local-authority-eng:CAT": "DIS",
    "local-authority-eng:CBF": "UTA",
    "local-authority-eng:CHA": "DIS",
    "local-authority-eng:CHC": "DIS",
    "local-authority-eng:CHE": "UTA",
    "local-authority-eng:CHI": "DIS",
    "local-authority-eng:CHL": "DIS",
    "local-authority-eng:CHN": "DIS",
    "local-authority-eng:CHO": "DIS",
    "local-authority-eng:CHR": "DIS",
    "local-authority-eng:CHS": "DIS",
    "local-authority-eng:CHT": "DIS",
    "local-authority-eng:CHW": "UTA",
    "local-authority-eng:CLD": "MTD",
    "local-authority-eng:CMA": "CTY",
    "local-authority-eng:CMD": "LBO",
    "local-authority-eng:COL": "DIS",
    "local-authority-eng:CON": "UTA",
    "local-authority-eng:COP": "DIS",
    "local-authority-eng:COR": "DIS",
    "local-authority-eng:COT": "DIS",
    "local-authority-eng:COV": "MTD",
    "local-authority-eng:CRA": "DIS",
    "local-authority-eng:CRW": "DIS",
    "local-authority-eng:CRY": "LBO",
    "local-authority-eng:DAC": "DIS",
    "local-authority-eng:DAL": "UTA",
    "local-authority-eng:DAR": "DIS",
    "local-authority-eng:DAV": "DIS",
    "local-authority-eng:DBY": "CTY",
    "local-authority-eng:DEB": "DIS",
    "local-authority-eng:DER": "UTA",
    "local-authority-eng:DEV": "CTY",
    "local-authority-eng:DNC": "MTD",
    "local-authority-eng:DOR": "CTY",
    "local-authority-eng:DOV": "DIS",
    "local-authority-eng:DUD": "MTD",
    "local-authority-eng:DUR": "UTA",
    "local-authority-eng:EAL": "LBO",
    "local-authority-eng:EAS": "DIS",
    "local-authority-eng:EAT": "DIS",
    "local-authority-eng:ECA": "DIS",
    "local-authority-eng:EDE": "DIS",
    "local-authority-eng:EDN": "DIS",
    "local-authority-eng:EDO": "DIS",
    "local-authority-eng:EHA": "DIS",
    "local-authority-eng:EHE": "DIS",
    "local-authority-eng:ELI": "DIS",
    "local-authority-eng:ELM": "DIS",
    "local-authority-eng:ENF": "LBO",
    "local-authority-eng:ENO": "DIS",
    "local-authority-eng:EPP": "DIS",
    "local-authority-eng:EPS": "DIS",
    "local-authority-eng:ERE": "DIS",
    "local-authority-eng:ERY": "UTA",
    "local-authority-eng:ESS": "CTY",
    "local-authority-eng:EST": "DIS",
    "local-authority-eng:ESX": "CTY",
    "local-authority-eng:EXE": "DIS",
    "local-authority-eng:FAR": "DIS",
    "local-authority-eng:FEN": "DIS",
    "local-authority-eng:FOE": "DIS",
    "local-authority-eng:FOR": "DIS",
    "local-authority-eng:FYL": "DIS",
    "local-authority-eng:GAT": "MTD",
    "local-authority-eng:GED": "DIS",
    "local-authority-eng:GLO": "DIS",
    "local-authority-eng:GLS": "CTY",
    "local-authority-eng:GOS": "DIS",
    "local-authority-eng:GRA": "DIS",
    "local-authority-eng:GRE": "LBO",
    "local-authority-eng:GRT": "DIS",
    "local-authority-eng:GRY": "DIS",
    "local-authority-eng:HAA": "DIS",
    "local-authority-eng:HAE": "DIS",
    "local-authority-eng:HAG": "DIS",
    "local-authority-eng:HAL": "UTA",
    "local-authority-eng:HAM": "CTY",
    "local-authority-eng:HAO": "DIS",
    "local-authority-eng:HAR": "DIS",
    "local-authority-eng:HAS": "DIS",
    "local-authority-eng:HAT": "DIS",
    "local-authority-eng:HAV": "LBO",
    "local-authority-eng:HCK": "LBO",
    "local-authority-eng:HEF": "UTA",
    "local-authority-eng:HER": "DIS",
    "local-authority-eng:HIG": "DIS",
    "local-authority-eng:HIL": "LBO",
    "local-authority-eng:HIN": "DIS",
    "local-authority-eng:HMF": "LBO",
    "local-authority-eng:HNS": "LBO",
    "local-authority-eng:HOR": "DIS",
    "local-authority-eng:HPL": "UTA",
    "local-authority-eng:HRT": "CTY",
    "local-authority-eng:HRW": "LBO",
    "local-authority-eng:HRY": "LBO",
    "local-authority-eng:HUN": "DIS",
    "local-authority-eng:HYN": "DIS",
    "local-authority-eng:IOS": "COI",
    "local-authority-eng:IOW": "UTA",
    "local-authority-eng:IPS": "DIS",
    "local-authority-eng:ISL": "LBO",
    "local-authority-eng:KEC": "LBO",
    "local-authority-eng:KEN": "CTY",
    "local-authority-eng:KET": "DIS",
    "local-authority-eng:KHL": "UTA",
    "local-authority-eng:KIN": "DIS",
    "local-authority-eng:KIR": "MTD",
    "local-authority-eng:KTT": "LBO",
    "local-authority-eng:KWL": "MTD",
    "local-authority-eng:LAC": "DIS",
    "local-authority-eng:LAN": "CTY",
    "local-authority-eng:LBH": "LBO",
    "local-authority-eng:LCE": "UTA",
    "local-authority-eng:LDS": "MTD",
    "local-authority-eng:LEC": "CTY",
    "local-authority-eng:LEE": "DIS",
    "local-authority-eng:LEW": "LBO",
    "local-authority-eng:LIC": "DIS",
    "local-authority-eng:LIF": "DIS",
    "local-authority-eng:LIN": "CTY",
    "local-authority-eng:LIV": "MTD",
    "local-authority-eng:LND": "LBO",
    "local-authority-eng:LUT": "UTA",
    "local-authority-eng:MAI": "DIS",
    "local-authority-eng:MAL": "DIS",
    "local-authority-eng:MAN": "MTD",
    "local-authority-eng:MAS": "DIS",
    "local-authority-eng:MAV": "DIS",
    "local-authority-eng:MDB": "UTA",
    "local-authority-eng:MDE": "DIS",
    "local-authority-eng:MDW": "UTA",
    "local-authority-eng:MEL": "DIS",
    "local-authority-eng:MEN": "DIS",
    "local-authority-eng:MIK": "UTA",
    "local-authority-eng:MOL": "DIS",
    "local-authority-eng:MRT": "LBO",
    "local-authority-eng:MSS": "DIS",
    "local-authority-eng:MSU": "DIS",
    "local-authority-eng:NBL": "UTA",
    "local-authority-eng:NDE": "DIS",
    "local-authority-eng:NDO": "DIS",
    "local-authority-eng:NEA": "DIS",
    "local-authority-eng:NEC": "DIS",
    "local-authority-eng:NED": "DIS",
    "local-authority-eng:NEL": "UTA",
    "local-authority-eng:NET": "MTD",
    "local-authority-eng:NEW": "DIS",
    "local-authority-eng:NFK": "CTY",
    "local-authority-eng:NGM": "UTA",
    "local-authority-eng:NHE": "DIS",
    "local-authority-eng:NKE": "DIS",
    "local-authority-eng:NLN": "UTA",
    "local-authority-eng:NNO": "DIS",
    "local-authority-eng:NOR": "DIS",
    "local-authority-eng:NOW": "DIS",
    "local-authority-eng:NSM": "UTA",
    "local-authority-eng:NTH": "CTY",
    "local-authority-eng:NTT": "CTY",
    "local-authority-eng:NTY": "MTD",
    "local-authority-eng:NUN": "DIS",
    "local-authority-eng:NWA": "DIS",
    "local-authority-eng:NWL": "DIS",
    "local-authority-eng:NWM": "LBO",
    "local-authority-eng:NYK": "CTY",
    "local-authority-eng:OAD": "DIS",
    "local-authority-eng:OLD": "MTD",
    "local-authority-eng:OXF": "CTY",
    "local-authority-eng:OXO": "DIS",
    "local-authority-eng:PEN": "DIS",
    "local-authority-eng:PLY": "UTA",
    "local-authority-eng:POL": "UTA",
    "local-authority-eng:POR": "UTA",
    "local-authority-eng:PRE": "DIS",
    "local-authority-eng:PTE": "UTA",
    "local-authority-eng:PUR": "DIS",
    "local-authority-eng:RCC": "UTA",
    "local-authority-eng:RCH": "MTD",
    "local-authority-eng:RDB": "LBO",
    "local-authority-eng:RDG": "UTA",
    "local-authority-eng:RED": "DIS",
    "local-authority-eng:REI": "DIS",
    "local-authority-eng:RIB": "DIS",
    "local-authority-eng:RIC": "LBO",
    "local-authority-eng:RIH": "DIS",
    "local-authority-eng:ROC": "DIS",
    "local-authority-eng:ROH": "DIS",
    "local-authority-eng:ROS": "DIS",
    "local-authority-eng:ROT": "MTD",
    "local-authority-eng:RUG": "DIS",
    "local-authority-eng:RUH": "DIS",
    "local-authority-eng:RUN": "DIS",
    "local-authority-eng:RUS": "DIS",
    "local-authority-eng:RUT": "UTA",
    "local-authority-eng:RYE": "DIS",
    "local-authority-eng:SAL": "DIS",
    "local-authority-eng:SAW": "MTD",
    "local-authority-eng:SBU": "DIS",
    "local-authority-eng:SCA": "DIS",
    "local-authority-eng:SCE": "DIS",
    "local-authority-eng:SDE": "DIS",
    "local-authority-eng:SED": "DIS",
    "local-authority-eng:SEG": "DIS",
    "local-authority-eng:SEL": "DIS",
    "local-authority-eng:SEV": "DIS",
    "local-authority-eng:SFK": "CTY",
    "local-authority-eng:SFT": "MTD",
    "local-authority-eng:SGC": "UTA",
    "local-authority-eng:SHA": "DIS",
    "local-authority-eng:SHE": "DIS",
    "local-authority-eng:SHF": "MTD",
    "local-authority-eng:SHN": "MTD",
    "local-authority-eng:SHO": "DIS",
    "local-authority-eng:SHR": "UTA",
    "local-authority-eng:SKE": "DIS",
    "local-authority-eng:SKP": "MTD",
    "local-authority-eng:SLA": "DIS",
    "local-authority-eng:SLF": "MTD",
    "local-authority-eng:SLG": "UTA",
    "local-authority-eng:SND": "MTD",
    "local-authority-eng:SNO": "DIS",
    "local-authority-eng:SNR": "DIS",
    "local-authority-eng:SOL": "MTD",
    "local-authority-eng:SOM": "CTY",
    "local-authority-eng:SOS": "UTA",
    "local-authority-eng:SOX": "DIS",
    "local-authority-eng:SPE": "DIS",
    "local-authority-eng:SRI": "DIS",
    "local-authority-eng:SRY": "CTY",
    "local-authority-eng:SSO": "DIS",
    "local-authority-eng:SST": "DIS",
    "local-authority-eng:STA": "DIS",
    "local-authority-eng:STE": "UTA",
    "local-authority-eng:STF": "DIS",
    "local-authority-eng:STH": "UTA",
    "local-authority-eng:STN": "LBO",
    "local-authority-eng:STO": "DIS",
    "local-authority-eng:STR": "DIS",
    "local-authority-eng:STS": "CTY",
    "local-authority-eng:STT": "UTA",
    "local-authority-eng:STV": "DIS",
    "local-authority-eng:STY": "MTD",
    "local-authority-eng:SUF": "DIS",
    "local-authority-eng:SUR": "DIS",
    "local-authority-eng:SWD": "UTA",
    "local-authority-eng:SWK": "LBO",
    "local-authority-eng:SWL": "DIS",
    "local-authority-eng:TAM": "MTD",
    "local-authority-eng:TAN": "DIS",
    "local-authority-eng:TAU": "DIS",
    "local-authority-eng:TAW": "DIS",
    "local-authority-eng:TEI": "DIS",
    "local-authority-eng:TEN": "DIS",
    "local-authority-eng:TES": "DIS",
    "local-authority-eng:TEW": "DIS",
    "local-authority-eng:TFW": "UTA",
    "local-authority-eng:THA": "DIS",
    "local-authority-eng:THE": "DIS",
    "local-authority-eng:THR": "UTA",
    "local-authority-eng:TOB": "UTA",
    "local-authority-eng:TON": "DIS",
    "local-authority-eng:TOR": "DIS",
    "local-authority-eng:TRF": "MTD",
    "local-authority-eng:TUN": "DIS",
    "local-authority-eng:TWH": "LBO",
    "local-authority-eng:UTT": "DIS",
    "local-authority-eng:VAL": "DIS",
    "local-authority-eng:WAE": "DIS",
    "local-authority-eng:WAR": "CTY",
    "local-authority-eng:WAT": "DIS",
    "local-authority-eng:WAV": "DIS",
    "local-authority-eng:WAW": "DIS",
    "local-authority-eng:WBK": "UTA",
    "local-authority-eng:WDE": "DIS",
    "local-authority-eng:WDO": "DIS",
    "local-authority-eng:WEA": "DIS",
    "local-authority-eng:WEL": "DIS",
    "local-authority-eng:WEW": "DIS",
    "local-authority-eng:WEY": "DIS",
    "local-authority-eng:WFT": "LBO",
    "local-authority-eng:WGN": "MTD",
    "local-authority-eng:WIL": "UTA",
    "local-authority-eng:WIN": "DIS",
    "local-authority-eng:WKF": "MTD",
    "local-authority-eng:WLA": "DIS",
    "local-authority-eng:WLI": "DIS",
    "local-authority-eng:WLL": "MTD",
    "local-authority-eng:WLV": "MTD",
    "local-authority-eng:WND": "LBO",
    "local-authority-eng:WNM": "UTA",
    "local-authority-eng:WOC": "DIS",
    "local-authority-eng:WOI": "DIS",
    "local-authority-eng:WOK": "UTA",
    "local-authority-eng:WOR": "CTY",
    "local-authority-eng:WOT": "DIS",
    "local-authority-eng:WOX": "DIS",
    "local-authority-eng:WRL": "MTD",
    "local-authority-eng:WRT": "UTA",
    "local-authority-eng:WSM": "LBO",
    "local-authority-eng:WSO": "DIS",
    "local-authority-eng:WSX": "CTY",
    "local-authority-eng:WYC": "DIS",
    "local-authority-eng:WYE": "DIS",
    "local-authority-eng:WYO": "DIS",
    "local-authority-eng:WYR": "DIS",
    "local-authority-eng:YOR": "UTA",
    "local-authority-sct:ABD": "UTA",
    "local-authority-sct:ABE": "UTA",
    "local-authority-sct:AGB": "UTA",
    "local-authority-sct:ANS": "UTA",
    "local-authority-sct:CLK": "UTA",
    "local-authority-sct:DGY": "UTA",
    "local-authority-sct:DND": "UTA",
    "local-authority-sct:EAY": "UTA",
    "local-authority-sct:EDH": "UTA",
    "local-authority-sct:EDU": "UTA",
    "local-authority-sct:ELN": "UTA",
    "local-authority-sct:ELS": "UTA",
    "local-authority-sct:ERW": "UTA",
    "local-authority-sct:FAL": "UTA",
    "local-authority-sct:FIF": "UTA",
    "local-authority-sct:GLG": "UTA",
    "local-authority-sct:HLD": "UTA",
    "local-authority-sct:IVC": "UTA",
    "local-authority-sct:MLN": "UTA",
    "local-authority-sct:MRY": "UTA",
    "local-authority-sct:NAY": "UTA",
    "local-authority-sct:NLK": "UTA",
    "local-authority-sct:ORK": "UTA",
    "local-authority-sct:PKN": "UTA",
    "local-authority-sct:RFW": "UTA",
    "local-authority-sct:SAY": "UTA",
    "local-authority-sct:SCB": "UTA",
    "local-authority-sct:SLK": "UTA",
    "local-authority-sct:STG": "UTA",
    "local-authority-sct:WDU": "UTA",
    "local-authority-sct:WLN": "UTA",
    "local-authority-sct:ZET": "UTA",
    "local-authority-wls:WRX": "UTA",
    "local-authority-wls:VGL": "UTA",
    "local-authority-wls:TOF": "UTA",
    "local-authority-wls:SWA": "UTA",
    "local-authority-wls:RCT": "UTA",
    "local-authority-wls:POW": "UTA",
    "local-authority-wls:PEM": "UTA",
    "local-authority-wls:NWP": "UTA",
    "local-authority-wls:NTL": "UTA",
    "local-authority-wls:MTY": "UTA",
    "local-authority-wls:MON": "UTA",
    "local-authority-wls:GWN": "UTA",
    "local-authority-wls:FLN": "UTA",
    "local-authority-wls:DEN": "UTA",
    "local-authority-wls:CWY": "UTA",
    "local-authority-wls:CRF": "UTA",
    "local-authority-wls:CMN": "UTA",
    "local-authority-wls:CGN": "UTA",
    "local-authority-wls:CAY": "UTA",
    "local-authority-wls:BGW": "UTA",
    "local-authority-wls:BGE": "UTA",
    "local-authority-wls:AGY": "UTA",
}


REGISTER_SUBTYPE_TO_BOUNDARYLINE_TYPE = {
    "CA": "UTA",  # Scottish Unitary
    "CC": "LBO",  # City of London Corporation
    "CTY": "CTY",  # English County
    "LBO": "LBO",  # London Borough
    "MD": "MTD",  # Metropolitan District
    "NMD": "DIS",  # Non-Metropolitan District
    "SRA": "GLA",  # Greater London Authority
    "UA": "UTA",  # English or Welsh Unitary
}
