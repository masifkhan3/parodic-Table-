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
        }
    },
    {
        "Atomic Number": 2,
        "Name": "Helium",
        "Symbol": "He",
        "Atomic Mass": 4.0026,
        "Electron Configuration": "1s²",
        "Group": 18,
        "Period": 1,
        "Nature of Element": "Noble gas",
        "Properties": {
            "Physical": "Colorless, odorless, tasteless gas.",
            "Chemical": "Inert, does not react under normal conditions."
        }
    },
    # Add more elements as needed
]

# Streamlit app code
st.title("Periodic Table")

# Dropdown to select an element
selected_element = st.selectbox("Select an element", [element["Name"] for element in elements])

# Display selected element details
for element in elements:
    if element["Name"] == selected_element:
        st.subheader(f"{element['Name']} (Symbol: {element['Symbol']})")
        st.write(f"**Atomic Number**: {element['Atomic Number']}")
        st.write(f"**Atomic Mass**: {element['Atomic Mass']}")
        st.write(f"**Electron Configuration**: {element['Electron Configuration']}")
        st.write(f"**Group**: {element['Group']}")
        st.write(f"**Period**: {element['Period']}")
        st.write(f"**Nature of Element**: {element['Nature of Element']}")
        st.write("**Properties**:")
        st.write(f" - **Physical**: {element['Properties']['Physical']}")
        st.write(f" - **Chemical**: {element['Properties']['Chemical']}")
