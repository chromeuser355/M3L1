from flask import Flask
import random

app = Flask(__name__)

tech_list = ['Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka',
'Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.',
'Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan',
'Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja',
'Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati',
'Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten',
'Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita',
'Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini']

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1><a href="/tech_fact">View interesting facts</a>'

@app.route("/tech_fact")
def fact():
    return f'<h1>{random.choice(tech_list)}</h1>'
    
@app.route("/coin_flip")
def coin_flip():
    result = random.choice(["Heads", "Tails"])
    return f'<h1>The coin landed on: {result}</h1>'
    
app.run(debug=True)