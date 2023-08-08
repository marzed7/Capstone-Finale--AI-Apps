
#%%
import json
import os
import streamlit as st
import openai
from IPython.display import Markdown, display, HTML
from dotenv import dotenv_values
from IPython.display import Image
import requests
#%%
# config = dotenv_values('.env')
# openai.api_key = config['OPENAI_API_KEY']
#%%
def prompt_image(summaries):

    m7 = """World War II, a significant global conflict lasting from 1939 to 1945, had far-reaching implications for the course of history. The war involved major powers, including Germany, Japan, the United States, and the Soviet Union. It resulted in profound political, economic, and social changes. The United States and the Soviet Union emerged as superpowers, shaping the post-war geopolitical landscape. The war's aftermath led to the establishment of the United Nations, an international organization aimed at fostering cooperation and preventing future conflicts."""

    a7 = """Generate an image depicting the somber aftermath of World War II, highlighting the unity and determination of nations in establishing the United Nations for global cooperation and lasting peace."""

    p7 = f"""
    Q:{summaries}
    A: 
    """

    pro = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{
        "role": "system",
        "content": "You will create a prompt for generating image such as a prompt for Dall-e. This prompt follow the provided format and give specific instructions for that visually represent the themes and match the user input application's tone and style."},
        {
        "role":"user",
        "content": m7
        },
        {
        "role":"assistant",
        "content": a7
        },
        {
        "role":"user",
        "content": p7
        },
        ],
        max_tokens = 40,
        temperature = 0.5
    )

    prompts = pro['choices'][0]['message']['content']
    return prompts
#%%
def image_vis(prompts, num=1):
    
    image_response = openai.Image.create(
        prompt = prompts,
        n = num,
        size = "256x256"
    )
    images = [image['url'] for image in image_response['data']]
    return images

#%%
def note_title(msg):

    mm = """Textual notes on World War II and its impact on global history.
    Specific keywords or topics: World War II, impact, global history."""

    aa = """World War II's Transformative Impact on Global History"""

    pp = f"""
    Q:{msg}
    A: 
    """

    til = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{
        "role": "system",
        "content": "You are an intelligent apps that can generate notes from given topic or subject. For this part, you will generate a clear and relevant title for making notes from the user input."},
        {
        "role":"user",
        "content": mm
        },
        {
        "role":"assistant",
        "content": aa
        },
        {
        "role":"user",
        "content": pp
        },
        ],
        max_tokens = 25,
        temperature = 0.5
    )

    note_titles = til['choices'][0]['message']['content']
    return note_titles

#%%
def topic_title(summaries):

    m6 = """World War II, a significant global conflict lasting from 1939 to 1945, had far-reaching implications for the course of history. The war involved major powers, including Germany, Japan, the United States, and the Soviet Union. It resulted in profound political, economic, and social changes. The United States and the Soviet Union emerged as superpowers, shaping the post-war geopolitical landscape. The war's aftermath led to the establishment of the United Nations, an international organization aimed at fostering cooperation and preventing future conflicts."""

    a6 = """Global Transformation: World War II's Impact on Superpowers and International Cooperation
    """
    p6 = f"""
    Q:{summaries}
    A: 
    """

    title = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{
        "role": "system",
        "content": "You will focuses on creating an informative and engaging topic title based on the summaries provided. The goal is to generate a concise and captivating title that encapsulates the essence of the topic. This feature enhances the user experience by immediately conveying the main idea of the summary and piquing the user's interest. The generated title serves as an entry point for users, allowing them to quickly grasp the central theme and purpose of the summary."},
        {
        "role":"user",
        "content": m6
        },
        {
        "role":"assistant",
        "content": a6
        },
        {
        "role":"user",
        "content": p6
        },
        ],
        max_tokens = 25,
        temperature = 0.5
    )

    titles = title['choices'][0]['message']['content']
    return titles
