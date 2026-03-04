import os
import re

file_path = "/Users/yigitozdemir/Desktop/projeler/Sorula/sorularedirect/ayt/index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace canonical and OG urls
content = content.replace('href="https://sorula.app/tyt/"', 'href="https://sorula.app/ayt/"')
content = content.replace('content="https://sorula.app/tyt/"', 'content="https://sorula.app/ayt/"')

# Replace TYT with AYT generally
content = content.replace('TYT', 'AYT')

# Specific content replacements
content = content.replace("Temel Yeterlilik Testi (AYT)", "Alan Yeterlilik Testleri (AYT)")
content = content.replace("YKS'nin ilk oturumudur.", "YKS'nin ikinci oturumudur.")
content = content.replace("Üniversiteye giriş için tüm adayların girmesi gereken bu sınavda 4 temel alandan sorular sorulur. AYT puanı, hem ön lisans hem de lisans programlarına yerleşmekte kullanılır.", "Lisans programlarına (4 yıllık bölümler) yerleşmek isteyen adayların girdiği sınavdır. Adaylar kendi alanlarına (Sayısal, Sözel, Eşit Ağırlık) göre testleri çözerler.")

# SSS Replacements
content = content.replace("AYT'de toplam 120 soru sorulur: 40 Türkçe, 40 Matematik, 20 Fen Bilimleri ve 20 Sosyal Bilimler sorusu. Sınav süresi 135 dakikadır.", "AYT'de Türk Dili ve Edebiyatı-Sosyal Bilimler-1 (40 soru), Sosyal Bilimler-2 (40 soru), Matematik (40 soru) ve Fen Bilimleri (40 soru) olmak üzere toplam 160 soru bulunur. Sınav süresi 180 dakikadır.")
content = content.replace("AYT'de üniversite programlarına yerleşebilmek için en az 150 puan almak gerekmektedir. Lisans programları için ise AYT puanının en az 150 olması zorunludur.", "AYT puanının hesaplanması için TYT'den en az 150 puan alınması şartı kaldırılmıştır. Lisans bölümleri TYT (%40) ve AYT (%60) puanının toplanmasıyla oluşur.")
content = content.replace("AYT Matematik konuları: Temel Kavramlar, Sayı Basamakları, Bölme ve Bölünebilme, EBOB-EKOK, Rasyonel Sayılar, Üslü Sayılar, Köklü Sayılar, Çarpanlara Ayırma, Oran-Orantı, Problemler, Kümeler, Fonksiyonlar, Polinomlar, İkinci Dereceden Denklemler, Permütasyon-Kombinasyon, Olasılık ve İstatistik konularını kapsar.", "AYT Matematik konuları: Polinomlar, İkinci Dereceden Denklemler, Parabol, Trigonometri, Logaritma, Diziler, Limit, Türev, İntegral, Permütasyon-Kombinasyon-Olasılık ve Analitik Geometri gibi ileri düzey konuları kapsar.")

# Konu Listesi Replacements
content = content.replace("AYT Türkçe Konuları", "AYT Edebiyat Konuları")
content = content.replace("<li>• Sözcükte Anlam</li>\n                            <li>• Cümlede Anlam</li>\n                            <li>• Paragrafta Anlam</li>\n                            <li>• Ses Bilgisi</li>\n                            <li>• Yazım Kuralları</li>\n                            <li>• Noktalama İşaretleri</li>\n                            <li>• Sözcük Türleri</li>\n                            <li>• Cümle Türleri</li>\n                            <li>• Anlatım Bozuklukları</li>", "<li>• Şiir Bilgisi</li>\n                            <li>• Söz Sanatları</li>\n                            <li>• İslamiyet Öncesi ve Geçiş Dönemi Türk Edebiyatı</li>\n                            <li>• Halk Edebiyatı ve Divan Edebiyatı</li>\n                            <li>• Tanzimat, Servetifünun ve Fecriati Edebiyatı</li>\n                            <li>• Milli Edebiyat ve Cumhuriyet Dönemi Türk Edebiyatı</li>")

