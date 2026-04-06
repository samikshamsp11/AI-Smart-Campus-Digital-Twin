import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Digital Twin", layout="wide")

# -------------------------------
# 🎨 UI
# -------------------------------
st.markdown("""
<style>
.stApp {background: #f5f7fa;}
section[data-testid="stSidebar"] {background: #1e293b;}
section[data-testid="stSidebar"] * {color: white !important;}

.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #1f2937;
}

.card {
    padding:20px;
    border-radius:12px;
    color:white;
    text-align:center;
    font-weight:bold;
    box-shadow:0px 4px 10px rgba(0,0,0,0.2);
}

.fixed-img img {
    width:100%;
    height:240px;
    object-fit:cover;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("🌍 Digital Twin")
menu = st.sidebar.radio("Navigate", [
    "Overview",
    "Data Input",
    "Dashboard",
    "Prediction",
    "AI Insights",
    "Smart Recommendations",
    "Simulation",
    "Score"
])

# -------------------------------
# DATA STORAGE
# -------------------------------
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Day","Energy","FoodWaste","Water"])

# -------------------------------
# OVERVIEW
# -------------------------------
if menu == "Overview":

    st.markdown('<p class="title">🌍 AI Smart Sustainable Campus Digital Twin</p>', unsafe_allow_html=True)

    st.markdown("<p style='text-align:center;color:gray;'>Monitor, analyze and optimize sustainability using AI</p>", unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)
    col1.markdown('<div class="card" style="background:#4facfe">⚡ Energy Monitoring</div>', unsafe_allow_html=True)
    col2.markdown('<div class="card" style="background:#43e97b">🍽 Waste Management</div>', unsafe_allow_html=True)
    col3.markdown('<div class="card" style="background:#fa709a">💧 Water Optimization</div>', unsafe_allow_html=True)

    st.subheader("🌱 Real World Sustainability")

    col1,col2,col3 = st.columns(3)

    with col1:
        st.markdown('<div class="fixed-img">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1466611653911-95081537e5b7")
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("Renewable Energy")

    with col2:
        st.markdown('<div class="fixed-img">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1501004318641-b39e6451bec6")
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("Waste Management")

    with col3:
        st.markdown('<div class="fixed-img">', unsafe_allow_html=True)
        st.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb")
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("Water Conservation")

# -------------------------------
# DATA INPUT
# -------------------------------
elif menu == "Data Input":
    st.title("📥 Enter Data")

    col1,col2,col3 = st.columns(3)
    energy = col1.number_input("⚡ Energy",100,1000,400)
    food = col2.number_input("🍽 Waste",10,200,50)
    water = col3.number_input("💧 Water",500,5000,2000)

    if st.button("Add Data"):
        day = len(st.session_state.data)+1
        new = pd.DataFrame([[day,energy,food,water]],
        columns=["Day","Energy","FoodWaste","Water"])
        st.session_state.data = pd.concat([st.session_state.data,new], ignore_index=True)
        st.success("Data Added")

    st.dataframe(st.session_state.data)

# -------------------------------
# DASHBOARD
# -------------------------------
elif menu == "Dashboard":
    st.title("📊 Dashboard")

    if not st.session_state.data.empty:
        data = st.session_state.data

        col1,col2,col3 = st.columns(3)
        col1.metric("⚡ Energy", int(data["Energy"].mean()))
        col2.metric("🍽 Waste", int(data["FoodWaste"].mean()))
        col3.metric("💧 Water", int(data["Water"].mean()))

        st.line_chart(data[["Energy","FoodWaste","Water"]])
    else:
        st.warning("Add data first")

# -------------------------------
# PREDICTION
# -------------------------------
elif menu == "Prediction":
    st.title("🔮 AI Prediction")

    if len(st.session_state.data)>2:
        data = st.session_state.data
        X = data[["Day"]]

        model = LinearRegression()

        model.fit(X,data["Energy"])
        e = int(model.predict([[len(data)+1]])[0])

        model.fit(X,data["FoodWaste"])
        f = int(model.predict([[len(data)+1]])[0])

        model.fit(X,data["Water"])
        w = int(model.predict([[len(data)+1]])[0])

        st.success(f"⚡ {e} | 🍽 {f} | 💧 {w}")
    else:
        st.warning("Add more data")

# -------------------------------
# AI INSIGHTS (FIXED)
# -------------------------------
elif menu == "AI Insights":
    st.title("🤖 AI Insights")

    if not st.session_state.data.empty:
        data = st.session_state.data

        energy_avg = data["Energy"].mean()
        waste_avg = data["FoodWaste"].mean()
        water_avg = data["Water"].mean()

        st.subheader("📊 Current Analysis")
        st.write(f"⚡ Energy Avg: {int(energy_avg)}")
        st.write(f"🍽 Waste Avg: {int(waste_avg)}")
        st.write(f"💧 Water Avg: {int(water_avg)}")

        st.subheader("🚨 Alerts")

        if energy_avg > 600:
            st.error("⚡ High Energy Usage")
        else:
            st.success("⚡ Energy usage is under control")

        if waste_avg > 80:
            st.error("🍽 High Waste")
        else:
            st.success("🍽 Waste is under control")

        if water_avg > 3000:
            st.error("💧 High Water Usage")
        else:
            st.success("💧 Water usage is efficient")

    else:
        st.warning("Add data first")

# -------------------------------
# SMART RECOMMENDATIONS
# -------------------------------
elif menu == "Smart Recommendations":
    st.title("🤖 Smart Recommendations")

    if not st.session_state.data.empty:
        data = st.session_state.data

        st.info("⚡ Reduce energy by 15% to save cost")
        st.info("🍽 Reduce waste by 20% for better sustainability")
        st.info("💧 Save 200L water daily")

    else:
        st.warning("Add data first")

# -------------------------------
# SIMULATION
# -------------------------------
elif menu == "Simulation":
    st.title("🧠 What-if Simulation")

    energy = st.slider("Energy",100,1000,400)
    food = st.slider("Waste",10,200,50)
    water = st.slider("Water",500,5000,2000)

    score = 100 - (energy/10 + food + water/50)
    score = max(0,int(score))

    st.metric("Predicted Score", score)

# -------------------------------
# SCORE
# -------------------------------
elif menu == "Score":
    st.title("⭐ Sustainability Score")

    if not st.session_state.data.empty:
        data = st.session_state.data

        score = 100 - (
            data["Energy"].mean()/10 +
            data["FoodWaste"].mean() +
            data["Water"].mean()/50
        )

        score = max(0,int(score))
        st.metric("Score",score)

    else:
        st.warning("Add data first")