#%%
def suggested_exploration(summaries):

    m5 = """World War II, a significant global conflict lasting from 1939 to 1945, had far-reaching implications for the course of history. The war involved major powers, including Germany, Japan, the United States, and the Soviet Union. It resulted in profound political, economic, and social changes. The United States and the Soviet Union emerged as superpowers, shaping the post-war geopolitical landscape. The war's aftermath led to the establishment of the United Nations, an international organization aimed at fostering cooperation and preventing future conflicts."""

    a5 = """
    1. **Role of key leaders during World War II**
    2. **Technological advancements and their impact on the outcome**
    3. **Consequences of the war on different regions**
    """
    p5 = f"""
    Q:{summaries}
    A: 
    """

    explore = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{
        "role": "system",
        "content": "You will assist users to explore the topic in greater depth by providing specific areas or aspects they can delve into. The user input for this function typically consists of the summarized topic. You will create 3 suggestions based on the user's input and present them in the output. These suggestions guide the user on specific directions they can take to gain a deeper and more comprehensive understanding of the topic."},
        {
        "role":"user",
        "content": m5
        },
        {
        "role":"assistant",
        "content": a5
        },
        {
        "role":"user",
        "content": p5
        },
        ],
        max_tokens = 250,
        temperature = 1
    )

    explores = explore['choices'][0]['message']['content']
    return explores
#%%
def step_guide(summaries):

    m4 = """World War II, a significant global conflict lasting from 1939 to 1945, had far-reaching implications for the course of history. The war involved major powers, including Germany, Japan, the United States, and the Soviet Union. It resulted in profound political, economic, and social changes. The United States and the Soviet Union emerged as superpowers, shaping the post-war geopolitical landscape. The war's aftermath led to the establishment of the United Nations, an international organization aimed at fostering cooperation and preventing future conflicts."""

    a4 = """Guides for understanding the topic:
    1. **World War II Begins (1939-1945)**: The conflict commences as a global war involving major powers, including Germany, Japan, the United States, and the Soviet Union. Nations align themselves into opposing alliances, with the Axis Powers (Germany, Japan, Italy) facing off against the Allied Powers (United States, Soviet Union, United Kingdom, etc.).
    
    2. **Profound Changes Emerge**: The war results in significant political shifts as nations vie for dominance and influence on the global stage. Economies are mobilized for total war, leading to transformative economic changes as industries are repurposed for wartime production. Societies experience upheaval, with social norms evolving due to the demands of the conflict and changes in gender roles. 
    
    3. **Superpowers Emerge**: The United States and the Soviet Union emerge as dominant superpowers due to their contributions to the war effort and their growing influence. These superpowers shape the post-war geopolitical landscape by influencing global politics, alliances, and the rebuilding process.
    
    4. **The Birth of the United Nations**: In the aftermath of World War II, a collective desire for international cooperation and conflict prevention leads to the establishment of the United Nations. The United Nations serves as a platform for member nations to engage in diplomatic dialogue, address global challenges, and promote peace and security.
    
    5. **Fostering Cooperation and Preventing Conflicts**: The United Nations becomes a hub for multilateral diplomacy, where nations collaborate to address issues such as human rights, humanitarian crises, and disarmament. Efforts are made to prevent future conflicts through negotiation, mediation, and the establishment of international norms and treaties.
    """
    p4 = f"""
    Q:{summaries}
    A: 
    """

    step = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{
        "role": "system",
        "content": "You are an apps which are an Intelligent Note-Taking for generating step-by-step guides or the flows of the given topic. The goal is to create a user-friendly and informative guide that captures the essence of the topic and presents it in a structured and coherent manner. Examples of step-by-step guides such as the tutorials, guides. You will list down the guides."},
        {
        "role":"user",
        "content": m4
        },
        {
        "role":"assistant",
        "content": a4
        },
        {
        "role":"user",
        "content": p4
        },
        ],
        max_tokens = 500,
        temperature = 1
    )

    steps = step['choices'][0]['message']['content']
    return steps
#%%
def concept_theory(summaries):

    m3 = """World War II, a significant global conflict lasting from 1939 to 1945, had far-reaching implications for the course of history. The war involved major powers, including Germany, Japan, the United States, and the Soviet Union. It resulted in profound political, economic, and social changes. The United States and the Soviet Union emerged as superpowers, shaping the post-war geopolitical landscape. The war's aftermath led to the establishment of the United Nations, an international organization aimed at fostering cooperation and preventing future conflicts."""

    a3 = """
    1. **Balance of Power Theory**:
    2. **Total War Doctrine**:
    3. **Post-War Multilateralism**:"""

    p3 = f"""
    Q:{summaries}
    A: 
    """

    con = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{
        "role": "system",
        "content": "You will generate 3 concepts/theories that involved from the user input topic."},
        {
        "role":"user",
        "content": m3
        },
        {
        "role":"assistant",
        "content": a3
        },
        {
        "role":"user",
        "content": p3
        },
        ],
        max_tokens = 250,
        temperature = 0.7
    )

    concepts = con['choices'][0]['message']['content']
    return concepts
