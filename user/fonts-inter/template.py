pkgname = "fonts-inter"
pkgver = "4.0"
pkgrel = 0
pkgdesc = "Inter typeface family"
maintainer = "beb <beb_@tutamail.com>"
license = "OFL-1.1"
url = "https://rsms.me/inter"
source = f"https://github.com/rsms/inter/releases/download/v{pkgver}/Inter-{pkgver}.zip"
sha256 = "ff970a5d4561a04f102a7cb781adbd6ac4e9b6c460914c7a101f15acb7f7d1a4"
options = ["empty"]


def install(self):
    self.install_file("*.ttf", "usr/share/fonts/inter", glob=True)
    self.install_file("extras/ttf/*.ttf", "usr/share/fonts/inter", glob=True)
    self.install_file("extras/otf/*.otf", "usr/share/fonts/inter", glob=True)
    self.install_license("LICENSE.txt")


@subpackage("fonts-inter-otf")
def _(self):
    self.subdesc = "OpenType"
    self.depends = [self.parent, "!fonts-inter-ttf"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/inter/*.otf"]


@subpackage("fonts-inter-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent, "!fonts-inter-otf"]

    return ["usr/share/fonts/inter/*.ttf"]
