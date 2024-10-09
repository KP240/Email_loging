import streamlit as st
from PIL import Image
from io import BytesIO
from datetime import datetime
import pandas as pd

# List to store email opens (in a real scenario, you might use a database)
if "open_logs" not in st.session_state:
    st.session_state["open_logs"] = []

# Log and display query parameters for debugging
query_params = st.query_params
st.write("Query Parameters:", query_params)

# Get the recipient's email from the URL query params
recipient = query_params.get('recipient', [''])[0]

# Log the open event with the timestamp if recipient is valid
if recipient:
    st.session_state["open_logs"].append({
        "email": recipient,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# Create a 1x1 transparent image (transparent pixel)
img = Image.new('RGBA', (1, 1), (255, 255, 255, 0))
buf = BytesIO()
img.save(buf, format="PNG")
buf.seek(0)

# Serve the transparent pixel as the response
st.image(buf, use_column_width=False)

# Display logged opens (optional, for debugging)
st.write("Email Open Logs:")
st.write(pd.DataFrame(st.session_state["open_logs"]))
