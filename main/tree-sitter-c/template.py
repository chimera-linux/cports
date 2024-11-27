pkgname = "tree-sitter-c"
pkgver = "0.21.3"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "C grammar for tree-sitter"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/tree-sitter/tree-sitter-c"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "75a3780df6114cd37496761c4a7c9fd900c78bee3a2707f590d78c0ca3a24368"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link("usr/lib/tree-sitter/c.so", "../libtree-sitter-c.so.0")


@subpackage("tree-sitter-c-devel")
def _(self):
    return self.default_devel()
