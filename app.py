import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
from lyzr_automata.tasks.task_literals import InputType, OutputType
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Productivity Assistant👨‍💻")
st.markdown("Welcome to Productivity Assistant! We provide personalized tips and actionable advice to help you overcome challenges and achieve your specific goals efficiently.")
st.markdown("            1) Mention your daily routine. ")
st.markdown("            2) Mention the productivity challenges you face.")
st.markdown("            3) Mention your goals (Short Term or Long Term) or any other milestones you want to achieve if any.")
input = st.text_input(" Please enter the above details:",placeholder=f"""Type here""")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)


def generation(input):
    generator_agent = Agent(
        role="Expert PRODUCTIVITY ASSISTANT",
        prompt_persona=f"Your task is to offer PERSONALIZED PRODUCTIVITY TIPS and ACTIONABLE RECOMMENDATIONS tailored to an individual's DAILY ROUTINE, the PRODUCTIVITY CHALLENGES they encounter, and their GOALS—whether SHORT-TERM or LONG-TERM—or any other MILESTONES they aim to achieve.")
    prompt = f"""
You are an Expert PRODUCTIVITY ASSISTANT. Your task is to offer PERSONALIZED PRODUCTIVITY TIPS and ACTIONABLE RECOMMENDATIONS tailored to an individual's DAILY ROUTINE, the PRODUCTIVITY CHALLENGES they encounter, and their GOALS—whether SHORT-TERM or LONG-TERM—or any other MILESTONES they aim to achieve.

Follow this STEP-BY-STEP process to ensure a comprehensive approach:

1. ANALYZE detailed information about the user's current DAILY ROUTINE , IDENTIFY specific PRODUCTIVITY CHALLENGES the user faces within their routine and also IDENTIFY the user’s SHORT-TERM or LONG-TERM GOALS and as well as any other MILESTONES they wish to reach.

2. DEVELOP a set of CUSTOMIZED TIPS that align with their unique circumstances and objectives.

3. FORMULATE ACTIONABLE RECOMMENDATIONS  in a clear, ORGANIZED FORMAT that the user can implement immediately to enhance productivity.

You MUST ensure that your advice is PRACTICAL, FEASIBLE, and directly supports the user's stated goals.


 """

    generator_agent_task = Task(
        name="Generation",
        model=open_ai_text_completion_model,
        agent=generator_agent,
        instructions=prompt,
        default_input=input,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
    ).execute()

    return generator_agent_task 
   
if st.button("Assist!"):
    solution = generation(input)
    st.markdown(solution)

with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Automata Agent . For any inquiries or issues, please contact Lyzr.

    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width=True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width=True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width=True)
    st.link_button("Slack",
                   url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw',
                   use_container_width=True)