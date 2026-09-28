pkgname = "mergiraf"
pkgver = "0.20.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
checkdepends = ["git", "jj"]
pkgdesc = "Syntax-aware git merge driver"
license = "GPL-3.0-only"
url = "https://mergiraf.org"
source = f"https://codeberg.org/mergiraf/mergiraf/archive/v{pkgver}.tar.gz"
sha256 = "85a1dc9e60e8ebc22ffe161cc08cb998f18f5e27b7e23319f35328a69a95fd10"


def post_install(self):
    self.install_license("LICENSE.txt")
    self.install_file("doc/src/*.md", "usr/share/doc/mergiraf", glob=True)
    self.install_files("doc/src/adding-a-language", "usr/share/doc/mergiraf")