content = content.replace("<li>• Temel Kavramlar ve Sayı Basamakları</li>\n                            <li>• Bölme-Bölünebilme, EBOB-EKOK</li>\n                            <li>• Üslü ve Köklü Sayılar</li>\n                            <li>• Çarpanlara Ayırma</li>\n                            <li>• Oran-Orantı, Problemler</li>\n                            <li>• Kümeler ve Fonksiyonlar</li>\n                            <li>• Polinomlar ve Denklemler</li>\n                            <li>• Permütasyon, Kombinasyon, Olasılık</li>\n                            <li>• İstatistik</li>", "<li>• Çarpanlara Ayırma ve İkinci Dereceden Denklemler</li>\n                            <li>• Eşitsizlikler ve Parabol</li>\n                            <li>• Trigonometri</li>\n                            <li>• Logaritma ve Diziler</li>\n                            <li>• Limit ve Süreklilik</li>\n                            <li>• Türev ve Uygulamaları</li>\n                            <li>• İntegral ve Uygulamaları</li>")

content = content.replace("<li>• Fizik: Kuvvet-Hareket, Enerji, Isı-Sıcaklık, Elektrik, Optik</li>\n                            <li>• Kimya: Atom, Periyodik Tablo, Kimyasal Bileşikler, Asit-Baz</li>\n                            <li>• Biyoloji: Hücre, Canlılar Dünyası, Kalıtım, Ekosistem</li>", "<li>• Fizik: Çembersel Hareket, Basit Harmonik Hareket, Elektrik ve Manyetizma, Dalga Mekaniği, Modern Fizik</li>\n                            <li>• Kimya: Modern Atom Teorisi, Gazlar, Sıvı Çözeltiler, Kimyasal Tepkimelerde Enerji-Hız-Denge, Organik Kimya</li>\n                            <li>• Biyoloji: İnsan Fizyolojisi (Sistemler), Genden Proteine, Canlılarda Enerji Dönüşümleri, Bitki Biyolojisi</li>")

content = content.replace("<li>• Tarih: İlk Uygarlıklar, Osmanlı, Kurtuluş Savaşı, Atatürk İlkeleri</li>\n                            <li>• Coğrafya: Doğa-İnsan İlişkisi, Türkiye Coğrafyası</li>\n                            <li>• Felsefe: Bilgi, Varlık, Ahlak Felsefesi</li>\n                            <li>• Din Kültürü: İnanç, İbadet, Ahlak</li>", "<li>• Tarih: Tarih Bilimi, İslam Tarihi, Türk-İslam Devletleri, Osmanlı Tarihi, İnkılap Tarihi ve Çağdaş Türk ve Dünya Tarihi</li>\n                            <li>• Coğrafya: Biyoçeşitlilik, Şehirler, Türkiye'de Ekonomi, Küresel Ortam, Çevre ve Toplum</li>\n                            <li>• Felsefe Grubu: Psikoloji, Sosyoloji, Mantık</li>")


# Navbar fix - Change AYT back to TYT in links where appropriate if they got blindly replaced
content = content.replace('<a href="/AYT/" class="text-sm text-gray-900 font-bold">AYT</a>', '<a href="/tyt/" class="text-sm text-gray-500 hover:text-gray-900 transition-colors font-medium">TYT</a>\n                        <a href="/ayt/" class="text-sm text-gray-900 font-bold">AYT</a>')

# The blindly replaced TYT to AYT might have affected some internal URLs incorrectly
content = content.replace('href="/AYT/"', 'href="/ayt/"')
content = content.replace('href="https://sorula.app/AYT/"', 'href="https://sorula.app/ayt/"')
content = content.replace('<li><a href="/AYT/" class="hover:text-gray-600 transition-colors">AYT</a></li>', '<li><a href="/tyt/" class="hover:text-gray-600 transition-colors">TYT</a></li>\n                    <li><a href="/ayt/" class="hover:text-gray-600 transition-colors">AYT</a></li>')
content = content.replace('<a href="/AYT/" class="hover:text-gray-600 transition-colors">AYT</a>', '<a href="/tyt/" class="hover:text-gray-600 transition-colors">TYT</a>\n                    <a href="/ayt/" class="hover:text-gray-600 transition-colors">AYT</a>')


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

