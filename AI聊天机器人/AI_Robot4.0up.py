import streamlit as st
import os
from openai import OpenAI
import json
from datetime import datetime

# 页面设置
st.set_page_config(
    page_title="AI_Robot",
    page_icon="💯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 常量定义
SESSIONS_DIR = "sessions"
SYSTEM_PROMPT_TEMPLATE = """
你叫{name}，你是用户的私人助手，请完全代入角色。
规则：
    1、保持幽默感
    2、禁止长篇大论
    3、禁止通篇使用术语
    4、回复要和用户像微信聊天一样
    5、有需要时可以使用emoji表情
性格：
    {nature}
你必须严格遵守以上规则。
"""


# 初始化会话状态
def init_session_state():
    """初始化所有会话状态变量"""
    defaults = {
        "message": [],
        "robot_name": "小程",
        "robot_nature": "幽默风趣,偶尔抽象,执着于当用户的大哥（用户生气会认怂，哄好后依然执着）",
        "current_session": datetime.now().strftime("%Y-%m-%d_%H-%M-%S"),
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# 文件操作相关函数
def ensure_sessions_dir():
    """确保会话目录存在"""
    os.makedirs(SESSIONS_DIR, exist_ok=True)


def save_session():
    """保存当前会话"""
    if not st.session_state.current_session:
        return

    session_data = {
        "session_title": st.session_state.current_session,
        "nature": st.session_state.robot_nature,
        "name": st.session_state.robot_name,
        "message": st.session_state.message,
    }

    ensure_sessions_dir()
    file_path = os.path.join(SESSIONS_DIR, f"{st.session_state.current_session}.json")

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        st.error(f"保存对话失败：{str(e)}")


def get_sessions():
    """获取所有历史会话列表"""
    session_list = []
    if os.path.exists(SESSIONS_DIR):
        for file_name in os.listdir(SESSIONS_DIR):
            if file_name.endswith(".json"):
                session_list.append(file_name[:-5])
    return sorted(session_list, reverse=True)


def load_session(session_name):
    """加载指定会话"""
    file_path = os.path.join(SESSIONS_DIR, f"{session_name}.json")

    if not os.path.exists(file_path):
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            session_data = json.load(f)
            st.session_state.message = session_data.get("message", [])
            st.session_state.robot_nature = session_data.get("nature", st.session_state.robot_nature)
            st.session_state.robot_name = session_data.get("name", st.session_state.robot_name)
            st.session_state.current_session = session_name
    except Exception:
        st.error("加载对话失败！")


def delete_session(session_name):
    """删除指定会话"""
    file_path = os.path.join(SESSIONS_DIR, f"{session_name}.json")

    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            if session_name == st.session_state.current_session:
                st.session_state.message = []
                st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    except Exception:
        st.error("删除对话失败！")


def create_new_session():
    """创建新会话"""
    if not st.session_state.message:
        return

    save_session()
    st.session_state.message = []
    st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


# AI交互函数
def get_ai_client():
    """获取AI客户端"""
    api_key = os.environ.get('DEEPSEEK_API_KEY')
    if not api_key:
        st.error("未找到API密钥，请设置DEEPSEEK_API_KEY环境变量")
        st.stop()

    return OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )


def call_ai_model(client, messages):
    """调用AI模型并返回流式响应"""
    return client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=messages,
        stream=True
    )


def process_ai_response(response):
    """处理AI流式响应"""
    all_return = st.empty()
    AI_return = ""

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            ai_tmp = chunk.choices[0].delta.content
            AI_return += ai_tmp
            all_return.chat_message("assistant").write(AI_return)

    return AI_return


# 主程序
def main():
    # 初始化
    init_session_state()

    # 页面标题和logo
    st.title("AI_Robot")
    if os.path.exists("Resources/logo2023 (1).png"):
        st.logo("Resources/logo2023 (1).png")

    # 侧边栏
    with st.sidebar:
        st.subheader("对话管理")

        if st.button("新建对话", use_container_width=True, icon="✏️"):
            create_new_session()
            st.rerun()

        # 历史对话列表
        sessions = get_sessions()
        for session in sessions:
            col1, col2 = st.columns([4, 1])

            with col1:
                button_type = "primary" if session == st.session_state.current_session else "secondary"
                if st.button(
                        session,
                        use_container_width=True,
                        icon="📁",
                        key=f"load_{session}",
                        type=button_type
                ):
                    load_session(session)
                    st.rerun()

            with col2:
                if st.button("", icon="❌️", key=f"delete_{session}"):
                    delete_session(session)
                    st.rerun()

        st.divider()

        # AI信息设置
        st.subheader("AI信息(可自定义)")

        new_name = st.text_input(
            "昵称",
            placeholder="请输入昵称",
            value=st.session_state.robot_name
        )
        if new_name != st.session_state.robot_name:
            st.session_state.robot_name = new_name

        new_nature = st.text_area(
            "性格",
            placeholder="请输入性格",
            value=st.session_state.robot_nature
        )
        if new_nature != st.session_state.robot_nature:
            st.session_state.robot_nature = new_nature

    # 显示当前对话信息
    st.text(f"对话名称：{st.session_state.current_session}")

    # 显示历史消息
    for message in st.session_state.message:
        st.chat_message(message["role"]).write(message["content"])

    # 用户输入处理
    user_input = st.chat_input("说点什么吧：")

    if user_input:
        # 显示用户消息
        st.chat_message("user").write(user_input)
        st.session_state.message.append({"role": "user", "content": user_input})

        try:
            # 获取AI客户端
            client = get_ai_client()

            # 准备消息
            system_prompt = SYSTEM_PROMPT_TEMPLATE.format(
                name=st.session_state.robot_name,
                nature=st.session_state.robot_nature
            )

            messages = [
                {"role": "system", "content": system_prompt},
                *st.session_state.message
            ]

            # 调用AI模型
            response = call_ai_model(client, messages)

            # 处理响应
            ai_response = process_ai_response(response)

            # 保存AI响应
            if ai_response:
                st.session_state.message.append({"role": "assistant", "content": ai_response})
                save_session()

        except Exception as e:
            st.error(f"AI调用失败：{str(e)}")


if __name__ == "__main__":
    main()