pkgname = "fonts-stix"
pkgver = "2.14"
pkgrel = 0
pkgdesc = "Fonts for scientific, technical and mathematical texts"
license = "OFL-1.1"
url = "https://www.stixfonts.org"
source = [
    f"https://github.com/stipub/stixfonts/releases/download/v{pkgver}/fonts.zip",
    f"!https://raw.githubusercontent.com/stipub/stixfonts/refs/tags/v{pkgver}/OFL.txt",
]
sha256 = [
    "b9ce7effe9cf97185bc3bfd9b3c5e79e0928a500127d1f55d0a704e04d274420",
    "0c8825913b60d858aacdb33c4ca6660a7d64b0d6464702efbb19313f5765861a",
]
options = ["empty"]


def install(self):
    self.install_file("fonts/*/*/*.otf", "usr/share/fonts/stix", glob=True)
    self.install_file("fonts/*/*/*.ttf", "usr/share/fonts/stix", glob=True)
    self.install_license(self.sources_path / "OFL.txt")


@subpackage("fonts-stix-otf")
def _(self):
    self.subdesc = "OpenType"
    self.depends = [self.parent, "!fonts-stix-ttf"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/stix/*.otf"]


@subpackage("fonts-stix-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent, "!fonts-stix-otf"]

    return ["usr/share/fonts/stix/*.ttf"]
