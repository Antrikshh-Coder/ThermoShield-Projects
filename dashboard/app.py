import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="ThermoShield Analytics",
    layout="wide",
    page_icon="🏭"
)

# -------------------------------------------------
# ADVANCED UI DESIGN
# -------------------------------------------------

st.markdown("""
<style>

body{
background: linear-gradient(135deg,#eef2f3,#8e9eab);
}

/* TITLE */

.main-title{
font-size:48px;
font-weight:900;
background: linear-gradient(90deg,#ff512f,#dd2476,#00c9ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
animation: glow 3s infinite alternate;
}

@keyframes glow{
from{filter:brightness(1);}
to{filter:brightness(1.3);}
}

.subtitle{
font-size:18px;
color:#444;
margin-bottom:20px;
}

/* KPI CARDS */

.kpi-card{
background: rgba(255,255,255,0.15);
backdrop-filter: blur(10px);
padding:25px;
border-radius:18px;
color:white;
text-align:center;
box-shadow:0 8px 30px rgba(0,0,0,0.2);
transition: all 0.3s ease;
}

.kpi-card:hover{
transform: translateY(-6px);
box-shadow:0 12px 40px rgba(0,0,0,0.35);
}

.kpi1{background: linear-gradient(135deg,#667eea,#764ba2);}
.kpi2{background: linear-gradient(135deg,#ff9966,#ff5e62);}
.kpi3{background: linear-gradient(135deg,#56ab2f,#a8e063);}
.kpi4{background: linear-gradient(135deg,#00c9ff,#92fe9d);}

.metric-title{
font-size:16px;
opacity:0.9;
}

.metric-value{
font-size:32px;
font-weight:bold;
margin-top:5px;
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
background: linear-gradient(180deg,#141e30,#243b55);
color:white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown('<div class="main-title">🏭 ThermoShield Manufacturing Intelligence Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Advanced Business Analytics Platform for Insulation Manufacturing</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------

df = pd.read_csv("../data/synthetic_insulation_manufacturing_data.csv")

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.header("⚙ Business Simulation")

investment = st.sidebar.number_input("Initial Investment (Crores)",4.0)

operational_cost = st.sidebar.number_input("Operational Cost (Crores)",1.6)

units = st.sidebar.slider("Units Produced",5000,20000,10000)

price = st.sidebar.slider("Selling Price",5000,12000,8000)

# -------------------------------------------------
# CALCULATIONS
# -------------------------------------------------

revenue = units * price / 10000000
profit = revenue - operational_cost
roi = (profit/investment)*100
breakeven = investment/profit if profit>0 else 0

# -------------------------------------------------
# KPI CARDS
# -------------------------------------------------

st.subheader("📊 Executive Financial Overview")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card kpi1">
    <div class="metric-title">Revenue</div>
    <div class="metric-value">₹{round(revenue,2)} Cr</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card kpi2">
    <div class="metric-title">Net Profit</div>
    <div class="metric-value">₹{round(profit,2)} Cr</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card kpi3">
    <div class="metric-title">ROI</div>
    <div class="metric-value">{round(roi,2)}%</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card kpi4">
    <div class="metric-title">Break Even</div>
    <div class="metric-value">{round(breakeven,2)} yrs</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# TABS
# -------------------------------------------------

tab1,tab2,tab3 = st.tabs([
"📈 Financial Analysis",
"⚙ Production Analytics",
"📊 Market Insights"
])

# -------------------------------------------------
# TAB 1
# -------------------------------------------------

with tab1:

    st.subheader("Profit Sensitivity Analysis")

    price_range = np.linspace(5000,15000,20)

    profit_curve = (units*price_range/10000000) - operational_cost

    fig = px.line(
        x=price_range,
        y=profit_curve,
        markers=True,
        labels={"x":"Selling Price","y":"Profit (Crores)"},
        title="Profit vs Selling Price",
        color_discrete_sequence=["#ff512f"]
    )

    st.plotly_chart(fig,use_container_width=True)

# -------------------------------------------------
# TAB 2
# -------------------------------------------------

with tab2:

    st.subheader("Machine Efficiency Distribution")

    fig2 = px.histogram(
        df,
        x="Machine_Efficiency_Percent",
        nbins=20,
        title="Machine Efficiency Distribution",
        color_discrete_sequence=["#764ba2"]
    )

    st.plotly_chart(fig2,use_container_width=True)

    st.subheader("Energy vs Production Cost")

    fig3 = px.scatter(
        df,
        x="Energy_Consumption_kWh",
        y="Unit_Production_Cost_INR",
        color="Material_Type",
        title="Energy Consumption vs Production Cost"
    )

    st.plotly_chart(fig3,use_container_width=True)

# -------------------------------------------------
# TAB 3
# -------------------------------------------------

with tab3:

    st.subheader("Market Demand Trend")

    fig4 = px.line(
        df["Market_Demand_Index"],
        title="Market Demand Index Trend",
        color_discrete_sequence=["#00c9ff"]
    )

    st.plotly_chart(fig4,use_container_width=True)

# -------------------------------------------------
# FINAL RECOMMENDATION
# -------------------------------------------------

st.divider()

st.subheader("🧠 Investment Recommendation")

if profit > 0 and roi > 20:

    st.success("✅ Based on the simulation, establishing the manufacturing unit is financially viable.")

else:

    st.error("❌ Based on the current simulation parameters, the investment is not recommended.")