with open(r"c:\Users\wareb\OneDrive\Desktop\Area de Trabalho\Impulsy.ai\Prévias\02_CLIENTES\space_elegance\index_v2.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Fix HTML img tags (0-indexed)
lines[139] = lines[139].replace('src="assets/hero.png"', 'src="assets/sobre_detalhe.png"')
lines[209] = lines[209].replace('src="assets/sobre_clinica.png"', 'src="assets/facial.png"')
lines[222] = lines[222].replace('src="assets/facial.png"', 'src="assets/limpeza_pele.png"')
lines[302] = lines[302].replace('src="assets/limpeza_pele.png"', 'src="assets/facial.png"')
lines[306] = lines[306].replace('src="assets/microagulhamento.png"', 'src="assets/facial.png"')
lines[387] = lines[387].replace('src="assets/hero.png"', 'src="assets/especialista.png"')

# Fix JS object
lines[664] = lines[664].replace("image: 'assets/microagulhamento.png'", "image: 'assets/facial.png'")
lines[669] = lines[669].replace("image: 'assets/facial.png'", "image: 'assets/limpeza_pele.png'")

with open(r"c:\Users\wareb\OneDrive\Desktop\Area de Trabalho\Impulsy.ai\Prévias\02_CLIENTES\space_elegance\index_v2.html", "w", encoding="utf-8") as f:
    f.writelines(lines)
