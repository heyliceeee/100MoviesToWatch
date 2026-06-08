# 🎬 Empire Online — Top 100 Movies Scraper

Este projeto recolhe automaticamente a lista dos **100 melhores filmes de sempre** segundo a Empire Online e gera um ficheiro de texto com todos os títulos organizados do nº 1 ao nº 100.

---

## 📌 Objetivo

Extrair os títulos presentes na página oficial da Empire Online, filtrá‑los de forma precisa e gerar uma lista final limpa e ordenada. O foco está em:

- Aceder à página com cabeçalhos de navegador para evitar bloqueios  
- Identificar corretamente os elementos HTML que contêm os títulos  
- Filtrar apenas os títulos válidos  
- Reverter a ordem para obter a lista do 1 ao 100  
- Guardar o resultado num ficheiro simples

---

## 🧠 Como Funciona

O programa:

- Obtém o HTML da página da Empire Online usando cabeçalhos que simulam um browser real  
- Analisa o conteúdo com BeautifulSoup  
- Localiza os elementos que contêm os títulos dos filmes  
- Extrai apenas os textos relevantes, ignorando elementos como “Director:”  
- Organiza a lista na ordem correta  
- Exporta todos os títulos para um ficheiro `movies.txt`