# #导入模块
# import streamlit as st
# import os
# from openai import OpenAI
# import json
# from datetime import  datetime
#
# #页面设置
# st.set_page_config(
#     #设置网站标题
#     page_title="AI_Robot",
#     #网站图标
#     page_icon="💯",
#     #设置页面布局（宽度）
#     layout="wide",
#     #控制网站侧边栏状态
#     initial_sidebar_state="expanded",
#     #网站菜单栏
#     menu_items={}
# )
#
# #保存对话信息
# def save_session():
#     #构建对话信息对象
#     if st.session_state.current_session:
#         session_data = {
#             "session_title": st.session_state.current_session,
#             "nature": st.session_state.robot_nature,
#             "name": st.session_state.robot_name,
#             "message": st.session_state.message,
#         }
#
#         #如果sessions目录不存在则创建
#         if not os.path.exists("sessions"):
#             os.mkdir("sessions")
#
#         #以写的方式打开文件
#         #with关键字会自保证了程序一定会关闭打开的文件
#         with open(f"sessions/{st.session_state.current_session}.json","w",encoding="utf_8") as f:
#             #如果当前对话存在以json格式写入信息
#             json.dump(session_data,f,ensure_ascii=False,indent=2)
#
# #加载对话信息
# def get_session():
#     #存储对话标题的列表
#     session_list = []
#     if os.path.exists("sessions"):
#         #获取sessions文件夹下所有文件的文件名
#         file_list = os.listdir("sessions")
#         for file_name in file_list:
#             #判断文件名后缀是否为".json",我们仅需要获取".json"文件
#             if file_name.endswith(".json"):
#                 #切片去除后缀
#                 session_list.append(file_name[:-5])
#     session_list.sort(reverse=True)
#     return session_list
#
# #加载指定对话信息
# def load_session(session_name):
#     try:
#         if os.path.exists(f"sessions/{session_name}.json"):
#             # 指定文件存在，则打开
#             with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
#                 session_data = json.load(f)
#                 st.session_state.message = session_data["message"]
#                 st.session_state.robot_nature = session_data["nature"]
#                 st.session_state.robot_name = session_data["name"]
#                 st.session_state.current_session = session_name
#     except Exception:
#         st.error("加载对话失败！")
#
# #删除对话文件
# def delete_session(session_name):
#     try:
#         if os.path.exists(f"sessions/{session_name}.json"):
#             os.remove(f"sessions/{session_name}.json")
#             #如果删除的是当前对话，则清空消息列表
#             if session_name == st.session_state.current_session:
#                 st.session_state.message = []
#                 st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     except Exception:
#         st.error("删除对话失败！")
#
# #网站大标题
# st.title("AI_Robot")
#
# #设置网站logo
# st.logo("Resources/logo2023 (1).png")
#
# # 系统提示词
# system_set = """
#     你叫%s,你是用户的私人助手，请完全代入角色。
#         规则：
#             1、保持幽默感
#             2、禁止长篇大论
#             3、禁止通篇使用术语
#             4、回复要和用户像微信聊天一样
#             5、有需要时可以使用emoji表情
#         性格：
#             %s
#     你必须严格遵守以上规则。
# """
#
# #初始化聊天信息
# #此处用一个列表存储信息
# #列表中的每一个元素类型为dict，即{"role": "代表角色", "content": 对话内容}
# #st.session_state是一个字典可以用来缓存对话信息
# if "message" not in st.session_state:
#     #初始化为空列表
#     st.session_state.message = []
#
# #存储姓名
# if "robot_name" not in st.session_state:
#     st.session_state.robot_name = "小程"
#
# #存储性格
# if "robot_nature" not in st.session_state:
#     st.session_state.robot_nature = "幽默风趣,偶尔抽象,执着于当用户的大哥（用户生气会认怂，哄好后依然执着）"
#
# #当前对话标题
# if "current_session" not in st.session_state:
#     st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#
# #展示聊天信息
# st.text(f"对话名称：{st.session_state.current_session}")
# for message in st.session_state.message:
#     #判断对话内容属于哪一个角色
#     # if message["role"] == "user":
#     #     st.chat_message("user").write(message["content"])
#     # else:
#     #     st.chat_message("assistant").write(message["content"])
#
#     st.chat_message(message["role"]).write(message["content"]) #简化代码
#
# #创建与AI大模型交互的客户端
# client = OpenAI(
#     # DEEPSEEK_API_KEY 为调用大模型的API key
#     # 此处已经在系统环境变量中配置好
#     # 这种做法可以保护API不被泄露
#     api_key=os.environ.get('DEEPSEEK_API_KEY'),
#     base_url="https://api.deepseek.com")
#
# #添加侧边栏
# with st.sidebar:
#     st.subheader("对话管理")
#
#     # # 1. popover 是一个上下文管理器，点击按钮后展开面板
#     # with st.popover("✏️ 新建对话",use_container_width=True):
#     #
#     #     # 2. 在展开的面板里放置输入框
#     #     session_title = st.text_input("对话标题", placeholder="输入标题名称...")
#     #     if session_title:
#     #         st.session_state.current_session = session_title
#     #
#     #     # 3. 布局：创建两列让按钮并排
#     #     # col1, col2 = st.columns(2)
#     #
#     #     # with col1:
#     #     if st.button("创建", use_container_width=True):
#     #         if session_title:
#     #
#     #             #创建新对话
#     #             if st.session_state.message:
#     #                 # 保存当前对话
#     #                 save_session()
#     #
#     #                 st.session_state.message = []
#     #                 st.session_state.current_session = ""
#     #                 st.rerun()
#     #             else:
#     #                 st.write("你已经在新对话中了！",)
#     #         else:
#     #             st.error("请输入标题")
#     #
#     #     # with col2:
#     #     if st.button("取消", use_container_width=True):
#     #         st.rerun()  # 直接刷新关闭弹窗
#
#     # session_title = st.text_input("对话标题", placeholder="输入标题名称...")
#     # if session_title:
#     #     st.session_state.current_session = session_title
#
#
#     if st.button("新建对话",width="stretch",icon="✏️"):
#         #1、保存对话
#         save_session()
#
#         #2、创建新对话(if判断防止重复创建新对话)
#         if st.session_state.message:
#             st.session_state.message = []
#             st.session_state.current_session = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#             save_session()
#             st.rerun()
#         else:
#             st.write("你已经在新对话中了！")
#
#     #展示历史对话
#     st.subheader("历史对话")
#     #获取历史对话
#     session_list = get_session()
#     for session in session_list:
#         #在一行创建两个按钮，按钮所占区域4:1
#         col1, col2 = st.columns([4,1])
#         with col1:
#             #加载对话信息
#             if st.button(session,width="stretch",icon="📁",key=f"load_{session}",type="primary" if session == st.session_state.current_session else "secondary"):
#                 # #1、保存当前对话
#                 # if st.session_state.message:
#                 #     save_session()
#
#                 #2、加载历史对话信息
#                 load_session(session)
#                 st.rerun()
#
#         with col2:
#             #删除历史对话
#             if st.button("", icon="❌️", key=f"delete_{session}"):
#                 delete_session(session)
#                 st.rerun()
#
#     #分隔线
#     st.divider()
#
#     st.subheader("AI信息(可自定义)")
#     robot_name = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.robot_name)
#     if robot_name:
#         st.session_state.robot_name = robot_name
#     robot_nature = st.text_area("性格", placeholder="请输入性格", value=st.session_state.robot_nature)
#     if robot_nature:
#         print("+++++++",robot_nature)
#         st.session_state.robot_nature = robot_nature
#
# #消息输入框
# user_say = st.chat_input("说点什么吧：")
#
# if user_say:
#     #展示用户输入的内容
#     st.chat_message("user").write(user_say)
#     print("---------->调用大模型提示词：", user_say)
#     #保存用户输入提示词
#     st.session_state.message.append({"role": "user", "content": user_say})
#
#     #调用AI大模型
#     response = client.chat.completions.create(
#         #指明调用的大模型
#         model="deepseek-v4-flash",
#         messages=[
#             {"role": "system", "content": system_set % (robot_name, robot_nature)},
#             #解包将历史对话信息一并传递给大模型，使得大模型具备记忆功能
#             *st.session_state.message
#
#             #因为调用大模型前已将本次对话用户输入内容存入列表，所以下面一行代码可以注释掉，避免重复传入
#
#             #将用户输入的内容传递给大模型
#             # {"role": "user", "content": user_say},
#         ],
#         #控制流式输出和非流式输出
#         stream=True
#     )
#
#     # #展示大模型返回结果
#     #以下是非流式输出解析法方式
#     # st.chat_message("assistant").write(response.choices[0].message.content)
#     # print("---------->大模型返回结果：",response.choices[0].message.content)
#     #保存大模型返回结果（非流式输出）
#     # st.session_state.message.append({"role": "assistant","content":response.choices[0].message.content})
#
#     #流式输出解析方式
#     all_return = st.empty()
#     AI_return = ""
#     for ai in response:
#         if ai.choices[0].delta.content is not None:
#             ai_tmp = ai.choices[0].delta.content
#             AI_return += ai_tmp
#             all_return.chat_message("assistant").write(AI_return)
#     #保存流式输出返回结果
#     st.session_state.message.append({"role": "assistant","content":AI_return})
#
#     save_session()