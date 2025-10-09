pkgname = "xplr"
pkgver = "1.0.1"
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
license = "MIT"
url = "https://xplr.dev"
source = (
    f"https://github.com/sayanarijit/xplr/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "6d766bc52c49782e3ca8ba7130f1cab95c69e42ff3c15eec2b0ac823ab7a36b3"
# needs rebuild with non-release to use bin from debug/
options = ["!check"]


def post_extract(self):
    self.rm(".cargo/config.toml")


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
