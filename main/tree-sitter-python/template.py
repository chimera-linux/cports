pkgname = "tree-sitter-python"
pkgver = "0.25.0"
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
sha256 = "4609a3665a620e117acf795ff01b9e965880f81745f287a16336f4ca86cf270c"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/python.so", "../libtree-sitter-python.so.15"
    )


@subpackage("tree-sitter-python-devel")
def _(self):
    return self.default_devel()
