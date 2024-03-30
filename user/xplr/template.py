pkgname = "xplr"
pkgver = "0.21.8"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--no-default-features"]
make_install_args = list(make_build_args)
hostmakedepends = [
    "cargo-auditable",
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
sha256 = "6fa6ab87cd9f48e531146e2f04c980f2ec90259b3e7b874bf9e165e613be0789"
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
