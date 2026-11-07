pkgname = "font-manager"
pkgver = "0.9.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dnautilus=true",
    "-Dreproducible=true",
    "-Dthunar=true",
]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
    "yelp-tools",
]
makedepends = [
    "gtk4-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libsoup-devel",
    "nautilus-devel",
    "thunar-devel",
    "webkitgtk4-devel",
]
pkgdesc = "Font management application"
license = "GPL-3.0-or-later"
url = "https://fontmanager.github.io"
source = f"https://github.com/FontManager/font-manager/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2d887c93bba13139cb50e9f61480f37258584abbb5a7f5476ec4e475aa38e3a8"
# gobject-introspection
options = ["!cross"]


@subpackage("font-manager-nautilus")
def _(self):
    self.subdesc = "nautilus plugin"
    self.install_if = [self.parent, "nautilus"]
    return ["usr/lib/nautilus"]


@subpackage("font-manager-thunar")
def _(self):
    self.subdesc = "thunar plugin"
    self.install_if = [self.parent, "thunar"]
    return ["usr/lib/thunarx-3"]
