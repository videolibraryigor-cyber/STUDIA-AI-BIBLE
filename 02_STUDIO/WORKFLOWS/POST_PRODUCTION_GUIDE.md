# POST-PRODUCTION & COLOR SCIENCE GUIDE
## AI FILM STUDIO — EDITORIAL, COLOR & CONFORMING

**Status:** ACTIVE v1.0  
**Authority:** COLORIST / POST-PRODUCTION SUPERVISOR  
**Reference:** `08_MASTER_STYLE/MASTER_STYLE_v2.md`, `08_MASTER_STYLE/MASTER_STYLE_ENHANCEMENT_v2.1.md`  

---

## 1. Color Management Architecture (Архитектура цвета)

Для объединения генераций из различных нейросетей (Midjourney, Flux, Kling, Runway Gen-3) в единый визуальный ряд применяется стандартизированный цветовой пайплайн.

### DaVinci Resolve Settings:
* **Color Science:** `DaVinci YRGB Color Managed` или `ACEScct (ACES 1.3)`.
* **Input Color Space:** `Rec.709 / Gamma 2.4` (для стандартных генераций) или `sRGB`.
* **Timeline Color Space:** `DaVinci Wide Gamut / Intermediate`.
* **Output Color Space:** `Rec.709 / Gamma 2.4` (Master Export) или `DCI-P3` (Cinema).

---

## 2. Master Style Look & Film Emulation (Эмуляция кинопленки)

### Photochemical Film Print Emulation:
* **Target Stock:** `Kodak 5207 Vision3 250D` (для дневных сцен и заката) / `Kodak 5219 Vision3 500T` (для ночных сцен со свечами).
* **Highlight Rolloff:** Мягкая компрессия ярких участков (Soft Clip) без жесткого цифрового отсечения (clipping).
* **Shadow Density:** Глубокие, но читаемые тени с легким теплым отпечатком известняка.
* **Skin Tones:** Строгое следование вектору тона кожи на векторскопе (Mediterranean Olive/Golden tones). Исключить цифровой magenta/green сдвиг.

---

## 3. Aspect Ratio & Optical Texture (Геометрия и зерно)

1. **Aspect Ratio:** `CinemaScope 2.39:1` (Letterbox 3840x1608 для 4K UHD).
2. **Organic Film Grain Overlay:**
   * Сканированное зерно 35mm / 65mm (Real 4K Film Grain Plate).
   * Режим наложения: `Overlay / Soft Light` с прозрачностью 15–22%.
   * Функция: маскирует микро-артефакты генерации и связывает слои изображения.
3. **Halation & Optical Glow:**
   * Деликатный теплый ореол вокруг ярких источников (пламя свечи, край окна) с радиусом 4–8 пикселей.

---

## 4. Timeline Conforming & Export Standards (Стандарты экспорта)

* **Master Video Codec:** `Apple ProRes 422 HQ` / `Avid DNxHR HQX` (4K 24.000 fps).
* **Delivery Web Codec:** `H.265 / HEVC 10-bit` (CBR 45 Mbps, Rec.709).
* **Master Audio:** Linear PCM 24-bit 48 kHz Stereo / 5.1 Surround.
