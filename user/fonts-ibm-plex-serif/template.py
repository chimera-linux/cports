pkgname = "fonts-ibm-plex-serif"
pkgver = "2.0.0"
pkgrel = 0
pkgdesc = "IBM's typeface, IBM Plex Serif"
license = "OFL-1.1"
url = "https://www.ibm.com/plex"
source = f"https://github.com/IBM/plex/releases/download/%40ibm%2Fplex-serif%40{pkgver}/ibm-plex-serif.zip"
sha256 = "c006b095c47b919c6c8d78319e9e628745033f5db94507c1c9dfe4b35dd51f1e"
options = ["empty"]


def install(self):
    self.install_file(
        "fonts/complete/otf/*.otf", "usr/share/fonts/ibm-plex", glob=True
    )
    self.install_file(
        "fonts/complete/ttf/*.ttf", "usr/share/fonts/ibm-plex", glob=True
    )
    self.install_license("LICENSE.txt")


@subpackage("fonts-ibm-plex-serif-otf")
def _(self):
    self.subdesc = "OpenType"
    self.depends = [self.parent, "!fonts-ibm-plex-serif-ttf"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/ibm-plex/*.otf"]


@subpackage("fonts-ibm-plex-serif-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent, "!fonts-ibm-plex-serif-otf"]

    return ["usr/share/fonts/ibm-plex/*.ttf"]
