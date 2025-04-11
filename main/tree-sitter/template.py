pkgname = "tree-sitter"
# match to tree-sitter-cli
pkgver = "0.25.3"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
pkgdesc = "Incremental parsing library for language grammars"
license = "MIT"
url = "https://tree-sitter.github.io/tree-sitter"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "862fac52653bc7bc9d2cd0630483e6bdf3d02bcd23da956ca32663c4798a93e3"
# check requires cargo/fixture stuff (from remote repositories)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tree-sitter-devel")
def _(self):
    return self.default_devel()
