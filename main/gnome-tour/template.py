pkgname = "gnome-tour"
pkgver = "49.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo-auditable",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = ["gdk-pixbuf-devel", "libadwaita-devel", "rust-std"]
pkgdesc = "GNOME tour and greeter"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Tour"
source = f"$(GNOME_SITE)/gnome-tour/{pkgver.split('.')[0]}/gnome-tour-{pkgver}.tar.xz"
sha256 = "2d7d8a2a0cd1178063a414da58093d26c0fb1a77608d8ad7fbd7911a5d6264d3"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"build/src/{self.profile().triplet}/release/gnome-tour")
