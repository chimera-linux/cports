pkgname = "font-manager"
pkgver = "0.9.2"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://fontmanager.github.io"
source = f"https://github.com/FontManager/font-manager/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2e4eff44d9cee01ae14cf7271ae27170c327ddfbc776f4c0908b7589f2eb1bfb"
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
