pkgname = "tree-sitter-python"
pkgver = "0.23.6"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "Python grammar for tree-sitter"
license = "MIT"
url = "https://github.com/tree-sitter/tree-sitter-python"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "630a0f45eccd9b69a66a07bf47d1568e96a9c855a2f30e0921c8af7121e8af96"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/python.so", "../libtree-sitter-python.so.14"
    )


@subpackage("tree-sitter-python-devel")
def _(self):
    return self.default_devel()
