# importing libraries
import pandas as pd
import mysql.connector
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.express as px
import time

# kerala bus
lists_k=[]
df_k=pd.read_csv("C:/RedBus Project/Routes/df_k.csv")
for i,r in df_k.iterrows():
    lists_k.append(r["Route_name"])

#Andhra bus
lists_A=[]
df_A=pd.read_csv("C:/RedBus Project/Routes/df_k.csv")
for i,r in df_A.iterrows():
    lists_A.append(r["Route_name"])

#Telungana bus
lists_T=[]
df_T=pd.read_csv("C:/RedBus Project/Routes/df_T.csv")
for i,r in df_T.iterrows():
    lists_T.append(r["Route_name"])

#Goa bus
lists_g=[]
df_G=pd.read_csv("C:/RedBus Project/Routes/df_G.csv")
for i,r in df_G.iterrows():
    lists_g.append(r["Route_name"])

#Rajastan bus
lists_R=[]
df_R=pd.read_csv("C:/RedBus Project/Routes/df_R.csv")
for i,r in df_R.iterrows():
    lists_R.append(r["Route_name"])


# South bengal bus 
lists_SB=[]
df_SB=pd.read_csv("C:/RedBus Project/Routes/df_R.csv")
for i,r in df_SB.iterrows():
    lists_SB.append(r["Route_name"])

# Haryana bus
lists_H=[]
df_H=pd.read_csv("C:/RedBus Project/Routes/df_H.csv")
for i,r in df_H.iterrows():
    lists_H.append(r["Route_name"])

#Assam bus
lists_AS=[]
df_AS=pd.read_csv("C:/RedBus Project/Routes/df_AS.csv")
for i,r in df_AS.iterrows():
    lists_AS.append(r["Route_name"])

#UP bus
lists_UP=[]
df_UP=pd.read_csv("C:/RedBus Project/Routes/df_UP.csv")
for i,r in df_UP.iterrows():
    lists_UP.append(r["Route_name"])

#West bengal bus
lists_WB=[]
df_WB=pd.read_csv("C:/RedBus Project/Routes/df_WB.csv")
for i,r in df_WB.iterrows():
    lists_WB.append(r["Route_name"])

#setting up streamlit page
slt.set_page_config(page_title="Redbus Data Scraping", page_icon="🚌", layout="wide")

# Option menu for navigation
web = option_menu(menu_title="🚌OnlineBus",
                  options=["Home", "📍States and Routes"],
                  icons=["house", "info-circle"],
                  orientation="horizontal"
                 ) 

if web == "Home":
    slt.image("D:/slit/t.png", width=150)
    

    # Display Logo Image with Center Alignment

    # Title and Subtitle
    slt.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit</h1>", unsafe_allow_html=True)
    slt.markdown("<h3 style='text-align: center; color: #1f77b4;'>Domain: Transportation</h3>", unsafe_allow_html=True)

    # Objective Section with Icons
    slt.subheader("🌟 **Objective**")
    slt.markdown("""
        The **Redbus Data Scraping and Filtering with Streamlit Application** aims to revolutionize the transportation industry by providing a 
        comprehensive solution for **collecting, analyzing, and visualizing bus travel data**. Using **Selenium** for automated web scraping, 
        the project extracts detailed information from Redbus, including:
        
        - **Bus Routes**
        - **Schedules**
        - **Prices**
        - **Seat Availability**

        This streamlined solution enhances **operational efficiency** and **strategic planning** in the transportation sector.
    """)

    # Overview Section with Bullet Points
    slt.subheader("📊 **Overview**")
    slt.markdown("""
    - **Selenium**: A powerful browser automation tool for web scraping, simulating user interactions like clicking, form filling, and page navigation.
    - **Pandas**: Transforms raw data into structured dataframes for **manipulation, cleaning, and preprocessing**.
    - **MySQL**: Integrates seamlessly with Python to store and retrieve large datasets efficiently using **SQL queries**.
    - **Streamlit**: Builds an interactive web interface for real-time **data visualization and filtering**, offering an intuitive user experience.
    """)

    # Skills Section with Badges
    slt.subheader("💡 **Skills Acquired**")
    slt.markdown("""
    <div style="display: flex; gap: 10px;">
        <div style="background-color: #4CAF50; color: white; padding: 5px 10px; border-radius: 5px;">Selenium</div>
        <div style="background-color: #2196F3; color: white; padding: 5px 10px; border-radius: 5px;">Python</div>
        <div style="background-color: #FFC107; color: black; padding: 5px 10px; border-radius: 5px;">Pandas</div>
        <div style="background-color: #f44336; color: white; padding: 5px 10px; border-radius: 5px;">MySQL</div>
        <div style="background-color: #ff5722; color: white; padding: 5px 10px; border-radius: 5px;">Streamlit</div>
    </div>
    """, unsafe_allow_html=True)

    # Developed By Section
    slt.subheader("👨‍💻 **Developed by:**")
    slt.markdown("<h4 style='color: #2E8B57;'>Pranesh D     </h4>", unsafe_allow_html=True)

    # Footer
    slt.markdown(
        """
        <hr style="border: 1px solid #ddd;">
        <footer style="text-align: center; color: gray;">
            🚀 Powered by <b>Python, Selenium, and Streamlit</b> | © 2024 Sridhar M
        </footer>
        """,
        unsafe_allow_html=True
    )


   # States and Routes page setting
