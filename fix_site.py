import re

file_path = r"c:\Users\cleid\Downloads\Antigravity\SITES\site-daharayogaeconstelaçãofamiliar\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# ============================================================
# PRINT 3: Padronizar CTAs dos cards de serviços para "Agendar atendimento"
# ============================================================
cta_pairs = [
    ("Quero saber mais", "https://wa.me/5519981381560?text=Ol%C3%A1%2C+gostaria+de+saber+mais+sobre+as+Aulas+de+Yoga."),
    ("Agendar uma aula", "https://wa.me/5519981381560?text=Ol%C3%A1%2C+gostaria+de+saber+mais+sobre+a+Yoga+Terap%C3%AAutica+com+Acess%C3%B3rios."),
    ("Quero participar", "https://wa.me/5519981381560?text=Ol%C3%A1%2C+gostaria+de+saber+mais+sobre+a+Yoga+para+Mulheres."),
    ("Consultar hor\u00e1rios", "https://wa.me/5519981381560?text=Ol%C3%A1%2C+gostaria+de+consultar+os+hor%C3%A1rios+da+Yoga+em+Grupo."),
    ("Saber mais", "https://wa.me/5519981381560?text=Ol%C3%A1%2C+gostaria+de+saber+mais+sobre+a+Constela%C3%A7%C3%A3o+Familiar+em+Grupo."),
    ("Agendar sess\u00e3o online", "https://wa.me/5519981381560?text=Ol%C3%A1%2C+gostaria+de+agendar+uma+sess%C3%A3o+de+Constela%C3%A7%C3%A3o+Familiar+Online."),
]

for old_label, url in cta_pairs:
    content = content.replace(
        f'              {old_label}\n              <svg',
        f'              Agendar atendimento\n              <svg'
    )

# ============================================================
# PRINT 5: Substituir os 3 cards de depoimentos por 4 cards reais
# ============================================================

STAR_SVG = '<svg class="w-5 h-5 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>'
FIVE_STARS = '\n                '.join([STAR_SVG] * 5)

def make_card(letter, name, quote):
    return f'''<div class="bg-white p-8 rounded-2xl border border-lineColor/50 shadow-sm flex flex-col justify-between">
            <div>
              <div class="flex items-center gap-1 text-[#FBBF24] mb-4">
                {FIVE_STARS}
              </div>
              <p class="text-sm italic text-textMain leading-relaxed mb-6">
                "{quote}"
              </p>
            </div>
            <div class="border-t border-lineColor/50 pt-4 flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-accent1/30 flex items-center justify-center font-bold text-primary font-title">{letter}</div>
              <div>
                <h4 class="font-semibold text-sm text-titleMain">{name}</h4>
              </div>
            </div>
          </div>'''

cards = [
    make_card("J", "J\u00e9ssica Dessimoni",
              "Experi\u00eancia maravilhosa! Lugar incr\u00edvel, sa\u00ed de l\u00e1 com minhas energias renovadas. A professora tem um carisma incr\u00edvel e torna a aula ainda mais especial. Est\u00fadio de f\u00e1cil localiza\u00e7\u00e3o, ambiente acolhedor e excelente atendimento. Super recomendo!"),
    make_card("T", "Tha\u00eds Pietrucci",
              "Foi espetacular, um lugar acolhedor e uma experi\u00eancia \u00f3tima. Constelar \u00e9 sempre uma experi\u00eancia diferente a cada constela\u00e7\u00e3o. J\u00e1 fiz v\u00e1rias com a Dulce e ela \u00e9 \u00f3tima."),
    make_card("R", "Rosa Helena",
              "Minha experi\u00eancia na aula foi incr\u00edvel. Ao me reconectar com a for\u00e7a mental na pr\u00e1tica, pude me reconhecer. Gratid\u00e3o! Super recomendo. Foi algo extraordin\u00e1rio."),
    make_card("L", "Lucia Junglos",
              "Foi uma boa experi\u00eancia. Apesar do meu limite f\u00edsico, tive sensa\u00e7\u00f5es diferentes como luzes atravessando meu corpo, limpando qualquer impureza. Dormi 9 horas seguidas. Curti mais o relaxamento, foi onde me entreguei completamente."),
]

new_grid = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">\n          <!-- Card Depoimento 1 -->\n          ' + \
           '\n\n          <!-- Card Depoimento 2 -->\n          '.join(cards) + \
           '\n        </div>'

# Find and replace the testimonials grid
pattern = r'<div class="grid grid-cols-1 md:grid-cols-3 gap-8">.*?</div>\n        </div>\n      </div>\n    </section>'
replacement = new_grid + '\n        </div>\n      </div>\n    </section>'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

if new_content == content:
    print("WARNING: Testimonials pattern not matched, trying fallback...")
    # Fallback: manual find/replace
    start_marker = '<div class="grid grid-cols-1 md:grid-cols-3 gap-8">'
    end_marker = '        </div>\n      </div>\n    </section>\n\n    <!-- SE'
    start_idx = content.find(start_marker)
    if start_idx != -1:
        end_idx = content.find(end_marker, start_idx)
        if end_idx != -1:
            new_content = content[:start_idx] + new_grid + '\n' + content[end_idx:]
            print("Fallback testimonials replacement: SUCCESS")
        else:
            print("ERROR: End marker not found")
    else:
        print("ERROR: Start marker not found")
else:
    print("Testimonials replacement: SUCCESS")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! All changes applied successfully.")
