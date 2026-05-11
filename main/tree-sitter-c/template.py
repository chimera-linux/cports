pkgname = "tree-sitter-c"
pkgver = "0.24.2"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "C grammar for tree-sitter"
license = "MIT"
url = "https://github.com/tree-sitter/tree-sitter-c"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2eeb4db31f8fa0865e45488503d13403923bcb485a1bdb637abff8c42dd97364"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link("usr/lib/tree-sitter/c.so", "../libtree-sitter-c.so.15")


@subpackage("tree-sitter-c-devel")
def _(self):
    return self.default_devel()
