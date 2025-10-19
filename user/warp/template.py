pkgname = "warp"
pkgver = "0.9.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dqr-code-scanning=disabled"]
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "gtk+3-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "libadwaita-devel",
    "rust-std",
]
pkgdesc = "GTK-based magic wormhole client"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/warp"
source = f"{url}/-/archive/v{pkgver}/warp-{pkgver}.tar.gz"
sha256 = "3b553c2f5a6331e4edaf8747d7b5e782400731e889e16dfdd2019147e5a3e61c"


def post_prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()
    cargo.clear_vendor_checksums(self, "zvariant")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/warp")
