import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random  # For demo data, remove in production

def show():
    st.title("Cultivation Management 🌱")
    
    # Create tabs for different cultivation management sections
    tab1, tab2, tab3 = st.tabs(["My Plants", "Add New Plant", "Irrigation Control"])
    
    with tab1:
        show_plants()
    
    with tab2:
        add_new_plant()
    
    with tab3:
        irrigation_control()

def show_plants():
    st.subheader("My Melon Plants")
    
    # In a real app, this would come from the database
    plants = [
        {
            "id": 1,
            "name": "Plant #1",
            "variety": "Honeydew",
            "planting_date": "2023-05-15",
            "age": "32 days",
            "media": "Cocopeat",
            "irrigation": "Drip Fertigation",
            "health": "Good",
            "stage": "Fruiting"
        },
        {
            "id": 2,
            "name": "Plant #2",
            "variety": "Cantaloupe",
            "planting_date": "2023-05-20",
            "age": "27 days",
            "media": "Rockwool",
            "irrigation": "Drip Fertigation",
            "health": "Excellent",
            "stage": "Flowering"
        },
        {
            "id": 3,
            "name": "Plant #3",
            "variety": "Galia",
            "planting_date": "2023-05-25",
            "age": "22 days",
            "media": "Perlite",
            "irrigation": "Deep Water Culture",
            "health": "Fair",
            "stage": "Vegetative"
        }
    ]
    
    # Convert to DataFrame for display
    df_plants = pd.DataFrame(plants)
    
    # Display plants with expanders for details
    for i, plant in enumerate(plants):
        with st.expander(f"{plant['name']} - {plant['variety']} ({plant['stage']})"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Variety:** {plant['variety']}")
                st.write(f"**Planted:** {plant['planting_date']}")
                st.write(f"**Age:** {plant['age']}")
                st.write(f"**Health Status:** {plant['health']}")
            
            with col2:
                st.write(f"**Growing Media:** {plant['media']}")
                st.write(f"**Irrigation System:** {plant['irrigation']}")
                st.write(f"**Growth Stage:** {plant['stage']}")
                
                # Action buttons
                col_btn1, col_btn2, col_btn3 = st.columns(3)
                with col_btn1:
                    st.button("Update", key=f"update_{i}")
                with col_btn2:
                    st.button("Analyze", key=f"analyze_{i}")
                with col_btn3:
                    st.button("Harvest", key=f"harvest_{i}")
            
            # Growth chart
            dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(int(plant['age'].split()[0]), 0, -1)]
            heights = [random.uniform(5, 50) for _ in range(len(dates))]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=dates, y=heights, mode='lines+markers', name='Plant Height (cm)'))
            
            fig.update_layout(
                title=f"Growth Progress - {plant['name']}",
                xaxis_title="Date",
                yaxis_title="Height (cm)"
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Recent notes
            st.write("**Recent Notes:**")
            notes = [
                {"date": "2023-06-14", "note": "Pruned side shoots to encourage vertical growth."},
                {"date": "2023-06-10", "note": "Applied foliar spray for micronutrients."},
                {"date": "2023-06-05", "note": "First flowers appeared."}
            ]
            
            for note in notes:
                st.write(f"- {note['date']}: {note['note']}")
            
            # Add new note
            new_note = st.text_area("Add Note", key=f"note_{i}")
            if st.button("Save Note", key=f"save_note_{i}"):
                st.success("Note saved successfully!")

def add_new_plant():
    st.subheader("Add New Melon Plant")
    
    # Form for adding a new plant
    with st.form("new_plant_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            plant_name = st.text_input("Plant Name", "Plant #4")
            variety = st.selectbox(
                "Melon Variety",
                ["Honeydew", "Cantaloupe", "Galia", "Charentais", "Crenshaw", "Other"]
            )
            if variety == "Other":
                custom_variety = st.text_input("Custom Variety Name")
            
            planting_date = st.date_input("Planting Date", datetime.now())
        
        with col2:
            media = st.selectbox(
                "Growing Media",
                ["Cocopeat", "Rockwool", "Perlite", "Vermiculite", "Hydroton", "Other"]
            )
            if media == "Other":
                custom_media = st.text_input("Custom Media Type")
            
            irrigation = st.selectbox(
                "Irrigation System",
                ["Drip Fertigation", "Ebb and Flow", "Deep Water Culture", "NFT", "Aeroponics", "Other"]
            )
            if irrigation == "Other":
                custom_irrigation = st.text_input("Custom Irrigation Type")
            
            initial_height = st.number_input("Initial Height (cm)", min_value=0.0, value=5.0, step=0.5)
        
        notes = st.text_area("Initial Notes")
        
        # Submit button
        submitted = st.form_submit_button("Add Plant")
        if submitted:
            st.success(f"Plant '{plant_name}' added successfully!")
            st.balloons()

def irrigation_control():
    st.subheader("Irrigation Control System")
    
    # System selection
    system = st.selectbox(
        "Select Irrigation System",
        ["All Systems", "System #1 (Drip Fertigation)", "System #2 (Deep Water Culture)", "System #3 (NFT)"]
    )
    
    # Current status
    st.write("#### Current Status")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Water Temperature", value="24.5 °C", delta="0.3 °C")
    
    with col2:
        st.metric(label="EC Level", value="2.1 mS/cm", delta="-0.1 mS/cm")
    
    with col3:
        st.metric(label="pH Level", value="5.8", delta="0.0")
    
    # Irrigation schedule
    st.write("#### Irrigation Schedule")
    
    schedules = [
        {"system": "System #1", "start_time": "06:00", "duration": "15 min", "frequency": "Every 3 hours", "nutrient_mix": "Vegetative Growth"},
        {"system": "System #1", "start_time": "09:00", "duration": "15 min", "frequency": "Every 3 hours", "nutrient_mix": "Vegetative Growth"},
        {"system": "System #1", "start_time": "12:00", "duration": "15 min", "frequency": "Every 3 hours", "nutrient_mix": "Vegetative Growth"},
        {"system": "System #1", "start_time": "15:00", "duration": "15 min", "frequency": "Every 3 hours", "nutrient_mix": "Vegetative Growth"},
        {"system": "System #1", "start_time": "18:00", "duration": "15 min", "frequency": "Every 3 hours", "nutrient_mix": "Vegetative Growth"},
        {"system": "System #2", "start_time": "Continuous", "duration": "24 hours", "frequency": "Daily", "nutrient_mix": "Fruiting Formula"},
        {"system": "System #3", "start_time": "Continuous", "duration": "24 hours", "frequency": "Daily", "nutrient_mix": "Flowering Formula"}
    ]
    
    # Filter schedules based on selected system
    if system != "All Systems":
        system_name = system.split(" ")[0] + " " + system.split(" ")[1]
        schedules = [schedule for schedule in schedules if schedule["system"] == system_name]
    
    # Display schedules
    df_schedules = pd.DataFrame(schedules)
    st.dataframe(df_schedules)
    
    # Add new schedule
    st.write("#### Add New Schedule")
    
    with st.form("new_schedule_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            schedule_system = st.selectbox(
                "System",
                ["System #1", "System #2", "System #3"]
            )
            
            start_time = st.time_input("Start Time", datetime.strptime("06:00", "%H:%M").time())
            duration = st.selectbox(
                "Duration",
                ["5 min", "10 min", "15 min", "20 min", "30 min", "1 hour", "Continuous"]
            )
        
        with col2:
            frequency = st.selectbox(
                "Frequency",
                ["Every hour", "Every 2 hours", "Every 3 hours", "Every 4 hours", "Every 6 hours", "Daily"]
            )
            
            nutrient_mix = st.selectbox(
                "Nutrient Mix",
                ["Vegetative Growth", "Flowering Formula", "Fruiting Formula", "Custom Mix"]
            )
            
            if nutrient_mix == "Custom Mix":
                custom_mix = st.text_input("Custom Mix Name")
        
        # Submit button
        submitted = st.form_submit_button("Add Schedule")
        if submitted:
            st.success("Irrigation schedule added successfully!")
    
    # Manual control
    st.write("#### Manual Control")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**System Control**")
        system_control = st.selectbox(
            "Select System to Control",
            ["System #1", "System #2", "System #3"]
        )
        
        st.write("System Status:")
        status = st.radio(
            "Power",
            ["On", "Off"],
            horizontal=True
        )
        
        if st.button("Apply System Status"):
            st.success(f"{system_control} turned {status.lower()}")
    
    with col2:
        st.write("**Nutrient Dosing**")
        
        ec_target = st.slider("Target EC (mS/cm)", 1.0, 3.0, 2.1, 0.1)
        ph_target = st.slider("Target pH", 5.0, 7.0, 5.8, 0.1)
        
        if st.button("Apply Nutrient Settings"):
            st.success(f"Nutrient settings updated: EC={ec_target} mS/cm, pH={ph_target}")