pkgname = "loupe"
pkgver = "46.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo",
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
sha256 = "3a15a3f9cf8f889a7e642e3902299f79218a9001c08c56374e05914ffef5ab30"
# Runs `cargo test` but doesn't actually have any rust tests for that to execute
options = ["!check"]


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"./build/src/{self.profile().triplet}/release/loupe")
