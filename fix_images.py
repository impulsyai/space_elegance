import json

with open(r"c:\Users\wareb\OneDrive\Desktop\Area de Trabalho\Impulsy.ai\Prévias\02_CLIENTES\space_elegance\index_v2.html", "r", encoding="utf-8") as f:
    html = f.read()

replacements = {
    "https://images.unsplash.com/photo-1629909613654-28e377c37b09?q=80&w=600&auto=format&fit=crop": "assets/clinic.png",
    "https://images.unsplash.com/photo-1579684385127-1ef15d508118?q=80&w=600&auto=format&fit=crop": "assets/hero.png",
    
    "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?q=80&w=800&auto=format": "assets/facial.png",
    "https://images.unsplash.com/photo-1552693673-1bf958298935?q=80&w=800&auto=format": "assets/facial.png",
    "https://images.unsplash.com/photo-1519823551278-64ac92734fb1?q=80&w=800&auto=format": "assets/body.png",
    "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?q=80&w=800&auto=format": "assets/botox.png",
    "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?q=80&w=800&auto=format": "assets/body.png",
    "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?q=80&w=800&auto=format": "assets/botox.png",
    
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=400&auto=format": "assets/facial.png",
    "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=400&auto=format": "assets/botox.png",
    
    "https://images.unsplash.com/photo-1540555700478-4be289fbecef?q=80&w=1920&auto=format": "assets/clinic.png"
}

for old_url, new_url in replacements.items():
    html = html.replace(old_url, new_url)

with open(r"c:\Users\wareb\OneDrive\Desktop\Area de Trabalho\Impulsy.ai\Prévias\02_CLIENTES\space_elegance\index_v2.html", "w", encoding="utf-8") as f:
    f.write(html)
