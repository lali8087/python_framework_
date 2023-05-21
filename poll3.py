import streamlit as st

# Define the options for the poll
brands = ["PocoC3", "Poco X5", "Poco X4", "Poco F3"]
quality_options = [" poor", "2", "3", "4", "5 (excellent)"]
price_options = ["1 (expensive)", "2", "3", "4", "5 (affordable)"]
features_options = ["Easy to use", "Feature 2", "Feature 3", "Feature 4", "Feature 5"]
recommend_options = ["Definitely not", "Probably not", "Undecided", "Probably yes", "Definitely yes"]


# Define the function to create the poll
def create_poll():
 
    # Show the options for the poll
    brand = st.selectbox("Brand", brands)
    quality = st.selectbox("How would you rate the quality of the product?", quality_options)
    price = st.selectbox("How would you rate the price of the product?", price_options)
    features = st.multiselect("Which features did you find useful in the product?", features_options)
    recommend = st.selectbox("Would you recommend this product to others?", recommend_options)
    

    # Add a button to submit the poll
    if st.button("Submit Survey"):
        # Save the poll results
        st.session_state.poll_results = {
            "Brand": brand,
            "Quality": quality,
            "Price": price,
            "Features": features,
            "Recommend": recommend,
           
        }

# Define the function to show the poll results
def show_results():
    # Show the poll results
    st.header("Poll Results")
    st.write("Brand:", st.session_state.poll_results["Brand"])
    st.write("Quality:", st.session_state.poll_results["Quality"])
    st.write("Price:", st.session_state.poll_results["Price"])
    st.write("Features:", ", ".join(st.session_state.poll_results["Features"]))
    st.write("Recommend:", st.session_state.poll_results["Recommend"])
    

# Define the app layout

st.title("Survey")


# Show the poll screen
create_poll()

# Check if the poll has been submitted
if "poll_results" in st.session_state:
    # Show the results screen
    st.markdown("---")
    
    st.markdown("---")
    show_results()