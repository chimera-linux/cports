pkgname = "bibata-cursor"
pkgver = "2.0.6"
pkgrel = 1
pkgdesc = "Material design cursor set"
maintainer = "ogromny <ogromnycoding@gmail.com>"
license = "GPL-3.0-only"
url = "https://github.com/ful1e5/Bibata_Cursor"
source = f"https://github.com/ful1e5/Bibata_Cursor/releases/download/v{pkgver}/Bibata.tar.xz"
sha256 = "88252b36063a85e8f2123502917c7e64296a94290d08731884625d7436bd24cb"


def do_install(self):
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
