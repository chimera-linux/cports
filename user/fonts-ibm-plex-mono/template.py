pkgname = "fonts-ibm-plex-mono"
pkgver = "1.1.0"
pkgrel = 0
pkgdesc = "IBM's typeface, IBM Plex Mono"
license = "OFL-1.1"
url = "https://www.ibm.com/plex"
source = f"https://github.com/IBM/plex/releases/download/%40ibm%2Fplex-mono%40{pkgver}/ibm-plex-mono.zip"
sha256 = "4bfc936d0e1fd19db6327a3786eabdbc3dc0d464500576f6458f6706df68d26c"
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
