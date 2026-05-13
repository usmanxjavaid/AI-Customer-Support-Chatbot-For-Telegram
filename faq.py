import extractor

_knowledge = ""

def load(website_url: str = None):
    # Loads everything from knowledge/ folder +  optional website
    global _knowledge
    _knowledge = extractor.load_all(
        knowledge_folder='knowledge',
        website_url=website_url
    )

def get_system_prompt() -> str:
    if not _knowledge:
        return "You are a friendly customer support agent. Answer helpfully in under 80 words."
    
    return f"""You are a friendly customer support agent.
    Answeer ONLY based on the business information below.
    If something is not covered say: "I don't have that information. Please contact us directly.
    Keep answers under 80 words."
    {_knowledge}"""

