def checkAnswer(element_nr, answer):
    
    l = [
        "Wasserstoff", "Helium", "Lithium", "Beryllium", "Bor", "Kohlenstoff", "Stickstoff", "Sauerstoff", "Fluor", "Neon",
        "Natrium", "Magnesium", "Aluminium", "Silizium", "Phosphor", "Schwefel", "Chlor", "Argon", "Kalium", "Calcium",
        "Scandium", "Titan", "Vanadium", "Chrom", "Mangan", "Eisen", "Kobalt", "Nickel", "Kupfer", "Zink",
        "Gallium", "Germanium", "Arsen", "Selen", "Brom", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
        "Niob", "Molybdän", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silber", "Cadmium", "Indium", "Zinn",
        "Antimon", "Tellur", "Iod", "Xenon", "Caesium", "Barium", "Lanthan", "Cer", "Praseodym", "Neodym",
        "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
        "Lutetium", "Hafnium", "Tantal", "Wolfram", "Rhenium", "Osmium", "Iridium", "Platin", "Gold", "Quecksilber",
        "Thallium", "Blei", "Bismut", "Polonium", "Astat", "Radon", "Francium", "Radium", "Actinium", "Thorium",
        "Protactinium", "Uran", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
        "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium",
        "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tenness", "Oganesson"
    ]

    if answer in l:
        if l.index(answer) + 1 == element_nr:
            print("Richtig!")
            return(True)
        else:
            print("Falsch! Die richtige Antwort ist: " + l[element_nr - 1] + ". Deine Antwort ist vielleicht falsch geschrieben.")
            return(False)
    else:
        print("Falsch! Die richtige Antwort ist: " + l[element_nr - 1])
        return(False)