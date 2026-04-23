import streamlit as st
from src.recommender import SwiggyRecommender

st.set_page_config(
    page_title="Swiggy Restaurant Recommendation System",
    page_icon="🍽️",
    layout="wide"
)

@st.cache_resource
def load_recommender():
    return SwiggyRecommender()

recommender = load_recommender()

st.title("🍽️ Swiggy’s Restaurant Recommendation System")
st.markdown("Find restaurants based on your preferences or discover similar restaurants.")

tab1, tab2 = st.tabs(["Recommend by Preferences", "Find Similar Restaurants"])

with tab1:
    st.subheader("Preference-Based Recommendation")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        city = st.selectbox("Select City", recommender.get_cities())

    with col2:
        cuisine = st.selectbox("Select Cuisine", recommender.get_all_cuisines())

    with col3:
        min_rating = st.slider("Minimum Rating", min_value=0.0, max_value=5.0, value=3.5, step=0.1)

    with col4:
        max_cost = st.slider("Maximum Cost", min_value=50, max_value=2000, value=500, step=50)

    top_n = st.slider("Number of Recommendations", min_value=5, max_value=20, value=10, step=1)

    if st.button("Get Recommendations"):
        results = recommender.recommend_by_preferences(
            city=city,
            cuisine=cuisine,
            min_rating=min_rating,
            max_cost=max_cost,
            top_n=top_n
        )

        if results.empty:
            st.warning("No restaurants found for the selected criteria.")
        else:
            st.success(f"Found {len(results)} recommended restaurants.")
            display_cols = ['name', 'city', 'rating', 'rating_count', 'cost', 'cuisine', 'address', 'link']
            st.dataframe(results[display_cols], use_container_width=True)

with tab2:
    st.subheader("Restaurant-to-Restaurant Similarity")

    restaurant_name = st.selectbox(
        "Select a Restaurant",
        recommender.get_restaurant_names()
    )

    top_n_similar = st.slider("Number of Similar Restaurants", min_value=3, max_value=15, value=5, step=1)

    if st.button("Find Similar Restaurants"):
        results = recommender.recommend_by_restaurant(restaurant_name, top_n=top_n_similar)

        if results.empty:
            st.warning("No similar restaurants found.")
        else:
            st.success(f"Found {len(results)} similar restaurants.")
            display_cols = ['name', 'city', 'rating', 'rating_count', 'cost', 'cuisine', 'address', 'link', 'similarity_score']
            st.dataframe(results[display_cols], use_container_width=True)

st.markdown("---")
st.caption("Built with Python, Scikit-learn, and Streamlit")
