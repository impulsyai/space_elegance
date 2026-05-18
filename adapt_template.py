import re

with open(r"c:\Users\wareb\OneDrive\Desktop\Area de Trabalho\Impulsy.ai\Prévias\01_TEMPLATES\Template_Premium_02\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Colors & Fonts
html = html.replace("Natalia Garcia Estética - Template 03 Premium", "Space Elegance - Cintia Neri Saúde & Estética")
html = html.replace("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&family=Inter:wght@300;400;500;600;700&display=swap", "https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap")
html = html.replace("'Playfair Display'", "'Cormorant Garamond'")
html = html.replace("'Inter'", "'Montserrat'")

html = html.replace("nude: '#f0f5f2'", "nude: '#FAF8F5'")
html = html.replace("rose: '#c9dacd'", "rose: '#E8E0D5'")
html = html.replace("red: '#1a3b2b'", "red: '#C9A84C'")
html = html.replace("'red-light': '#3c7155'", "'red-light': '#C05070'")
html = html.replace("dark: '#091a10'", "dark: '#3D2C1E'")

# 2. Header / Brand
html = html.replace(">NG<", ">CN<")
html = html.replace("NATALIA GARCIA", "SPACE ELEGANCE")
html = html.replace("Estética Facial Avançada", "Saúde & Estética")
html = html.replace("5518997261240", "5571987497258")

# 3. Hero
html = html.replace("Estética Facial Avançada em Pres. Prudente", "Centro de Estética e Beleza em Salvador")
html = html.replace("A pele perfeita a <span class=\"italic text-brand-red\">poucas sessões</span> de você", "Transformando <span class=\"italic text-brand-red\">beleza</span> e bem-estar")
html = html.replace("Especialista em Retirada de Microvasos, Melasma e Botox. Protocolos modernos e personalizados para o seu bem-estar e autoestima.", "Procedimentos faciais e corporais de alta performance com resultados reais. Agende sua avaliação e viva a experiência Space Elegance.")
html = html.replace("./natalia_perfil.png", "assets/hero.png")

# 4. About
html = html.replace("Sobre o Studio", "Sobre a Clínica")
html = html.replace("Excelência em <br> <span class=\"italic text-brand-red\">estética avançada</span>", "Cuidamos de você de <br> <span class=\"italic text-brand-red\">forma completa</span>")
html = html.replace("O Studio Natalia Garcia nasceu com o propósito", "A Space Elegance nasceu com o propósito")
html = html.replace("retirada de microvasos, tratamento de melasma, botox, limpeza de pele e muito mais", "Botox, Microagulhamento, Drenagem Linfática, Preenchimento e muito mais")
html = html.replace(">I<", ">CN<")

# 5. Treatments (Replace titles & texts)
html = html.replace("Retirada de Microvasos", "Limpeza de Pele")
html = html.replace("Escleroterapia para secagem de vasinhos.", "Pele renovada, limpa e com brilho saudável.")

html = html.replace("Tratamento de Estrias", "Microagulhamento")
html = html.replace("Renovação completa da textura da pele.", "Estimulação de colágeno e redução de cicatrizes.")

html = html.replace("Clareamento de Áreas", "Drenagem Linfática")
html = html.replace("Axilas e virilhas com tom uniforme.", "Redução de inchaço e modelagem corporal.")

html = html.replace("Rejuvenescimento", "Botox & Preenchimento")
html = html.replace("Vitalidade e brilho para peles maduras.", "Suavização de rugas e contorno harmonioso.")

# Update the JS object for treatments
html = html.replace("tratamento especializado para Melasma e aplicação de Botox", "Limpeza de Pele com Peeling de Diamante, Botox e Microagulhamento")
html = html.replace("Somos especialistas em Escleroterapia (secagem de vasinhos). Um tratamento seguro e eficaz para eliminar os microvasos que causam desconforto estético, devolvendo a beleza e a uniformidade para a sua pele.", "Pele renovada, limpa e com brilho saudável após cada sessão de limpeza de pele avançada.")

# 6. Team
html = html.replace("A Especialista", "A Especialista")
html = html.replace("Natalia <span class=\"italic text-brand-red\">Garcia</span>", "Cintia <span class=\"italic text-brand-red\">Neri</span>")

# 7. Testimonials
html = html.replace("Juliana Mendes", "Maria S.")
html = html.replace("Carolina Freitas", "Fernanda L.")
html = html.replace("Amanda Oliveira", "Ana P.")

# 8. Location
html = html.replace("R. Francisco Nogueira, 105 - Jardim Aviação<br>Pres. Prudente - SP, 19020-560", "Av. Dorival Caymmi Nº 28, Itapuã<br>Galeria Marieta, Salvador - BA")
html = html.replace("(18) 99726-1240", "(71) 98749-7258")
html = html.replace("08:00 às 18:00", "08:00 às 17:00")
html = html.replace("08:00 às 12:00", "08:30 às 15:00")

# 9. Footer
html = html.replace("Natalia Garcia Estética", "Space Elegance - Cintia Neri Saúde & Estética")
html = html.replace("studiolataliagarcia", "space.elegance")

with open(r"c:\Users\wareb\OneDrive\Desktop\Area de Trabalho\Impulsy.ai\Prévias\02_CLIENTES\space_elegance\index_v2.html", "w", encoding="utf-8") as f:
    f.write(html)
