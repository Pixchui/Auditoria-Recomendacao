def validar_titulo(titulo, titulos_disponiveis):
    """Valida título ignorando caixa e espaços externos; retorna (ok, mensagem/título)."""
    if titulo is None or not str(titulo).strip():
        return False, "Digite o título de um livro."
    procurado = str(titulo).strip().casefold()
    mapa = {str(t).strip().casefold(): t for t in titulos_disponiveis if t is not None}
    if procurado in mapa:
        return True, mapa[procurado]
    if len(procurado) <= 100:
        sugestoes = [str(t) for t in titulos_disponiveis if procurado in str(t).casefold()][:5]
        if sugestoes:
            return False, "Título não encontrado exatamente. Sugestões: " + "; ".join(sugestoes)
    return False, "Título não encontrado no CSV."
