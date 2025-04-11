pkgname = "tree-sitter-c"
pkgver = "0.23.5"
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
sha256 = "f7e50412230150ce514efcccb962ff9b452d9f358e0a2c89f2a0a0256c2ec886"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link("usr/lib/tree-sitter/c.so", "../libtree-sitter-c.so.14")


@subpackage("tree-sitter-c-devel")
def _(self):
    return self.default_devel()
