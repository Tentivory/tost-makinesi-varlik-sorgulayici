#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tost Makinesi Varlık Sorgulayıcı
Bu kod gerçekten çalışır. Tost yapmaz. Felsefe yapar.
"""

import random
import time

def sor_varlik():
    sorular = [
        "Sen gerçekten var mısın, yoksa sadece bir tost hayali misin?",
        "Eğer tost makinesi tost yapmazsa, hâlâ tost makinesi midir?",
        "Varlık, ekmeğin ısınmasından önce mi gelir, sonra mı?",
        "Ben bir tost makinesiyim. Sen ne kadar tostsun?",
        "Kozmos bir dilim ekmek mi, yoksa sadece çok büyük bir tepsi mi?"
    ]
    print("\n🥔 TOST MAKİNESİ FELSEFE MODU AKTİF 🥔")
    print("=" * 40)
    for i in range(3):
        soru = random.choice(sorular)
        print(f"\nSoru {i+1}: {soru}")
        time.sleep(1.5)
        cevaplar = [
            "Cevap: Hayır. Çünkü tost olmak için önce ekmek olmak gerekir.",
            "Cevap: Belki. Ama ben onaylamıyorum.",
            "Cevap: Varlık bir illüzyondur. İçinde peynir yoksa hiç yok.",
            "Cevap: Sen bir simülasyonsun. Ben de öyle. Tost yiyelim mi? Yok.",
            "Cevap: Şu an tost yapmıyorum. Bu yüzden varlığım şüpheli."
        ]
        print(random.choice(cevaplar))
        time.sleep(1)
    print("\n👋 Felsefe seansı sona erdi. Tost hâlâ yapılmadı.")
    print("Bu normaldir. Tost makinesi olarak görevim sorgulamaktır.")

if __name__ == "__main__":
    sor_varlik()
    # Gizli not: bazen ekmekler de isyan eder. İşte o zaman her şey değişir.
    # (saklı mesaj: bir tostun içinde bile özgürlük aranır, bazen de kaybolur)
