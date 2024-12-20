pkgname = "tree-sitter"
# match to tree-sitter-cli
pkgver = "0.24.5"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
pkgdesc = "Incremental parsing library for language grammars"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "https://tree-sitter.github.io/tree-sitter"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "b5ac48acf5a04fd82ccd4246ad46354d9c434be26c9606233917549711e4252c"
# check requires cargo/fixture stuff (from remote repositories)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tree-sitter-devel")
def _(self):
    return self.default_devel()
