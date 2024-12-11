pkgname = "mint-themes"
pkgver = "2.2.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = [
    "bash",
    "gsed",
    "python",
    "libsass-python",
]
pkgdesc = "Mint-X and Mint-Y themes"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://projects.linuxmint.com/mint"
source = f"https://github.com/linuxmint/mint-themes/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8d4276e07d306529c2da449ec252431e9d50edd40bbfefeff6403ddd31fed892"
# No tests
options = ["!check"]
exec_wrappers = [("/usr/bin/gsed", "sed")]


def install(self):
    self.install_files("usr", "")
