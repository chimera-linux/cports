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
source = [
    f"{url}/-/archive/v{pkgver}/warp-{pkgver}.tar.gz",
    "https://github.com/spdx/license-list-data/archive/refs/tags/v3.27.0.tar.gz",
]
source_paths = [".", "license-list-data"]
sha256 = [
    "3b553c2f5a6331e4edaf8747d7b5e782400731e889e16dfdd2019147e5a3e61c",
    "7a1eade71449d2ff3ae42957452f6e3a660a3704b477d0e72afc2b43be94c907",
]


def post_prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()
    cargo.clear_vendor_checksums(self, "zvariant")


def post_patch(self):
    # excellent ecosystems :|
    self.mv("license-list-data", "vendor/license")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/warp")
