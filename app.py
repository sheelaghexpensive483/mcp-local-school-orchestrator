import streamlit as st
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

st.set_page_config(page_title="School MCP Admin", page_icon="🏫")
st.title("🏫 Agentic School Administrator")

# --- ASYNC LOGIC ---


async def run_agent(user_query):
    # MCP Client Layer: Connect to Server
    # 1. Define Server Parameters (Path to our server.py)
    server_params = StdioServerParameters(command="python", args=["server.py"])
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 2. Load MCP Tools into LangChain format
            tools = await load_mcp_tools(session)

            # Orchestrator Layer: Local LLM + LangGraph
            # 3. Setup LLM & Graph Orchestrator
            model = ChatOllama(model="llama3.1", temperature=0)
            agent = create_react_agent(model, tools)

            # 4. Execute
            response = await agent.ainvoke({"messages": [("user", user_query)]})
            return response["messages"][-1].content

# --- UI INTERFACE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("e.g., Who is the top student in grade 10?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Querying School Systems..."):
            answer = asyncio.run(run_agent(prompt))
            st.write(answer)
            st.session_state.messages.append(
                {"role": "assistant", "content": answer})
