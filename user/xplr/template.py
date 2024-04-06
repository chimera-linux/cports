pkgname = "xplr"
pkgver = "0.21.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo",
    "pkgconf",
]
makedepends = [
    "luajit-devel",
    "rust-std",
]
pkgdesc = "TUI file explorer"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://xplr.dev"
source = (
    f"https://github.com/sayanarijit/xplr/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "d38f94cc46044dac3cfc96d89dec81989b69a66a98c2f960ea3abe44313675a6"
# needs rebuild with non-release to use bin from debug/
options = ["!check"]


def post_extract(self):
    self.rm(".cargo/config")


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


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
