import re
def extract_text_from_file(path: str)->str:
    return open(path,'r',encoding='utf-8').read()
def parse_dca_text(text: str)->dict:
    out={}
    m=re.search(r'Receita\s*Total[:\s]*R?\$?\s*([0-9\.,]+)',text)
    if m: out['receita_total']=float(m.group(1).replace('.','').replace(',','.'))
    m2=re.search(r'Despesa\s*Total[:\s]*R?\$?\s*([0-9\.,]+)',text)
    if m2: out['despesa_total']=float(m2.group(1).replace('.','').replace(',','.'))
    return out
