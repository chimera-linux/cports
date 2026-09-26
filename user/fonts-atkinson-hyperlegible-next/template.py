pkgname = "fonts-atkinson-hyperlegible-next"
pkgver = "20210430"
pkgrel = 0
pkgdesc = "New (2024) second version of the Atkinson Hyperlegible fonts"
license = "OFL-1.1"
url = "https://www.brailleinstitute.org/freefont"
source = "https://github.com/googlefonts/atkinson-hyperlegible-next/archive/7925f50f649b3813257faf2f4c0b381011f434f1.tar.gz"
sha256 = "4b455dcf5ce2d6261df7caf6f4d035c893b446f14269106a07bc03c204368626"
options = ["empty"]


def install(self):
    self.install_file(
        "fonts/ttf/*.ttf",
        "usr/share/fonts/atkinson-hyperlegible-next",
        glob=True,
    )
    self.install_file(
        "fonts/otf/*.otf",
        "usr/share/fonts/atkinson-hyperlegible-next",
        glob=True,
    )
    self.install_license("OFL.txt")


@subpackage("fonts-atkinson-hyperlegible-next-otf")
def _(self):
    self.subdesc = "OpenType"
    self.depends = [self.parent, "!atkinson-hyperlegible-next-ttf"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/atkinson-hyperlegible-next/*.otf"]


@subpackage("fonts-atkinson-hyperlegible-next-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent, "!fonts-atkinson-hyperlegible-next-otf"]

    return ["usr/share/fonts/atkinson-hyperlegible-next/*.ttf"]
