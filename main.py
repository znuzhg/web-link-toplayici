# ==========================================
# V1 - Tek sayfadan link çekme (basit hali)
# ==========================================

#
# import requests
# from bs4 import BeautifulSoup
# url = "https://atilsamancioglu.com"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
# response = requests.get(url=url, headers=headers)
# if response.status_code < 400:
#     soup = BeautifulSoup(response.text,'html.parser')
#
#     href_list = []
#
#     link_tags = soup.find_all('a', href=True)
#
#     for link in link_tags:
#         href_link = link["href"]
#         href_list.append(href_link)
#
#     temiz_href_list = [href for href in href_list if href.startswith("http")]
#
#     # for href in href_list:
#     #     if href.startswith("http"):
#     #         temiz_href_list.append(href)
#     #     else:
#     #         print("silindi",href)
#
#     if temiz_href_list:
#         print(f" --- Toplam {len(temiz_href_list)} link bulundu ---")
#         # i=[print(i) for i in range(len(temiz_href_list))]
#         [print(f"[] |", link) for link in temiz_href_list]
#
#     else:print("Hiç geçerli link bulunamadı.")
# else:
#     print(f"Error: {response.status_code}")

# ==========================================
# V2 - Tüm sayfaları dolaşan, threadsiz crawler
# ==========================================


# import requests
# from bs4 import BeautifulSoup
# import threading
# from time import time
# url = "https://atilsamancioglu.com"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
#
# st = time()
# bulunan = []
# bulunan_linkler = []
# class html_parser_class():
#
#     url = url
#     headers = headers
#     def __init__(self,url,headers):
#         self.url = url
#         self.headers = headers
#         self.bulunan = bulunan
#         self.bulunan_linkler= bulunan_linkler
#
#
#
#     def html_parser(self, url, headers):
#         self.response = requests.get(url=self.url, headers=self.headers)
#         self.soup = BeautifulSoup(self.response.text, 'html.parser')
#
#         for href in self.soup.find_all("a"):
#             self.alınan_link = href.get("href")
#             if self.alınan_link not in self.bulunan:
#                 self.bulunan.append(self.alınan_link)
#
#         for link in self.bulunan:
#             if link.startswith("http"):
#                 self.bulunan_linkler.append(link)
#         self.bulunan_linkler = list(dict.fromkeys(self.bulunan_linkler))
#         return bulunan_linkler
#
# bulunan = html_parser_class(url,headers).html_parser(url,headers)
#
#
# def html_parser(url,headers):
#     tum_linkler = []
#     temiz_link_listesi = []
#     response = requests.get(url=url,headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     for href in soup.find_all("a"):
#         alınan_link = href.get("href")
#         if alınan_link not in tum_linkler:
#             tum_linkler.append(alınan_link)
#
#     for link in tum_linkler:
#         if link.startswith("http"):
#             if link not in temiz_link_listesi:
#                 temiz_link_listesi.append(link)
#     return temiz_link_listesi
#
# temiz_link_listesi =[]
#
# try:
#     for link in bulunan:
#         temiz_link_listesi = temiz_link_listesi + (html_parser(f"{link}",headers))
# except requests.exceptions.InvalidSchema:
#     print("sıkıntı")
#
# thread = threading.Thread(target=basla)
# thread.start()
# thread.join()
# temiz_linkler= list(dict.fromkeys(temiz_link_listesi))
#
# print(len(temiz_linkler))
# [print(link) for link in temiz_linkler]
# et = time()
#
# elapsed_time = et - st
# print(round(elapsed_time,5))

# ==========================================
# V3 - (multi-thread) web link toplayıcı
# ==========================================



import requests
from bs4 import BeautifulSoup
import threading
from time import time

url = "https://atilsamancioglu.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

# Zaman ölçümü
start = time()

# -----------------------------
# 1) Ana sayfadaki linkleri alma
# -----------------------------
def ana_sayfa_linkleri(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    bulunan = []

    for href in soup.find_all("a"):
        link = href.get("href")
        if link and link.startswith("http"):
            if link not in bulunan:
                bulunan.append(link)

    return bulunan


bulunan = ana_sayfa_linkleri(url)


# -----------------------------------------
# 2) Her link için thread çalıştıracak fonk.
# -----------------------------------------
global_sonuc = []
lock = threading.Lock()     # thread'lerin aynı anda listeye yazmasını kontrol eder


def linkleri_cek(link):
    try:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        temiz = []
        for href in soup.find_all("a"):
            l = href.get("href")
            if l and l.startswith("http"):
                temiz.append(l)

        # Thread-safe liste ekleme
        with lock:
            global_sonuc.extend(temiz)

    except Exception as e:
        print("Hata:", e)


# -----------------------
# 3) Thread'leri başlatma
# -----------------------
threads = []

for link in bulunan:
    t = threading.Thread(target=linkleri_cek, args=(link,))
    t.start()
    threads.append(t)

# Tüm threadlerin bitmesini bekle
for t in threads:
    t.join()

# -------------------------
# 4) Duplicate temizleme
# -------------------------
final_list = list(dict.fromkeys(global_sonuc))

print("Toplam link:", len(final_list))
for link in final_list:
    print(link)

# Süre
print("\nSüre:", round(time() - start, 5), "sn")
