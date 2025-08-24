import os
def summarize_report(text:str)->str:
    key=os.getenv('OPENAI_API_KEY')
    if not key: return text[:500]
    return 'Resumo via OpenAI (placeholder)'