if web == "📍States and Routes":
    slt.markdown("""
        <style>
            .custom-title {
                background-color: #ff6f61;
                color: white;
                padding: 10px;
                border-radius: 8px;
                text-align: center;
                font-size: 24px;
                font-weight: bold;
            }
            .custom-container {
                background-color: #f2f2f2;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .select-style {
                font-size: 16px;
                color: #333;
            }
        </style>
    """, unsafe_allow_html=True)

    slt.markdown('<div class="custom-title">🚌 Explore States & Routes</div>', unsafe_allow_html=True)
    slt.markdown('<div class="custom-container">', unsafe_allow_html=True)

    # State Selector
    S = slt.selectbox(
        "🚩 **Lists of States**",
        ["Kerala", "Adhra Pradesh", "Telugana", "Goa", "Rajastan", 
         "South Bengal", "Haryana", "Assam", "Uttar Pradesh", "West Bengal"],
        help="Select a state to view available bus routes."
    )

    # Two Columns for Bus Type & Fare
    col1, col2 = slt.columns(2)
    with col1:
        select_type = slt.radio(
            "🚌 **Choose Bus Type**", 
            ("Sleeper", "Semi-Sleeper", "Others"),
            help="Filter buses by type."
        )
    with col2:
        select_fare = slt.radio(
            "💰 **Choose Fare Range**", 
            ("50-1000", "1000-2000", "2000 and above"),
            help="Filter buses by fare range."
        )

    # Time Selector
    TIME = slt.time_input("⏰ **Select Departure Time**", help="Select the preferred departure time.")
    slt.markdown("</div>", unsafe_allow_html=True)


        # Kerala bus fare filtering
    if S == "Kerala":
        K = slt.selectbox("List of routes",lists_k)

        def type_and_fare(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Jackie@2018", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  # assuming a high max value for "2000 and above"

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{K}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare(select_type, select_fare)
        slt.dataframe(df_result)

         # Adhra Pradesh bus fare filtering
    if S=="Adhra Pradesh":
        A=slt.selectbox("list of routes",lists_A)

        def type_and_fare_A(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Jackie@2018", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{A}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_A(select_type, select_fare)
        slt.dataframe(df_result)
          

    # Telugana bus fare filtering
    if S=="Telugana":
        T=slt.selectbox("list of routes",lists_T)

        def type_and_fare_T(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Jackie@2018", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{T}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_T(select_type, select_fare)
        slt.dataframe(df_result)

if S == "Goa":
    Goa = slt.selectbox("List of routes", lists_Goa)

    def type_and_fare_Goa(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="Jackie@2018", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper%'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_routes
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{Goa}"
            AND {bus_type_condition} AND Start_time >= '{TIME}'
            ORDER BY Price and Start_time DESC
        '''
        my_cursor.execute(query)
        out = my_cursor.fetchall()
        conn.close()

        df = pd.DataFrame(out, columns=[
            "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
            "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
        ])
        return df

    df_result = type_and_fare_Goa(select_type, select_fare)
    slt.dataframe(df_result)

    # Rajastan bus fare filtering
    if S=="Rajastan":
        R=slt.selectbox("list of routes",lists_R)

        def type_and_fare_R(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Jackie@2018", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{R}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_R(select_type, select_fare)
        slt.dataframe(df_result)
          

    # South Bengal bus fare filtering       
    if S=="South Bengal":
        SB=slt.selectbox("list of rotes",lists_SB)

        def type_and_fare_SB(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Jackie@2018", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{SB}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_SB(select_type, select_fare)
        slt.dataframe(df_result)
    
    # Haryana bus fare filtering
    if S=="Haryana":
        H=slt.selectbox("list of rotes",lists_H)

        def type_and_fare_H(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Jackie@2018", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{H}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_H(select_type, select_fare)
        slt.dataframe(df_result)


    # Assam bus fare filtering
    if S=="Assam":
        AS=slt.selectbox("list of rotes",lists_AS)

        def type_and_fare_AS(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Jackie@2018", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{AS}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_AS(select_type, select_fare)
        slt.dataframe(df_result)

    # Uttar Pradesh bus fare filtering
if S == "Uttar Pradesh":
    UP = slt.selectbox("List of routes", lists_UP)

    def type_and_fare_UP(bus_type, fare_range):
        conn = mysql.connector.connect(host="localhost", user="root", password="Jackie@2018", database="RED_BUS_DETAILS")
        my_cursor = conn.cursor()
        # Define fare range based on selection
        if fare_range == "50-1000":
            fare_min, fare_max = 50, 1000
        elif fare_range == "1000-2000":
            fare_min, fare_max = 1000, 2000
        else:
            fare_min, fare_max = 2000, 100000

        # Define bus type condition
        if bus_type == "sleeper":
            bus_type_condition = "Bus_type LIKE '%Sleeper%'"
        elif bus_type == "semi-sleeper":
            bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper%'"
        else:
            bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

        query = f'''
            SELECT * FROM bus_routes
            WHERE Price BETWEEN {fare_min} AND {fare_max}
            AND Route_name = "{UP}"
            AND {bus_type_condition} AND Start_time >= '{TIME}'
            ORDER BY Price and Start_time DESC
        '''
        my_cursor.execute(query)
        out = my_cursor.fetchall()
        conn.close()

        df = pd.DataFrame(out, columns=[
            "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
            "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
        ])
        return df

    df_result = type_and_fare_UP(select_type, select_fare)
    slt.dataframe(df_result)

    # West Bengal bus fare filtering
    if S=="West Bengal":
        WB=slt.selectbox("list of rotes",lists_WB)

        def type_and_fare_WB(bus_type, fare_range):
            conn = mysql.connector.connect(host="localhost", user="root", password="Jackie@2018", database="RED_BUS_DETAILS")
            my_cursor = conn.cursor()
            # Define fare range based on selection
            if fare_range == "50-1000":
                fare_min, fare_max = 50, 1000
            elif fare_range == "1000-2000":
                fare_min, fare_max = 1000, 2000
            else:
                fare_min, fare_max = 2000, 100000  

            # Define bus type condition
            if bus_type == "sleeper":
                bus_type_condition = "Bus_type LIKE '%Sleeper%'"
            elif bus_type == "semi-sleeper":
                bus_type_condition = "Bus_type LIKE '%A/c Semi Sleeper %'"
            else:
                bus_type_condition = "Bus_type NOT LIKE '%Sleeper%' AND Bus_type NOT LIKE '%Semi-Sleeper%'"

            query = f'''
                SELECT * FROM bus_routes 
                WHERE Price BETWEEN {fare_min} AND {fare_max}
                AND Route_name = "{WB}"
                AND {bus_type_condition} AND Start_time>='{TIME}'
                ORDER BY Price and Start_time  DESC
            '''
            my_cursor.execute(query)
            out = my_cursor.fetchall()
            conn.close()

            df = pd.DataFrame(out, columns=[
                "ID", "Bus_name", "Bus_type", "Start_time", "End_time", "Total_duration",
                "Price", "Seats_Available", "Ratings", "Route_link", "Route_name"
            ])
            return df

        df_result = type_and_fare_WB(select_type, select_fare)
        slt.dataframe(df_result)


