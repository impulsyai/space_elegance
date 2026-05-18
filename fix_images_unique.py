import re

with open(r"c:\Users\wareb\OneDrive\Desktop\Area de Trabalho\Impulsy.ai\Prévias\02_CLIENTES\space_elegance\index_v2.html", "r", encoding="utf-8") as f:
    html = f.read()

facial_replacements = [
    "assets/sobre_clinica.png", 
    "assets/facial.png",        
    "assets/limpeza_pele.png",  
    "assets/microagulhamento.png", 
    "assets/microagulhamento.png", 
    "assets/facial.png",        
    "assets/limpeza_pele.png",  
]

facial_count = 0
def replace_facial(match):
    global facial_count
    res = facial_replacements[facial_count] if facial_count < len(facial_replacements) else match.group(0)
    facial_count += 1
    return res

html = re.sub(r"assets/facial\.png", replace_facial, html)

body_replacements = [
    "assets/body.png",          
    "assets/drenagem.png",      
    "assets/body.png",          
    "assets/drenagem.png",      
]
body_count = 0
def replace_body(match):
    global body_count
    res = body_replacements[body_count] if body_count < len(body_replacements) else match.group(0)
    body_count += 1
    return res

html = re.sub(r"assets/body\.png", replace_body, html)

botox_replacements = [
    "assets/microagulhamento.png", 
    "assets/botox.png",            
    "assets/botox.png",            
    "assets/botox.png",            
    "assets/microagulhamento.png", 
    "assets/botox.png",            
]
botox_count = 0
def replace_botox(match):
    global botox_count
    res = botox_replacements[botox_count] if botox_count < len(botox_replacements) else match.group(0)
    botox_count += 1
    return res

html = re.sub(r"assets/botox\.png", replace_botox, html)

with open(r"c:\Users\wareb\OneDrive\Desktop\Area de Trabalho\Impulsy.ai\Prévias\02_CLIENTES\space_elegance\index_v2.html", "w", encoding="utf-8") as f:
    f.write(html)
