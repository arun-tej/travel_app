import streamlit as st

# Embedding CSS directly into the Streamlit app
st.markdown(
    """
    <style>
    /* General Body Styles */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f4f8;
        color: #333;
        margin: 0;
        padding: 0;
    }

    /* Header Styles */
    header {
        background-color: #4CAF50;
        color: white;
        padding: 15px 20px;
        text-align: center;
        font-size: 2em;
    }

    /* Container for Main Content */
    .container {
        width: 80%;
        margin: 20px auto;
        padding: 20px;
        background-color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
    }

    /* Button Styles */
    button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 1em;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #45a049;
    }

    /* Form Inputs */
    input, select {
        width: 100%;
        padding: 12px 20px;
        margin: 10px 0;
        border: 1px solid #ddd;
        border-radius: 5px;
        box-sizing: border-box;
    }

    /* Card for Destinations */
    .card {
        background-color: #fff;
        border-radius: 8px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }

    .card:hover {
        transform: scale(1.05);
    }

    /* Footer Styles */
    footer {
        background-color: #333;
        color: white;
        padding: 10px 0;
        text-align: center;
        position: fixed;
        bottom: 0;
        width: 100%;
    }

    /* Responsive Design for Mobile */
    @media (max-width: 768px) {
        body {
            font-size: 14px;
        }
        .container {
            width: 90%;
        }
        header {
            font-size: 1.5em;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)
