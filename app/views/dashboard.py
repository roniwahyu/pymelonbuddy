import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random  # For demo data, remove in production

def show():
    st.title("Melon Buddy Dashboard 🍈")
    
    # Create tabs for different dashboard sections
    tab1, tab2, tab3 = st.tabs(["Overview", "Plant Health", "Analytics"])
    
    with tab1:
        show_overview()
    
    with tab2:
        show_plant_health()
    
    with tab3:
        show_analytics()

def show_overview():
    # Header section with key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Active Plants", value="12", delta="2")
    
    with col2:
        st.metric(label="Avg. Plant Health", value="87%", delta="3%")
    
    with col3:
        st.metric(label="Days to Harvest", value="18", delta="-2")
    
    with col4:
        st.metric(label="Yield Forecast", value="42 kg", delta="5%")
    
    # Recent activities
    st.subheader("Recent Activities")
    
    # In a real app, this would come from the database
    activities = [
        {"date": "2023-06-15", "activity": "Added 3 new melon plants (Variety: Honeydew)", "type": "Plant"},
        {"date": "2023-06-14", "activity": "Adjusted nutrient solution EC to 2.1", "type": "Nutrient"},
        {"date": "2023-06-13", "activity": "Detected minor magnesium deficiency in Plant #5", "type": "Health"},
        {"date": "2023-06-12", "activity": "Updated irrigation schedule to 4x daily", "type": "Irrigation"},
        {"date": "2023-06-10", "activity": "Harvested 3.2kg from Plant #2", "type": "Harvest"}
    ]
    
    # Convert to DataFrame for display
    df_activities = pd.DataFrame(activities)
    
    # Color-code by activity type
    def highlight_activity(s):
        if s.type == 'Health':
            return ['background-color: #ffcccc'] * len(s)
        elif s.type == 'Harvest':
            return ['background-color: #ccffcc'] * len(s)
        elif s.type == 'Plant':
            return ['background-color: #ccccff'] * len(s)
        else:
            return [''] * len(s)
    
    # Display styled dataframe
    st.dataframe(df_activities[['date', 'activity']].style.apply(highlight_activity, axis=1))
    
    # Weather forecast (placeholder)
    st.subheader("Environment Forecast")
    
    # Generate demo data
    dates = [(datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
    temps = [random.uniform(22, 28) for _ in range(7)]
    humidity = [random.uniform(60, 80) for _ in range(7)]
    
    # Create forecast chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=temps, name="Temperature (°C)"))
    fig.add_trace(go.Scatter(x=dates, y=humidity, name="Humidity (%)", yaxis="y2"))
    
    fig.update_layout(
        title="7-Day Greenhouse Forecast",
        xaxis_title="Date",
        yaxis_title="Temperature (°C)",
        yaxis2=dict(
            title="Humidity (%)",
            overlaying="y",
            side="right"
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)

def show_plant_health():
    st.subheader("Plant Health Overview")
    
    # Plant selection
    plant_options = ["All Plants", "Plant #1 (Honeydew)", "Plant #2 (Cantaloupe)", "Plant #3 (Galia)"]
    selected_plant = st.selectbox("Select Plant", plant_options)
    
    # Date range selection
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
    with col2:
        end_date = st.date_input("End Date", datetime.now())
    
    # Generate demo data for plant health metrics
    dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(30, 0, -1)]
    health_score = [random.uniform(70, 95) for _ in range(30)]
    leaf_count = [int(20 + i/2) for i in range(30)]
    fruit_count = [int(i/5) if i > 10 else 0 for i in range(30)]
    
    # Create health metrics chart
    fig1 = px.line(
        x=dates, 
        y=health_score, 
        title="Plant Health Score Over Time",
        labels={"x": "Date", "y": "Health Score (0-100)"}
    )
    
    st.plotly_chart(fig1, use_container_width=True)
    
    # Create growth metrics chart
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=dates, y=leaf_count, name="Leaf Count"))
    fig2.add_trace(go.Scatter(x=dates, y=fruit_count, name="Fruit Count"))
    
    fig2.update_layout(
        title="Plant Growth Metrics",
        xaxis_title="Date",
        yaxis_title="Count",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Health alerts
    st.subheader("Health Alerts")
    
    # Demo alerts
    alerts = [
        {"date": "2023-06-13", "plant": "Plant #3", "issue": "Possible magnesium deficiency", "severity": "Medium"},
        {"date": "2023-06-10", "plant": "Plant #1", "issue": "Early signs of powdery mildew", "severity": "Low"},
        {"date": "2023-06-05", "plant": "Plant #2", "issue": "Irregular watering detected", "severity": "Low"}
    ]
    
    # Filter alerts for selected plant
    if selected_plant != "All Plants":
        plant_name = selected_plant.split(" ")[0] + " " + selected_plant.split(" ")[1]
        alerts = [alert for alert in alerts if alert["plant"] == plant_name]
    
    if alerts:
        df_alerts = pd.DataFrame(alerts)
        st.dataframe(df_alerts)
    else:
        st.info("No health alerts for the selected plant.")

def show_analytics():
    st.subheader("Growth Analytics")
    
    # Media comparison
    st.write("#### Growing Media Comparison")
    
    # Generate demo data
    media_types = ["Cocopeat", "Rockwool", "Perlite", "Vermiculite", "Hydroton"]
    growth_rate = [8.2, 7.5, 6.8, 7.0, 6.5]
    fruit_yield = [4.2, 3.8, 3.5, 3.6, 3.3]
    
    # Create comparison chart
    fig1 = go.Figure(data=[
        go.Bar(name="Growth Rate (cm/week)", x=media_types, y=growth_rate),
        go.Bar(name="Fruit Yield (kg/plant)", x=media_types, y=fruit_yield)
    ])
    
    fig1.update_layout(
        title="Performance by Growing Media",
        xaxis_title="Media Type",
        yaxis_title="Value",
        barmode="group",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    st.plotly_chart(fig1, use_container_width=True)
    
    # Irrigation comparison
    st.write("#### Irrigation System Comparison")
    
    # Generate demo data
    irrigation_types = ["Drip Fertigation", "Ebb and Flow", "Deep Water Culture", "NFT", "Aeroponics"]
    water_usage = [2.5, 3.8, 4.2, 3.0, 1.8]
    nutrient_efficiency = [85, 75, 90, 80, 95]
    
    # Create dual-axis chart
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=irrigation_types, y=water_usage, name="Water Usage (L/day/plant)"))
    fig2.add_trace(go.Scatter(x=irrigation_types, y=nutrient_efficiency, 
                             mode="markers+lines", name="Nutrient Efficiency (%)", yaxis="y2",
                             marker=dict(size=10)))
    
    fig2.update_layout(
        title="Irrigation System Efficiency",
        xaxis_title="Irrigation Type",
        yaxis_title="Water Usage (L/day/plant)",
        yaxis2=dict(
            title="Nutrient Efficiency (%)",
            overlaying="y",
            side="right",
            range=[0, 100]
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Yield prediction
    st.write("#### Yield Prediction")
    
    # Variety selection for prediction
    variety = st.selectbox(
        "Select Melon Variety",
        ["Honeydew", "Cantaloupe", "Galia", "Charentais", "Crenshaw"]
    )
    
    # Media and irrigation selection
    col1, col2 = st.columns(2)
    with col1:
        media = st.selectbox("Growing Media", media_types)
    with col2:
        irrigation = st.selectbox("Irrigation System", irrigation_types)
    
    # Generate prediction based on selections (in a real app, this would use a trained model)
    base_yield = {
        "Honeydew": 4.0,
        "Cantaloupe": 3.8,
        "Galia": 3.5,
        "Charentais": 3.2,
        "Crenshaw": 4.5
    }
    
    media_factor = {
        "Cocopeat": 1.05,
        "Rockwool": 1.0,
        "Perlite": 0.95,
        "Vermiculite": 0.97,
        "Hydroton": 0.93
    }
    
    irrigation_factor = {
        "Drip Fertigation": 1.0,
        "Ebb and Flow": 0.95,
        "Deep Water Culture": 1.1,
        "NFT": 0.98,
        "Aeroponics": 1.15
    }
    
    # Calculate predicted yield
    predicted_yield = base_yield[variety] * media_factor[media] * irrigation_factor[irrigation]
    
    # Display prediction
    st.metric(
        label=f"Predicted Yield for {variety} Melon",
        value=f"{predicted_yield:.2f} kg/plant",
        delta=f"{((predicted_yield / base_yield[variety]) - 1) * 100:.1f}% vs. average"
    )
    
    # Factors affecting yield
    st.write("#### Factors Affecting Yield")
    
    # Create radar chart for variety characteristics
    characteristics = {
        "Honeydew": [4, 3, 5, 4, 3],
        "Cantaloupe": [3, 4, 4, 5, 3],
        "Galia": [5, 3, 3, 4, 4],
        "Charentais": [4, 5, 3, 3, 4],
        "Crenshaw": [5, 4, 4, 3, 5]
    }
    
    categories = ['Growth Rate', 'Disease Resistance', 'Heat Tolerance', 'Water Efficiency', 'Fruit Size']
    
    fig3 = go.Figure()
    
    fig3.add_trace(go.Scatterpolar(
        r=characteristics[variety],
        theta=categories,
        fill='toself',
        name=variety
    ))
    
    fig3.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )
        ),
        title=f"{variety} Characteristics (1-5 scale)"
    )
    
    st.plotly_chart(fig3, use_container_width=True)