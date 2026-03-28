import streamlit as st
import json
from auth import login
from fantasy_rules import validate_team
from league import add_score, leaderboard

st.set_page_config("Fantasy Cricket", layout="wide")

if "user" not in st.session_state:
    login()
    st.stop()

st.title("🏏 Fantasy Cricket League")

players = json.load(open("players.json"))

selected = st.multiselect(
    "Select 11 Players",
    players,
    format_func=lambda x: f"{x['name']} ({x['SkillName']})"
)

if len(selected) == 11:
    result = validate_team(selected)
    if result != "OK":
        st.error(result)
    else:
        captain = st.selectbox(
            "Select Captain",
            [p["name"] for p in selected]
        )

        if st.button("Save Team"):
            st.success("Team Saved Successfully")
