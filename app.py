
import streamlit as st
# Your app code
st.title("My Periodic Table App developed by mak3.6")

# List of dictionaries containing information about each element
elements = [
    {
        "Atomic Number": 1,
        "Name": "Hydrogen",
        "Symbol": "H",
        "Atomic Mass": 1.008,
        "Electron Configuration": "1s¹",
        "Group": 1,
        "Period": 1,
        "Nature of Element": "Non-metal",
        "Properties": {
            "Physical": "Colorless, odorless, tasteless gas. The lightest element.",
            "Chemical": "Highly reactive, forms compounds with most elements."
        },
        "Uses": "Rocket fuel, fuel cells, ammonia production.",
        "Isotopes": ["¹H (Protium, stable)", "²H (Deuterium, stable)", "³H (Tritium, radioactive)"],
        "History": "Hydrogen was discovered by Henry Cavendish in 1766. Its name comes from the Greek 'hydro' (water) and 'genes' (creator), meaning water former.",
        "Sources": "Natural sources include water and hydrocarbons."
    },
     {
        "Atomic Number": 2,
        "Name": "Helium",
        "Symbol": "He",
        "Atomic Mass": 4.0026,
        "Electron Configuration": "1s²",
        "Group": 18,
        "Period": 1,
        "Nature of Element": "Noble Gas (non-metal)",
        "Properties": {
            "Physical": "Colorless, odorless gas. Low density, second lightest element.",
            "Chemical": "Inert, non-reactive under standard conditions."
        },
        "Uses": "Cryogenics, cooling superconducting magnets, balloons.",
        "Isotopes": ["⁴He (stable)", "³He (stable, rare)"],
        "History": "Helium was first detected in the spectrum of the sun during a solar eclipse in 1868 by Jules Janssen and Norman Lockyer.",
        "Sources": "Extracted from natural gas deposits."
    },
    {
        "Atomic Number": 3,
        "Name": "Lithium",
        "Symbol": "Li",
        "Atomic Mass": 6.94,
        "Electron Configuration": "[He] 2s¹",
        "Group": 1,
        "Period": 2,
        "Nature of Element": "Alkali Metal",
        "Properties": {
            "Physical": "Soft, silver-white metal, lightest metal.",
            "Chemical": "Highly reactive, especially with water, forms lithium hydroxide."
        },
        "Uses": "Batteries, ceramics, mood stabilizers.",
        "Isotopes": ["⁶Li (stable)", "⁷Li (stable, more abundant)"],
        "History": "Lithium was discovered in 1817 by Johan August Arfwedson in petalite.",
        "Sources": "Found in minerals such as spodumene and lepidolite."
    },
    {
        "Atomic Number": 4,
        "Name": "Beryllium",
        "Symbol": "Be",
        "Atomic Mass": 9.0122,
        "Electron Configuration": "[He] 2s²",
        "Group": 2,
        "Period": 2,
        "Nature of Element": "Alkaline Earth Metal",
        "Properties": {
            "Physical": "Hard, brittle, gray-white metal. Low density.",
            "Chemical": "Resistant to corrosion. Forms beryllium oxide when heated."
        },
        "Uses": "Aerospace materials, X-ray windows, nuclear reactors.",
        "Isotopes": ["⁹Be (stable)"],
        "History": "Beryllium was discovered in 1798 by Louis-Nicolas Vauquelin in beryl and emerald.",
        "Sources": "Primarily sourced from beryl and chrysoberyl."
    },
    {
        "Atomic Number": 5,
        "Name": "Boron",
        "Symbol": "B",
        "Atomic Mass": 10.81,
        "Electron Configuration": "[He] 2s² 2p¹",
        "Group": 13,
        "Period": 2,
        "Nature of Element": "Metalloid",
        "Properties": {
            "Physical": "Hard, brittle black solid. Conducts electricity at high temperatures.",
            "Chemical": "Forms compounds like borax and boric acid, burns with a green flame."
        },
        "Uses": "Borosilicate glass, detergents, neutron absorbers.",
        "Isotopes": ["¹⁰B (stable)", "¹¹B (stable, more abundant)"],
        "History": "Boron was discovered in 1808 by Humphry Davy, Joseph Louis Gay-Lussac, and Louis Jacques Thénard.",
        "Sources": "Found in borate minerals such as borax and kernite."
    },
    {
        "Atomic Number": 6,
        "Name": "Carbon",
        "Symbol": "C",
        "Atomic Mass": 12.011,
        "Electron Configuration": "[He] 2s² 2p²",
        "Group": 14,
        "Period": 2,
        "Nature of Element": "Non-metal",
        "Properties": {
            "Physical": "Exists in graphite, diamond forms. Basis of organic life.",
            "Chemical": "Forms vast number of compounds (organic chemistry)."
        },
        "Uses": "Steel production, fuels, organic life.",
        "Isotopes": ["¹²C (stable)", "¹³C (stable)", "¹⁴C (radioactive)"],
        "History": "Carbon has been known since antiquity, used in the form of charcoal and soot.",
        "Sources": "Found in all organic compounds, coal, and natural gas."
    },
    {
        "Atomic Number": 7,
        "Name": "Nitrogen",
        "Symbol": "N",
        "Atomic Mass": 14.007,
        "Electron Configuration": "[He] 2s² 2p³",
        "Group": 15,
        "Period": 2,
        "Nature of Element": "Non-metal",
        "Properties": {
            "Physical": "Colorless, odorless gas. 78% of Earth's atmosphere.",
            "Chemical": "Inert under standard conditions, forms ammonia and nitrates."
        },
        "Uses": "Fertilizers, explosives, refrigerants (liquid nitrogen).",
        "Isotopes": ["¹⁴N (stable)", "¹⁵N (stable)"],
        "History": "Nitrogen was discovered in 1772 by Daniel Rutherford, though it was recognized as a separate substance by several others.",
        "Sources": "Extracted from the atmosphere."
    },
    {
        "Atomic Number": 8,
        "Name": "Oxygen",
        "Symbol": "O",
        "Atomic Mass": 15.999,
        "Electron Configuration": "[He] 2s² 2p⁴",
        "Group": 16,
        "Period": 2,
        "Nature of Element": "Non-metal",
        "Properties": {
            "Physical": "Colorless, odorless gas. Supports life and combustion.",
            "Chemical": "Highly reactive, forms oxides with most elements."
        },
        "Uses": "Breathing, steelmaking, water treatment.",
        "Isotopes": ["¹⁶O (stable)", "¹⁷O (stable)", "¹⁸O (stable)"],
        "History": "Oxygen was discovered independently by Carl Wilhelm Scheele and Joseph Priestley in the 1770s.",
        "Sources": "Extracted from air or water."
    },
    {
        "Atomic Number": 9,
        "Name": "Fluorine",
        "Symbol": "F",
        "Atomic Mass": 18.998,
        "Electron Configuration": "[He] 2s² 2p⁵",
        "Group": 17,
        "Period": 2,
        "Nature of Element": "Halogen (non-metal)",
        "Properties": {
            "Physical": "Pale yellow gas with a pungent smell.",
            "Chemical": "Extremely reactive, forms compounds with most elements."
        },
        "Uses": "Toothpaste, water fluoridation, Teflon.",
        "Isotopes": ["¹⁹F (stable)"],
        "History": "Fluorine was first isolated by Henri Moissan in 1886.",
        "Sources": "Found in minerals such as fluorite and cryolite."
    },
    {
        "Atomic Number": 10,
        "Name": "Neon",
        "Symbol": "Ne",
        "Atomic Mass": 20.180,
        "Electron Configuration": "[He] 2s² 2p⁶",
        "Group": 18,
        "Period": 2,
        "Nature of Element": "Noble gas (non-metal)",
        "Properties": {
            "Physical": "Colorless, odorless gas, emits red-orange glow in signs.",
            "Chemical": "Inert, does not form compounds easily."
        },
        "Uses": "Neon signs, high-voltage indicators, cryogenics.",
        "Isotopes": ["²⁰Ne (stable)", "²¹Ne (stable)", "²²Ne (stable)"],
        "History": "Neon was discovered in 1898 by William Ramsay and Morris Travers.",
        "Sources": "Extracted from air during fractional distillation."
    },
    {
        "Atomic Number": 11,
        "Name": "Sodium",
        "Symbol": "Na",
        "Atomic Mass": 22.990,
        "Electron Configuration": "[Ne] 3s¹",
        "Group": 1,
        "Period": 3,
        "Nature of Element": "Alkali Metal",
        "Properties": {
            "Physical": "Soft, silver-white metal. Highly reactive.",
            "Chemical": "React vigorously with water, forming sodium hydroxide."
        },
        "Uses": "Table salt, soap making, chemical synthesis.",
        "Isotopes": ["²²Na (radioactive)", "²³Na (stable)"],
        "History": "Sodium was isolated in 1807 by Humphry Davy.",
        "Sources": "Found in salt (sodium chloride) and various minerals."
    },
    {
        "Atomic Number": 12,
        "Name": "Magnesium",
        "Symbol": "Mg",
        "Atomic Mass": 24.305,
        "Electron Configuration": "[Ne] 3s²",
        "Group": 2,
        "Period": 3,
        "Nature of Element": "Alkaline Earth Metal",
        "Properties": {
            "Physical": "Light, silver-white metal, low density.",
            "Chemical": "Burns with a bright white light; reacts with water at high temperatures."
        },
        "Uses": "Alloys, fireworks, flares, and as a reducing agent.",
        "Isotopes": ["²⁴Mg (stable)", "²⁵Mg (stable)", "²⁶Mg (stable)"],
        "History": "Magnesium was discovered in 1808 by Sir Humphry Davy.",
        "Sources": "Found in minerals like dolomite and magnesite."
    },
    {
        "Atomic Number": 13,
        "Name": "Aluminum",
        "Symbol": "Al",
        "Atomic Mass": 26.982,
        "Electron Configuration": "[Ne] 3s² 3p¹",
        "Group": 13,
        "Period": 3,
        "Nature of Element": "Post-transition Metal",
        "Properties": {
            "Physical": "Lightweight, silver-white metal, malleable.",
            "Chemical": "Resistant to corrosion due to an oxide layer."
        },
        "Uses": "Aerospace, packaging, construction, and electrical applications.",
        "Isotopes": ["²⁶Al (radioactive)", "²⁷Al (stable)"],
        "History": "Aluminum was first isolated in 1825 by Hans Christian Ørsted.",
        "Sources": "Found in bauxite and cryolite."
    },
    {
        "Atomic Number": 14,
        "Name": "Silicon",
        "Symbol": "Si",
        "Atomic Mass": 28.085,
        "Electron Configuration": "[Ne] 3s² 3p²",
        "Group": 14,
        "Period": 3,
        "Nature of Element": "Metalloid",
        "Properties": {
            "Physical": "Hard, brittle crystalline solid, shiny metallic luster.",
            "Chemical": "Forms covalent bonds; reacts with halogens."
        },
        "Uses": "Semiconductors, solar cells, glass production.",
        "Isotopes": ["²⁸Si (stable)", "²⁹Si (stable)", "³⁰Si (stable)"],
        "History": "Silicon was isolated in 1824 by Jöns Jacob Berzelius.",
        "Sources": "Found in sand and silicate minerals."
    },
    {
        "Atomic Number": 15,
        "Name": "Phosphorus",
        "Symbol": "P",
        "Atomic Mass": 30.974,
        "Electron Configuration": "[Ne] 3s² 3p³",
        "Group": 15,
        "Period": 3,
        "Nature of Element": "Non-metal",
        "Properties": {
            "Physical": "Exists in several allotropes; white phosphorus is highly reactive.",
            "Chemical": "Combines with oxygen and other elements easily."
        },
        "Uses": "Fertilizers, detergents, matches, and explosives.",
        "Isotopes": ["¹⁵P (stable)"],
        "History": "Phosphorus was discovered in 1669 by Hennig Brand.",
        "Sources": "Found in phosphate rocks."
    },
    {
        "Atomic Number": 16,
        "Name": "Sulfur",
        "Symbol": "S",
        "Atomic Mass": 32.06,
        "Electron Configuration": "[Ne] 3s² 3p⁴",
        "Group": 16,
        "Period": 3,
        "Nature of Element": "Non-metal",
        "Properties": {
            "Physical": "Yellow, brittle solid at room temperature.",
            "Chemical": "Forms sulfides and oxides; reacts with metals."
        },
        "Uses": "Fertilizers, sulfuric acid production, rubber vulcanization.",
        "Isotopes": ["³²S (stable)", "³⁴S (stable)", "³⁶S (stable)"],
        "History": "Sulfur has been known since antiquity.",
        "Sources": "Found in volcanic regions and in sulfide minerals."
    },
    {
        "Atomic Number": 17,
        "Name": "Chlorine",
        "Symbol": "Cl",
        "Atomic Mass": 35.45,
        "Electron Configuration": "[Ne] 3s² 3p⁵",
        "Group": 17,
        "Period": 3,
        "Nature of Element": "Halogen (non-metal)",
        "Properties": {
            "Physical": "Greenish-yellow gas with a pungent odor.",
            "Chemical": "Highly reactive, forms salts with metals."
        },
        "Uses": "Water purification, bleaching agents, and disinfectants.",
        "Isotopes": ["³⁵Cl (stable)", "³⁷Cl (stable)"],
        "History": "Chlorine was discovered by Carl Wilhelm Scheele in 1774.",
        "Sources": "Found in nature mainly as chloride salts."
    },
    {
        "Atomic Number": 18,
        "Name": "Argon",
        "Symbol": "Ar",
        "Atomic Mass": 39.948,
        "Electron Configuration": "[Ne] 3s² 3p⁶",
        "Group": 18,
        "Period": 3,
        "Nature of Element": "Noble gas (non-metal)",
        "Properties": {
            "Physical": "Colorless, odorless gas. Non-toxic.",
            "Chemical": "Inert, does not react with other elements."
        },
        "Uses": "Inert gas shield for welding, neon lights, and filling light bulbs.",
        "Isotopes": ["³⁸Ar (stable)", "³⁹Ar (radioactive)", "⁴⁰Ar (stable)"],
        "History": "Argon was discovered in 1894 by Lord Rayleigh and William Ramsay.",
        "Sources": "Extracted from air during fractional distillation."
    },
    {
        "Atomic Number": 19,
        "Name": "Potassium",
        "Symbol": "K",
        "Atomic Mass": 39.098,
        "Electron Configuration": "[Ar] 4s¹",
        "Group": 1,
        "Period": 4,
        "Nature of Element": "Alkali Metal",
        "Properties": {
            "Physical": "Soft, waxy, silvery metal. Highly reactive.",
            "Chemical": "Reacts violently with water, forming potassium hydroxide."
        },
        "Uses": "Fertilizers, salt substitutes, and fireworks.",
        "Isotopes": ["³⁹K (stable)", "⁴⁰K (radioactive)", "⁴¹K (stable)"],
        "History": "Potassium was isolated in 1807 by Humphry Davy.",
        "Sources": "Found in potash and various minerals."
    },
    {
        "Atomic Number": 20,
        "Name": "Calcium",
        "Symbol": "Ca",
        "Atomic Mass": 40.078,
        "Electron Configuration": "[Ar] 4s²",
        "Group": 2,
        "Period": 4,
        "Nature of Element": "Alkaline Earth Metal",
        "Properties": {
            "Physical": "Soft, gray metal. Reacts with water.",
            "Chemical": "Forms calcium hydroxide with water."
        },
        "Uses": "Cement, plaster, dietary supplement.",
        "Isotopes": ["⁴⁰Ca (stable)", "⁴²Ca (stable)", "⁴³Ca (stable)", "⁴⁴Ca (stable)", "⁴⁶Ca (stable)"],
        "History": "Calcium was first isolated in 1808 by Humphry Davy.",
        "Sources": "Found in limestone, gypsum, and fluorite."
    },
    {
        "Atomic Number": 21,
        "Name": "Scandium",
        "Symbol": "Sc",
        "Atomic Mass": 44.956,
        "Electron Configuration": "[Ar] 3d¹⁃ 4s²",
        "Group": 3,
        "Period": 4,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Soft, silvery-white metal.",
            "Chemical": "Does not react with water, but reacts with acids."
        },
        "Uses": "Aerospace components, sports equipment.",
        "Isotopes": ["⁴⁴Sc (radioactive)", "⁴⁵Sc (stable)"],
        "History": "Scandium was discovered in 1879 by Lars Fredrik Nilson.",
        "Sources": "Found in trace amounts in various ores."
    },
    {
        "Atomic Number": 22,
        "Name": "Titanium",
        "Symbol": "Ti",
        "Atomic Mass": 47.867,
        "Electron Configuration": "[Ar] 3d² 4s²",
        "Group": 4,
        "Period": 4,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Strong, low-density, silver metal.",
            "Chemical": "Corrosion-resistant, forms a protective oxide layer."
        },
        "Uses": "Aerospace, medical implants, pigments.",
        "Isotopes": ["⁴⁶Ti (stable)", "⁴⁷Ti (stable)", "⁴⁸Ti (stable)"],
        "History": "Titanium was discovered in 1791 by William Gregor.",
        "Sources": "Found in minerals such as ilmenite and rutile."
    },
    {
        "Atomic Number": 23,
        "Name": "Vanadium",
        "Symbol": "V",
        "Atomic Mass": 50.941,
        "Electron Configuration": "[Ar] 3d³ 4s²",
        "Group": 5,
        "Period": 4,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Soft, ductile, silver-gray metal.",
            "Chemical": "Resistant to corrosion, forms a protective oxide layer."
        },
        "Uses": "Steel alloys, catalysts, and batteries.",
        "Isotopes": ["⁴⁹V (stable)", "⁵¹V (stable)"],
        "History": "Vanadium was discovered in 1801 by Andrés Manuel del Río.",
        "Sources": "Found in minerals like vanadinite and carnallite."
    },
    {
        "Atomic Number": 24,
        "Name": "Chromium",
        "Symbol": "Cr",
        "Atomic Mass": 51.996,
        "Electron Configuration": "[Ar] 3d⁵ 4s¹",
        "Group": 6,
        "Period": 4,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Shiny, hard metal with a bluish tint.",
            "Chemical": "Corrosion-resistant; forms various oxides."
        },
        "Uses": "Stainless steel, chrome plating, pigments.",
        "Isotopes": ["⁵²Cr (stable)", "⁵³Cr (stable)", "⁵⁴Cr (stable)"],
        "History": "Chromium was discovered in 1797 by Louis Nicolas Vauquelin.",
        "Sources": "Found in minerals like chromite."
    },
    {
        "Atomic Number": 25,
        "Name": "Manganese",
        "Symbol": "Mn",
        "Atomic Mass": 54.938,
        "Electron Configuration": "[Ar] 3d⁵ 4s²",
        "Group": 7,
        "Period": 4,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Hard, brittle metal.",
            "Chemical": "Does not react with water, forms various oxides."
        },
        "Uses": "Steel production, batteries, fertilizers.",
        "Isotopes": ["⁵⁴Mn (radioactive)", "⁵⁵Mn (stable)"],
        "History": "Manganese was discovered in 1774 by Johan Gottlieb Gahn.",
        "Sources": "Found in minerals like pyrolusite."
    },
    {
        "Atomic Number": 26,
        "Name": "Iron",
        "Symbol": "Fe",
        "Atomic Mass": 55.845,
        "Electron Configuration": "[Ar] 3d⁶ 4s²",
        "Group": 8,
        "Period": 4,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Metallic, ductile, and malleable.",
            "Chemical": "Reacts with oxygen, forms rust."
        },
        "Uses": "Steel production, construction, tools.",
        "Isotopes": ["⁵⁶Fe (stable)", "⁵⁷Fe (stable)", "⁵⁸Fe (stable)"],
        "History": "Iron has been known since ancient times.",
        "Sources": "Found in minerals like hematite and magnetite."
    },
    {
        "Atomic Number": 27,
        "Name": "Cobalt",
        "Symbol": "Co",
        "Atomic Mass": 58.933,
        "Electron Configuration": "[Ar] 3d⁷ 4s²",
        "Group": 9,
        "Period": 4,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Hard, lustrous metal.",
            "Chemical": "Forms several important compounds."
        },
        "Uses": "Batteries, alloys, and pigments.",
        "Isotopes": ["⁵⁷Co (radioactive)", "⁵⁹Co (stable)"],
        "History": "Cobalt was discovered in 1735 by Georg Brandt.",
        "Sources": "Found in minerals like cobaltite."
    },
    {
        "Atomic Number": 28,
        "Name": "Nickel",
        "Symbol": "Ni",
        "Atomic Mass": 58.693,
        "Electron Configuration": "[Ar] 3d⁸ 4s²",
        "Group": 10,
        "Period": 4,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Shiny, silvery-white metal.",
            "Chemical": "Corrosion-resistant, forms various alloys."
        },
        "Uses": "Coins, batteries, stainless steel.",
        "Isotopes": ["⁵⁸Ni (stable)", "⁵⁹Ni (stable)", "⁶⁰Ni (stable)"],
        "History": "Nickel was discovered in 1751 by Axel Fredrik Cronstedt.",
        "Sources": "Found in minerals like pentlandite."
    },
    {
        "Atomic Number": 29,
        "Name": "Copper",
        "Symbol": "Cu",
        "Atomic Mass": 63.546,
        "Electron Configuration": "[Ar] 3d¹⁰ 4s¹",
        "Group": 11,
        "Period": 4,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Red-orange metal, highly conductive.",
            "Chemical": "Forms compounds with various oxidation states."
        },
        "Uses": "Electrical wiring, plumbing, coins.",
        "Isotopes": ["⁶³Cu (stable)", "⁶⁴Cu (stable)"],
        "History": "Copper has been known since ancient times.",
        "Sources": "Found in native copper and various ores."
    },
    {
        "Atomic Number": 30,
        "Name": "Zinc",
        "Symbol": "Zn",
        "Atomic Mass": 65.38,
        "Electron Configuration": "[Ar] 3d¹⁰ 4s²",
        "Group": 12,
        "Period": 4,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Bluish-white metal, brittle at room temperature.",
            "Chemical": "Corrodes easily, forms a protective oxide layer."
        },
        "Uses": "Galvanization, alloys, and batteries.",
        "Isotopes": ["²⁶Zn (stable)", "²⁷Zn (stable)", "²⁸Zn (stable)"],
        "History": "Zinc was known in antiquity, though isolated in 1746.",
        "Sources": "Found in minerals like sphalerite."
    },
    {
        "Atomic Number": 31,
        "Name": "Gallium",
        "Symbol": "Ga",
        "Atomic Mass": 69.723,
        "Electron Configuration": "[Ar] 3d¹⁰ 4s² 4p¹",
        "Group": 13,
        "Period": 4,
        "Nature of Element": "Post-transition Metal",
        "Properties": {
            "Physical": "Soft, silvery metal that melts at just above room temperature.",
            "Chemical": "Stable in dry air, reacts with alkalis and acids."
        },
        "Uses": "Semiconductors, LEDs, and solar panels.",
        "Isotopes": ["⁶⁹Ga (stable)", "⁷¹Ga (stable)"],
        "History": "Gallium was discovered in 1875 by Paul Émile Lecoq de Boisbaudran.",
        "Sources": "Found in bauxite and zinc ores."
    },
    {
        "Atomic Number": 32,
        "Name": "Germanium",
        "Symbol": "Ge",
        "Atomic Mass": 72.630,
        "Electron Configuration": "[Ar] 3d¹⁰ 4s² 4p²",
        "Group": 14,
        "Period": 4,
        "Nature of Element": "Metalloid",
        "Properties": {
            "Physical": "Hard, gray-white metal.",
            "Chemical": "Forms compounds with oxidation states of +4 and +2."
        },
        "Uses": "Semiconductors, fiber optics, and solar cells.",
        "Isotopes": ["⁶⁶Ge (stable)", "⁶⁸Ge (stable)", "⁶⁹Ge (stable)"],
        "History": "Germanium was discovered in 1886 by Clemens Winkler.",
        "Sources": "Found in minerals like germanite."
    },
    {
        "Atomic Number": 33,
        "Name": "Arsenic",
        "Symbol": "As",
        "Atomic Mass": 74.922,
        "Electron Configuration": "[Ar] 3d¹⁰ 4s² 4p³",
        "Group": 15,
        "Period": 4,
        "Nature of Element": "Metalloid",
        "Properties": {
            "Physical": "Gray or silver-colored, brittle solid.",
            "Chemical": "Forms various compounds with metals and nonmetals."
        },
        "Uses": "Pesticides, semiconductors, and alloys.",
        "Isotopes": ["⁷₄As (stable)", "⁷₅As (stable)"],
        "History": "Arsenic has been known since ancient times.",
        "Sources": "Found in arsenopyrite and other minerals."
    },
    {
        "Atomic Number": 34,
        "Name": "Selenium",
        "Symbol": "Se",
        "Atomic Mass": 78.971,
        "Electron Configuration": "[Ar] 3d¹⁰ 4s² 4p⁴",
        "Group": 16,
        "Period": 4,
        "Nature of Element": "Non-metal",
        "Properties": {
            "Physical": "Gray or red solid, brittle.",
            "Chemical": "Forms various compounds, including selenides."
        },
        "Uses": "Glass production, electronics, and photocopiers.",
        "Isotopes": ["⁷⁸Se (stable)", "⁷⁹Se (stable)", "⁸⁰Se (stable)"],
        "History": "Selenium was discovered in 1817 by Jöns Jacob Berzelius.",
        "Sources": "Found in sulfide minerals."
    },
    {
        "Atomic Number": 35,
        "Name": "Bromine",
        "Symbol": "Br",
        "Atomic Mass": 79.904,
        "Electron Configuration": "[Ar] 3d¹⁰ 4s² 4p⁵",
        "Group": 17,
        "Period": 4,
        "Nature of Element": "Halogen (non-metal)",
        "Properties": {
            "Physical": "Dark reddish-brown liquid with a pungent odor.",
            "Chemical": "Reacts with many elements and compounds."
        },
        "Uses": "Flame retardants, photography, and water purification.",
        "Isotopes": ["⁷⁹Br (stable)", "⁸¹Br (stable)"],
        "History": "Bromine was discovered in 1826 by Antoine Jérôme Balard.",
        "Sources": "Found in brines and seawater."
    },
    {
        "Atomic Number": 36,
        "Name": "Krypton",
        "Symbol": "Kr",
        "Atomic Mass": 83.798,
        "Electron Configuration": "[Ar] 3d¹⁰ 4s² 4p⁶",
        "Group": 18,
        "Period": 4,
        "Nature of Element": "Noble gas (non-metal)",
        "Properties": {
            "Physical": "Colorless gas, very dense.",
            "Chemical": "Inert, does not react with most elements."
        },
        "Uses": "Lighting, photography, and as an inert gas in nuclear reactors.",
        "Isotopes": ["⁸⁴Kr (stable)", "⁸⁶Kr (stable)", "⁸⁸Kr (stable)"],
        "History": "Krypton was discovered in 1898 by William Ramsay and Morris Travers.",
        "Sources": "Extracted from air during fractional distillation."
    },
    {
        "Atomic Number": 37,
        "Name": "Rubidium",
        "Symbol": "Rb",
        "Atomic Mass": 85.468,
        "Electron Configuration": "[Kr] 5s¹",
        "Group": 1,
        "Period": 5,
        "Nature of Element": "Alkali Metal",
        "Properties": {
            "Physical": "Soft, silvery-white metal.",
            "Chemical": "Highly reactive, especially with water."
        },
        "Uses": "Atomic clocks, research, and fireworks.",
        "Isotopes": ["⁸⁵Rb (stable)", "⁸⁷Rb (stable)"],
        "History": "Rubidium was discovered in 1861 by Robert Bunsen and Gustav Kirchhoff.",
        "Sources": "Found in minerals like lepidolite."
    },
    {
        "Atomic Number": 38,
        "Name": "Strontium",
        "Symbol": "Sr",
        "Atomic Mass": 87.62,
        "Electron Configuration": "[Kr] 5s²",
        "Group": 2,
        "Period": 5,
        "Nature of Element": "Alkaline Earth Metal",
        "Properties": {
            "Physical": "Soft, silver-yellow metal.",
            "Chemical": "Burns with a bright red flame."
        },
        "Uses": "Fireworks, magnets, and in nuclear reactors.",
        "Isotopes": ["⁸⁴Sr (stable)", "⁸⁶Sr (stable)", "⁸⁷Sr (stable)", "⁸⁸Sr (stable)"],
        "History": "Strontium was discovered in 1790 by William Cruickshank.",
        "Sources": "Found in minerals like celestine."
    },
    {
        "Atomic Number": 39,
        "Name": "Yttrium",
        "Symbol": "Y",
        "Atomic Mass": 88.906,
        "Electron Configuration": "[Kr] 4d¹ 5s²",
        "Group": 3,
        "Period": 5,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Silvery-metallic, ductile.",
            "Chemical": "Resistant to corrosion and oxidation."
        },
        "Uses": "LEDs, phosphors, and superconductors.",
        "Isotopes": ["⁸₉Y (stable)", "⁹₁Y (stable)"],
        "History": "Yttrium was discovered in 1794 by Johan Gadolin.",
        "Sources": "Found in minerals like yttrium iron garnet."
    },
    {
        "Atomic Number": 40,
        "Name": "Zirconium",
        "Symbol": "Zr",
        "Atomic Mass": 91.224,
        "Electron Configuration": "[Kr] 4d² 5s²",
        "Group": 4,
        "Period": 5,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Silvery-gray metal, hard and ductile.",
            "Chemical": "Resistant to corrosion and oxidation."
        },
        "Uses": "Nuclear reactors, ceramics, and alloys.",
        "Isotopes": ["⁹²Zr (stable)", "⁹⁴Zr (stable)", "⁹⁶Zr (stable)"],
        "History": "Zirconium was discovered in 1789 by Martin Heinrich Klaproth.",
        "Sources": "Found in minerals like zircon."
    },
    {
        "Atomic Number": 41,
        "Name": "Niobium",
        "Symbol": "Nb",
        "Atomic Mass": 92.906,
        "Electron Configuration": "[Kr] 4d⁴ 5s²",
        "Group": 5,
        "Period": 5,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Gray, ductile metal.",
            "Chemical": "Resistant to oxidation and corrosion."
        },
        "Uses": "Superconductors, electronics, and steel alloys.",
        "Isotopes": ["⁹⁴Nb (stable)", "⁹⁵Nb (stable)"],
        "History": "Niobium was discovered in 1801 by Charles Hatchett.",
        "Sources": "Found in minerals like columbite."
    },
    {
        "Atomic Number": 42,
        "Name": "Molybdenum",
        "Symbol": "Mo",
        "Atomic Mass": 95.95,
        "Electron Configuration": "[Kr] 4d⁵ 5s¹",
        "Group": 6,
        "Period": 5,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Hard, silvery metal.",
            "Chemical": "Resistant to corrosion, high melting point."
        },
        "Uses": "Steel production, electrical contacts, and filaments.",
        "Isotopes": ["⁹⁸Mo (stable)", "⁹⁹Mo (radioactive)"],
        "History": "Molybdenum was discovered in 1778 by Carl Wilhelm Scheele.",
        "Sources": "Found in minerals like molybdenite."
    },
    {
        "Atomic Number": 43,
        "Name": "Technetium",
        "Symbol": "Tc",
        "Atomic Mass": 98,
        "Electron Configuration": "[Kr] 4d⁵ 5s²",
        "Group": 7,
        "Period": 5,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Silvery-gray metal.",
            "Chemical": "Radioactive, has no stable isotopes."
        },
        "Uses": "Radioactive tracers in medicine, and nuclear reactors.",
        "Isotopes": ["⁹⁹Tc (radioactive)"],
        "History": "Technetium was discovered in 1937 by Carlo Perrier and Emilio Segrè.",
        "Sources": "Produced synthetically."
    },
    {
        "Atomic Number": 44,
        "Name": "Ruthenium",
        "Symbol": "Ru",
        "Atomic Mass": 101.07,
        "Electron Configuration": "[Kr] 4d⁷ 5s¹",
        "Group": 8,
        "Period": 5,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Hard, white metal.",
            "Chemical": "Resistant to wear and corrosion."
        },
        "Uses": "Electrical contacts, catalysts, and jewelry.",
        "Isotopes": ["⁹⁴Ru (stable)", "⁹⁶Ru (stable)", "⁹⁷Ru (stable)", "⁹⁸Ru (stable)"],
        "History": "Ruthenium was discovered in 1844 by Karl Klaus.",
        "Sources": "Found in platinum ores."
    },
    {
        "Atomic Number": 45,
        "Name": "Rhodium",
        "Symbol": "Rh",
        "Atomic Mass": 102.91,
        "Electron Configuration": "[Kr] 4d⁸ 5s¹",
        "Group": 9,
        "Period": 5,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Hard, silvery-white metal.",
            "Chemical": "Highly reflective, resistant to corrosion."
        },
        "Uses": "Catalytic converters, jewelry, and mirrors.",
        "Isotopes": ["¹⁰⁴Rh (stable)", "¹⁰⁶Rh (stable)", "¹⁰⁷Rh (stable)"],
        "History": "Rhodium was discovered in 1803 by William Hyde Wollaston.",
        "Sources": "Found in platinum ores."
    },
    {
        "Atomic Number": 46,
        "Name": "Palladium",
        "Symbol": "Pd",
        "Atomic Mass": 106.42,
        "Electron Configuration": "[Kr] 4d¹⁰ 5s⁰",
        "Group": 10,
        "Period": 5,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Soft, malleable, and ductile.",
            "Chemical": "Resistant to corrosion and oxidation."
        },
        "Uses": "Catalytic converters, electronics, and jewelry.",
        "Isotopes": ["¹⁰²Pd (stable)", "¹⁰⁴Pd (stable)", "¹⁰⁶Pd (stable)", "¹⁰⁸Pd (stable)"],
        "History": "Palladium was discovered in 1803 by William Hyde Wollaston.",
        "Sources": "Found in platinum ores."
    },
    {
        "Atomic Number": 47,
        "Name": "Silver",
        "Symbol": "Ag",
        "Atomic Mass": 107.87,
        "Electron Configuration": "[Kr] 4d¹⁰ 5s¹",
        "Group": 11,
        "Period": 5,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Shiny, white metal.",
            "Chemical": "Conducts electricity and heat well."
        },
        "Uses": "Jewelry, coins, and electronics.",
        "Isotopes": ["¹⁰³Ag (stable)", "¹⁰⁵Ag (stable)"],
        "History": "Silver has been known since ancient times.",
        "Sources": "Found in native silver and various ores."
    },
    {
        "Atomic Number": 48,
        "Name": "Cadmium",
        "Symbol": "Cd",
        "Atomic Mass": 112.41,
        "Electron Configuration": "[Kr] 4d¹⁰ 5s²",
        "Group": 12,
        "Period": 5,
        "Nature of Element": "Transition Metal",
        "Properties": {
            "Physical": "Soft, bluish-white metal.",
            "Chemical": "Reacts with acids, toxic."
        },
        "Uses": "Batteries, pigments, and coatings.",
        "Isotopes": ["¹⁰⁶Cd (stable)", "¹⁰⁸Cd (stable)", "¹⁰⁹Cd (stable)"],
        "History": "Cadmium was discovered in 1817 by Friedrich Strohmeyer.",
        "Sources": "Found in zinc ores."
    },
    {
        "Atomic Number": 49,
        "Name": "Indium",
        "Symbol": "In",
        "Atomic Mass": 114.82,
        "Electron Configuration": "[Kr] 4d¹⁰ 5s² 5p¹",
        "Group": 13,
        "Period": 5,
        "Nature of Element": "Post-transition Metal",
        "Properties": {
            "Physical": "Soft, malleable, and ductile metal.",
            "Chemical": "Stable in air, reacts with acids."
        },
        "Uses": "Semiconductors, coatings, and alloys.",
        "Isotopes": ["¹¹³In (stable)", "¹¹⁵In (stable)"],
        "History": "Indium was discovered in 1863 by Ferdinand Reich and Heinrich Richter.",
        "Sources": "Found in zinc ores."
    },
    {
        "Atomic Number": 50,
        "Name": "Tin",
        "Symbol": "Sn",
        "Atomic Mass": 118.71,
        "Electron Configuration": "[Kr] 4d¹⁰ 5s² 5p²",
        "Group": 14,
        "Period": 5,
        "Nature of Element": "Post-transition Metal",
        "Properties": {
            "Physical": "Silvery-white metal, malleable.",
            "Chemical": "Forms various compounds with other elements."
        },
        "Uses": "Alloys, plating, and solder.",
        "Isotopes": ["¹¹⁰Sn (stable)", "¹¹²Sn (stable)", "¹¹⁴Sn (stable)", "¹¹⁶Sn (stable)"],
        "History": "Tin has been known since ancient times.",
        "Sources": "Found in cassiterite."
    },
    {
        "Atomic Number": 51,
        "Name": "Antimony",
        "Symbol": "Sb",
        "Atomic Mass": 121.76,
        "Electron Configuration": "[Kr] 4d¹⁰ 5s² 5p³",
        "Group": 15,
        "Period": 5,
        "Nature of Element": "Metalloid",
        "Properties": {
            "Physical": "Silvery-gray, brittle solid.",
            "Chemical": "Forms various alloys and compounds."
        },
        "Uses": "Flame retardants, batteries, and electronics.",
        "Isotopes": ["¹²¹Sb (stable)", "¹²³Sb (stable)"],
        "History": "Antimony has been known since ancient times.",
        "Sources": "Found in stibnite."
    },
    {
        "Atomic Number": 52,
        "Name": "Tellurium",
        "Symbol": "Te",
        "Atomic Mass": 127.60,
        "Electron Configuration": "[Kr] 4d¹⁰ 5s² 5p⁴",
        "Group": 16,
        "Period": 5,
        "Nature of Element": "Metalloid",
        "Properties": {
            "Physical": "Brittle, silvery-white solid.",
            "Chemical": "Forms various compounds, including tellurides."
        },
        "Uses": "Alloys, semiconductors, and photocells.",
        "Isotopes": ["¹²⁶Te (stable)", "¹²⁷Te (stable)", "¹²⁸Te (stable)"],
        "History": "Tellurium was discovered in 1782 by Franz-Joseph Müller von Reichenstein.",
        "Sources": "Found in gold ores and tellurides."
    },
    {
        "Atomic Number": 53,
        "Name": "Iodine",
        "Symbol": "I",
        "Atomic Mass": 126.90,
        "Electron Configuration": "[Kr] 4d¹⁰ 5s² 5p⁵",
        "Group": 17,
        "Period": 5,
        "Nature of Element": "Halogen (non-metal)",
        "Properties": {
            "Physical": "Shiny, purple-black solid.",
            "Chemical": "Reacts with many elements."
        },
        "Uses": "Antiseptics, dyes, and photography.",
        "Isotopes": ["¹²₅I (stable)", "¹²⁷I (stable)"],
        "History": "Iodine was discovered in 1811 by Bernard Courtois.",
        "Sources": "Found in seawater and certain minerals."
    },
    {
        "Atomic Number": 54,
        "Name": "Xenon",
        "Symbol": "Xe",
        "Atomic Mass": 131.29,
        "Electron Configuration": "[Kr] 4d¹⁰ 5s² 5p⁶",
        "Group": 18,
        "Period": 5,
        "Nature of Element": "Noble gas (non-metal)",
        "Properties": {
            "Physical": "Colorless gas, very dense.",
            "Chemical": "Inert, does not react with most elements."
        },
        "Uses": "Lighting, anesthetics, and as an inert gas in nuclear reactors.",
        "Isotopes": ["¹³⁰Xe (stable)", "¹³²Xe (stable)", "¹³⁴Xe (stable)"],
        "History": "Xenon was discovered in 1898 by William Ramsay and Morris Travers.",
        "Sources": "Extracted from air during fractional distillation."
    },
    {
        "Atomic Number": 55,
        "Name": "Cesium",
        "Symbol": "Cs",
        "Atomic Mass": 132.91,
        "Electron Configuration": "[Xe] 6s¹",
        "Group": 1,
        "Period": 6,
        "Nature of Element": "Alkali Metal",
        "Properties": {
            "Physical": "Soft, gold-colored metal.",
            "Chemical": "Highly reactive, especially with water."
        },
        "Uses": "Atomic clocks, research, and photoelectric cells.",
        "Isotopes": ["¹³³Cs (stable)", "¹³⁵Cs (stable)"],
        "History": "Cesium was discovered in 1860 by Robert Bunsen and Gustav Kirchhoff.",
        "Sources": "Found in minerals like pollucite."
    },
    {
        "Atomic Number": 56,
        "Name": "Barium",
        "Symbol": "Ba",
        "Atomic Mass": 137.33,
        "Electron Configuration": "[Xe] 6s²",
        "Group": 2,
        "Period": 6,
        "Nature of Element": "Alkaline Earth Metal",
        "Properties": {
            "Physical": "Soft, silvery-white metal.",
            "Chemical": "Reactive, especially with water."
        },
        "Uses": "Medical imaging, fireworks, and alloys.",
        "Isotopes": ["¹³⁴Ba (stable)", "¹³⁶Ba (stable)", "¹³⁷Ba (stable)", "¹³⁸Ba (stable)"],
        "History": "Barium was discovered in 1774 by Carl Wilhelm Scheele.",
        "Sources": "Found in minerals like barite."
    },
    {
        "Atomic Number": 57,
        "Name": "Lanthanum",
        "Symbol": "La",
        "Atomic Mass": 138.91,
        "Electron Configuration": "[Xe] 5d¹ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Silvery-white metal, ductile.",
            "Chemical": "Reacts with water and acids."
        },
        "Uses": "Lighting, catalysts, and glass production.",
        "Isotopes": ["¹³⁷La (stable)"],
        "History": "Lanthanum was discovered in 1839 by Karl Gustav Mosander.",
        "Sources": "Found in monazite and other minerals."
    },
    {
        "Atomic Number": 58,
        "Name": "Cerium",
        "Symbol": "Ce",
        "Atomic Mass": 140.12,
        "Electron Configuration": "[Xe] 4f¹ 5d¹ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Silvery-white metal, ductile.",
            "Chemical": "Oxidizes readily in air."
        },
        "Uses": "Catalysts, glass polishing, and in alloys.",
        "Isotopes": ["¹³⁴Ce (stable)", "¹³⁶Ce (stable)", "¹³⁷Ce (stable)", "¹³⁸Ce (stable)"],
        "History": "Cerium was discovered in 1803 by Jöns Jacob Berzelius and Wilhelm Hisinger.",
        "Sources": "Found in monazite and bastnäsite."
    },
    {
        "Atomic Number": 59,
        "Name": "Praseodymium",
        "Symbol": "Pr",
        "Atomic Mass": 140.91,
        "Electron Configuration": "[Xe] 4f³ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Silvery-white metal.",
            "Chemical": "Reacts with water and acids."
        },
        "Uses": "Alloys, magnets, and glasses.",
        "Isotopes": ["¹⁴³Pr (stable)", "¹⁴⁵Pr (stable)"],
        "History": "Praseodymium was discovered in 1885 by Karl Auer von Welsbach.",
        "Sources": "Found in minerals like monazite."
    },
    {
        "Atomic Number": 60,
        "Name": "Neodymium",
        "Symbol": "Nd",
        "Atomic Mass": 144.24,
        "Electron Configuration": "[Xe] 4f⁴ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Silvery-white metal.",
            "Chemical": "Oxidizes readily in air."
        },
        "Uses": "Magnets, lasers, and glasses.",
        "Isotopes": ["¹⁴²Nd (stable)", "¹⁴⁴Nd (stable)", "¹⁴⁵Nd (stable)", "¹⁴⁶Nd (stable)"],
        "History": "Neodymium was discovered in 1885 by Carl Auer von Welsbach.",
        "Sources": "Found in minerals like monazite."
    },
    
    {
        "Atomic Number": 61,
        "Name": "Promethium",
        "Symbol": "Pm",
        "Atomic Mass": 145,
        "Electron Configuration": "[Xe] 4f⁵ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Silvery, metallic.",
            "Chemical": "Radioactive, no stable isotopes."
        },
        "Uses": "Pacemakers, luminous paint, atomic batteries.",
        "Isotopes": ["¹⁴⁵Pm (radioactive)", "¹⁴⁶Pm (radioactive)", "¹⁴⁷Pm (radioactive)"],
        "History": "Promethium was first produced and identified in 1945 by Jacob Marinsky and Lawrence Glendenin.",
        "Sources": "Produced in nuclear reactors and found in uranium ores."
    },
    {
        "Atomic Number": 62,
        "Name": "Samarium",
        "Symbol": "Sm",
        "Atomic Mass": 150.36,
        "Electron Configuration": "[Xe] 4f⁶ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Silvery-white metal.",
            "Chemical": "Oxidizes in air, reacts with water.",
        },
        "Uses": "Magnets, nuclear reactors, lasers.",
        "Isotopes": ["¹⁴⁸Sm (stable)", "¹⁵²Sm (stable)", "¹⁵⁴Sm (stable)"],
        "History": "Discovered in 1879 by Paul-Émile Lecoq de Boisbaudran.",
        "Sources": "Found in minerals like monazite and bastnäsite."
    },
    {
        "Atomic Number": 63,
        "Name": "Europium",
        "Symbol": "Eu",
        "Atomic Mass": 151.96,
        "Electron Configuration": "[Xe] 4f⁷ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Soft, silvery metal.",
            "Chemical": "Highly reactive, oxidizes quickly in air.",
        },
        "Uses": "Phosphorescent in TV screens, fluorescent lamps.",
        "Isotopes": ["¹⁵¹Eu (stable)", "¹⁵³Eu (stable)"],
        "History": "Discovered by Eugène-Anatole Demarçay in 1901.",
        "Sources": "Found in bastnäsite and monazite ores."
    },
    {
        "Atomic Number": 64,
        "Name": "Gadolinium",
        "Symbol": "Gd",
        "Atomic Mass": 157.25,
        "Electron Configuration": "[Xe] 4f⁷ 5d¹ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Silvery-white, malleable, ductile.",
            "Chemical": "Oxidizes in air, reacts slowly with water.",
        },
        "Uses": "MRI contrast agents, neutron capture in nuclear reactors.",
        "Isotopes": ["¹⁵⁴Gd (stable)", "¹⁵⁶Gd (stable)", "¹⁵⁸Gd (stable)"],
        "History": "Discovered by Jean Charles Galissard de Marignac in 1880.",
        "Sources": "Found in minerals like monazite and bastnäsite."
    },
    {
        "Atomic Number": 65,
        "Name": "Terbium",
        "Symbol": "Tb",
        "Atomic Mass": 158.93,
        "Electron Configuration": "[Xe] 4f⁸ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Silvery-white, soft, malleable.",
            "Chemical": "Oxidizes slowly in air, reacts with water.",
        },
        "Uses": "Green phosphor in color TV tubes, lasers, fuel cells.",
        "Isotopes": ["¹⁵⁹Tb (stable)"],
        "History": "Discovered by Carl Gustaf Mosander in 1843.",
        "Sources": "Found in gadolinite, monazite, and other rare earth minerals."
    },
    {
        "Atomic Number": 66,
        "Name": "Dysprosium",
        "Symbol": "Dy",
        "Atomic Mass": 162.5,
        "Electron Configuration": "[Xe] 4f¹⁰ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Soft, silvery metal.",
            "Chemical": "Oxidizes slowly in air, reacts with water and acids.",
        },
        "Uses": "Magnets, nuclear reactor control rods, laser materials.",
        "Isotopes": ["¹⁶⁰Dy (stable)", "¹⁶²Dy (stable)", "¹⁶⁴Dy (stable)"],
        "History": "Discovered by Paul-Émile Lecoq de Boisbaudran in 1886.",
        "Sources": "Found in minerals such as xenotime and monazite."
    },
    {
        "Atomic Number": 67,
        "Name": "Holmium",
        "Symbol": "Ho",
        "Atomic Mass": 164.93,
        "Electron Configuration": "[Xe] 4f¹¹ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Soft, malleable, silvery-white metal.",
            "Chemical": "Oxidizes in air, reacts with water.",
        },
        "Uses": "Nuclear reactors, magnets, lasers.",
        "Isotopes": ["¹⁶⁵Ho (stable)"],
        "History": "Discovered by Marc Delafontaine and Jacques-Louis Soret in 1878.",
        "Sources": "Found in minerals like monazite and gadolinite."
    },
    {
        "Atomic Number": 68,
        "Name": "Erbium",
        "Symbol": "Er",
        "Atomic Mass": 167.26,
        "Electron Configuration": "[Xe] 4f¹² 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Soft, malleable, silvery-white metal.",
            "Chemical": "Oxidizes slowly in air, reacts with water.",
        },
        "Uses": "Lasers, fiber optics, nuclear technology.",
        "Isotopes": ["¹⁶⁶Er (stable)", "¹⁶⁸Er (stable)", "¹⁷°Er (stable)"],
        "History": "Discovered by Carl Gustaf Mosander in 1843.",
        "Sources": "Found in minerals like monazite and xenotime."
    },
    {
        "Atomic Number": 69,
        "Name": "Thulium",
        "Symbol": "Tm",
        "Atomic Mass": 168.93,
        "Electron Configuration": "[Xe] 4f¹³ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Silvery-gray, soft, ductile.",
            "Chemical": "Oxidizes in air, reacts with water and acids.",
        },
        "Uses": "Portable X-ray machines, lasers, radiation sources.",
        "Isotopes": ["¹⁶⁹Tm (stable)"],
        "History": "Discovered by Per Teodor Cleve in 1879.",
        "Sources": "Found in minerals like monazite and xenotime."
    },
    {
        "Atomic Number": 70,
        "Name": "Ytterbium",
        "Symbol": "Yb",
        "Atomic Mass": 173.05,
        "Electron Configuration": "[Xe] 4f¹⁴ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Soft, malleable, silvery-white metal.",
            "Chemical": "Oxidizes slowly in air, reacts with acids.",
        },
        "Uses": "Lasers, atomic clocks, alloys.",
        "Isotopes": ["¹⁷²Yb (stable)", "¹⁷³Yb (stable)", "¹⁷⁴Yb (stable)"],
        "History": "Discovered by Jean Charles Galissard de Marignac in 1878.",
        "Sources": "Found in minerals like monazite and xenotime."
    },
    {
        "Atomic Number": 71,
        "Name": "Lutetium",
        "Symbol": "Lu",
        "Atomic Mass": 174.97,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d¹ 6s²",
        "Group": 3,
        "Period": 6,
        "Nature of Element": "Lanthanide",
        "Properties": {
            "Physical": "Hard, silvery-white metal.",
            "Chemical": "Oxidizes slowly in air, reacts with water and acids.",
        },
        "Uses": "Petroleum refining, cancer treatment (radioisotopes).",
        "Isotopes": ["¹⁷⁵Lu (stable)"],
        "History": "Discovered by Georges Urbain in 1907.",
        "Sources": "Found in minerals like monazite and xenotime."
    },
    {
        "Atomic Number": 72,
        "Name": "Hafnium",
        "Symbol": "Hf",
        "Atomic Mass": 178.49,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d² 6s²",
        "Group": 4,
        "Period": 6,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Shiny, silvery, corrosion-resistant.",
            "Chemical": "Resistant to acids and bases, reacts with halogens.",
        },
        "Uses": "Control rods in nuclear reactors, semiconductors, superalloys.",
        "Isotopes": ["¹⁷⁴Hf (stable)", "¹⁷⁶Hf (stable)", "¹⁷⁸Hf (stable)", "¹⁸°Hf (stable)"],
        "History": "Discovered by Dirk Coster and George de Hevesy in 1923.",
        "Sources": "Found in zirconium minerals."
    },
    {
        "Atomic Number": 73,
        "Name": "Tantalum",
        "Symbol": "Ta",
        "Atomic Mass": 180.95,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d³ 6s²",
        "Group": 5,
        "Period": 6,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Dense, hard, blue-gray metal.",
            "Chemical": "Corrosion-resistant, forms stable oxides.",
        },
        "Uses": "Capacitors, medical implants, alloys.",
        "Isotopes": ["¹⁸¹Ta (stable)"],
        "History": "Discovered by Anders Gustaf Ekeberg in 1802.",
        "Sources": "Found in minerals like coltan and tantalite."
    },
    {
        "Atomic Number": 74,
        "Name": "Tungsten",
        "Symbol": "W",
        "Atomic Mass": 183.84,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d⁴ 6s²",
        "Group": 6,
        "Period": 6,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Hard, dense, gray-white metal.",
            "Chemical": "High melting point, resistant to corrosion.",
        },
        "Uses": "Light bulb filaments, cutting tools, high-temperature alloys.",
        "Isotopes": ["¹⁸²W (stable)", "¹⁸⁴W (stable)", "¹⁸⁶W (stable)"],
        "History": "Discovered by Juan José and Fausto Elhuyar in 1783.",
        "Sources": "Found in minerals like wolframite and scheelite."
    },
    {
        "Atomic Number": 75,
        "Name": "Rhenium",
        "Symbol": "Re",
        "Atomic Mass": 186.21,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d⁵ 6s²",
        "Group": 7,
        "Period": 6,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Dense, silvery-white metal.",
            "Chemical": "High melting point, resists corrosion.",
        },
        "Uses": "Superalloys, jet engines, thermocouples.",
        "Isotopes": ["¹⁸⁵Re (stable)"],
        "History": "Discovered by Masataka Ogawa in 1908.",
        "Sources": "Found in molybdenite and porphyry copper deposits."
    },
    {
        "Atomic Number": 76,
        "Name": "Osmium",
        "Symbol": "Os",
        "Atomic Mass": 190.23,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d⁶ 6s²",
        "Group": 8,
        "Period": 6,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Hard, brittle, bluish-white metal.",
            "Chemical": "Resists acids, reacts with oxygen at high temperatures.",
        },
        "Uses": "Pen tips, electrical contacts, alloys.",
        "Isotopes": ["¹⁸⁸Os (stable)", "¹⁹°Os (stable)", "¹⁹²Os (stable)"],
        "History": "Discovered by Smithson Tennant in 1803.",
        "Sources": "Found in platinum ores."
    },
    {
        "Atomic Number": 77,
        "Name": "Iridium",
        "Symbol": "Ir",
        "Atomic Mass": 192.22,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d⁷ 6s²",
        "Group": 9,
        "Period": 6,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Dense, hard, brittle, silvery-white.",
            "Chemical": "Highly corrosion-resistant, resists acids.",
        },
        "Uses": "Spark plugs, crucibles, pen nibs, alloys.",
        "Isotopes": ["¹⁹¹Ir (stable)", "¹⁹³Ir (stable)"],
        "History": "Discovered by Smithson Tennant in 1803.",
        "Sources": "Found in platinum ores and as a byproduct of nickel mining."
    },
    {
        "Atomic Number": 78,
        "Name": "Platinum",
        "Symbol": "Pt",
        "Atomic Mass": 195.08,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d⁹ 6s¹",
        "Group": 10,
        "Period": 6,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Dense, malleable, silvery-white metal.",
            "Chemical": "Resistant to corrosion and oxidation.",
        },
        "Uses": "Catalysts, jewelry, electrical contacts.",
        "Isotopes": ["¹⁹⁴Pt (stable)", "¹⁹⁵Pt (stable)", "¹⁹⁶Pt (stable)", "¹⁹⁸Pt (stable)"],
        "History": "Used by pre-Columbian South Americans and officially discovered by Antonio de Ulloa in 1735.",
        "Sources": "Found in nickel and copper ores, as well as alluvial deposits."
    },

    {
        "Atomic Number": 79,
        "Name": "Gold",
        "Symbol": "Au",
        "Atomic Mass": 196.97,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s¹",
        "Group": 11,
        "Period": 6,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Dense, malleable, yellow metal.",
            "Chemical": "Resistant to corrosion, reacts with halogens.",
        },
        "Uses": "Jewelry, electronics, currency.",
        "Isotopes": ["¹⁹⁷Au (stable)"],
        "History": "Known since antiquity, used in jewelry and trade.",
        "Sources": "Found in alluvial deposits and as a byproduct of copper and lead refining."
    },
    {
        "Atomic Number": 80,
        "Name": "Mercury",
        "Symbol": "Hg",
        "Atomic Mass": 200.59,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s²",
        "Group": 12,
        "Period": 6,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Liquid at room temperature, silvery-white metal.",
            "Chemical": "Forms amalgams with metals, reacts with sulfur and halogens."
        },
        "Uses": "Thermometers, barometers, fluorescent lighting.",
        "Isotopes": ["¹⁹⁶Hg (stable)", "¹⁹⁸Hg (stable)", "²⁰²Hg (stable)", "²⁰⁴Hg (stable)"],
        "History": "Known since ancient times; used by alchemists.",
        "Sources": "Found in cinnabar (HgS) deposits."
    },

    {
        "Atomic Number": 81,
        "Name": "Thallium",
        "Symbol": "Tl",
        "Atomic Mass": 204.38,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹",
        "Group": 13,
        "Period": 6,
        "Nature of Element": "Post-transition metal",
        "Properties": {
            "Physical": "Soft, malleable, silvery-white metal.",
            "Chemical": "Oxidizes in air, forms poisonous compounds."
        },
        "Uses": "Electronic components, optical lenses, rat poison (historically).",
        "Isotopes": ["²⁰³Tl (stable)", "²⁰⁵Tl (stable)"],
        "History": "Discovered by William Crookes in 1861.",
        "Sources": "Found in minerals like crookesite and lorandite."
    },
    {
        "Atomic Number": 82,
        "Name": "Lead",
        "Symbol": "Pb",
        "Atomic Mass": 207.2,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²",
        "Group": 14,
        "Period": 6,
        "Nature of Element": "Post-transition metal",
        "Properties": {
            "Physical": "Dense, soft, malleable, bluish-gray metal.",
            "Chemical": "Resistant to corrosion, forms oxides.",
        },
        "Uses": "Batteries, radiation shielding, ammunition.",
        "Isotopes": ["²⁰⁴Pb (stable)", "²⁰⁶Pb (stable)", "²⁰⁷Pb (stable)", "²⁰⁸Pb (stable)"],
        "History": "Known since ancient times; used by Romans for plumbing.",
        "Sources": "Found in galena (PbS) and other lead ores."
    },
    {
        "Atomic Number": 83,
        "Name": "Bismuth",
        "Symbol": "Bi",
        "Atomic Mass": 208.98,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³",
        "Group": 15,
        "Period": 6,
        "Nature of Element": "Post-transition metal",
        "Properties": {
            "Physical": "Brittle, crystalline, silvery-pink metal.",
            "Chemical": "Stable and non-toxic, expands upon solidification.",
        },
        "Uses": "Cosmetics, fire sprinklers, pharmaceuticals.",
        "Isotopes": ["²⁰⁹Bi (stable)"],
        "History": "Known since ancient times, often confused with lead.",
        "Sources": "Found in bismuthinite (Bi₂S₃) and native bismuth."
    },
    {
        "Atomic Number": 84,
        "Name": "Polonium",
        "Symbol": "Po",
        "Atomic Mass": 209,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁴",
        "Group": 16,
        "Period": 6,
        "Nature of Element": "Metalloid",
        "Properties": {
            "Physical": "Silvery, radioactive, brittle metal.",
            "Chemical": "Highly radioactive and toxic.",
        },
        "Uses": "Antistatic devices, heat sources in space equipment.",
        "Isotopes": ["²⁰⁹Po (radioactive)", "²¹⁰Po (radioactive)"],
        "History": "Discovered by Marie Curie and Pierre Curie in 1898.",
        "Sources": "Found in uranium ores."
    },
    {
        "Atomic Number": 85,
        "Name": "Astatine",
        "Symbol": "At",
        "Atomic Mass": 210,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁵",
        "Group": 17,
        "Period": 6,
        "Nature of Element": "Halogen",
        "Properties": {
            "Physical": "Radioactive, dark solid at room temperature.",
            "Chemical": "Forms compounds similar to iodine, very rare and unstable."
        },
        "Uses": "Cancer treatment (research), radiotherapy.",
        "Isotopes": ["²¹⁰At (radioactive)", "²¹¹At (radioactive)"],
        "History": "First synthesized by Dale R. Corson, Kenneth Ross MacKenzie, and Emilio Segrè in 1940.",
        "Sources": "Produced artificially in particle accelerators."
    },
    {
        "Atomic Number": 86,
        "Name": "Radon",
        "Symbol": "Rn",
        "Atomic Mass": 222,
        "Electron Configuration": "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶",
        "Group": 18,
        "Period": 6,
        "Nature of Element": "Noble gas",
        "Properties": {
            "Physical": "Colorless, odorless, radioactive gas.",
            "Chemical": "Inert, radioactive decay product of radium."
        },
        "Uses": "Cancer treatment (historically), earthquake prediction (research).",
        "Isotopes": ["²²²Rn (radioactive)"],
        "History": "Discovered by Friedrich Ernst Dorn in 1898.",
        "Sources": "Occurs naturally from the decay of radium in rocks and soil."
    },
    {
        "Atomic Number": 87,
        "Name": "Francium",
        "Symbol": "Fr",
        "Atomic Mass": 223,
        "Electron Configuration": "[Rn] 7s¹",
        "Group": 1,
        "Period": 7,
        "Nature of Element": "Alkali metal",
        "Properties": {
            "Physical": "Highly radioactive, metallic.",
            "Chemical": "Extremely reactive, similar to cesium."
        },
        "Uses": "No significant uses due to rarity and radioactivity.",
        "Isotopes": ["²²³Fr (radioactive)"],
        "History": "Discovered by Marguerite Perey in 1939.",
        "Sources": "Occurs naturally as a decay product of actinium."
    },
    {
        "Atomic Number": 88,
        "Name": "Radium",
        "Symbol": "Ra",
        "Atomic Mass": 226,
        "Electron Configuration": "[Rn] 7s²",
        "Group": 2,
        "Period": 7,
        "Nature of Element": "Alkaline earth metal",
        "Properties": {
            "Physical": "Silvery-white, highly radioactive metal.",
            "Chemical": "Reacts with water, forms radium hydroxide."
        },
        "Uses": "Cancer treatment (historical), luminous paints (historical).",
        "Isotopes": ["²²⁶Ra (radioactive)"],
        "History": "Discovered by Marie Curie and Pierre Curie in 1898.",
        "Sources": "Found in uranium ores like pitchblende."
    },
    {
        "Atomic Number": 89,
        "Name": "Actinium",
        "Symbol": "Ac",
        "Atomic Mass": 227,
        "Electron Configuration": "[Rn] 6d¹ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Silvery, radioactive, glows in the dark.",
            "Chemical": "Reacts with oxygen and moisture, forming oxides."
        },
        "Uses": "Neutron sources, cancer treatment (research).",
        "Isotopes": ["²²⁷Ac (radioactive)"],
        "History": "Discovered by Friedrich Oskar Giesel in 1899.",
        "Sources": "Occurs naturally in uranium and thorium ores."
    },
    {
        "Atomic Number": 90,
        "Name": "Thorium",
        "Symbol": "Th",
        "Atomic Mass": 232.04,
        "Electron Configuration": "[Rn] 6d² 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Silvery, radioactive metal.",
            "Chemical": "Reacts slowly with oxygen and water.",
        },
        "Uses": "Nuclear reactors, gas mantles, alloying agent.",
        "Isotopes": ["²³²Th (radioactive)"],
        "History": "Discovered by Jöns Jakob Berzelius in 1828.",
        "Sources": "Found in thorite and monazite ores."
    },
    {
        "Atomic Number": 91,
        "Name": "Protactinium",
        "Symbol": "Pa",
        "Atomic Mass": 231.04,
        "Electron Configuration": "[Rn] 5f² 6d¹ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Dense, silvery-gray metal.",
            "Chemical": "Highly reactive, forms various oxides and halides."
        },
        "Uses": "No major uses, research interest.",
        "Isotopes": ["²³¹Pa (radioactive)"],
        "History": "Discovered by Otto Hahn and Lise Meitner in 1913.",
        "Sources": "Found in uranium ores."
    },
    {
        "Atomic Number": 92,
        "Name": "Uranium",
        "Symbol": "U",
        "Atomic Mass": 238.03,
        "Electron Configuration": "[Rn] 5f³ 6d¹ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Silvery-gray, dense, radioactive metal.",
            "Chemical": "Reacts with oxygen, forming uranium oxides."
        },
        "Uses": "Nuclear fuel, weapons, radiation shielding.",
        "Isotopes": ["²³⁸U (radioactive)", "²³⁵U (radioactive)"],
        "History": "Discovered by Martin Heinrich Klaproth in 1789.",
        "Sources": "Found in minerals like uraninite and pitchblende."
    },
    {
        "Atomic Number": 93,
        "Name": "Neptunium",
        "Symbol": "Np",
        "Atomic Mass": 237,
        "Electron Configuration": "[Rn] 5f⁴ 6d¹ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Silvery, radioactive metal.",
            "Chemical": "Reacts with oxygen and halogens.",
        },
        "Uses": "Nuclear reactors, research.",
        "Isotopes": ["²³⁷Np (radioactive)"],
        "History": "Discovered by Edwin McMillan and Philip H. Abelson in 1940.",
        "Sources": "Produced in nuclear reactors from uranium."
    },
    {
        "Atomic Number": 94,
        "Name": "Plutonium",
        "Symbol": "Pu",
        "Atomic Mass": 244,
        "Electron Configuration": "[Rn] 5f⁶ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Silvery, radioactive metal.",
            "Chemical": "Forms various oxides and hydrides.",
        },
        "Uses": "Nuclear weapons, reactors, space probes.",
        "Isotopes": ["²³⁹Pu (radioactive)", "²⁴⁰Pu (radioactive)"],
        "History": "Discovered by Glenn T. Seaborg, Arthur Wahl, and Joseph Kennedy in 1940.",
        "Sources": "Produced in nuclear reactors."
    },
    {
        "Atomic Number": 95,
        "Name": "Americium",
        "Symbol": "Am",
        "Atomic Mass": 243,
        "Electron Configuration": "[Rn] 5f⁷ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Silvery-white, radioactive metal.",
            "Chemical": "Reacts with oxygen, forms americium oxides.",
        },
        "Uses": "Smoke detectors, neutron sources.",
        "Isotopes": ["²⁴¹Am (radioactive)", "²⁴³Am (radioactive)"],
        "History": "Discovered by Glenn T. Seaborg in 1944.",
        "Sources": "Produced in nuclear reactors."
    },
    {
        "Atomic Number": 96,
        "Name": "Curium",
        "Symbol": "Cm",
        "Atomic Mass": 247,
        "Electron Configuration": "[Rn] 5f⁷ 6d¹ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Radioactive, silvery metal.",
            "Chemical": "Reacts with oxygen to form oxides.",
        },
        "Uses": "Power source for space equipment.",
        "Isotopes": ["²⁴⁴Cm (radioactive)", "²⁴⁵Cm (radioactive)"],
        "History": "Discovered by Glenn T. Seaborg, Albert Ghiorso, and James in 1944.",
        "Sources": "Produced in nuclear reactors."
    },
    {
        "Atomic Number": 97,
        "Name": "Berkelium",
        "Symbol": "Bk",
        "Atomic Mass": 247,
        "Electron Configuration": "[Rn] 5f⁹ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Radioactive, silvery metal.",
            "Chemical": "Oxidizes slowly in air.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁴⁷Bk (radioactive)"],
        "History": "Discovered by Glenn T. Seaborg, Albert Ghiorso, and Stanley G. Thompson in 1949.",
        "Sources": "Produced in nuclear reactors."
    },
    {
        "Atomic Number": 98,
        "Name": "Californium",
        "Symbol": "Cf",
        "Atomic Mass": 251,
        "Electron Configuration": "[Rn] 5f¹⁰ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Radioactive, silvery-white metal.",
            "Chemical": "Reacts with water and oxygen.",
        },
        "Uses": "Neutron sources, cancer treatment, radiography.",
        "Isotopes": ["²⁵²Cf (radioactive)"],
        "History": "Discovered by Stanley G. Thompson, Albert Ghiorso, and Glenn T. Seaborg in 1950.",
        "Sources": "Produced in nuclear reactors."
    },
    {
        "Atomic Number": 99,
        "Name": "Einsteinium",
        "Symbol": "Es",
        "Atomic Mass": 252,
        "Electron Configuration": "[Rn] 5f¹¹ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Radioactive, silvery metal.",
            "Chemical": "Oxidizes slowly in air.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁵³Es (radioactive)"],
        "History": "Discovered by Albert Ghiorso in 1952.",
        "Sources": "Produced in nuclear reactors."
    },
    {
        "Atomic Number": 100,
        "Name": "Fermium",
        "Symbol": "Fm",
        "Atomic Mass": 257,
        "Electron Configuration": "[Rn] 5f¹² 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Radioactive, silvery metal.",
            "Chemical": "Reacts with oxygen to form oxides.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁵⁷Fm (radioactive)"],
        "History": "Discovered by Albert Ghiorso and team in 1952.",
        "Sources": "Produced in nuclear reactors."
    },
    {
        "Atomic Number": 101,
        "Name": "Mendelevium",
        "Symbol": "Md",
        "Atomic Mass": 258,
        "Electron Configuration": "[Rn] 5f¹³ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁵⁸Md (radioactive)"],
        "History": "Discovered by Albert Ghiorso and team in 1955.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 102,
        "Name": "Nobelium",
        "Symbol": "No",
        "Atomic Mass": 259,
        "Electron Configuration": "[Rn] 5f¹⁴ 7s²",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁵⁹No (radioactive)"],
        "History": "Discovered by Albert Ghiorso and team in 1966.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 103,
        "Name": "Lawrencium",
        "Symbol": "Lr",
        "Atomic Mass": 262,
        "Electron Configuration": "[Rn] 5f¹⁴ 7s² 7p¹",
        "Group": 3,
        "Period": 7,
        "Nature of Element": "Actinide",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁶²Lr (radioactive)"],
        "History": "Discovered by Albert Ghiorso and team in 1961.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 104,
        "Name": "Rutherfordium",
        "Symbol": "Rf",
        "Atomic Mass": 267,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d² 7s²",
        "Group": 4,
        "Period": 7,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁶⁷Rf (radioactive)"],
        "History": "Discovered by Georgy Flerov and team in 1964.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 105,
        "Name": "Dubnium",
        "Symbol": "Db",
        "Atomic Mass": 270,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d³ 7s²",
        "Group": 5,
        "Period": 7,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁷°Db (radioactive)"],
        "History": "Discovered by Albert Ghiorso and team in 1967.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 106,
        "Name": "Seaborgium",
        "Symbol": "Sg",
        "Atomic Mass": 271,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d⁴ 7s²",
        "Group": 6,
        "Period": 7,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁷¹Sg (radioactive)"],
        "History": "Discovered by Albert Ghiorso and team in 1974.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 107,
        "Name": "Bohrium",
        "Symbol": "Bh",
        "Atomic Mass": 274,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d⁵ 7s²",
        "Group": 7,
        "Period": 7,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁷⁴Bh (radioactive)"],
        "History": "Discovered by Peter Armbruster and Gottfried Münzenberg in 1981.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 108,
        "Name": "Hassium",
        "Symbol": "Hs",
        "Atomic Mass": 277,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d⁶ 7s²",
        "Group": 8,
        "Period": 7,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁷⁷Hs (radioactive)"],
        "History": "Discovered by Peter Armbruster and Gottfried Münzenberg in 1984.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 109,
        "Name": "Meitnerium",
        "Symbol": "Mt",
        "Atomic Mass": 278,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d⁷ 7s²",
        "Group": 9,
        "Period": 7,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁷⁸Mt (radioactive)"],
        "History": "Discovered by Peter Armbruster and Gottfried Münzenberg in 1982.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 110,
        "Name": "Darmstadtium",
        "Symbol": "Ds",
        "Atomic Mass": 281,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d⁸ 7s²",
        "Group": 10,
        "Period": 7,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁸¹Ds (radioactive)"],
        "History": "Discovered by Peter Armbruster and Gottfried Münzenberg in 1994.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 111,
        "Name": "Roentgenium",
        "Symbol": "Rg",
        "Atomic Mass": 282,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d⁹ 7s²",
        "Group": 11,
        "Period": 7,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁸²Rg (radioactive)"],
        "History": "Discovered by Peter Armbruster and Gottfried Münzenberg in 1994.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 112,
        "Name": "Copernicium",
        "Symbol": "Cn",
        "Atomic Mass": 285,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d¹⁰ 7s²",
        "Group": 12,
        "Period": 7,
        "Nature of Element": "Transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁸⁵Cn (radioactive)"],
        "History": "Discovered by Sigurd Hofmann and Victor Ninov in 1996.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 113,
        "Name": "Nihonium",
        "Symbol": "Nh",
        "Atomic Mass": 286,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p¹",
        "Group": 13,
        "Period": 7,
        "Nature of Element": "Post-transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁸⁶Nh (radioactive)"],
        "History": "Discovered by Kosuke Morita and team in 2003.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 114,
        "Name": "Flerovium",
        "Symbol": "Fl",
        "Atomic Mass": 289,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p²",
        "Group": 14,
        "Period": 7,
        "Nature of Element": "Post-transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁸⁹Fl (radioactive)"],
        "History": "Discovered by Yuri Oganessian and team in 1999.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 115,
        "Name": "Moscovium",
        "Symbol": "Mc",
        "Atomic Mass": 290,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p³",
        "Group": 15,
        "Period": 7,
        "Nature of Element": "Post-transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁹⁰Mc (radioactive)"],
        "History": "Discovered by Yuri Oganessian and team in 2003.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 116,
        "Name": "Livermorium",
        "Symbol": "Lv",
        "Atomic Mass": 293,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁴",
        "Group": 16,
        "Period": 7,
        "Nature of Element": "Post-transition metal",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁹³Lv (radioactive)"],
        "History": "Discovered by Yuri Oganessian and team in 2000.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 117,
        "Name": "Tennessine",
        "Symbol": "Ts",
        "Atomic Mass": 294,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁵",
        "Group": 17,
        "Period": 7,
        "Nature of Element": "Halogen",
        "Properties": {
            "Physical": "Radioactive, metallic.",
            "Chemical": "No bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁹⁴Ts (radioactive)"],
        "History": "Discovered by Yuri Oganessian and team in 2010.",
        "Sources": "Produced in particle accelerators."
    },
    {
        "Atomic Number": 118,
        "Name": "Oganesson",
        "Symbol": "Og",
        "Atomic Mass": 294,
        "Electron Configuration": "[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁶",
        "Group": 18,
        "Period": 7,
        "Nature of Element": "Noble gas",
        "Properties": {
            "Physical": "Radioactive, unknown state.",
            "Chemical": "Inert, no bulk properties observed.",
        },
        "Uses": "Scientific research.",
        "Isotopes": ["²⁹⁴Og (radioactive)"],
        "History": "Discovered by Yuri Oganessian and team in 2002.",
        "Sources": "Produced in particle accelerators."
    }
]


