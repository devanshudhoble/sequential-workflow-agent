from google.adk.agents import LlmAgent
from google.adk.agents import LlmAgent, SequentialAgent


MODEL = "groq/llama-3.1-8b-instant"

# -------------------------------
# Code Writer Agent
# -------------------------------
code_writer_agent = LlmAgent(
    name="CodeWriterAgent",
    model=MODEL,
    instruction=(
        "You are a Python code generator.\n"
        "Based only on the user's request, generate correct Python code.\n"
        "Output only Python code."
    ),
    output_key="generated_code"
)

# -------------------------------
# Code Reviewer Agent
# -------------------------------
code_reviewer_agent = LlmAgent(
    name="CodeReviewerAgent",
    model=MODEL,
    instruction=(
        "You are a Python code reviewer.\n"
        "Review the following code for correctness, readability, and best practices:\n\n"
        "{generated_code}\n\n"
        "Provide concise review comments."
    ),
    output_key="review_comments"
)

# -------------------------------
# Code Refactorer Agent
# -------------------------------
code_refactorer_agent = LlmAgent(
    name="CodeRefactorerAgent",
    model=MODEL,
    instruction=(
        "You are a Python code refactorer.\n"
        "Refactor the code based on the review comments.\n\n"
        "Original Code:\n{generated_code}\n\n"
        "Review Comments:\n{review_comments}\n\n"
        "Return improved Python code only."
    ),
    output_key="refactored_code"
)

# -------------------------------
# Sequential Workflow Agent
# -------------------------------
code_pipeline_agent = SequentialAgent(
    name="CodePipelineAgent",
    sub_agents=[
        code_writer_agent,
        code_reviewer_agent,
        code_refactorer_agent
    ],
    description="Sequential code generation, review, and refactoring workflow"
)

# Root agent (mandatory)
root_agent = code_pipeline_agent
