pkgname = "fonts-commit-mono"
pkgver = "1.143"
pkgrel = 0
pkgdesc = "Programming fonts intended for readability"
license = "OFL-1.1"
url = "https://commitmono.com"
source = f"https://github.com/eigilnikolajsen/commit-mono/releases/download/v{pkgver}/CommitMono-{pkgver}.zip"
sha256 = "f7d1f26a7c7554800a996f76f5d706bf0648b936ca2a66b5bc4d46e3a2c49ed0"
options = ["empty"]


def install(self):
    self.install_file("*.otf", "usr/share/fonts/commit-mono", glob=True)
    self.install_file(
        "ttfautohint/*.ttf", "usr/share/fonts/commit-mono", glob=True
    )

    self.install_license("license.txt")


@subpackage("fonts-commit-mono-otf")
def _(self):
    self.subdesc = "OpenType"
    self.depends = [self.parent, "!fonts-commit-mono-ttf"]
    self.install_if = [self.parent]

    return ["usr/share/fonts/commit-mono/*.otf"]


@subpackage("fonts-commit-mono-ttf")
def _(self):
    self.subdesc = "TrueType"
    self.depends = [self.parent, "!fonts-commit-mono-otf"]

    return ["usr/share/fonts/commit-mono/*.ttf"]
