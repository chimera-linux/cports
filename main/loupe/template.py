pkgname = "loupe"
pkgver = "47.1"
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
sha256 = "f603569a94e17301f2dac34b02c12c6d8e3ca6aeb9be6ab5b983393f955ed87a"
# Runs `cargo test` but doesn't actually have any rust tests for that to execute
options = ["!check"]


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/loupe")
