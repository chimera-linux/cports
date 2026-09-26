pkgname = "mergiraf"
pkgver = "0.19.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
checkdepends = ["git", "jj"]
pkgdesc = "Syntax-aware git merge driver"
license = "GPL-3.0-only"
url = "https://mergiraf.org"
source = f"https://codeberg.org/mergiraf/mergiraf/archive/v{pkgver}.tar.gz"
sha256 = "36ccbbd80a3f79bdb23e9e087c9109aeaaed9cc80d85a7722c8db0c0295d107f"


def post_install(self):
    self.install_license("LICENSE.txt")
    self.install_file("doc/src/*.md", "usr/share/doc/mergiraf", glob=True)
    self.install_files("doc/src/adding-a-language", "usr/share/doc/mergiraf")
    self.install_files("helpers", "usr/share/mergiraf")


@subpackage("mergiraf-helpers")
def _(self):
    self.depends = ["bash"]
    self.subdesc = "helper scripts"

    return ["usr/share/mergiraf/helpers"]
