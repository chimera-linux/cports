pkgname = "tree-sitter"
# match to tree-sitter-cli
pkgver = "0.25.8"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
pkgdesc = "Incremental parsing library for language grammars"
license = "MIT"
url = "https://tree-sitter.github.io/tree-sitter"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "178b575244d967f4920a4642408dc4edf6de96948d37d7f06e5b78acee9c0b4e"
# check requires cargo/fixture stuff (from remote repositories)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tree-sitter-devel")
def _(self):
    return self.default_devel()
