import streamlit as st
import PIL
#st.image("/home/sukuna/Desktop/logo.png", width = 100)

st.title("Medi-Flow Wiki")
st.header("Your place to explore the medicinal flowers")
#st.sidebar.image("/home/sukuna/Desktop/logo.png")
st.sidebar.header("Options")
names_tup = ('Nithyakalyani (Catharanthus roseus)', 'tiger', 'bears')
x = st.sidebar.selectbox('Search your flower:', names_tup)

but = st.sidebar.button("Search")

if but:
    if x == "Nithyakalyani (Catharanthus roseus)":

        st.image("/home/sukuna/Desktop/f1.jpg", caption="Nithyakalyani flower")
        st.write(
            """Nithyakalyani, also known as Catharanthus roseus or periwinkle, is a flowering plant native to Madagascar. It has long been revered for its ornamental beauty, adorning gardens and landscapes with its vibrant blooms. However, Nithyakalyani holds far greater significance in the realm of medicine, harboring potent compounds that have revolutionized cancer treatment."""
        )
        st.header("Introduction")
        st.write(
            """Nithyakalyani, also known as Catharanthus roseus or periwinkle, is a flowering plant native to Madagascar. It has long been revered for its ornamental beauty, adorning gardens and landscapes with its vibrant blooms. However, Nithyakalyani holds far greater significance in the realm of medicine, harboring potent compounds that have revolutionized cancer treatment."""
        )

        # Medicinal Properties section
        st.header("Medicinal Properties")
        st.write(
            """Nithyakalyani's claim to fame lies in its ability to produce two remarkable alkaloids: vincristine and vinblastine. These alkaloids exhibit exceptional antimitotic properties, meaning they can disrupt the cell division process, a crucial step in cancer development. As a result, vincristine and vinblastine have become cornerstones of chemotherapy, effectively treating a wide range of cancers, including leukemia, lymphoma, Hodgkin's disease, and many solid tumors."""
        )

        # Traditional Uses section
        st.header("Traditional Uses")
        st.write(
            """Beyond its modern pharmaceutical applications, Nithyakalyani has a rich history of traditional use in various cultures around the world. In Madagascar, the plant has been employed to treat a variety of ailments, including diabetes, hypertension, and malaria. In other parts of the world, Nithyakalyani has been used to manage menstrual irregularities, alleviate stomach disorders, and promote wound healing."""
        )

        # Active Compounds section
        st.header("Active Compounds")
        st.write(
            """Apart from vincristine and vinblastine, Nithyakalyani contains a plethora of other bioactive compounds, each contributing to its diverse medicinal potential. These compounds include vincosamide, ajmalicine, and catharanthine, which exhibit antihypertensive, antidiabetic, and antioxidant properties, respectively."""
        )

        # Potential Side Effects section
        st.header("Potential Side Effects")
        st.write(
            """While Nithyakalyani offers remarkable therapeutic benefits, it is important to acknowledge its potential side effects. The plant's alkaloids can cause nerve damage, leading to numbness, tingling, and muscle weakness. Additionally, Nithyakalyani may induce hair loss, nausea, and vomiting."""
        )

        # Conclusion section
        st.header("Conclusion")
        st.write(
            """Nithyakalyani stands as a testament to nature's remarkable ability to provide healing remedies. Its unique chemical composition has yielded invaluable drugs that have significantly improved cancer treatment outcomes. As research continues to unravel the plant's full potential, Nithyakalyani promises to continue its legacy of alleviating suffering and promoting well-being."""
        )
    if x == "tiger":
        st.write("You chose tiger")
    if x == "bears":
        st.write("You chose bears")


