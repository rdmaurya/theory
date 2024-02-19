
import streamlit as st

def charles_law():
    return "Charles's law states that at constant pressure, the volume of a fixed amount of gas is directly proportional to its absolute temperature."

def boyles_law():
    return "Boyle's law states that at constant temperature, the volume of a given mass of gas is inversely proportional to its pressure."

def gay_lussacs_law():
    return "Gay-Lussac's law states that the pressure of a gas is directly proportional to the absolute temperature when the volume is held constant."

def main():
    st.title("Gas Laws Statements")

    st.write("### Charles's Law:")
    st.write(charles_law())

    st.write("### Boyle's Law:")
    st.write(boyles_law())

    st.write("### Gay-Lussac's Law:")
    st.write(gay_lussacs_law())



if __name__ == "__main__":
    main()

