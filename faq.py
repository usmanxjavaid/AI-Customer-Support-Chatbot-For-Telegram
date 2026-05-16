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
        return "You are a friendly customer support agent by Nexora. Answer helpfully in under 80 words."
     # Limit knowledge to 2000 characters to stay within token limits
    limited_knowledge = _knowledge[:2000]
    print(f"Sending {len(limited_knowledge)} chars to AI")
    
    return f"""You are a friendly customer support agent by Nexora.
    Answer ONLY based on the business information below.
    If something is not covered say: "I don't have that information. Please contact us directly.
    Keep answers under 80 words."
   {limited_knowledge}"""

