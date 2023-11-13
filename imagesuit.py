import streamlit as st
from PIL import Image

st.title('Image Processing Suite')

if 'Grayscale' not in st.session_state:
    st.session_state.Grayscale = False

uploaded_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
col1, col2 = st.columns(2)

with col1:
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption='Uploaded Image', use_column_width=True)
        st.sidebar.subheader('Image Manipulation Options')
        if st.sidebar.button("Convert to GrayScale"):
            st.session_state.Grayscale = True
            img = img.convert("L")
            st.image(img, caption='Grayscale Image')

with col2:
    download_button = st.sidebar.button('Download Edited Image')

    if download_button:
        if st.session_state.Grayscale:
            img = Image.open(uploaded_file)  # Re-open the uploaded image
            grayscale_img = img.convert("L")
            grayscale_img.save('grayscale_image.jpg')
            st.success('Grayscale Image Downloaded Successfully!')
        else:
            st.warning('Please apply a modification before downloading.')
