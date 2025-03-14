# Setup Environmental - Terminal
cd dashboard
pip freeze > requirements.txt
pip install -r requirements.txt

# Run Streamlit App 
streamlit run dashboard.py
