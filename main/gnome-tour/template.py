pkgname = "gnome-tour"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cargo",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
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
sha256 = "f32652aa9d7ef0643760ce63932082cfd3641e7733b76c429b78d09783b7c46a"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"build/src/{self.profile().triplet}/release/gnome-tour")
