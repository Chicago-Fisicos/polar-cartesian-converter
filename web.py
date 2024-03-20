import streamlit as st
from conversor import polar_a_cartesiana, cartesiana_a_polar

def main():
    
    st.set_page_config(
        page_title="Fisica 1",
       # page_icon="images/nekark-icon.png",
    )
    
    hide_streamlit_style = """
        <style>
        MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    
    st.title("Conversor de Coordenadass")
    conversion = st.selectbox("Selecciona la conversión", 
                            ("Polar a Cartesiana", 
                            "Cartesiana a Polar"))

    if conversion == "Polar a Cartesiana":
        r = st.number_input("Radio (r)", value=0.0)
        theta = st.number_input("Ángulo (θ)", value=0.0)
        x, y = polar_a_cartesiana(r, theta)
        st.write("(X, Y) = ", (x, y))

    elif conversion == "Cartesiana a Polar":
        x = st.number_input("Coordenada X", value=0.0)
        y = st.number_input("Coordenada Y", value=0.0)
        r, theta = cartesiana_a_polar(x, y)
        st.write("(r, theta) = ", (r, theta))

if __name__ == "__main__":
    main()
