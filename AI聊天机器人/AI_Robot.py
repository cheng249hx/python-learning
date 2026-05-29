# #导入模块
# import streamlit as st
# import os
# from openai import OpenAI
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
# #展示聊天信息
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
#     st.header("Robot Message")
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
#         model="deepseek-chat",
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