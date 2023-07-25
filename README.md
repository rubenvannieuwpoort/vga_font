# VGA font extractor

Meant to extract an 8x16 font to a binary format (I used this for my implementation of text mode in my CPU implementation).

See https://int10h.org/oldschool-pc-fonts/fontlist/font?ibm_vga_8x16

## Running

```
git clone git@github.com:rubenvannieuwpoort/vga_font.git
cd vga_font
python3 -m venv .venv
source .venv/bin/activate
pip -r requirements.txt
python main.py
```
