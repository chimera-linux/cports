pkgname = "tree-sitter-c"
pkgver = "0.21.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "C grammar for tree-sitter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/tree-sitter/tree-sitter-c"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6f0f5d1b71cf8ffd8a37fb638c6022fa1245bd630150b538547d52128ce0ea7e"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link("usr/lib/tree-sitter/c.so", "../libtree-sitter-c.so.0")


@subpackage("tree-sitter-c-devel")
def _devel(self):
    return self.default_devel()
