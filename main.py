import tensorflow as tf
import streamlit as st
import cv2
from PIL import Image, ImageOps
import numpy as np


@st.cache_resource()
def load_model():
    model = tf.keras.models.load_model('densenet.h5')
    return model


with st.spinner('Model is being loaded..'):
    model = load_model()

st.header("""Medi-Flow""")
st.header("Your place to find the medicinal flowers")

file = st.file_uploader("Please upload the images", type=["jpg", "png"])

st.set_option('deprecation.showfileUploaderEncoding', False)


def import_and_predict(image_data, model):
    size = (224, 224)
    # img = cv2.resize(img, (224, 224))
    # img = np.reshape(img, [1, 224, 224, 3])
    # img = img / 255

    image = ImageOps.fit(image_data, size)
    image = np.asarray(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.reshape(img, [1, 224, 224, 3])
    img = img / 255

    prediction = model.predict(img)

    return prediction


def web_writer(ans):
    format_of_data = ".txt"
    file_name = ans + format_of_data
    with open(file_name, 'r') as f:
        vari = f.read()
    temp_text = vari
    st.markdown(temp_text)


if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    score = tf.nn.softmax(predictions[0])
    print(predictions)
    print(score)
    class_names = {0: 'ashwagandha',
                   1: 'cardamom',
                   2: 'madagascar', }
    st.write(
        "This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)],
                                                                                        100 * np.max(score))
    )
    web_writer(class_names[np.argmax(score)])
