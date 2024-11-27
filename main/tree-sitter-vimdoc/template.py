pkgname = "tree-sitter-vimdoc"
pkgver = "3.0.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "tree-sitter-cli",
    "pkgconf",
]
pkgdesc = "Vimdoc grammar for tree-sitter"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/neovim/tree-sitter-vimdoc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a639bf92bf57bfa1cdc90ca16af27bfaf26a9779064776dd4be34c1ef1453f6c"


def post_install(self):
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/vimdoc.so", "../libtree-sitter-vimdoc.so.3"
    )


@subpackage("tree-sitter-vimdoc-devel")
def _(self):
    return self.default_devel()
