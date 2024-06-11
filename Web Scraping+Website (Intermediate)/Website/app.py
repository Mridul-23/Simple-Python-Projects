import streamlit as st
import pandas as pd

def details(book_name, books_df):
    book_details = books_df[books_df['title'] == book_name]
    
    if book_details.empty:
        print(f"Book '{book_name}' not found.")
        return None
    
    book_details = book_details.iloc[0]

    book_title = book_details['title']
    price = book_details['price']
    genre = book_details['category']
    stars = book_details['stars']
    availability = book_details['availability']

    return  book_title, price, genre, stars, availability
        
def star(stars):
    counter = 0
    for i in range(stars):
        counter += 1
    return "★"*counter

background_image_path = r"C:\Users\HP\Desktop\Placement Projects\Simple Python Projects\Web Scraping (Advanced)\Website\5172658.jpg"



page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1512386923336-1440f4afe1d9");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


df = pd.read_json(r"C:\Users\HP\Desktop\Placement Projects\Simple Python Projects\Web Scraping (Advanced)\bookscraper\bookdata.json")

df_list = df['title']
st.header("Books Database")
selector = st.selectbox(
    "Enter/Choose from the name of book here...", 
    df_list
)

if st.button('Show Details'):
    book_title, price, genre, stars, availability  = details(selector, df)
    with st.chat_message("assistant"):
        st.markdown(" :grey[Hey there! Here are the details]")

        st.write(f'Title of the Book: {book_title}')
        st.write(f"Price of the Book: €{price}")
        st.write(f'Gneres: {genre}')
        st.write(f'Reviews in stars: {star(stars)}')
        st.write(f'Availability: {availability}')
        

import os

def run_streamlit_app():
    os.system("streamlit run app.py")

if __name__ == "__main__":
    # Check if the Streamlit server is already running
    if "streamlit" not in os.popen("tasklist").read():
        run_streamlit_app()
    else:
        print("Streamlit app is already running.")
