pkgname = "font-manager"
pkgver = "0.9.4"
pkgrel = 2
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
sha256 = "3e4aefdaa0fbd37410c35421501819b19ba1f6847bad7a1f51707209c4147063"
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
