import fitz

def extract_citation_from_pdf(file):
    try:
        doc = fitz.open(stream=file.read(), filetype='pdf')
        citation = ""

        title = ""
        authors = []
        year = ""

        # Checa se o arquivo tiver seção "Como Referenciar"
        for page in doc:
            text = page.get_text()
            if "Como referenciar" in text:
                start_index = text.index("Como referenciar") + len("Como referenciar:")
                citation = text[start_index:].strip()
                citation_lines = citation.splitlines()
                if len(citation_lines) > 1:
                    citation = citation_lines[0] + " " + citation_lines[1]
                else:
                    citation = citation_lines[0]
                return citation  

        # Tenta extrair do jeito tradicional
        for page in doc:
            text = page.get_text()
            lines = text.splitlines()

            if not title:
                title = f"{lines[2].strip()} {lines[3].strip()}"

            if not authors:
                for i in range(3, len(lines)):
                    if "Orientadoras:" in lines[i]:
                        break
                    if "1" in lines[i]:
                        author = lines[i].split("|")[0].strip()
                        author = author.rstrip('0123456789 ').strip()
                        # Invertendo a ordem do nome
                        name_parts = author.split()
                        if len(name_parts) > 1:
                            inverted_author = f"{name_parts[-1]}, {' '.join(name_parts[:-1])}"
                        else:
                            inverted_author = author  # Em caso de nome único
                        authors.append(inverted_author)

            if "Publicado:" in text:
                year_line = text.split("Publicado:")[1]
                year = year_line.split()[0][-4:]

        if authors and year and title:
            citation = f"{'; '.join(authors)}. ({year}) {title}."
        else:
            citation = "Erro ao criar a citação."

        return citation

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
        return "Erro ao processar o arquivo."
