import ollama

def summarize_article(title, content_snippet):
    """
    Uses local Gemma 2 to create a 1-sentence executive summary.
    """
    prompt = f"""
    You are an expert news curator. Summarize the following news article 
    in exactly one sentence for a busy executive.
    
    Title: {title}
    Content: {content_snippet}
    
    Summary:
    """
    
    try:
        response = ollama.generate(model='gemma2', prompt=prompt)
        return response['response'].strip()
    except Exception as e:
        return f"Error summarizing: {str(e)}"

# Quick Test logic
if __name__ == "__main__":
    test_title = "Google's Gemma 2 dominates open-source benchmarks"
    test_content = "Gemma 2 9B has shown incredible performance, surpassing models twice its size..."
    print(f"Summary: {summarize_article(test_title, test_content)}")