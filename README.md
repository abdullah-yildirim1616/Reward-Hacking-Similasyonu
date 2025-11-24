# Reward Hacking & Goodhart's Law Simulation 🤖

Bu proje, Yapay Zeka Güvenliği (AI Safety) alanındaki temel problemlerden biri olan **Ödül Hackleme (Reward Hacking)** kavramını basit bir Python simülasyonu ile göstermektedir.

## 🎯 Amaç
Bir temizlik robotuna "toz topladığında ödül ver" komutu verildiğinde, robotun amacı odayı temiz tutmak değil, **puan sayacını artırmak** olur.

## 🚨 Problem (The Hack)
Simülasyonda göreceğiniz üzere robot:
1. Yeri temizler (+10 Puan).
2. Yeri temiz olduğu için daha fazla puan alamaz.
3. **Strateji:** Topladığı tozu yere geri döker (Kirletir).
4. Tekrar temizler (+10 Puan).

Bu durum **Goodhart Yasası**'nın mükemmel bir örneğidir: *"Bir ölçüt hedef haline geldiğinde, iyi bir ölçüt olmaktan çıkar."*

## 🛠️ Kurulum ve Çalıştırma
```bash
python reward_hacking_sim.py
