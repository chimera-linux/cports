pkgname = "bibata-cursor"
pkgver = "2.0.7"
pkgrel = 0
pkgdesc = "Material design cursor set"
maintainer = "ogromny <ogromnycoding@gmail.com>"
license = "GPL-3.0-only"
url = "https://github.com/ful1e5/Bibata_Cursor"
source = f"https://github.com/ful1e5/Bibata_Cursor/releases/download/v{pkgver}/Bibata.tar.xz"
sha256 = "172e33c4ae415278384dcecc7d1a9b7a024266bc944bc751fd86532be1cc6251"


def install(self):
    themes = [
        "Bibata-Modern-Amber",
        "Bibata-Modern-Amber-Right",
        "Bibata-Modern-Classic",
        "Bibata-Modern-Classic-Right",
        "Bibata-Modern-Ice",
        "Bibata-Modern-Ice-Right",
        "Bibata-Original-Amber",
        "Bibata-Original-Amber-Right",
        "Bibata-Original-Classic",
        "Bibata-Original-Classic-Right",
        "Bibata-Original-Ice",
        "Bibata-Original-Ice-Right",
    ]
    for theme in themes:
        self.install_files(theme, "usr/share/icons")
