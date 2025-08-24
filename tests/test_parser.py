from src.interpreter.extractor.parser import parse_dca_text

def test_parse():
    t='Receita Total: R$ 1.000,00\nDespesa Total: R$ 500,00'
    out=parse_dca_text(t)
    assert out['receita_total']==1000.0
    assert out['despesa_total']==500.0
