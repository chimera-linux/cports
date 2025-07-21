pkgname = "gdm-settings"
pkgver = "5.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
    "gettext",
    "gobject-introspection",
    "meson",
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
license = "AGPL-3.0-or-later"
url = "https://gdm-settings.github.io"
source = f"https://github.com/gdm-settings/gdm-settings/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "adfc33250589217531e9fa679cad03cbe7c845b39fb99fcc226329453ce0ac40"


def post_install(self):
    self.install_license("LICENSE")
