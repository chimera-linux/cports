pkgname = "fonts-commit-mono"
pkgver = "1.143"
pkgrel = 0
pkgdesc = (
    "Anonymous and neutral programming typeface for better reading experience"
)
license = "OFL-1.1"
url = "https://commitmono.com"
source = f"https://github.com/eigilnikolajsen/commit-mono/releases/download/v{pkgver}/CommitMono-{pkgver}.zip"
sha256 = "f7d1f26a7c7554800a996f76f5d706bf0648b936ca2a66b5bc4d46e3a2c49ed0"
options = ["empty"]

_install_dir = "usr/share/fonts/commit-mono"


def install(self):
    self.install_file("*.otf", _install_dir, glob=True)
    self.install_file("ttfautohint/*.ttf", _install_dir, glob=True)

    self.install_license("license.txt")


@subpackage("fonts-commit-mono-otf")
def _(self):
    self.subdesc = "OpenType"
    self.depends = [self.parent, "!fonts-commit-mono-ttf"]
    self.install_if = [self.parent]

    return [_install_dir + "/*.otf"]


@subpackage("fonts-commit-mono-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent, "!fonts-commit-mono-otf"]

    return [_install_dir + "/*.ttf"]
