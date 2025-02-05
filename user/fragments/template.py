pkgname = "fragments"
pkgver = "3.0.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "git",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "libadwaita-devel",
    "openssl3-devel",
    "rust-std",
]
depends = ["transmission-daemon"]
pkgdesc = "BitTorrent client for the GNOME desktop environment"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/Fragments"
source = f"{url}/-/archive/{pkgver}/Fragments-{pkgver}.tar.gz"
sha256 = "33b9b68a85450288e930fcbcf1af0fcf3f630e3493f5e8784f05f4e32620703f"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(
        f"./build/target/{self.profile().triplet}/release/fragments"
    )
