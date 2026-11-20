pkgname = "fonts-atkinson-hyperlegible-next-mono"
pkgver = "2.1"
pkgrel = 0
_commit = "154d50362016cc3e873eb21d242cd0772384c8f9"
pkgdesc = "New (2024) monospace sibling family to Atkinson Hyperlegible Next"
license = "OFL-1.1"
url = "https://www.brailleinstitute.org/freefont"
source = f"https://github.com/googlefonts/atkinson-hyperlegible-next-mono/archive/{_commit}.tar.gz"
sha256 = "d8b50ca876781ef6c2f0e1dd1a7ed6896a7f7769242e76be901b98c6d7edfafb"
options = ["empty"]


def install(self):
    self.install_file(
        "fonts/ttf/*.ttf",
        "usr/share/fonts/atkinson-hyperlegible-next-mono",
        glob=True,
    )
    self.install_file(
        "fonts/otf/*.otf",
        "usr/share/fonts/atkinson-hyperlegible-next-mono",
        glob=True,
    )
    self.install_license("OFL.txt")


@subpackage("fonts-atkinson-hyperlegible-next-mono-otf")
def _(self):
    self.subdesc = "OpenType"
    self.depends = [self.parent, "!atkinson-hyperlegible-next-mono-ttf"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/atkinson-hyperlegible-next-mono/*.otf"]


@subpackage("fonts-atkinson-hyperlegible-next-mono-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent, "!fonts-atkinson-hyperlegible-next-mono-otf"]

    return ["usr/share/fonts/atkinson-hyperlegible-next-mono/*.ttf"]
