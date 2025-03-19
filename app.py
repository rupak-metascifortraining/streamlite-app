import streamlit as st
from PIL import Image

# Set the title of the app
st.title('Streamlit App with Button, Slider, and Image')

# Add a slider
slider_value = st.slider('Select a value', 0, 100, 50)

# Display the selected value from the slider
st.write(f'Slider Value: {slider_value}')

# Add a button that shows an image when clicked
if st.button('Show Image'):
    # Load an image using PIL
    img = Image.open(r"C:\Users\91984\Downloads\python_streamline.jpg")  # Use raw string here
    
    # Display the image
    st.image(img, caption='Python Image - Rupak Charan', use_column_width=True)
