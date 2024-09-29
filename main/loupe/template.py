pkgname = "loupe"
pkgver = "47.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "glib",
    "gtk-update-icon-cache",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtk4-devel",
    "lcms2-devel",
    "libadwaita-devel",
    "libgweather-devel",
    "libseccomp-devel",
    "rust-std",
]
depends = ["glycin-loaders"]
pkgdesc = "GNOME image viewer"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Loupe"
source = f"$(GNOME_SITE)/loupe/{pkgver[:-2]}/loupe-{pkgver}.tar.xz"
sha256 = "58938ba673b2f769b5f7b89b9854a3d55dbf3541fed5e60e08e146595115f791"
# Runs `cargo test` but doesn't actually have any rust tests for that to execute
options = ["!check"]


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/loupe")
