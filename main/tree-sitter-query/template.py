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
    "https://github.com/nvim-treesitter/nvim-treesitter/archive/9866036ec3c5db40700a9178494e0cfdcfe6ecfd.tar.gz",
    "https://github.com/nvim-treesitter/nvim-treesitter-textobjects/archive/71385f191ec06ffc60e80e6b0c9a9d5daed4824c.tar.gz",
]
source_paths = [
    ".",
    ".tests/nvim-treesitter",
    ".tests/nvim-treesitter-textobjects",
]
sha256 = [
    "c2b23b9a54cffcc999ded4a5d3949daf338bebb7945dece229f832332e6e6a7d",
    "e5d345447a560d50e8e926a657c772060b17665cf34ba296d413af46e3411c00",
    "ff6435187774f11f846420de3a982d754c105c86cbab0cb1bd76384eb209bbfd",
]


def post_install(self):
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/query.so", "../libtree-sitter-query.so.15"
    )


@subpackage("tree-sitter-query-devel")
def _(self):
    return self.default_devel()
