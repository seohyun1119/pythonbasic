import streamlit as st
from streamlit_chat import message  # python 3.8 이상  # 웹 연결해줌 
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

@st.cache(allow_output_mutation=True)  # 결과값 바뀌게 만듦 
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model   # 딜레이를 방지하기 위해 모델 한 번만 로드 

@st.cache(allow_output_mutation=True)
def get_dataset():
    df = pd.read_csv('C:/dev/github/pythonbasic/mental-health-chatbot/wellness_dataset.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header('챗봇 by 짱돌')

if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # 챗봇이 대화한 내용 저장 

if 'past' not in st.session_state:
    st.session_state['past'] = []  # 내가 대화한 내용을 저장
    print(f"past: {len(st.session_state['past'])}")
    # streamlit이 자동으로 재실행되어도 초기화되지 않는 변수 

with st.form('form', clear_on_submit=True): # form 만듦 
    user_input = st.text_input('당신: ', key= ['past'])
    submitted = st.form_submit_button('전송')  # submit 버튼 누르면 텍스트를 지울 수 있음 

if submitted and user_input:
    embedding = model.encode(user_input)

    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze())
    answer = df.loc[df['distance'].idxmax()]

    st.session_state.past.append(user_input)  # user가 입력한 문장 저장 
    st.session_state.generated.append(answer['챗봇'])  # 챗봇의 답변 저장

for i in range(len(st.session_state['past'])):
    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
    if len(st.session_state['generated']) > i:
        message(st.session_state['generated'][i], key=str(i) + '_bot')