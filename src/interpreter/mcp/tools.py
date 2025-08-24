from ..extractor.parser import extract_text_from_file, parse_dca_text
from ..openai_client import summarize_report
def interpret_file(path:str):
    text=extract_text_from_file(path)
    return {'parsed': parse_dca_text(text)}
def summarize(path:str):
    text=extract_text_from_file(path)
    return {'summary': summarize_report(text)}
