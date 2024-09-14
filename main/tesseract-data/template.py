pkgname = "tesseract-data"
pkgver = "4.1.0"
pkgrel = 0
pkgdesc = "OCR engine"
subdesc = "language files"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://tesseract-ocr.github.io"
source = f"https://github.com/tesseract-ocr/tessdata_fast/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d0e3bb6f3b4e75748680524a1d116f2bfb145618f8ceed55b279d15098a530f9"
options = ["empty"]


def install(self):
    self.install_file("*.traineddata", "usr/share/tessdata", glob=True)
    self.install_files("script", "usr/share/tessdata")


def _gen_scriptp(code, name):
    @subpackage(f"tesseract-data-script-{code.lower()}")
    def _(self):
        self.subdesc = f"language files for {name} script"
        self.install_if = [self.parent]

        return [f"usr/share/tessdata/script/{code}.*"]


_scripts = [
    ("Arabic", "Arabic"),
    ("Armenian", "Armenian"),
    ("Bengali", "Bengali"),
    ("Canadian_Aboriginal", "Canadian Aboriginal"),
    ("Cherokee", "Cherokee"),
    ("Cyrillic", "Cyrillic"),
    ("Devanagari", "Devanagari"),
    ("Ethiopic", "Ethiopic"),
    ("Fraktur", "Fraktur"),
    ("Georgian", "Georgian"),
    ("Greek", "Greek"),
    ("Gujarati", "Gujarati"),
    ("Gurmukhi", "Gurmukhi"),
    ("HanS", "Han - Simplified"),
    ("HanS_vert", "Han - Simplified, vertical"),
    ("HanT", "Han - Traditional"),
    ("HanT_vert", "Han - Traditional, vertical"),
    ("Hangul", "Hangul"),
    ("Hangul_vert", "Hangul, vertical"),
    ("Hebrew", "Hebrew"),
    ("Japanese", "Japanese"),
    ("Japanese_vert", "Japanese, vertical"),
    ("Kannada", "Kannada"),
    ("Khmer", "Khmer"),
    ("Lao", "Lao"),
    ("Latin", "Latin"),
    ("Malayalam", "Malayalam"),
    ("Myanmar", "Myanmar"),
    ("Oriya", "Oriya"),
    ("Sinhala", "Sinhala"),
    ("Syriac", "Syriac"),
    ("Tamil", "Tamil"),
    ("Telugu", "Telugu"),
    ("Thaana", "Thaana"),
    ("Thai", "Thai"),
    ("Tibetan", "Tibetan"),
    ("Vietnamese", "Vietnamese"),
]

for _code, _name in _scripts:
    _gen_scriptp(_code, _name)


def _gen_langp(code, name):
    @subpackage(f"tesseract-data-{code}")
    def _(self):
        self.subdesc = f"language files for {name}"
        self.install_if = [self.parent]

        return [f"usr/share/tessdata/{code}.*"]


