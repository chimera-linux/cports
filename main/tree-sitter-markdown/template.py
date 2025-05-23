pkgname = "tree-sitter-markdown"
pkgver = "0.5.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "nodejs",
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "Markdown grammar for tree-sitter"
license = "MIT"
url = "https://github.com/tree-sitter-grammars/tree-sitter-markdown"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "14c2c948ccf0e9b606eec39b09286c59dddf28307849f71b7ce2b1d1ef06937e"


def configure(self):
    for x in ("tree-sitter-markdown", "tree-sitter-markdown-inline"):
        with self.pushd(x):
            self.do(
                "tree-sitter",
                "generate",
                env={"ALL_EXTENSIONS": "1"},
            )
    # weird bug with the make stuff
    self.cp("tree-sitter-markdown/grammar.js", "tree-sitter-markdown/src")
    self.cp(
        "tree-sitter-markdown-inline/grammar.js",
        "tree-sitter-markdown-inline/src",
    )


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/markdown.so",
        "../libtree-sitter-markdown.so.15",
    )
    self.install_link(
        "usr/lib/tree-sitter/markdown_inline.so",
        "../libtree-sitter-markdown-inline.so.15",
    )


@subpackage("tree-sitter-markdown-devel")
def _(self):
    return self.default_devel()
