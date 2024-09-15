pkgname = "warp"
pkgver = "0.7.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dqr-code-scanning=disabled"]
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "libadwaita-devel",
    "rust-std",
]
pkgdesc = "GTK-based magic wormhole client"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/warp"
source = f"{url}/-/archive/v{pkgver}/warp-{pkgver}.tar.gz"
sha256 = "c832ddb2c619b1d1e3ebfd9bbe8c485871ab7759e9a854c324bcac41d9e02196"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/warp")