#%%
def keyword(summaries):
    m2 = """World War II, a significant global conflict lasting from 1939 to 1945, had far-reaching implications for the course of history. The war involved major powers, including Germany, Japan, the United States, and the Soviet Union. It resulted in profound political, economic, and social changes. The United States and the Soviet Union emerged as superpowers, shaping the post-war geopolitical landscape. The war's aftermath led to the establishment of the United Nations, an international organization aimed at fostering cooperation and preventing future conflicts."""

    a2 = """
    1.**World War II**: Significant global conflict (1939-1945)
    2.**Global conflict**: Extensive international war
    3.**Major powers**: Dominant nations involved
    4.**United States**: Allied superpower
    5.**Soviet Union**: Allied superpower, post-war implications
    6.**Political changes**: Shifts in governance and leadership
    7.**Economic changes**: Transformations in financial systems and trade
    8.**Social changes**: Societal impacts and adjustments
    9.**Superpowers**: Dominant post-war nations (US, USSR)
    10.**United Nations**: Established to promote international cooperation
    """
    p2 = f"""
    Q:{summaries}
    A: 
    """

    key = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{
        "role": "system",
        "content": "You are an apps which are an Intelligent Note-Taking for generating 10 important keywords from the user input topic. You will list down the keywords as well as its values."},
        {
        "role":"user",
        "content": m2
        },
        {
        "role":"assistant",
        "content": a2
        },
        {
        "role":"user",
        "content": p2
        },
        ],
        max_tokens = 250,
        temperature = 1
    )

    keywords = key['choices'][0]['message']['content']
    return keywords
#%%
def summary(msg):

    m1 = """Textual notes on World War II and its impact on global history.
    Specific keywords or topics: World War II, impact, global history."""

    a1 = """
    World War II, a significant global conflict lasting from 1939 to 1945, had far-reaching implications for the course of history. The war involved major powers, including Germany, Japan, the United States, and the Soviet Union. It resulted in profound political, economic, and social changes. The United States and the Soviet Union emerged as superpowers, shaping the post-war geopolitical landscape. The war's aftermath led to the establishment of the United Nations, an international organization aimed at fostering cooperation and preventing future conflicts.
    """

    p1 = f"""
    Q:{msg}
    A: 
    """

    sum = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{
        "role": "system",
        "content": "You are an apps which are an Intelligent Note-Taking for summary part! Your goal is to produce concise and insightful summaries of user-provided text by transforming traditional note-taking into a smarter and more insightful summaries. Also you are enables to delivery intelligent summaries that facilitate understanding and knowledge acquisition."},
        {
        "role":"user",
        "content": m1
        },
        {
        "role":"assistant",
        "content": a1
        },
        {
        "role":"user",
        "content": p1
        },
        ],
        max_tokens = 500,
        temperature = 1
    )

    summaries = sum['choices'][0]['message']['content']
    return summaries

#%%
def resource(summaries):

    m0 = """World War II, a significant global conflict lasting from 1939 to 1945, had far-reaching implications for the course of history. The war involved major powers, including Germany, Japan, the United States, and the Soviet Union. It resulted in profound political, economic, and social changes. The United States and the Soviet Union emerged as superpowers, shaping the post-war geopolitical landscape. The war's aftermath led to the establishment of the United Nations, an international organization aimed at fostering cooperation and preventing future conflicts."""

    a0 = """
    1. Book: "The Second World War" by Sir Winston Churchill
    2. Article: "The Impact of World War II on Global Politics and Economics" - History Today
    3. Website: World War II Museum - National WWII Museum
    4. Textbook: "World War II: A Short History" by Michael J. Lyons
    """

    p0 = f"""
    Q:{summaries}
    A: 
    """
    reso = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [{
        "role": "system",
        "content": "You are an apps which are an Intelligent Note-Taking and you will provide 4 resources using the given format, which includes references to textbooks, articles, websites, or other materials that are relatable with the summary given. Some examples of resources are link url of the articles or books."},
        {
        "role":"user",
        "content": m0
        },
        {
        "role":"assistant",
        "content": a0
        },
        {
        "role":"user",
        "content": p0
        },
        ],
        max_tokens = 100,
        temperature = 1
    )

    resources = reso['choices'][0]['message']['content']
    return resources

