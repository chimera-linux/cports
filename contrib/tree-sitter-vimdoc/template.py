pkgname = "tree-sitter-vimdoc"
pkgver = "2.5.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = [
    "gmake",
    "tree-sitter-cli",
    "pkgconf",
]
pkgdesc = "Vimdoc grammar for tree-sitter"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/neovim/tree-sitter-vimdoc"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "063645096504b21603585507c41c6d8718ff3c11b2150c5bfc31e8f3ee9afea3"


def post_install(self):
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/vimdoc.so", "../libtree-sitter-vimdoc.so.2"
    )
    self.install_files("queries/vimdoc", "usr/share/tree-sitter/queries")


@subpackage("tree-sitter-vimdoc-devel")
def _devel(self):
    return self.default_devel()
