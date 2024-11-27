pkgname = "xplr"
pkgver = "0.21.9"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--no-default-features"]
make_install_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "luajit-devel",
    "rust-std",
]
pkgdesc = "TUI file explorer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://xplr.dev"
source = (
    f"https://github.com/sayanarijit/xplr/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "345400c2fb7046963b2e0fcca8802b6e523e0fb742d0d893cb7fd42f10072a55"
# needs rebuild with non-release to use bin from debug/
options = ["!check"]


def post_extract(self):
    self.rm(".cargo/config")


def post_install(self):
    self.install_license("LICENSE")
    self.install_file("assets/desktop/xplr.desktop", "usr/share/applications")
    self.install_file(
        "assets/icon/xplr.svg", "usr/share/icons/hicolor/scalable/apps"
    )
    for s in ["16", "32", "64", "128"]:
        self.install_file(
            f"assets/icon/xplr{s}.png",
            f"usr/share/icons/hicolor/{s}x{s}/apps",
            name="xplr.png",
        )
