pkgname = "warp"
pkgver = "0.8.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/warp"
source = [
    f"{url}/-/archive/v{pkgver}/warp-{pkgver}.tar.gz",
    "https://github.com/spdx/license-list-data/archive/refs/tags/v3.25.0.tar.gz",
]
source_paths = [".", "license-list-data"]
sha256 = [
    "8da6871aca17873264639817c8ba903c96a193d89cbcec46edf64d95d1e143e5",
    "f3114e9f3fbf27b9768a5fc2ab427e9bc4282d30fea0abc9272456d6abf26fae",
]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()
    # excellent ecosystems :|
    self.mv("license-list-data", "vendor/license")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/warp")
