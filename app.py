import streamlit as st
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

st.set_page_config(page_title="School MCP Admin", page_icon="🏫")
st.title("🏫 Agentic School Administrator")


async def run_agent(user_query):
    # MCP Client Layer: Connect to Server
    server_params = StdioServerParameters(command="python", args=["server.py"])
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)

            # Orchestrator Layer: Local LLM + LangGraph
            model = ChatOllama(model="llama3.1", temperature=0)
            agent = create_react_agent(model, tools)
            response = await agent.ainvoke({"messages": [("user", user_query)]})
            return response["messages"][-1].content

if prompt := st.chat_input("Ask about students or generate a report..."):
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        res = asyncio.run(run_agent(prompt))
        st.write(res)
