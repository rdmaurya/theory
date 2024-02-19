import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Boyle's Law: P1 * V1 = P2 * V2
def boyles_law(V1, P1, V2):
    return P1 * V1 / V2

# Charles's Law: V1 / T1 = V2 / T2
def charles_law(V1, T1, V2):
    return V2 * T1 / V1

# Pressure Law: P1 / T1 = P2 / T2
def pressure_law(P1, T1, P2):
    return P2 * T1 / P1

def main():
    st.title("Gas Laws Visualization")

    # Sidebar inputs
    st.sidebar.header("Gas Properties")
    P1 = st.sidebar.number_input("Initial Pressure (P1)", value=1.0)
    T1 = st.sidebar.number_input("Initial Temperature (T1)", value=273.15)
    V1 = st.sidebar.number_input("Initial Volume (V1)", value=1.0)
    V2 = st.sidebar.number_input("Final Volume (V2)", value=1.0)

    # Calculate final pressures using the gas laws
    P2_boyle = boyles_law(V1, P1, V2)
    T2_charles = charles_law(V1, T1, V2)
    P2_pressure = pressure_law(P1, T1, P2_boyle)

    # Display the results
    st.write("## Results")
    st.write(f"Final Pressure (Boyle's Law): {P2_boyle:.2f} atm")
    st.write(f"Final Temperature (Charles's Law): {T2_charles:.2f} K")
    st.write(f"Final Pressure (Pressure Law): {P2_pressure:.2f} atm")

    # Create plots
    plt.figure(figsize=(12, 4))

    # Boyle's Law
    plt.subplot(1, 3, 1)
    plt.plot([V1, V2], [P1, P2_boyle], marker='o')
    plt.xlabel('Volume (Liters)')
    plt.ylabel('Pressure (atm)')
    plt.title("Boyle's Law")

    # Charles's Law
    plt.subplot(1, 3, 2)
    plt.plot([T1, T2_charles], [V1, V2], marker='o')
    plt.xlabel('Temperature (K)')
    plt.ylabel('Volume (Liters)')
    plt.title("Charles's Law")

    # Pressure Law
    plt.subplot(1, 3, 3)
    plt.plot([P1, P2_pressure], [T1, T1], marker='o')
    plt.xlabel('Pressure (atm)')
    plt.ylabel('Temperature (K)')
    plt.title("Pressure Law")

    # Display plots
    st.pyplot(plt)

if __name__ == "__main__":
    main()