# Function to display element information
def display_element_info_by_name(element_name):
    found = False
    for element in elements:
        if element_name.lower() == element["Name"].lower():
            found = True
            st.write(f"### {element['Name']} (Symbol: {element['Symbol']})")
            st.write(f"**Atomic Number**: {element['Atomic Number']}")
            st.write(f"**Atomic Mass**: {element['Atomic Mass']} u")
            st.write(f"**Electron Configuration**: {element['Electron Configuration']}")
            st.write(f"**Group**: {element['Group']}")
            st.write(f"**Period**: {element['Period']}")
            st.write(f"**Nature of Element**: {element['Nature of Element']}")
            st.write("**Properties**:")
            st.write(f"  - **Physical**: {element['Properties']['Physical']}")
            st.write(f"  - **Chemical**: {element['Properties']['Chemical']}")
            st.write(f"**Uses**: {element['Uses']}")
            st.write(f"**Isotopes**: {', '.join(element['Isotopes'])}")
            st.write(f"**History**: {element['History']}")
            st.write(f"**Sources**: {element['Sources']}")
            break
    if not found:
        st.write(f"No element found with the name: {element_name}")

# Streamlit app setup
st.title("Periodic Table Explorer")

# Dropdown to select an element by name
element_name = st.selectbox("Select an element", [element["Name"] for element in elements])

# Display the selected element information
display_element_info_by_name(element_name)
