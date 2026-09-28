pkgname = "fonts-ibm-plex-mono"
pkgver = "2.5.0"
pkgrel = 0
pkgdesc = "IBM's typeface, IBM Plex Mono"
license = "OFL-1.1"
url = "https://www.ibm.com/plex"
source = f"https://github.com/IBM/plex/releases/download/%40ibm%2Fplex-mono%40{pkgver}/ibm-plex-mono.zip"
sha256 = "6d23f01257663d8cc49a0d64c22ced630b79e0e2a0ac08a0da86e9a38bbc481c"
options = ["empty"]


def install(self):
    self.install_file(
        "fonts/complete/otf/*.otf", "usr/share/fonts/ibm-plex", glob=True
    )
    self.install_file(
        "fonts/complete/ttf/*.ttf", "usr/share/fonts/ibm-plex", glob=True
    )
    self.install_license("LICENSE.txt")


@subpackage("fonts-ibm-plex-mono-otf")
def _(self):
    self.subdesc = "OpenType"
    self.depends = [self.parent, "!fonts-ibm-plex-mono-ttf"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/ibm-plex/*.otf"]


@subpackage("fonts-ibm-plex-mono-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent, "!fonts-ibm-plex-mono-otf"]

    return ["usr/share/fonts/ibm-plex/*.ttf"]
