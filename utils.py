import os
import tempfile
import urllib.request
from fpdf import FPDF
from data import FONT_URL, CONVERSION_EXAMPLES

def download_font():
    font_dir = os.path.join(tempfile.gettempdir(), "fonts")
    os.makedirs(font_dir, exist_ok=True)
    font_path = os.path.join(font_dir, "DejaVuSans.ttf")
    if not os.path.exists(font_path):
        urllib.request.urlretrieve(FONT_URL, font_path)
    return font_path

def generate_pdf_report(user_data: dict) -> str:
    font_path = download_font()
    
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)
    
    pdf.set_font_size(16)
    pdf.cell(0, 10, txt="ТОЧКА ТЕХНОЛОГИЧЕСКОГО ПЕРЕХОДА", ln=1, align='C')
    pdf.set_font_size(12)
    pdf.cell(0, 10, txt="Персональная карта технолидера", ln=1, align='C')
    pdf.ln(10)
    
    pdf.set_font("DejaVu", style="B", size=12)
    pdf.cell(0, 8, txt="Профиль:", ln=1)
    pdf.set_font("DejaVu", size=12)
    pdf.cell(0, 6, txt=f"Военно-учётная группа: {user_data.get('vug', '—')}", ln=1)
    pdf.cell(0, 6, txt=f"Архетип: {user_data.get('archetype_name', '—')}", ln=1)
    pdf.ln(5)
    
    pdf.set_font("DejaVu", style="B", size=12)
    pdf.cell(0, 8, txt="🎯 Целевые позиции (Tech Lead / Head):", ln=1)
    pdf.set_font("DejaVu", size=11)
    professions = user_data.get('professions', '—')
    pdf.multi_cell(0, 6, txt=professions)
    pdf.ln(5)
    
    pdf.set_font("DejaVu", style="B", size=12)
    pdf.cell(0, 8, txt="📌 Примеры конвертации опыта:", ln=1)
    pdf.set_font("DejaVu", size=11)
    for ex in CONVERSION_EXAMPLES:
        pdf.multi_cell(0, 6, txt=ex)
    pdf.ln(5)
    
    pdf.set_font("DejaVu", style="B", size=12)
    pdf.cell(0, 8, txt="🛤 Дорожная карта:", ln=1)
    pdf.set_font("DejaVu", size=11)
    roadmap_text = user_data.get('roadmap_text', '—')
    pdf.multi_cell(0, 6, txt=roadmap_text)
    pdf.ln(5)
    
    pdf.set_font("DejaVu", style="B", size=12)
    pdf.cell(0, 8, txt="✅ Первый шаг сегодня:", ln=1)
    pdf.set_font("DejaVu", size=11)
    pdf.multi_cell(0, 6, txt="• Обновите резюме, используя примеры конвертации.\n• Откликнитесь на 3 вакансии для технических руководителей.\n• Запишитесь на профильные курсы повышения квалификации.")
    
    fd, path = tempfile.mkstemp(suffix=".pdf")
    os.close(fd)
    pdf.output(path)
    return path