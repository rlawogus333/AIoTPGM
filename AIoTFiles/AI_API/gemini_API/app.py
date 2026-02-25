import streamlit as st
from google import genai
import os
import json
from dotenv import load_dotenv
from datetime import datetime

# .env 파일에서 API 키 로드
load_dotenv()

# Gemini 클라이언트 설정
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 파일 경로 설정
LOG_FILE = "chat_history_log.json"

# --- 함수: 대화 내역 저장 및 불러오기 ---
def load_data():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# --- 세션 상태 초기화 ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = load_data()

st.set_page_config(page_title="Gemini AI Chatbot", layout="wide")

# --- 사이드바: 대화 목록 관리 ---
with st.sidebar:
    st.title("📂 대화 히스토리")
    if st.button("🗑️ 전체 내역 삭제"):
        st.session_state.chat_history = []
        save_data([])
        st.rerun()
    
    st.divider()
    st.info("대화 내용은 자동으로 파일에 저장됩니다.")
    
    # 저장된 기록이 있을 경우 간략하게 표시
    if st.session_state.chat_history:
        st.write("최근 질문 목록:")
        for i, msg in enumerate(st.session_state.chat_history[-10:]): # 최근 10개만 표시
            if msg["role"] == "user":
                st.text(f"{i+1}. {msg['content'][:15]}...")

# --- 메인 화면 UI ---
st.title("🤖 기억력 있는 AI 챗봇")
st.caption("이전 대화를 기억하며, 모든 대화는 파일로 기록됩니다.")

# 상단에 초기화 버튼 배치
col1, col2 = st.columns([8, 2])
with col2:
    if st.button("화면 비우기"):
        # 파일은 남겨두고 현재 화면(세션)만 비우고 싶을 때 사용
        st.session_state.chat_history = []
        st.rerun()

# --- 이전 대화 내역 출력 ---
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- 채팅 입력 및 처리 ---
if prompt := st.chat_input("메시지를 입력하세요..."):
    # 1. 사용자 입력 표시 및 저장
    with st.chat_message("user"):
        st.write(prompt)
    
    # 시간 정보를 포함하여 저장 가능 (선택 사항)
    user_entry = {"role": "user", "content": prompt, "timestamp": str(datetime.now())}
    st.session_state.chat_history.append(user_entry)

    # 2. AI 응답 생성
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("생각 중...")
        
        try:
            # 전체 히스토리를 전달하여 문맥 유지
            chat = client.chats.create(
                model="gemini-2.0-flash", 
                history=[{"role": m["role"], "content": m["content"]} for m in st.session_state.chat_history[:-1]]
            )
            
            response = chat.send_message(prompt)
            full_response = response.text
            
            # 화면 업데이트 및 저장
            message_placeholder.markdown(full_response)
            ai_entry = {"role": "assistant", "content": full_response, "timestamp": str(datetime.now())}
            st.session_state.chat_history.append(ai_entry)
            
            # 3. 파일에 영구 저장
            save_data(st.session_state.chat_history)
            
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")