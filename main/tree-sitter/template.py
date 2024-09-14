pkgname = "tree-sitter"
# match to tree-sitter-cli
pkgver = "0.23.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
pkgdesc = "Incremental parsing library for language grammars"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "https://tree-sitter.github.io/tree-sitter"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "6403b361b0014999e96f61b9c84d6950d42f0c7d6e806be79382e0232e48a11b"
# check requires cargo/fixture stuff (from remote repositories)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tree-sitter-devel")
def _(self):
    return self.default_devel()
