import streamlit as st
from promptflow.client import load_flow
import os

# 1. INITIALIZE SESSION STATE (The fix for your error)
if 'needs_rerun' not in st.session_state:
    st.session_state.needs_rerun = False
if 'pending_task' not in st.session_state:
    st.session_state.pending_task = None

# 2. LOAD FLOW
# Using @st.cache_resource prevents reloading the flow on every click
@st.cache_resource
def get_flow():
    return load_flow(source="./")

run_flow = get_flow()

st.title("🤖 Managed Task Assistant")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Controls")
    if st.button("🗑️ Clear Grocery List"):
        if os.path.exists("groceries.txt"):
            os.remove("groceries.txt")
            st.session_state.needs_rerun = True
            st.success("Deleted!")

    if st.button("🗑️ Clear To-Do List"):
        if os.path.exists("todo.txt"):
            os.remove("todo.txt")
            st.session_state.needs_rerun = True
            st.success("Deleted!")

# --- MAIN INPUT ---
user_input = st.text_input("What's the task?")

if st.button("Submit") and user_input:
    with st.spinner("Classifying..."):
        result = run_flow(question=user_input)
        if "UNCERTAIN" in result.upper() or "ERROR" in result.upper():
            st.session_state.pending_task = user_input
        else:
            st.success(result)

# --- HUMAN-IN-THE-LOOP ---
if st.session_state.pending_task:
    st.info(f"❓ Categorize: **{st.session_state.pending_task}**")
    c_g, c_t = st.columns(2)
    with c_g:
        if st.button("🛒 Grocery"):
            with open("groceries.txt", "a") as f: f.write(f"- {st.session_state.pending_task}\n")
            st.session_state.pending_task = None
            st.session_state.needs_rerun = True
    with c_t:
        if st.button("✅ To-Do"):
            with open("todo.txt", "a") as f: f.write(f"- {st.session_state.pending_task}\n")
            st.session_state.pending_task = None
            st.session_state.needs_rerun = True

st.divider()

# --- DISPLAY ---
st.header("📋 Your Current Lists")
col1, col2 = st.columns(2)

def show_list(filename, header):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            lines = [l for l in f.readlines() if l.strip().startswith("-")]
            st.text("".join(lines) if lines else "Empty.")
    else:
        st.write("List is clear!")

with col1:
    st.subheader("🛒 Groceries")
    show_list("groceries.txt", "Grocery")

with col2:
    st.subheader("✅ To-Dos")
    show_list("todo.txt", "To-Do")

# 3. THE RERUN TRIGGER (Placed at the bottom to avoid threading issues)
if st.session_state.needs_rerun:
    st.session_state.needs_rerun = False
    st.rerun()
