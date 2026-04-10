"""
Generate a comprehensive PDF guide for the Adaptive RAG project.
Covers: Resume bullets, architecture, run guide, and interview prep.
"""

from fpdf import FPDF


class GuidePDF(FPDF):
    @staticmethod
    def safe(text):
        """Sanitize text for latin-1 encoding."""
        replacements = {
            "\u2013": "--", "\u2014": "--", "\u2018": "'", "\u2019": "'",
            "\u201c": '"', "\u201d": '"', "\u2022": "-", "\u2026": "...",
            "\u2192": "->", "\u2190": "<-", "\u2194": "<->",
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        return text.encode("latin-1", "replace").decode("latin-1")

    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "Adaptive RAG - Complete Project Guide & Interview Prep", align="C", new_x="LMARGIN", new_y="NEXT")
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title):
        self.ln(6)
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(30, 80, 160)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(30, 80, 160)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def sub_title(self, title):
        self.ln(3)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(50, 50, 50)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def sub_sub_title(self, title):
        self.ln(2)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(70, 70, 70)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, self.safe(text))
        self.ln(1)

    def bullet(self, text, indent=10):
        x = self.get_x()
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.set_x(x + indent)
        self.cell(5, 5.5, "-", new_x="END")
        self.multi_cell(0, 5.5, f"  {self.safe(text)}")
        self.ln(0.5)

    def code_block(self, text):
        self.set_font("Courier", "", 9)
        self.set_fill_color(240, 240, 240)
        self.set_text_color(30, 30, 30)
        self.set_draw_color(200, 200, 200)
        x = self.get_x() + 5
        w = self.w - 2 * self.l_margin - 10
        text = self.safe(text)
        lines = text.split("\n")
        h = 5 * len(lines) + 6
        if self.get_y() + h > self.h - 25:
            self.add_page()
        y_start = self.get_y()
        self.rect(x, y_start, w, h, style="FD")
        self.ln(3)
        for line in lines:
            self.set_x(x + 3)
            self.cell(0, 5, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def table_row(self, cols, widths, bold=False, fill=False):
        style = "B" if bold else ""
        self.set_font("Helvetica", style, 9)
        if fill:
            self.set_fill_color(220, 230, 245)
        else:
            self.set_fill_color(255, 255, 255)
        self.set_text_color(30, 30, 30)
        row_h = 7
        for i, col in enumerate(cols):
            self.cell(widths[i], row_h, self.safe(str(col)), border=1, fill=True)
        self.ln(row_h)

    def qa_block(self, question, answer):
        if self.get_y() > 240:
            self.add_page()
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(30, 80, 160)
        self.multi_cell(0, 5.5, self.safe(f"Q: {question}"))
        self.ln(1)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 5.5, self.safe(f"A: {answer}"))
        self.ln(4)


