speelingAbbre = [
    #road abbreviation
    ['^SQUARE ', 'SQ '],
    ['^BOULEVARD ', 'BD '],
    ['^CHEMIN ', 'CHEM? '],
    ['^IMPASSE ', 'IMP '],
    ['^ROUTE ', 'RTE '],
    ['^PLACE ', 'PL '],
    ['^AVENUE ', 'AV '],
    ['^LIEU DIT ', 'LDT '],
    ['^RUELLE ', 'RLE '],
    ['^SENTIER ', 'SENT '],
    ['^VOIE COMMUNALE ', 'VC '],
    ['^ALLEE ', 'ALL '],
    ['^PASSAGE ', 'PASS '],
    ['^CHEMIN DÉPARTEMENTAL ', 'CD '],

    #special char
    ['\s', '( |, |\'|\.|-)?'],

    #speeling abbreviation
    [' ST(-| |\.)', ' S(AIN)?T(-| |\.)'],
    [' SAINT(-| |\.)', ' S(AIN)?T(-| |\.)'],

    #other
    #[" ", ",? "]
    
]



# roadType = '-lot-rue-av-imp-res-rte-bd-cite-rd-rn-sent-chem-cd-pass-lot-sent-quai-vc-za-zi-pl-'.upper()

# regRoadType = '^(lot|rue|av|imp|res|rte|bd|cite|rd|rn|sent|chem|cd|pass|lot|sent|quai|vc|za|zi|pl)\s'.upper()
# regRetermining = '(le|la|les|au|aux|du|des|de|notre)?\s?'.upper()

# reqSpeeling = '(l |d |n )?[\W\s\-\.]*\s([\W\s\-\.])*$'


# roadReg = regRoadType + regRetermining + regRetermining + reqSpeeling


# test = '^(rue|route)\s(de|la)?\s?(de|la)?\s?(l |d |n )?[\W\s\-\.]*\s([\W\s\-\.])*$'


















