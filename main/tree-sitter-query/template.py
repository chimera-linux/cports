pkgname = "tree-sitter-query"
pkgver = "0.8.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "Tree-sitter query grammar for tree-sitter"
license = "Apache-2.0"
url = "https://github.com/tree-sitter-grammars/tree-sitter-query"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/nvim-treesitter/nvim-treesitter/archive/42fc28ba918343ebfd5565147a42a26580579482.tar.gz",
    "https://github.com/nvim-treesitter/nvim-treesitter-textobjects/archive/5ca4aaa6efdcc59be46b95a3e876300cfead05ef.tar.gz",
]
source_paths = [
    ".",
    ".tests/nvim-treesitter",
    ".tests/nvim-treesitter-textobjects",
]
sha256 = [
    "c2b23b9a54cffcc999ded4a5d3949daf338bebb7945dece229f832332e6e6a7d",
    "91c764237034be845648581b39e76f197a38b93e41199055400e2851076a1498",
    "c38279bbfedd4a1859d5f3ebdb8641201b3140365c197b68d8a9be092ef7b686",
]


def post_install(self):
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/query.so", "../libtree-sitter-query.so.15"
    )


@subpackage("tree-sitter-query-devel")
def _(self):
    return self.default_devel()
