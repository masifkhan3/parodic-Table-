import streamlit as st
# Your app code
st.title("My Periodic Table App")
import streamlit as st

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
    }
    # Add more elements as needed
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