_langs = [
    ("afr", "Afrikaans"),
    ("amh", "Amharic"),
    ("ara", "Arabic"),
    ("asm", "Assamese"),
    ("aze", "Azerbaijani"),
    ("aze_cyrl", "Azerbaijani - Cyrillic"),
    ("bel", "Belarusian"),
    ("ben", "Bengali"),
    ("bod", "Tibetan"),
    ("bos", "Bosnian"),
    ("bre", "Breton"),
    ("bul", "Bulgarian"),
    ("cat", "Catalan; Valencian"),
    ("ceb", "Cebuano"),
    ("ces", "Czech"),
    ("chi_sim", "Chinese - Simplified"),
    ("chi_sim_vert", "Chinese - Simplified, vertical"),
    ("chi_tra", "Chinese - Traditional"),
    ("chi_tra_vert", "Chinese - Traditional, vertical"),
    ("chr", "Cherokee"),
    ("cos", "Corsican"),
    ("cym", "Welsh"),
    ("dan", "Danish"),
    ("deu", "German"),
    ("div", "Divehi"),
    ("dzo", "Dzongkha"),
    ("ell", "Greek, Modern (1453-)"),
    ("eng", "English"),
    ("enm", "English, Middle (1100-1500)"),
    ("epo", "Esperanto"),
    ("equ", "equations"),
    ("est", "Estonian"),
    ("eus", "Basque"),
    ("fao", "Faroese"),
    ("fas", "Persian"),
    ("fil", "Filipino"),
    ("fin", "Finnish"),
    ("fra", "French"),
    ("frk", "German Fraktur"),
    ("frm", "French, Middle (ca. 1400-1600)"),
    ("fry", "Frisian, western"),
    ("gla", "Gaelic, scots"),
    ("gle", "Irish"),
    ("glg", "Galician"),
    ("grc", "Greek, Ancient (-1453)"),
    ("guj", "Gujarati"),
    ("hat", "Haitian; Haitian Creole"),
    ("heb", "Hebrew"),
    ("hin", "Hindi"),
    ("hrv", "Croatian"),
    ("hun", "Hungarian"),
    ("hye", "Armenian"),
    ("iku", "Inuktitut"),
    ("ind", "Indonesian"),
    ("isl", "Icelandic"),
    ("ita", "Italian"),
    ("ita_old", "Italian - Old"),
    ("jav", "Javanese"),
    ("jpn", "Japanese"),
    ("jpn_vert", "Japanese, vertical"),
    ("kan", "Kannada"),
    ("kat", "Georgian"),
    ("kat_old", "Georgian - Old"),
    ("kaz", "Kazakh"),
    ("khm", "Central Khmer"),
    ("kir", "Kirghiz; Kyrgyz"),
    ("kmr", "Kurmanji, latin"),
    ("kor", "Korean"),
    ("kor_vert", "Korean, vertical"),
    ("lao", "Lao"),
    ("lat", "Latin"),
    ("lav", "Latvian"),
    ("lit", "Lithuanian"),
    ("ltz", "Luxembourgish"),
    ("mal", "Malayalam"),
    ("mar", "Marathi"),
    ("mkd", "Macedonian"),
    ("mlt", "Maltese"),
    ("mon", "Mongolian"),
    ("mri", "Maori"),
    ("msa", "Malay"),
    ("mya", "Burmese"),
    ("nep", "Nepali"),
    ("nld", "Dutch; Flemish"),
    ("nor", "Norwegian"),
    ("oci", "Occitan, post 1500"),
    ("ori", "Oriya"),
    ("osd", "script and orientation"),
    ("pan", "Panjabi; Punjabi"),
    ("pol", "Polish"),
    ("por", "Portuguese"),
    ("pus", "Pushto; Pashto"),
    ("que", "Quechua"),
    ("ron", "Romanian; Moldavian; Moldovan"),
    ("rus", "Russian"),
    ("san", "Sanskrit"),
    ("sin", "Sinhala; Sinhalese"),
    ("slk", "Slovak"),
    ("slv", "Slovenian"),
    ("snd", "Sindhi"),
    ("spa", "Spanish; Castilian"),
    ("spa_old", "Spanish; Castilian - Old"),
    ("sqi", "Albanian"),
    ("srp", "Serbian"),
    ("srp_latn", "Serbian - Latin"),
    ("sun", "Sundanese"),
    ("swa", "Swahili"),
    ("swe", "Swedish"),
    ("syr", "Syriac"),
    ("tam", "Tamil"),
    ("tat", "Tatar"),
    ("tel", "Telugu"),
    ("tgk", "Tajik"),
    ("tha", "Thai"),
    ("tir", "Tigrinya"),
    ("ton", "Tonga"),
    ("tur", "Turkish"),
    ("uig", "Uighur; Uyghur"),
    ("ukr", "Ukrainian"),
    ("urd", "Urdu"),
    ("uzb", "Uzbek"),
    ("uzb_cyrl", "Uzbek - Cyrillic"),
    ("vie", "Vietnamese"),
    ("yid", "Yiddish"),
    ("yor", "Yoruba"),
]

for _code, _name in _langs:
    _gen_langp(_code, _name)
