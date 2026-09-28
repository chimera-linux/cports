pkgname = "fonts-ibm-plex-sans"
pkgver = "1.1.0"
pkgrel = 0
pkgdesc = "IBM's typeface, IBM Plex Sans"
license = "OFL-1.1"
url = "https://www.ibm.com/plex"
source = f"https://github.com/IBM/plex/releases/download/%40ibm%2Fplex-sans%40{pkgver}/ibm-plex-sans.zip"
sha256 = "fb365d910566e6d199cc2c15579a7dd9a267128e18431a394ed81f1970c69200"
options = ["empty"]


def install(self):
    self.install_file(
        "fonts/complete/otf/*.otf", "usr/share/fonts/ibm-plex", glob=True
    )
    self.install_file(
        "fonts/complete/ttf/*.ttf", "usr/share/fonts/ibm-plex", glob=True
    )
    self.install_license("LICENSE.txt")


@subpackage("fonts-ibm-plex-sans-otf")
def _(self):
    self.subdesc = "OpenType"
    self.depends = [self.parent, "!fonts-ibm-plex-sans-ttf"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/ibm-plex/*.otf"]


@subpackage("fonts-ibm-plex-sans-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent, "!fonts-ibm-plex-sans-otf"]

    return ["usr/share/fonts/ibm-plex/*.ttf"]
