pkgname = "tree-sitter-vimdoc"
pkgver = "4.0.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "Vimdoc grammar for tree-sitter"
license = "Apache-2.0"
url = "https://github.com/neovim/tree-sitter-vimdoc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8096794c0f090b2d74b7bff94548ac1be3285b929ec74f839bd9b3ff4f4c6a0b"


def post_install(self):
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/vimdoc.so", "../libtree-sitter-vimdoc.so.4"
    )


@subpackage("tree-sitter-vimdoc-devel")
def _(self):
    return self.default_devel()
