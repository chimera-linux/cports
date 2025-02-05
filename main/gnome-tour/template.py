pkgname = "gnome-tour"
pkgver = "47.0"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://apps.gnome.org/Tour"
source = f"$(GNOME_SITE)/gnome-tour/{pkgver.split('.')[0]}/gnome-tour-{pkgver}.tar.xz"
sha256 = "72faaf89e006c89324a7e1572046916961b38aeba38f6d6d4cc41e3d3d466944"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"build/src/{self.profile().triplet}/release/gnome-tour")
