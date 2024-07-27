pkgname = "font-manager"
pkgver = "0.9.0"
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
    "libsoup-devel",
    "nautilus-devel",
    "thunar-devel",
    "webkitgtk4-devel",
]
pkgdesc = "Font management application"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://fontmanager.github.io"
source = f"https://github.com/FontManager/font-manager/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8c2a2bfd4b26430a9f376e2e868d11e2d7a0695523f97a5402c0c3edb0b5762c"
# gobject-introspection
options = ["!cross"]


@subpackage("font-manager-nautilus")
def _nautilus(self):
    self.subdesc = "nautilus plugin"
    self.install_if = [self.parent, "nautilus"]
    return ["usr/lib/nautilus"]


@subpackage("font-manager-thunar")
def _thunar(self):
    self.subdesc = "thunar plugin"
    self.install_if = [self.parent, "thunar"]
    return ["usr/lib/thunarx-3"]
