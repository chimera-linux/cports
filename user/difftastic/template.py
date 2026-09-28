pkgname = "difftastic"
pkgver = "0.71.0"
pkgrel = 0
build_style = "cargo"
prepare_after_patch = True
hostmakedepends = [
    "cargo-auditable",
    "mdbook",
]
makedepends = [
    "rust-std",
]
pkgdesc = "Structural diff tool"
license = "MIT"
url = "https://difftastic.wilfred.me.uk"
source = (
    f"https://github.com/Wilfred/difftastic/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "d6afd26103c6492a91307dc6779c7dd0ca4d4c85499f81d7dc53fdfa5107331d"


def post_build(self):
    with self.pushd("manual"):
        self.do(
            "sed",
            "-ie",
            f"s/DFT_VERSION_HERE/{pkgver}/g",
            "src/introduction.md",
        )
        self.do("mdbook", "build")


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("difft.1")
    self.install_files("manual/book", "usr/share/doc", name="difftastic")
