# LLM-und-tool.py
import subprocess
import os 
from langchain_ollama import ChatOllama
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# ----------------------------------------------------
# 1. Die Tools
# ----------------------------------------------------
@tool
def get_cpu_temperature() -> str:
    """Ruft die aktuelle CPU-Temperatur des Raspberry Pi ab (z.B. 'temp=60.1'C'). 
    Wird nur verwendet, um Fragen zur Hardware-Temperatur zu beantworten."""
    try:
        # Führt den Linux-Befehl aus
        result = subprocess.run(
            ['vcgencmd', 'measure_temp'], 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"FEHLER beim Abrufen der Temperatur: {e}"

# ----------------------------------------------------
# 2. Agenten-Setup
# ----------------------------------------------------

# Empfehlung: Nutze das offizielle Llama 3 8B Instruct Tag für beste Ergebnisse
#OLLAMA_MODEL = "llama3:8b" 
# Falls du dein spezifisches Modell nutzen willst:
#OLLAMA_MODEL ='ministral-3:8b-instruct-2512-q4_K_M'
OLLAMA_MODEL ='qwen2.5:1.5b'
REMOTE_URL='http://localhost:11434'

#llm = ChatOllama(model=OLLAMA_MODEL) 
llm = ChatOllama(
    model=OLLAMA_MODEL,
    base_url=REMOTE_URL
)


# 💡 KORREKTUR: STRENGES DEUTSCHES SYSTEM-PROMPT
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Du bist ein technisches System-Interface. Deine Regeln:\n"
            "1. Antworte IMMER nur auf Deutsch.\n"
            "2. Wenn du ein Tool nutzt, gib danach NUR das Ergebnis in einem kurzen Satz aus.\n"
            "3. Schreibe NIEMALS Erklärungen über dein Vorgehen (wie 'Ich habe kein Tool genutzt').\n"
            "4. Sei extrem präzise und kurz angebunden."

        ),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
        ("human", "{input}"),
    ]
)

tools = [get_cpu_temperature]
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# ----------------------------------------------------
# 3. Ausführung
# ----------------------------------------------------
if __name__ == "__main__":
    print("-" * 50)
    print(f"Agenten-Start mit Modell: {OLLAMA_MODEL}")
    print("-" * 50)

    # Test 1: Tool-Nutzung erforderlich (Muss zusammenfassen)
    print("\n--- Test 1: Tool-Nutzung (Temperatur) ---")
    try:
        agent_executor.invoke({
            "input": "Wie warm ist die CPU momentan?"
        }) 
    except Exception as e:
        print(f"\n[INFO] Agent konnte die Aufgabe möglicherweise nicht beenden. Fehler: {e}")
    
    print("\n" + "=" * 50 + "\n")

    # Test 2: Nur Textantwort (Muss Deutsch sprechen und kein Tool aufrufen)
    print("--- Test 2: Nur Textantwort (Hauptstadt) ---")
    agent_executor.invoke({
        "input": "Was ist die Hauptstadt von Polen?"
    })
    
    print("-" * 50)

# powerd by ai
#EOF



