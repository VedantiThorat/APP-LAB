import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from PyPDF2 import PdfReader
from docx import Document

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(
    page_title="AI Meeting Action Extractor",
    page_icon="📋",
    layout="wide"
)

st.title("📋 AI Meeting Action-Item Extractor")

st.write("Convert meeting transcripts into summaries and structured action items.")

# -----------------------------
# Read uploaded file
# -----------------------------
def read_file(file):

    if file.type == "text/plain":
        return file.read().decode("utf-8")

    elif file.type == "application/pdf":
        pdf = PdfReader(file)
        text = ""

        for page in pdf.pages:
            text += page.extract_text() + "\n"

        return text

    else:
        doc = Document(file)
        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

# -----------------------------
# AI Summary
# -----------------------------
def meeting_summary(text):

    prompt = f"""
Summarize this meeting in 5 bullet points.

Meeting:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content

# -----------------------------
# AI Action Extraction
# -----------------------------
def extract_actions(text):

    prompt = f"""
Extract action items.

Return ONLY JSON.

Format:

[
{{
"Task":"",
"Owner":"",
"Deadline":"",
"Priority":"",
"Status":"Pending",
"Confidence":"90%"
}}
]

Meeting:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )

    return response.choices[0].message.content

# -----------------------------
# Input Section
# -----------------------------
uploaded = st.file_uploader(
    "Upload TXT, PDF or DOCX",
    type=["txt","pdf","docx"]
)

transcript = st.text_area("Or paste transcript", height=220)

if uploaded:
    transcript = read_file(uploaded)
    st.success("File loaded successfully.")

# -----------------------------
# Main Button
# -----------------------------
if st.button("Generate Results", use_container_width=True):

    if transcript.strip()=="":

        st.warning("Please provide a transcript.")

    else:

        with st.spinner("Analyzing meeting..."):

            summary = meeting_summary(transcript)

            raw = extract_actions(transcript)

            try:
                data = json.loads(raw)

            except:
                start = raw.find("[")
                end = raw.rfind("]")+1
                data = json.loads(raw[start:end])

            df = pd.DataFrame(data)

        # -------------------------
        # Validation
        # -------------------------
        df["Validation"] = ""

        for i in range(len(df)):

            msg=""

            if df.loc[i,"Owner"]=="":
                msg += "Missing Owner "

            if df.loc[i,"Deadline"]=="":
                msg += "Missing Deadline"

            df.loc[i,"Validation"]=msg

        # -------------------------
        # Meeting Summary
        # -------------------------
        st.header("Meeting Summary")

        st.write(summary)

        st.divider()

        # -------------------------
        # Dashboard
        # -------------------------
        st.header("Dashboard")

        total=len(df)
        pending=(df["Status"]=="Pending").sum()
        high=(df["Priority"]=="High").sum()

        c1,c2,c3=st.columns(3)

        c1.metric("Total Tasks",total)
        c2.metric("Pending",pending)
        c3.metric("High Priority",high)

        st.divider()

        # -------------------------
        # Search & Filter
        # -------------------------
        st.header("Action Items")

        search=st.text_input("Search Task")

        status=st.selectbox(
            "Filter Status",
            ["All"]+list(df["Status"].unique())
        )

        filtered=df.copy()

        if search!="":
            filtered=filtered[
                filtered["Task"].str.contains(search,case=False)
            ]

        if status!="All":
            filtered=filtered[
                filtered["Status"]==status
            ]

        st.data_editor(filtered,use_container_width=True)

        st.divider()

        # -------------------------
        # Charts
        # -------------------------
        st.header("Analytics")

        if "Owner" in df.columns:

            owner=df.groupby("Owner").size().reset_index(name="Tasks")

            fig1=px.bar(
                owner,
                x="Owner",
                y="Tasks",
                title="Tasks Per Owner"
            )

            st.plotly_chart(fig1,use_container_width=True)

        if "Priority" in df.columns:

            pie=df.groupby("Priority").size().reset_index(name="Count")

            fig2=px.pie(
                pie,
                names="Priority",
                values="Count",
                title="Priority Distribution"
            )

            st.plotly_chart(fig2,use_container_width=True)

        st.divider()

        # -------------------------
        # Download
        # -------------------------
        csv=df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download CSV",
            csv,
            "meeting_action_items.csv",
            "text/csv",
            use_container_width=True
        )