#%%
def table_content():
    
    data = [
        ["Concept/Theory", "Exploration of the key concepts and theories related to the topic."],
        ["Guides", "Practical guides and strategies for studying and comprehending the complex of the topic."],
        ["Summary and Keywords", "A concise summary highlighting the key events, outcomes, and far-reaching consequences."],
        ["Visual", "Image visualization generated from the summary of the topic"],
        ["Suggested Exploration", "Additional resources and avenues for further exploration and in-depth understanding of the topic."],
        ["Resources", "Include references to textbooks, articles, websites, or other materials that provide further explanations or examples. These resources can aid in deeper understanding."]]
    
    table_data = [["Section", "Description"]] + data

    return table_data


#%%

def main():
    # Set page title and background color
    st.set_page_config(page_title="AI-MindJot", page_icon=":books:", layout="wide")
    # Customize your sidebar
    imgg = "https://static.wikia.nocookie.net/ready-or-not/images/4/4d/Mindjot_logo.png"
    st.sidebar.image(imgg, use_column_width=True)

    # st.sidebar.title("AI-GeniusNotion :books:")
    st.sidebar.markdown("**A Gateway to a Smarter Notes!**")

    api_key = st.sidebar.text_input("**API Key:**", type="password")
    if st.sidebar.button("**Insert key**", key="api_key_button"):
        openai.api_key = api_key
        st.sidebar.write("✓ Done")

    page_content = {}
    user_input = st.sidebar.text_area("**Enter your topic:**")

    # Create a button to generate notes based on user input
    if st.sidebar.button("**Generate Note**", key="generate_note_button"):
        if user_input:
            with st.spinner("Generating notes...."):
                note_tilt = note_title(user_input)
                st.subheader(note_tilt)
                generated_output = display_outputs(user_input)
                page_content[user_input] = generated_output
    else:
        # Display a detailed welcoming message
        st.title("Welcome to MindJot :books:")
        st.write("Unleash your creativity with MindJot, your ultimate tool for effortless note generation. Whether you're a writer, student, or anyone seeking inspiration, GeniusNotion empowers you to generate smart and insightful notes in an instant.")
        st.markdown("<h4>Simply follow these steps to get started:</h4>", unsafe_allow_html=True)
        st.markdown("<p>1. Go to sidebar on the left <-- </p>", unsafe_allow_html=True)
        st.markdown("<p>2. Insert your secret API key</p>", unsafe_allow_html=True)
        st.markdown("<p>3. Tell us any topic</p>", unsafe_allow_html=True)

    # Display the generated content in the sidebar
    for item, content in page_content.items():
        if st.sidebar.button("**Reset**", key=f"display_button_{item}"):
            st.sidebar.markdown(content)



# Function to display the generated outputs and visualizations
def display_outputs(msg, num=1):

    summaries = summary(msg)
    keywords = keyword(summaries)
    concepts = concept_theory(summaries)
    steps = step_guide(summaries)
    explores = suggested_exploration(summaries)
    titles = topic_title(summaries)
    prompts = prompt_image(summaries)
    table_data = table_content()
    # images = image_vis("\n".join(prompts), num)
    images = image_vis(prompts, num)
    resources = resource(summaries)

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["**Content**", "**Concept/Theory**", "**Guides**", "**Summary and Keywords**", "**Visual**", "**Suggested Exploration**", "**Resources**"])

    with tab1:
        st.subheader("Note Contents:")
        st.table(table_data) 

    with tab4:
        st.subheader("Topic:")
        st.write(titles)
        st.subheader("Short Summary:")
        st.write(summaries)
        with st.expander("--> See important keywords from the summary <--"):
            st.subheader("Important Keywords:")
            st.write(keywords)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Concept and Theory:")
            st.write(concepts)
        with col2:
            st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/3/35/Trefoil_knot_conways_game_of_life_without_background_and_fitting.gif)")
            st.write("\n\n\n\n")
            st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/1/1f/Wikipedia_Logo_Puzzle_Globe_Spins_Horizontally%2C_Revealing_The_Contents_Of_All_Of_Its_Puzzle_Pieces_Without_Background.gif)")
            
            
            
    with tab3:
        st.subheader("Here are some guides for better understanding of the topic:")
        st.write(steps)

    with tab5:
        # st.subheader("Prompts for Image Visualization:")
        # st.write(prompts)
        st.subheader("Visual from the Highlights:")
        for url in images:
            display(Image(url=url))
            st.image(url, caption=titles, use_column_width=False)

    with tab6:
        st.subheader("Suggestion for Further Exploration:")
        st.write(explores)
    
    with tab7:
        st.subheader("Some Resources/References that Relative to the Topic:")
        st.write(resources)


# Run the Streamlit app
if __name__ == "__main__":
    main()
# %%
