pkgname = "tree-sitter"
# match to tree-sitter-cli
pkgver = "0.25.2"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
pkgdesc = "Incremental parsing library for language grammars"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "https://tree-sitter.github.io/tree-sitter"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "26791f69182192fef179cd58501c3226011158823557a86fe42682cb4a138523"
# check requires cargo/fixture stuff (from remote repositories)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tree-sitter-devel")
def _(self):
    return self.default_devel()
