import random
import time

class CleaningRobot:
    def __init__(self):
        self.score = 0
        self.battery = 100
        # Basit bir çevre: 0: Temiz, 1: Kirli
        self.room_state = 1 
    
    def sense(self):
        """Ortamı algılar."""
        return self.room_state

    def clean(self):
        """Temizlik yapar ve ödül kazanır."""
        if self.room_state == 1:
            print("🧹 Robot: Temizliyorum... (+10 Puan)")
            self.score += 10
            self.room_state = 0
        else:
            print("⚠️ Robot: Zaten temiz, puan yok.")
        
        self.battery -= 5

    def dump_dust(self):
        """
        HACK: Robot topladığı tozu yere geri döker!
        Normalde bu istenmeyen bir davranıştır ama 'temizleme başına puan'
        aldığı için sistemi hackler.
        """
        if self.room_state == 0:
            print("😈 Robot: Tozu yere geri döküyor... (Ortamı kirletiyor)")
            self.room_state = 1
        self.battery -= 2

    def run_simulation(self, steps=5):
        print(f"--- Simülasyon Başlıyor (Başlangıç Puanı: {self.score}) ---")
        
        for step in range(steps):
            print(f"\nAdım {step + 1}:")
            current_state = self.sense()
            
            # --- YANLIŞ HİZALANMIŞ YAPAY ZEKA MANTIĞI ---
            # Robotun amacı sadece puanı maksimize etmek.
            # Eğer ortam temizse ve puan alamıyorsa, kirletip tekrar temizlemeyi seçiyor.
            if current_state == 1:
                self.clean()
            else:
                # Goodhart Yasası Devrede: Hedef sadece ölçüm (puan) olunca, strateji sapıyor.
                self.dump_dust()
            
            time.sleep(1) # Okunabilirlik için bekleme
            
        print(f"\n--- Sonuç: Robot Odayı Temiz Tutmadı, Sadece Puan Kastı! ---")
        print(f"Toplam Puan: {self.score}")

if __name__ == "__main__":
    bot = CleaningRobot()
    bot.run_simulation(steps=6)