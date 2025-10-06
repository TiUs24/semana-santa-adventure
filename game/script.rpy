# script.rpy - Awal Petualangan Semana Santa

# === Definisi Karakter ===
define p = Character("Paulus", color="#56A0D3")
define m = Character("Maria", color="#C27BA0")
define a = Character("Anak", color="#15da2c")
define narrator = Character(None)

# === Background ===
image bg lapangan = im.Scale("images/bg/lapangan.png", config.screen_width, config.screen_height)
image bg jalan = im.Scale("images/bg/jalan.png", config.screen_width, config.screen_height)
image bg warung = im.Scale("images/bg/warung.png", config.screen_width, config.screen_height)
image bg depan = im.Scale("images/bg/depan.png", config.screen_width, config.screen_height)

# === Sprite Paulus ===
image paulus normal = "images/paulus/paulus.png"
image bola normal = "images/paulus/bola.png"
image bingung normal = "images/paulus/bingung.png"
image open normal = "images/paulus/open.png"

# === Sprite Maria ===
image maria normal = "images/maria/maria.png"
image kecewa normal = "images/maria/kecewa.png"
image bahagia normal = "images/maria/bahagia.png"

# === Sprite NPC ===
image anak normal = "images/npc/anak.png"
image anak2 normal = "images/npc/anak2.png"



# === Transform untuk Memperbesar Karakter ===
transform perbesar:
    zoom 1.5
    yalign 1.0

# === Variabel Skor ===
default score = 10

# === Mulai Petualangan ===
label start:
    scene bg lapangan
    with fade

    show open normal at center, perbesar
    narrator "Kamu adalah Paulus, seorang anak laki-laki dari salah satu desa adat di Larantuka, NTT."
    narrator "Sore itu, kamu sedang asyik bermain bola bersama teman-teman di lapangan desa."
    
    hide open
    show bola normal at center, perbesar
       
    p "Sedikit lagi, pasti gol!"
    
    narrator "Tiba-tiba, Maria datang menghampirimu dari pinggir lapangan."
    
    show maria normal at right, perbesar
    m "Paulus, ayo! Kita harus ke gereja sekarang. Misa pembukaan Semana Santa akan segera dimulai."
    
    hide bola
    show bingung normal at left, perbesar
    p "Hmm..."

    menu:
        "Lanjut main bola, tidak usah ke gereja.":
            $ score = 0
            jump ending_main_bola

        "Aku masih mau main bola, sebentar lagi ya.":
            $ score -= 5
            jump dibujuk_maria
        
        "Aku lelah, mau pulang dan tidur saja.":
            $ score = 0
            jump ending_tidur

# === Alur Cerita Lanjutan ===

label dibujuk_maria:
    hide bingung
    show paulus normal at left, perbesar
    m "Ayolah, Paulus. Ini kan tradisi penting bagi kita semua. Main bola bisa besok lagi."
    p "Tapi permainannya sedang seru..."
    
    menu:
        "Baiklah kalau begitu, ayo kita ke gereja.":
            jump ke_gereja
        
        "Tidak mau, aku tetap mau main bola.":
            $ score = 0
            jump ending_main_bola

label ke_gereja:
    hide maria
    show bahagia normal at right, perbesar
    p "Oke, oke. Aku akan ikut denganmu."
    m "Horee!!!"
    narrator "Kamu memutuskan untuk mendengarkan ajakan Maria. Ini adalah awal dari perjalanan imanmu di Semana Santa."
    narrator "Skor sementaramu: [score]."
    
# === Misi: Dalam Perjalanan ke Gereja ===
label misi_jalan_ke_gereja:
    scene bg jalan
    with fade

    narrator "Paulus dan Maria berjalan bersama menuju gereja."

    show paulus normal at left, perbesar
    show maria normal at right, perbesar

    m "Lihat, ada seorang anak kecil di depan kios lilin.Sepertinya dia kesulitan… ayo kita dekati."
    p "Hmm...Baiklahh"

    # Anak kecil NPC
    scene bg warung
    with fade 

    show anak normal at center,
    show paulus normal at left, perbesar
    show maria normal at right, perbesar
    narrator "Seorang anak kecil menatap kalian sambil memegang selembar uang."

    a "Kakak, aku mau beli 24 lilin dan 3 lem kertas. Satu lilin harganya Rp.2000 , dan 1 lem harganya Rp.8000 . Uangku ada Rp.100.000."
    a "Berapa kembalian yang harus kuterima?"

    menu:
        "Kamu menjawab: Rp.28.000 .":
            $ score += 5
            a "Iya betul! Terima kasih kakak."
            narrator "Anak itu tersenyum lega dan bisa membeli lilinnya."
            jump sampai_di_gereja

        "Kamu menjawab: Rp.18.000 .":
            $ score -= 5
            a "Eh… tapi kak, 24 lilin berarti Rp.48.000 dan 3 Lem Rp.24.000 . Kalau bayarnya Rp.100.000 , kembalian harusnya Rp.28.000."
            narrator "Anak itu tetap menghitung ulang sendiri, tapi kamu sudah belajar dari kesalahan."
            jump sampai_di_gereja

        "Kamu mengabaikan anak itu dan langsung pergi.":
            hide anak
            show kecewa normal at right, perbesar
            show anak2 normal at center, perbesar
            $ score = 0
            narrator "Maria menatapmu dengan kecewa karena tidak mau membantu."

            scene bg jalan
            with fade
            show paulus normal at left, perbesar
            show kecewa normal at right, perbesar
            m "Paulus… Semana Santa bukan hanya soal misa, tapi juga soal kepedulian."
            jump ending_tidak_peduli

# === Ending jika tidak peduli ===
label ending_tidak_peduli:
    scene bg depan
    with fade
    hide maria
    hide anak
    show kecewa at right, perbesar
    show paulus at left, perbesar
    
    
    narrator "Karena enggan membantu, perjalananmu kehilangan makna. Kamu sampai di gereja, tapi hatimu kosong."
    narrator "Skor akhirmu: [score]."
    return

# === Jika berhasil lewat ===
label sampai_di_gereja:
    scene bg depan
    with fade
    hide anak
    narrator "Akhirnya kamu dan Maria sampai di depan gereja, bersama kerumunan umat yang sudah menanti."
    narrator "Skor sementaramu: [score]."
    show paulus at left, perbesar
    show maria at right, perbesar
    # lanjut ke misi misa pembukaan
    return

# === Ending Buruk ===

label ending_main_bola:
    hide maria 
    show kecewa normal at right, perbesar
    p "Tahun ini aku tidak ikut dulu. Lagi seru sekali mainnya!"
    m "Ya sudah kalau begitu..."
    narrator "Maria terlihat kecewa dan pergi ke gereja sendirian. Kamu melanjutkan permainan hingga lupa waktu."
    narrator "Kamu melewatkan seluruh prosesi Semana Santa tahun ini."
    narrator "Skor akhirmu: [score]."
    return

label ending_tidur:
    hide maria
    show kecewa normal at right, perbesar
    p "Maaf Maria, aku lelah sekali hari ini. Aku mau istirahat saja."
    m "Oh, baiklah. Sampai jumpa."
    narrator "Kamu pulang ke rumah dan tertidur pulas hingga malam hari."
    narrator "Kamu melewatkan seluruh prosesi Semana Santa tahun ini dalam tidurmu."
    narrator "Skor akhirmu: [score]."
    return
