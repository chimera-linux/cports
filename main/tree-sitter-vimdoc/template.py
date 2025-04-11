pkgname = "tree-sitter-vimdoc"
pkgver = "3.0.1"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "tree-sitter-cli",
    "pkgconf",
]
pkgdesc = "Vimdoc grammar for tree-sitter"
license = "Apache-2.0"
url = "https://github.com/neovim/tree-sitter-vimdoc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "76b65e5bee9ff78eb21256619b1995aac4d80f252c19e1c710a4839481ded09e"


def post_install(self):
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/vimdoc.so", "../libtree-sitter-vimdoc.so.3"
    )


@subpackage("tree-sitter-vimdoc-devel")
def _(self):
    return self.default_devel()
