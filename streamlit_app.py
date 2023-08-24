
import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



#####################
# Header
with st.container():
    col1, col2 = st.columns([0.6, 0.6], gap='small')
    with col1:
        st.title("Qiyao HE Is Here !")
        st.subheader("Hello, Welcome to my page 👋")
        st.write("📍Bordeaux, France")
        st.write("Hi, my name is Qiyao HE. A warm welcom👏! I built this webpage with self-learning knowledge so it might look not pretty and professional, please understand me. Super welcome to my page, if you want to know more about me, please explore here.")
    with col2:
        image = Image.open('mecv.png')
        st.image(image, width=300)

st.write('---')
st.header('Contact Me')
c1, c2 = st.columns(2)
with st.container():
    c1.write("Linkedin: https://www.linkedin.com/in/qiyao-he")
    c2.write("Email: mechealia.he3378@outlook.com")

with st.container():
    st.write("---")

    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who Is Qiyao HE:")
        st.write("##")
        st.write(
            """
            My name is Qiyao , i am a chinese girl and now live in France. I am master of supply chain management graduated from KEDGE business school in the year 2020, since then I have been working in different roles and industries for several years. I enjoy learning and I am constantly developing my skills, i love to use what i learned into the job and keep developing it . Now i am looking for a new job opportunity, if you are interested in my profile, please do not hesitate to contact with me!!!
            - I speak Chinese 🇨🇳, English 🇬🇧 and French 🇨🇵
            - I am experienced Project Coordinator, cross-functional communicator and customer facing problem solver. Worked in data-oriented environment and a passion for delivering high quality customer oriented projects. 
            - I am certified professional scrum master.
            - I am professional for JIRA, Dynamics CRM, Microsoft office softwares and solid knowledge of Oracle Procurement Business Process, Google Ads Measurement，Network defense essentials,Ethical hacking essentials


            """
        )
    with right_column:
        st.markdown('##')
        image = Image.open('comp.png')
        st.image(image, width=220)



st.write('---')
st.header('My Interests Are')
st.write(
    """
    - I love climbing, hiking and camping these outdoor activities. Reached the Annapurna Base Camp in snowstorm conditions
    - I am always interested in traveling(visited 12 countries). This helps me to communicate efficient with people from different cultures, and also allows me to adapt and explore new environments quickly. 
    - I love gardening 🌲 and planting vegetables 🥬. This is really help me to develop my problem solving skills, i have to always to take care them and find out the problems.
    - I like reading and watching videos that introduce and explain the new technology and rare culture. Besides this, I like to read self-improvement and philosophical books which help me to know more about myself.

    """
)


with st.container():
    st.write("---")
    st.header('👩‍💻 Work Experience')
    st.write(
        """
       Hello, here is the list of my past working experience, check it out! 

    """
    )

    col1, col2 = st.columns([0.6, 0.6], gap='large')
    with col1:
        st.subheader("Customer Service Agent – PeopleCert International LTD")
        st.info('''
        Remote: Dec 2021 - Sep 2022
        - Delivered fast, precise and high quality service to customers via live chat, emails and phone calls
        - Coordinated over different departments to solve customer facing issues and meet customer needs 
        - Coordinated and helped service providers in China region to resolve process conflicts arising from different business processes in the region
        - Received multiple monthly high-efficiency employee rewards
        ''')
    with col2:
        st.subheader("Supply Chain Software Analyst – Farheap Solutions")
        st.info('''
        Nevada, USA(Remote): Aug 2021 - May 2022
        - Handled day-to-day software and supply chain related issues faced by the factories 
        - Coordinated with engineers and local factory workers to solve software user-friendly interface issues  
        - Optimized the coordination of development and facilitated communication
        ''')
    st.markdown('##')
    col1, col2 = st.columns([0.6, 0.6], gap='large')
    with col1:
        st.subheader("Cyber Security Project Coordinator – Sony Electronics")
        st.info('''
        Istanbul, Turkey: Sep 2019 - Apr 2021
        - Completed 20 security projects: mainly responsible for Sony China & AP regions 
        - Cooperated with local engineers, 3rd party software companies and China regions business owners to solve technical and commercial problems faced in the projects
        - Worked in data-oriented environment and delivered high quality software projects
        - Translated the business security needs into feasible solutions, align the goals, clear road blocks, and ensure smooth execution
        ''')
    with col2:
        st.subheader("Business Executive Assistant – Chongqing Rare Fish Company")
        st.info('''
        Chongqing, China: Jan 2018 - Jun 2018
        - Maintained relationship with suppliers and developed new potential customers 
        - Organized events of visiting the fish farm for customers and suppliers
        - Organized visiting of supplier's factory for inspecting qualifications of suppliers 
        - Assisted for requiring for new supplies and requested for quotations and arranged visiting for new supplies 
              ''')
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


with st.container():
    st.write("---")
    st.header('👩‍🎓 My Education')
    st.write(
        """
       Hello, here is the list for my educations, check it out! 
           With 4 years education for my bachelor degree of Administrative Management at Harbin Normal University.
           Almost 2 years education for my master degree of Global Supply Chain Management at KEDGE Business School. 
           When I decided back to continue my career, i realised french is a very important skill, so i back to university to improve my it.  

    """
    )
st.markdown('##')

st.subheader("French Language Courses – Université Bordeaux-Montaigne")
st.info('''
Bordeaux, France: Sep 2022 - May 2023
- French Intermediate Courses
''')

st.subheader("Master of Science – Global Supply Chain Management (ISLI)   KEDGE Business School")
st.info('''
Bordeaux, France: Sep 2018 - Apr 2020
- 1st (France) and 5th (worldwide) Project in Supply Chain and Logistics
- Sourcing and inventory management(MRP/ BOM/ JIT / ASRS), line management, Project management, Logistics(Incoterms / Demand planning / order fulfillment )
- Company project:Designed and deployed new business model for shipping company using new energy for transportation
''')

st.subheader("Bachelor – Administrative Management                        Harbin Normal University")
st.info('''
Harbin, China: Sep 2014 - Jun 2018
- Business Negotiation, Marketing, International Trade, Business Etiquette
''')



with st.container():
    st.write("---")
    st.header(":mailbox: Get In Touch With Me!")
    contact_form = """
<form action="https://formsubmit.co/mechealia.he3378@outlook.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message to Qiyao"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
