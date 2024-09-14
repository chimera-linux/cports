pkgname = "gdm-settings"
pkgver = "4.4"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "meson",
    "gettext",
    "gobject-introspection",
    "pkgconf",
]
makedepends = [
    "appstream-glib",
    "desktop-file-utils",
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "python-gobject-devel",
]
depends = [
    "gdm",
    "glib-devel",
]
pkgdesc = "Settings app for GDM"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "AGPL-3.0-or-later"
url = "https://gdm-settings.github.io"
source = f"https://github.com/gdm-settings/gdm-settings/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9b9ac615e56ac1c96de567dd56c2ff5e9b869a1d50b2e497e60e8b55c596f744"


def post_install(self):
    self.install_license("LICENSE")
