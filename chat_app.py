import streamlit as st
from model import MyAIBot
from dotenv import load_dotenv

load_dotenv()

st.title("ChatGPT like Chat Bot")

# Initialize connection.
conn = st.connection('mysql', type='sql')


# Set OpenAI API key from Streamlit secrets
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model
if "my_bot" not in st.session_state:
    st.session_state["my_bot"] = MyAIBot("My Bot")


# Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages:list[dict[str,str]] = []


# Display chat messages from history on app return
for message in st.session_state.my_bot.get_messages():
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What's up?"):
    # Add user message to char history
    # st.session_state.messages.append({
    #     "role": "user",
    #     "content": prompt
    # })
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in char message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response:str = ""
        for response in st.session_state.my_bot.send_message({"role":"user", "content": prompt}):
            full_response += response.choices[0].delta.content or ""
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        
    st.session_state.my_bot.save_chat_history({"role": "assistant", "content": full_response})
        


        # for response in client.chat.completions.create(
        #     model=st.session_state["openai_model"],
        #     messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages], 
        #     stream=True,
        # ):
        #     full_response += (response.choices[0].delta.content or "")
        # assistant_response:list[str] = random.choice(
        #     [
        #      "Hello there! How can I help you today?",
        #      "Hi, human! Is there anything I can help you with?",
        #      "Do you need help?",
        #     ]
        # )
        # # Simulate stream of response with miliseconds delay
        # for chunk in assistant_response.split():
        #     full_response += chunk + " "
        #     time.sleep(0.05)
        #     # Add a blinking cursor to simulate typing
        #     message_placeholder.markdown(full_response + "▌")
        # message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    # st.session_state.messages.append({
    #     "role": "assistant",
    #     "content": full_response
    # })