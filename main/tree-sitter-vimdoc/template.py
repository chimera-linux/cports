pkgname = "tree-sitter-vimdoc"
pkgver = "4.1.0"
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
sha256 = "020e8f117f648c8697fca967995c342e92dbd81dab137a115cc7555207fbc84f"


def post_install(self):
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/vimdoc.so", "../libtree-sitter-vimdoc.so.4"
    )


@subpackage("tree-sitter-vimdoc-devel")
def _(self):
    return self.default_devel()