def build_pdf():
    pdf = GuidePDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # =========================================================================
    # TITLE PAGE
    # =========================================================================
    pdf.ln(30)
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(30, 80, 160)
    pdf.cell(0, 15, "Adaptive RAG", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 16)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "Agentic AI Chatbot with Dynamic Query Routing", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 10, "Complete Project Guide, Run Instructions & Interview Prep", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(20)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "Tech Stack: LangGraph | LangChain | FastAPI | OpenAI GPT-4o | FAISS/Qdrant | MongoDB | Streamlit | Tavily", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.cell(0, 8, "Generated: March 2026", align="C", new_x="LMARGIN", new_y="NEXT")

    # =========================================================================
    # TABLE OF CONTENTS
    # =========================================================================
    pdf.add_page()
    pdf.section_title("TABLE OF CONTENTS")
    toc = [
        "1. Resume Bullet Points (Copy-Paste Ready)",
        "2. Architecture Deep-Dive",
        "    2.1 The Graph Flow (Core Pipeline)",
        "    2.2 Node-by-Node Breakdown",
        "    2.3 State Schema",
        "3. How to Run the Project",
        "    3.1 Prerequisites",
        "    3.2 Step-by-Step Setup",
        "    3.3 Testing with cURL",
        "4. Interview Questions & Answers (15 Questions)",
        "5. Key Technologies Reference Table",
        "6. Things to Be Honest About in Interviews",
    ]
    for item in toc:
        pdf.set_font("Helvetica", "", 11)
        pdf.set_text_color(30, 30, 30)
        pdf.cell(0, 7, item, new_x="LMARGIN", new_y="NEXT")

    # =========================================================================
    # 1. RESUME BULLET POINTS
    # =========================================================================
    pdf.add_page()
    pdf.section_title("1. RESUME BULLET POINTS (Copy-Paste Ready)")
    pdf.body_text("Project Title: Adaptive RAG -- Agentic AI Chatbot with Dynamic Query Routing")
    pdf.ln(2)

    bullets = [
        "Built an end-to-end Agentic RAG system using LangGraph, LangChain, FastAPI, and Streamlit that dynamically routes user queries across 3 pipelines: indexed document retrieval, general LLM, and real-time web search (Tavily).",
        "Designed a LangGraph state machine with 7 nodes (query classification, retrieval, grading, rewriting, generation, web search, general LLM) and conditional edges for adaptive workflow orchestration.",
        "Implemented a ReAct (Reasoning + Acting) agent with tool-based document retrieval using FAISS/Qdrant vector stores with OpenAI embeddings for semantic search.",
        "Engineered self-corrective RAG with automated relevance grading (LLM-as-judge), query rewriting on low scores, and answer faithfulness verification to ensure hallucination-free responses.",
        "Built async chat memory with MongoDB (Motor) for persistent session-based conversation history, and a Streamlit UI with document upload (PDF/TXT), real-time chat, and authentication.",
        "Leveraged GPT-4o with structured outputs (Pydantic models) for query classification, grading, and verification -- ensuring type-safe, deterministic LLM outputs.",
    ]
    for b in bullets:
        b = b.replace("\u2013", "--").replace("\u2014", "--")
        pdf.bullet(b)
    for b in bullets:
        pdf.bullet(b)

    # =========================================================================
    # 2. ARCHITECTURE DEEP-DIVE
    # =========================================================================
    pdf.add_page()
    pdf.section_title("2. ARCHITECTURE DEEP-DIVE")

    pdf.sub_title("2.1 The Graph Flow (Core Pipeline)")
    pdf.body_text("This is the CORE of the project. Know this flow cold for interviews:")
    pdf.code_block(
        'User Query\n'
        '    |\n'
        '[1] query_analysis  ->  Classifies query as "index" | "general" | "search"\n'
        '    | (conditional edge via routing_tool)\n'
        '    |-- "index"   -> [2] retriever -> [3] grade -> (conditional via doc_tool)\n'
        '    |                                    |-- score="yes" -> [5] generate -> END\n'
        '    |                                    |-- score="no"  -> [4] rewrite -> [2] retriever (loop)\n'
        '    |-- "general" -> [7] general_llm -> END\n'
        '    |-- "search"  -> [6] web_search -> [5] generate -> END'
    )

    pdf.sub_title("2.2 Node-by-Node Breakdown")

    widths = [30, 75, 85]
    pdf.table_row(["Node", "What It Does", "Key Technology"], widths, bold=True, fill=True)
    nodes = [
        ["query_analysis", "Retrieves context from FAISS, uses LLM structured output (RouteIdentifier) to classify", "llm.with_structured_output(), PromptTemplate"],
        ["retriever", "ReAct agent calls retriever tool against FAISS vector store", "create_react_agent, AgentExecutor, create_retriever_tool"],
        ["grade", "LLM evaluates if retrieved docs are relevant - returns yes/no", "Grade Pydantic model, structured output"],
        ["rewrite", "LLM rewrites the query for better retrieval results", "PromptTemplate chain"],
        ["generate", "LLM generates a final readable answer from the context", "PromptTemplate chain"],
        ["web_search", "Uses Tavily API for real-time web search", "TavilySearchResults"],
        ["general_llm", "Direct LLM call for general knowledge questions", "ChatOpenAI (GPT-4o)"],
    ]
    for row in nodes:
        pdf.table_row(row, widths)

    pdf.sub_title("2.3 State Schema")
    pdf.code_block(
        'class State(TypedDict):\n'
        '    messages: Annotated[list[AnyMessage], add_messages]  # Chat history (reducer)\n'
        '    binary_score: Optional[str]      # "yes" or "no" from grading\n'
        '    route: Optional[str]             # "index", "general", or "search"\n'
        '    latest_query: Optional[str]      # Current/rewritten query'
    )
    pdf.body_text("The add_messages reducer appends new messages instead of replacing -- critical for accumulating conversation history across nodes.")

    # =========================================================================
    # 3. HOW TO RUN
    # =========================================================================
    pdf.add_page()
    pdf.section_title("3. HOW TO RUN THE PROJECT")

    pdf.sub_title("3.1 Prerequisites")
    pdf.bullet("Python 3.9+")
    pdf.bullet("MongoDB running locally (or cloud Atlas URI)")
    pdf.bullet("OpenAI API key (for GPT-4o)")
    pdf.bullet("Tavily API key (for web search)")
    pdf.bullet("(Optional) Qdrant for production vector store")

    pdf.sub_title("3.2 Step-by-Step Setup")

    pdf.sub_sub_title("Step 1: Clone & Virtual Environment")
    pdf.code_block(
        'git clone https://github.com/mohit5075/Adaptive-Rag.git\n'
        'cd Adaptive-Rag\n'
        'python -m venv venv\n'
        'source venv/bin/activate\n'
        'pip install -r requirements.txt'
    )

    pdf.sub_sub_title("Step 2: Create .env file in project root")
    pdf.code_block(
        'OPENAI_API_KEY=sk-your-key-here\n'
        'TAVILY_API_KEY=tvly-your-key-here\n'
        'QDRANT_URL=http://localhost:6333\n'
        'QDRANT_API_KEY=your-qdrant-key\n'
        'QDRANT_CODE_COLLECTION=code_documents\n'
        'QDRANT_DOCS_COLLECTION=documents\n'
        'MONGODB_URL=mongodb://localhost:27017\n'
        'MONGODB_DB_NAME=adaptive_rag'
    )

    pdf.sub_sub_title("Step 3: Start MongoDB")
    pdf.code_block('brew services start mongodb-community   # macOS')

    pdf.sub_sub_title("Step 4: Start FastAPI Backend (Terminal 1)")
    pdf.code_block('python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000')

    pdf.sub_sub_title("Step 5: Start Streamlit Frontend (Terminal 2)")
    pdf.code_block('streamlit run streamlit_app/home.py')

    pdf.sub_sub_title("Step 6: Access the Application")
    pdf.bullet("Chat UI: http://localhost:8501")
    pdf.bullet("API Docs (Swagger): http://localhost:8000/docs")
    pdf.bullet("API Docs (ReDoc): http://localhost:8000/redoc")

    pdf.sub_title("3.3 Testing with cURL")
    pdf.sub_sub_title("Upload a Document")
    pdf.code_block(
        'curl -X POST http://localhost:8000/rag/documents/upload \\\n'
        '  -H "X-Description: My Python tutorial document" \\\n'
        '  -F "file=@document.pdf"'
    )
    pdf.sub_sub_title("Query the RAG System")
    pdf.code_block(
        'curl -X POST http://localhost:8000/rag/query \\\n'
        '  -H "Content-Type: application/json" \\\n'
        '  -d \'{"query": "What is Python?", "session_id": "user_123"}\''
    )

    # =========================================================================
    # 4. INTERVIEW Q&A
    # =========================================================================
    pdf.add_page()
    pdf.section_title("4. INTERVIEW QUESTIONS & ANSWERS")

    qa_pairs = [
        (
            "Explain your project in 2 minutes.",
            "I built an Adaptive RAG system -- an AI chatbot that intelligently routes user queries through different pipelines. When a user asks a question, the system first retrieves context from a vector store, then uses an LLM to classify the query into three categories: 'index' for questions answerable from uploaded documents, 'general' for common knowledge, and 'search' for real-time web queries. For document-based queries, it uses a ReAct agent with FAISS vector search, then grades the retrieved results for relevance. If the results aren't good enough, it automatically rewrites the query and retries -- this is the self-corrective loop. The whole workflow is orchestrated as a state machine using LangGraph with conditional edges. I used FastAPI for the backend, Streamlit for the UI, MongoDB for chat history, and OpenAI GPT-4o for all LLM operations with Pydantic structured outputs."
        ),
        (
            "What is RAG and why did you need it?",
            "RAG stands for Retrieval-Augmented Generation. LLMs have a knowledge cutoff and can't access private data. RAG solves this by first retrieving relevant documents from a knowledge base, then feeding them as context to the LLM to generate grounded answers. In my project, users upload PDFs/TXTs, which get chunked, embedded, and stored in a FAISS vector store. When they ask questions, the retriever fetches relevant chunks, and the LLM generates answers based on that context -- reducing hallucination."
        ),
        (
            "What is LangGraph and why did you choose it over LangChain's basic chains?",
            "LangGraph is a framework for building stateful, multi-actor workflows as directed graphs. Unlike basic LangChain chains which are linear (A->B->C), LangGraph supports conditional edges, loops, and state management. I needed it because my pipeline has branching logic (3 different routes based on query classification) and a retry loop (if grading fails, rewrite query and re-retrieve). LangGraph's StateGraph with add_conditional_edges made this natural to implement."
        ),
        (
            "Explain the ReAct pattern you used.",
            "ReAct stands for Reasoning + Acting. The agent follows a Thought -> Action -> Observation loop. In my retriever node, the ReAct agent reasons about what tool to use (the retriever tool), calls it, observes the results, and then formulates a final answer. I used LangChain's create_react_agent with an AgentExecutor that has max_iterations=2 and handle_parsing_errors=True for robustness. The agent has a single tool -- the document retriever -- and the prompt template follows the standard ReAct format."
        ),
        (
            "How does query classification work?",
            "The query_classifier node first retrieves some context from the vector store for the incoming question. Then it sends both the question and the context to GPT-4o with a structured output schema (RouteIdentifier Pydantic model). The LLM classifies into: 'index' if the context is relevant, 'general' if it's a casual/common knowledge question, or 'search' if it needs real-time external data. The classification prompt has clear priority rules -- always prefer 'index' when context is relevant."
        ),
        (
            "What is structured output and why did you use it?",
            "Structured output means constraining the LLM to return a specific JSON schema instead of free-form text. I used llm.with_structured_output(PydanticModel) for three critical decisions: (1) RouteIdentifier for query classification, (2) Grade for relevance scoring (binary yes/no), and (3) VerificationResult for answer faithfulness checking. This ensures deterministic, parseable responses and eliminates the need for fragile regex parsing of LLM output."
        ),
        (
            "How does the self-corrective loop work?",
            "After the retriever fetches documents, the grade node evaluates their relevance using an LLM-as-judge pattern. If the grade is 'yes', we proceed to generate the final answer. If 'no', the doc_tool conditional edge routes to the rewrite node, which uses the LLM to rephrase the query for better retrieval. The rewritten query then goes back to the retriever. This creates a feedback loop that improves answer quality."
        ),
        (
            "How do you store and manage chat history?",
            "I use MongoDB with Motor (async driver) for persistent chat history. Each message is stored with session_id, type (human/ai), content, and timestamp. The ChatHistory class implements LangChain's BaseChatMessageHistory interface. When a query comes in, I load all messages for that session, pass them to the graph, and after getting a response, I save the AI message back. This gives full conversation context across sessions."
        ),
        (
            "How does document upload work end-to-end?",
            "User uploads a PDF/TXT through the Streamlit sidebar or API. The file is validated, loaded using PyPDFLoader or TextLoader, then split into chunks (1000 chars, 150 overlap) using RecursiveCharacterTextSplitter. The document description is enhanced by the LLM to create a better retriever tool instruction. Chunks are embedded with OpenAI embeddings and stored in a FAISS vector store. The retriever tool is dynamically configured with the enhanced description so the ReAct agent knows what the documents are about."
        ),
        (
            "What's the difference between FAISS and Qdrant in your project?",
            "The codebase supports both. Qdrant is the production-grade vector database (client-server, persistent, scalable), and FAISS is the in-memory alternative used for development. Currently, FAISS is the active backend -- it's initialized with a dummy document on startup and replaced when real documents are uploaded. The Qdrant code is commented out but ready to switch by uncommenting a few lines in retriever_setup.py."
        ),
        (
            "What happens if no documents are uploaded and a user queries?",
            "The system still works. The query_classifier retrieves context from FAISS, which at that point only has a placeholder document saying 'No documents uploaded yet'. The classifier sees the context is irrelevant and routes the query to either 'general' (LLM answers from knowledge) or 'search' (Tavily web search). So the system gracefully degrades."
        ),
        (
            "What is the add_messages reducer in State?",
            "In LangGraph, state fields can have reducers that define how updates are merged. add_messages is a built-in reducer that appends new messages to the existing list instead of replacing it. This is critical because different nodes add their own messages (human queries, AI responses, tool results), and we need to accumulate them all in the conversation history."
        ),
        (
            "Why FastAPI + Streamlit? Why not just one?",
            "Separation of concerns. FastAPI handles the business logic, RAG pipeline, and serves as a clean REST API that any client can consume. Streamlit is just one possible frontend. This API-first architecture means I could easily add a React frontend, mobile app, or integrate with Slack/Teams without touching the backend. FastAPI also gives me async support, automatic OpenAPI docs, and Pydantic validation for free."
        ),
        (
            "How would you scale this for production?",
            "Several improvements: (1) Switch from FAISS to Qdrant/Pinecone for persistent, distributed vector storage. (2) Add Redis caching for frequent queries. (3) Use Uvicorn with multiple workers or deploy behind Gunicorn. (4) Containerize with Docker + docker-compose. (5) Add rate limiting and authentication middleware. (6) Use connection pooling for MongoDB. (7) Implement streaming responses for better UX. (8) Add observability with LangSmith for tracing LLM calls."
        ),
        (
            "What are the chunking parameters and why?",
            "I use RecursiveCharacterTextSplitter with chunk_size=1000 and chunk_overlap=150. 1000 characters is roughly 200-250 tokens -- small enough for precise retrieval but large enough to contain meaningful context. The 150-char overlap (15%) ensures that concepts split across chunk boundaries still appear in at least one complete chunk, preventing information loss at boundaries."
        ),
    ]

    for i, (q, a) in enumerate(qa_pairs, 1):
        pdf.qa_block(f"{i}. {q}", a)

    # =========================================================================
    # 5. KEY TECHNOLOGIES
    # =========================================================================
    pdf.add_page()
    pdf.section_title("5. KEY TECHNOLOGIES REFERENCE")

    widths_tech = [35, 55, 100]
    pdf.table_row(["Technology", "Where Used", "Why It Matters"], widths_tech, bold=True, fill=True)
    techs = [
        ["LangGraph", "Workflow orchestration", "State machines for AI, conditional routing, loops"],
        ["LangChain", "LLM chains, tools, agents", "Industry-standard LLM framework"],
        ["FastAPI", "Backend REST API", "Async, auto-docs, Pydantic integration"],
        ["OpenAI GPT-4o", "All LLM calls", "Structured outputs, function calling"],
        ["FAISS/Qdrant", "Vector store", "Semantic similarity search on embeddings"],
        ["MongoDB+Motor", "Chat history", "Async persistent session storage"],
        ["Streamlit", "Frontend UI", "Rapid prototyping, file upload widget"],
        ["Tavily", "Web search", "Real-time information retrieval"],
        ["Pydantic", "Data models", "Type safety, structured LLM outputs"],
        ["ReAct Agent", "Document retrieval", "Reasoning + Acting agentic pattern"],
    ]
    for row in techs:
        pdf.table_row(row, widths_tech)

    # =========================================================================
    # 6. HONESTY POINTS
    # =========================================================================
    pdf.add_page()
    pdf.section_title("6. THINGS TO BE HONEST ABOUT IN INTERVIEWS")
    pdf.body_text("Interviewers appreciate self-awareness. Here are limitations to acknowledge proactively:")
    pdf.ln(3)

    honest_points = [
        "FAISS is in-memory -- data is lost on restart. Mention you'd use Qdrant/Pinecone in production for persistent vector storage.",
        "No streaming -- responses come all at once. You'd add SSE (Server-Sent Events) or WebSocket streaming for better UX.",
        "Single-document paradigm -- uploading a new document replaces the old FAISS store. No multi-document persistence currently.",
        "The Rust auth service (localhost:8080) is a separate dependency for Streamlit login. The core RAG system works independently without it.",
        "No unit tests yet -- mention you'd add pytest with mocked LLM calls for CI/CD.",
    ]
    for p in honest_points:
        pdf.bullet(p)

    pdf.ln(10)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(30, 80, 160)
    pdf.cell(0, 10, "Good luck with your interviews! You've got this!", align="C", new_x="LMARGIN", new_y="NEXT")

    # Save
    output_path = "/Users/in04361/Documents/Adaptive-Rag/Adaptive-Rag/Adaptive_RAG_Interview_Guide.pdf"
    pdf.output(output_path)
    return output_path


if __name__ == "__main__":
    path = build_pdf()
    print(f"PDF generated successfully at: {path}")
