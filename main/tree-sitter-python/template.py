pkgname = "tree-sitter-python"
pkgver = "0.21.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "Python grammar for tree-sitter"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/tree-sitter/tree-sitter-python"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "720304a603271fa89e4430a14d6a81a023d6d7d1171b1533e49c0ab44f1e1c13"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/python.so", "../libtree-sitter-python.so.0"
    )


@subpackage("tree-sitter-python-devel")
def _(self):
    return self.default_devel()
