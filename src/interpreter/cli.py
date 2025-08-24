import json, typer
from .extractor.parser import extract_text_from_file, parse_dca_text
from .openai_client import summarize_report
app=typer.Typer()
@app.command()
def interpret(path:str,out:str='out.json',summarize:bool=True):
    text=extract_text_from_file(path)
    parsed=parse_dca_text(text)
    if summarize: parsed['summary']=summarize_report(text)
    with open(out,'w',encoding='utf-8') as f: json.dump(parsed,f,ensure_ascii=False,indent=2)
    print('Wrote',out)
