import streamlit as st
import statement,cal,laws,graph

def main():
    st.title("Physics App")
    st.write("Welcome to the Physics App! This app provides various tools and simulations for learning physics concepts.")

    st.header("Ideal gas And Real gas")
    selected_topic = st.selectbox("Choose a topic", ["statement", "cal", "laws", "graph"])

    if selected_topic == "statement":
        statement.main()
    elif selected_topic == "cal":
        cal.main()
    elif selected_topic == "laws":
        laws.main()
    elif selected_topic == "graph":
         graph.main()



if __name__ == "__main__":
    main()
