from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Chaitannyaa", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r =requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def local_file(file_name):
    with open(file_name)  as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_file("style/style.css")
lottie_coding1= load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_tfb3estd.json")
lottie_coding2= load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_cgjrfdzx.json")
lottie_coding3= load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_buopyjyz.json")
lottie_coding4= load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_4kx2q32n.json")
lottie_coding5= load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fi0ty9ak.json")
image_3d=Image.open("images/c1.jpg")
image_2d=Image.open("images/c3.jpg")
image_logo=Image.open("images/logo.jpg")
# _____Header-Section____
with st.container():
    left_column, right_column = st.columns((1.5,1.5))
    with  left_column:
        st.subheader("Hi, I am Chaitannyaa :wave:")
        st.title("A Python Lover :heart:")
        st.write("I am passionate about learning new technologies and implement them to create some value")
        st.write("[Learn More >](https://www.linkedin.com/in/chaitannyaa-gaikwad-b16965115)")
        st.image(image_logo)    
    with right_column:
        st_lottie(lottie_coding1, height=450, key="coding")
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Technical Skills")
        st.write("##")
        st.write(
            '''
            Cloud - Amazon Web Services:\n
            - Compute and Networking
            - Identity and access management (IAM)
            - AWS CloudWatch
            - Amazon S3 & SNS
            '''
            )
        st.write("##")
        st.write(
            '''
            Ubuntu 20.04 (Basic 50 commands):
            - User account creation, account maintenance and setting password.
            - Configuring Logical Volume Management (LVM) Storage.
            - Installation and configuration of DNS, APACHE etc on Red Hat.
            '''
            )
        st.write("##")
        st.write(
            '''
            Containerization (Docker & Kubernetes)
            - Creating docker containers using images from docker hub.
            - Customizing the Docker images by writing Dockerfile according to the needs.
            - Tagging images and changing start-up commands of containers.
            - Creating objects like Pod, Replica Set, Service, Deployment.
            - Creating Kubernetes objects using YAML definition files.
            - Launched a simple web app on a single node Kubernetes cluster.
            - Deploying applications into Kubernetes as Deployments, Pods based on the need.
            - Working on Docker hub, creating Docker images and handling multiple images.
            '''
            )
        st.write("##")
        st.write(
            '''
            Python: Modules, Pip, Variables, Datatypes, Strings, Lists, Tuples, Dictionary, Sets, Conditional Expressions, 
            Loops, Functions, Recursions, File I/O, Object oriented programming (Oops), Inheritance, Exception 
            Handling, Virtual Environments
            
            Python Project:
            - This Webpage itself :tada:
            - Library book issue - return system
            - Rock- paper and scissor game
            - Perfect guess game
            - Tic-Tac-Toe game
            '''
            )
        st.write("[Learn More >](https://github.com/Chaitannyaa/Fun_Project_with.py.git)")
        
    with right_column:
        st_lottie(lottie_coding2, height=400)
        st_lottie(lottie_coding5, height=350)
        st_lottie(lottie_coding4, height=350)
with st.container():
    st.write('---')
    st.header("Academic Project")
    st.write("##")
    Image_column, middle_column, text_column = st.columns((1,1.025,2))
    with Image_column:
        st.image(image_3d)
    with middle_column:
        st.image(image_2d)
    with text_column:
        st.subheader("Liquid Cooling System for CPU Processor")
        st.write(
            '''
            Design and implementation of Thermosyphon based liquid cooling system for CPU processor to improve 
            its performance.
            
            It is a passive cooling system based on Thermosyphon principle for dissipating heat
            produced by a CPU processor. Acetone is used as a circulating coolant in the two-phase closed loop liquid 
            cooling system fixed on the processor of desktop computer. This proposed system gives extended
            standalone period of 4 minutes, 28 seconds and therefore helpful in critical system failure, which also 
            provides flexibility to raise the clock speed of the existing processors.
            '''
            )
        st.markdown("[Actual Photos..](https://drive.google.com/drive/folders/1MescWd78RyDYAZqnsjVBv5N-vYu9mS-0?usp=sharing)")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/chaitannyaagaikwad@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
