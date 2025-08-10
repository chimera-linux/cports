pkgname = "granite"
pkgver = "7.6.0"
pkgrel = 0
build_style = "meson"
# missing dep on meson-generated_Application.c.o somewhere for granite .a
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
    "sassc",
    "vala",
]
makedepends = [
    "gtk4-devel",
    "libgee-devel",
]
pkgdesc = "GTK widget extension library"
license = "LGPL-3.0-or-later"
url = "https://github.com/elementary/granite"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4b4e4f7f86eb3f55116faec42ebd87e04c3e424d82715ecd967ed39540dca5ef"
# introspection
options = ["!cross"]


@subpackage("granite-devel")
def _(self):
    return self.default_devel()


@subpackage("granite-demo")
def _(self):
    self.subdesc = "demo application"
    return ["usr/bin", "usr/share"]
