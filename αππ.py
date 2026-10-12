import streamlit as st
from datetime import date
from fpdf import FPDF
import tempfile
import os
def create_pdf(b_date, b_hour, main_g, asc_g):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Γήινο σκούρο καφέ χρώμα (RGB: 92, 64, 51)
    pdf.set_text_color(92, 64, 51) 

    # Τίτλος
    pdf.set_font("helvetica", "B", 18)
    pdf.cell(0, 10, "THE GOAT HOROSCOPE", align="C", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", "", 11)
    pdf.cell(0, 8, f"Birth Date: {b_date} | Hour: {b_hour}:00", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    
    # 1. Main Goat
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(0, 8, "1. MAIN GOAT", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "", 11)
    pdf.cell(0, 6, f"Breed: {main_g['name']}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, f"Vibe: Check the app screen for details", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, f"Matches: {main_g['matches']}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    
    # 2. Ascendant Goat
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(0, 8, "2. ASCENDANT GOAT", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", "", 11)
    pdf.cell(0, 6, f"Breed: {asc_g['name']}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, f"Vibe: Check the app screen for details", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, f"Matches: {asc_g['matches']}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(15)
    
    # Μεγάλη υπογραφή στο τέλος
    pdf.set_font("helvetica", "B", 22)
    pdf.cell(0, 12, "WITH LOVE,", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 12, "KATSIKOPODARES F.C.", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    
    # Clickable Instagram Link ακριβώς κάτω από την υπογραφή
    pdf.set_font("helvetica", "U", 11)
    pdf.cell(0, 8, "Instagram: @katsikopodares.fc", align="C", link="https://www.instagram.com/katsikopodares.fc/", new_x="LMARGIN", new_y="NEXT")

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)
    return temp_file.name
    
# Επιστροφή σε centered layout για να φαίνονται ολόκληρες και σωστές οι εικόνες
st.set_page_config(
    page_title="Το Κατσικίσιο Ωροσκόπιο",
    page_icon="🐐",
    layout="centered"
)

# Custom CSS για καφέ-μπεζ γήινο θέμα
st.markdown("""
    <style>
    .stApp {
        background-color: #FAF8F5;
    }
    .main-title {
        text-align: center; 
        padding: 18px; 
        background: linear-gradient(135deg, #6D4C41, #4E342E); 
        border-radius: 14px; 
        color: #EFEBE9; 
        margin-bottom: 20px; 
        font-family: sans-serif; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .card-main {
        background: #FAF8F5; 
        padding: 25px; 
        border-radius: 16px; 
        border-top: 6px solid #6D4C41; 
        box-shadow: 0 6px 15px rgba(109,76,65,0.1); 
        box-sizing: border-box; 
        border-left: 1px solid #EFEBE9; 
        border-right: 1px solid #EFEBE9; 
        border-bottom: 1px solid #EFEBE9;
        margin-bottom: 20px;
    }
    .card-asc {
        background: #FAF8F5; 
        padding: 25px; 
        border-radius: 16px; 
        border-top: 6px solid #A1887F; 
        box-shadow: 0 6px 15px rgba(109,76,65,0.1); 
        box-sizing: border-box; 
        border-left: 1px solid #EFEBE9; 
        border-right: 1px solid #EFEBE9; 
        border-bottom: 1px solid #EFEBE9;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Πλήρης βάση δεδομένων με τις 12 φυλές κατσίκας
goats_data = [
    {
        "id": 1, "name": "Fainting (Myotonic) Goat", 
        "keywords": "✨ Παρορμητική • ⚡ Ενθουσιώδης • 🧊 Ευαίσθητη στο Στρες",
        "desc": "Είναι η πρώτη που θα ορμήσει στην περιπέτεια με τεράστιο ενθουσιασμό, αλλά μόλις πιεστεί... κοκαλώνει επί τόπου! Θέλει να ηγείται, αλλά χρειάζεται υποστήριξη στα δύσκολα.",
        "matches": "Mountain Goat, Kri Kri Goat, Pygmy Goat",
        "img": "https://lifeandlandmagazine.com/wp-content/uploads/2024/12/IMG_8019.jpg" 
    },
    {
        "id": 2, "name": "Kiko Goat", 
        "keywords": "🛡️ Πεισματάρα • 🧗 Ανθεκτική • 🌿 Λιχούδω",
        "desc": "Πεισματάρα και αλύγιστη, δεν το βάζει κάτω με τίποτα. Εκτιμά την ησυχία της, την ασφάλεια και το καλό φαγητό. Αν προσπαθήσεις να τη μετακινήσεις, απλά θα στυλώσει τα πόδια.",
        "matches": "Saanen Goat, Alpine Goat, Kashmiri Goat",
        "img": "https://cdn.morningchores.com/wp-content/uploads/2019/12/The-Kiko-Goat-Breed-Info-Characteristics-Breeding-and-Care-FI.jpg"
    },
    {
        "id": 3, "name": "Pygmy Goat", 
        "keywords": "🚀 Υπερκινητική • 🔍 Περίεργη • 🌪️ Ανήσυχη",
        "desc": "Δεν σταματάει να πηδάει από βράχο σε βράχο και να εξερευνά τα πάντα. Αλλάζει γνώμη συνεχώς, θέλει συνεχή διέγερση και δεν αντέχει τη ρουτίνα ή την πλήξη.",
        "matches": "Anglo-Nubian Goat, Fainting Goat, Mountain Goat",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKaipbtrVkU0dkHtI1_TQhk9rykbBz07H01rtHE9QF5IosIqaPmK2EhRY&s=10"
    },
    {
        "id": 4, "name": "Kashmiri Goat", 
        "keywords": "🧶 Ευαίσθητη • 🤗 Στοργική • 🌸 Πρόσχαρη",
        "desc": "Ζεστή και δοτική (λόγω του πλούσιου μαλλιού της), θέλει αγκαλιές και συναισθηματική ασφάλεια. Αν νιώσει ότι την αδικούν, κρύβεται στη γωνία της και κρατάει κακία.",
        "matches": "Angora Goat, Black Bengal Goat, Kiko Goat",
        "img": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Kashmiri_Goat_-_Capra_Markhor_%28cropped%29.jpg"
    },
    {
        "id": 5, "name": "Kri Kri Goat", 
        "keywords": "👑 Βασιλική • 🌟 Επιβλητική • 🎭 Δραματική",
        "desc": "Γεννημένη σταρ! Θέλει όλα τα φώτα και την προσοχή πάνω της. Έχει ηγετική παρουσία, είναι υπερήφανη και απαιτεί τον ανάλογο σεβασμό από το υπόλοιπο κοπάδι.",
        "matches": "Fainting Goat, Mountain Goat, Anglo-Nubian Goat",
        "img": "https://krikrihunt.eu/wp-content/uploads/2022/06/P1070805-1-1024x769.jpg?v=1656343975"
    },
    {
        "id": 6, "name": "Alpine Goat", 
        "keywords": "📐 Οργανωτική • ⛰️ Πειθαρχημένη • 🎯 Ακριβής",
        "desc": "Σκαρφαλώνει στα πιο δύσκολα και απόκρημνα σημεία με ακρίβεια χιλιοστού. Υπολογίζει την κάθε της κίνηση, σιχαίνεται το χάος και θέλει τα πάντα σε τάξη.",
        "matches": "Saanen Goat, Kiko Goat, Angora Goat",
        "img": "https://ogden_images.s3.amazonaws.com/www.iamcountryside.com/images/sites/2/2019/03/13132426/GettyImages-524819365-scaled-1-e1671134403963.jpg"
    },
    {
        "id": 7, "name": "Anglo-Nubian Goat", 
        "keywords": "📢 Εκφραστική • 🥳 Κοινωνική • 🔊 Φωνακλού",
        "desc": "Με τα τεράστια αυτιά και τη δραματική της προσωπικότητα, δεν περνάει ποτέ απαρατήρητη. Αν κάτι δεν της αρέσει, θα το μάθει όλη η γειτονιά από το βέλασμά της.",
        "matches": "Valais Blackneck Goat, Pygmy Goat, Damascus Goat",
        "img": "https://thewoolfamilyfarm.com/wp-content/uploads/2024/07/o4S_wUvw-1500x1200.jpeg"
    },
    {
        "id": 8, "name": "Black Bengal Goat", 
        "keywords": "🌑 Μυστηριώδης • 🐾 Ανεξάρτητη • 🤫 Απρόβλεπτη",
        "desc": "Ήρεμη δύναμη που κινείται στο παρασκήνιο. Δεν καταλαβαίνεις τι σκέφτεται μέχρι να δεις το αποτέλεσμα (ή να διαπιστώσεις ότι σου έφαγε τα λουλούδια).",
        "matches": "Kashmiri Goat, Angora Goat, Saanen Goat",
        "img": "https://cdn.creatures.com/11c/623/ed3/aff5f.jpeg"
    },
    {
        "id": 9, "name": "Mountain Goat", 
        "keywords": "🧗 Ριψοκίνδυνη • 🦅 Ελεύθερη • 🌅 Αισιόδοξη",
        "desc": "Ελεύθερο πνεύμα που μισεί τους περιορισμούς. Θα σκαρφαλώσει στον πιο επικίνδυνο γκρεμό απλά και μόνο για τη θέα και την αίσθηση της ελευθερίας.",
        "matches": "Fainting Goat, Kri Kri Goat, Valais Blackneck Goat",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzz4x5tl9bDuErRijE17-3-kaWnoLSL2mhrjScHa95bBpqepS7NAFILIQ&s=10"
    },
    {
        "id": 10, "name": "Saanen Goat", 
        "keywords": "💼 Σοβαρή • 🥛 Εργατική • 👑 Ηγέτιδα",
        "desc": "Η επαγγελματίας του κοπαδιού. Αφοσιωμένη στους στόχους της, παράγει αποτελέσματα χωρίς πολλά λόγια και αναλαμβάνει πάντα τις ευθύνες όταν οι άλλοι πελαγώνουν.",
        "matches": "Alpine Goat, Kiko Goat, Black Bengal Goat",
        "img": "https://img.hobbyfarms.com/wp-content/uploads/2016/02/04234007/Saanen_Jeannette-Beranger1.jpg"
    },
    {
        "id": 11, "name": "Valais Blackneck Goat", 
        "keywords": "⚡ Αντισυμβατική • 🎨 Εναλλακτική • 🦄 Πρωτοποριακή",
        "desc": "Μισή μαύρη - μισή λευκή, ξεχωρίζει από χιλιόμετρα. Δεν ακολουθεί τους κανόνες του κοπαδιού, σκέφτεται εκτός ορίων και κάνει πάντα πράγματα με τον δικό της μοναδικό τρόπο.",
        "matches": "Anglo-Nubian Goat, Mountain Goat, Pygmy Goat",
        "img": "https://www.knuthenborg.dk/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvvzubf5j%2Fproduction%2Ff9cbd5a3fd1bebc0d7100bf9ca315b4205c5a3a8-5132x3393.jpg%3Fw%3D400%26h%3D400%26fit%3Dcrop%26dpr%3D2%26q%3D100&w=3840&q=75"
    },
    {
        "id": 12, "name": "Angora Goat", 
        "keywords": "🌸 Καλλιτεχνική • ☁️ Ονειροπόλα • 🕊️ Πράα",
        "desc": "Με τις μακριές, αφράτες μπούκλες της, ζει στον δικό της ρομαντικό κόσμο. Είναι ειρηνική, αποφεύγει τις συγκρούσεις και αναζητά την ομορφιά και την αρμονία παντού.",
        "matches": "Kashmiri Goat, Black Bengal Goat, Alpine Goat",
        "img": "https://cdn.britannica.com/29/529-050-6B31311A/Angora-goat.jpg"
    }
]

def get_main_goat(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19): return goats_data[0]
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20): return goats_data[1]
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20): return goats_data[2]
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22): return goats_data[3]
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22): return goats_data[4]
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22): return goats_data[5]
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22): return goats_data[6]
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21): return goats_data[7]
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21): return goats_data[8]
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19): return goats_data[9]
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18): return goats_data[10]
    else: return goats_data[11]

def get_ascendant_goat(hour):
    index = (hour // 2) % 12
    return goats_data[index]

# UI Header
st.markdown("""
    <div class="main-title">
        <h2 style="margin: 0; font-size: 26px;">🐐 Το Κατσικίσιο Ωροσκόπιο</h2>
        <p style="margin: 8px 0 0 0; font-size: 15px; color: #D7CCC8;">Ποια κατσίκα κρύβεις μέσα σου; Μάθε ζώδιο και ωροσκόπο !</p>
    </div>
""", unsafe_allow_html=True)

# Φόρμα εισόδου
with st.form("horoscope_form"):
    birth_date = st.date_input("📅 Ημερομηνία Γέννησης:", value=date(2000, 1, 1))
    birth_hour = st.slider("⏰ Ώρα Γέννησης (0-23):", min_value=0, max_value=23, value=12)
    submitted = st.form_submit_button("🔮 Υπολογισμός!", use_container_width=True)

if submitted:
    main_goat = get_main_goat(birth_date.month, birth_date.day)
    asc_goat = get_ascendant_goat(birth_hour)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
            <div class="card-main">
                <h4 style="color: #8D6E63; margin: 0; text-transform: uppercase; font-size: 12px; letter-spacing: 1px;">Κύριο Ζώδιο (Βάσει Ημερομηνίας)</h4>
                <h2 style="color: #4E342E; margin: 8px 0 12px 0; font-size: 20px;">{main_goat['name']}</h2>
                <div style="background-color: #EFEBE9; padding: 10px 14px; border-radius: 8px; font-weight: bold; color: #4E342E; font-size: 12px; margin-bottom: 15px; line-height: 1.4;">
                    {main_goat['keywords']}
                </div>
                <p style="color: #3E2723; font-size: 13px; line-height: 1.6; margin-bottom: 12px;"><b>📜 Χαρακτηριστικά:</b><br>{main_goat['desc']}</p>
                <p style="color: #5D4037; font-size: 12px; margin-bottom: 12px; line-height: 1.4;"><b>❤️ Ταιριάζει με:</b><br>{main_goat['matches']}</p>
                <div style="width: 100%; height: 220px; overflow: hidden; border-radius: 10px; margin-top: 15px; background: #EFEBE9;">
                    <img src="{main_goat['img']}" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
            <div class="card-asc">
                <h4 style="color: #8D6E63; margin: 0; text-transform: uppercase; font-size: 12px; letter-spacing: 1px;">Ωροσκόπος (από ώρα)</h4>
                <h2 style="color: #4E342E; margin: 8px 0 12px 0; font-size: 20px;">{asc_goat['name']}</h2>
                <div style="background-color: #EFEBE9; padding: 10px 14px; border-radius: 8px; font-weight: bold; color: #4E342E; font-size: 12px; margin-bottom: 15px; line-height: 1.4;">
                    {asc_goat['keywords']}
                </div>
                <p style="color: #3E2723; font-size: 13px; line-height: 1.6; margin-bottom: 12px;"><b>🎭 Πώς σε βλέπουν οι άλλοι:</b><br>{asc_goat['desc']}</p>
                <p style="color: #5D4037; font-size: 12px; margin-bottom: 12px; line-height: 1.4;"><b>🤝 Αρμονία Ωροσκόπου με:</b><br>{asc_goat['matches']}</p>
                <div style="width: 100%; height: 220px; overflow: hidden; border-radius: 10px; margin-top: 15px; background: #EFEBE9;">
                    <img src="{asc_goat['img']}" style="width: 100%; height: 100%; object-fit: cover; display: block;"/>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # (Εδώ τελειώνουν οι κάρτες σου με τα col1 και col2)

    st.markdown("---")

    
    # Κουμπί Instagram (100% σταθερό χωρίς στήλες)
    st.link_button("📸 Follow us on Instagram: @katsikopodares.fc", "https://www.instagram.com/katsikopodares.fc/", use_container_width=True)
        # Δημιουργία PDF αρχείου
    pdf_path = create_pdf(birth_date, birth_hour, main_goat, asc_goat)

    st.markdown("---")
    with open(pdf_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="📥 Κατέβασε το Ωροσκόπιό σου σε αρχείο PDF",
        data=PDFbyte,
        file_name="to_katsikisio_oroskopio.pdf",
        mime="application/pdf",
        use_container_width=True
    )
