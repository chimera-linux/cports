pkgname = "difftastic"
pkgver = "0.72.0"
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
sha256 = "ed8e2d59d44d62289b17c9d241e469bd72565fadf13c260676fc7a23bc28a844"


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
