import streamlit as st
def ideal_gas_description():
    """
    Provides a description of an ideal gas.
    """
    description = """
    An ideal gas is a theoretical gas composed of randomly moving point particles that do not interact 
    except through perfectly elastic collisions. The particles of an ideal gas have negligible volume 
    and do not exert intermolecular forces on each other. In an ideal gas, the pressure, volume, and 
    temperature are related by the ideal gas law, which is expressed as: PV = nRT, where P is the 
    pressure, V is the volume, n is the number of moles, R is the ideal gas constant, and T is the 
    temperature. Ideal gases follow Boyle's law, Charles's law, and Avogadro's law exactly under all 
    conditions of temperature and pressure.
    """
    return description
def real_gas_description():
    """
    Provides a description of a real gas.
    """
    description = """
    A real gas is a gas that does not behave according to the assumptions of the ideal gas law. Unlike 
    ideal gases, real gases have volume and exhibit intermolecular forces. Real gases deviate from 
    ideal behavior at high pressures and low temperatures. To account for the deviations of real gases 
    from ideal behavior, various modifications to the ideal gas law have been proposed. One such 
    modification is the Van der Waals equation, which introduces corrections for the volume of the gas 
    molecules and the attractive forces between them. Real gases also exhibit behavior such as 
    condensation and liquefaction under certain conditions.
    """
    return description
def main():
    st.title("Gas Descriptions")

    st.header("Ideal Gas Description:")
    st.write(ideal_gas_description())

    st.header("Real Gas Description:")
    st.write(real_gas_description())
if __name__ == "__main__":
    main()



