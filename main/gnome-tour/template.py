pkgname = "gnome-tour"
pkgver = "48.1"
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
sha256 = "b8a03b2574eb956abe9af1414161ccb17f830d53600b9c0499cef3bb6f4127c5"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_bin(f"build/src/{self.profile().triplet}/release/gnome-tour")
