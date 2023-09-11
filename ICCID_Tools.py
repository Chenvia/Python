"""

ICCID Tools


"""

def resolve_CSP(arg):

    """
    Resolves Content Service Provider based on
    ICCID (Integrated Circuit Card Identifier)

    https://www.controlf.net/iccid/

        MVNO - Mobile Virtual Network Operator


    Format - Operator, Possible MVNO's, Country
    
    """
    
    resolver = {

        "894410" : ["Vodafone",
                    ["Sainsbury's", "Talk Mobile", "Lebara", "Nomi Mobile", "Asda"],
                    "UK"],
        "894412" : ["Orange", ["Lyca Mobile", "IDT Mobile"], "UK"],
        "894420" : ["3 Hutchinson (3)", None, "UK"],
        "894430" : ["T-Mobile", ["Mobile World", "Everything Everywhere(EE)", "Virgin Mobile"], "UK"],
        "894411" : ["02 Telefonica",["Tesco Mobile", "Giffgaff"], "UK"],
        "894401" : ["Vectone Mobile", None, "UK" ],
        "894403" : ["Marathon Telecom Ltd", None, "UK(Jersey)"],
        "892340" : ["WorldSIM ", None , "Italy"],
        "892341" : ["WorldSIM ", None , "Italy"],
        "892342" : ["WorldSIM ", None , "Italy"],
        "892343" : ["WorldSIM ", None , "Italy"],
        "892344" : ["WorldSIM ", None , "Italy"],
        "892345" : ["WorldSIM ", None , "Italy"],
        "892346" : ["WorldSIM ", None , "Italy"],
        "892347" : ["WorldSIM ", None , "Italy"],
        "892348" : ["WorldSIM ", None , "Italy"],
        "892349" : ["WorldSIM ", None , "Italy"],
        "894230" : ["SIM 4 Travel", None, "Liechtenstein"]

    }

    return resolver.get(arg, "Invalid Prefix")



if __name__ == "__main__":

    print(resolve_CSP("894410"))
