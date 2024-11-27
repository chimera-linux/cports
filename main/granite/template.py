pkgname = "granite"
pkgver = "6.2.0"
pkgrel = 0
build_style = "meson"
# missing dep on meson-generated_Application.c.o somewhere for granite .a
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "sassc",
    "vala",
]
makedepends = [
    "gtk+3-devel",
    "libgee-devel",
]
pkgdesc = "GTK widget extension library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/elementary/granite"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "067d31445da9808a802fca523630c3e4b84d2d7c78ae547ced017cb7f3b9c6b5"


@subpackage("granite-devel")
def _(self):
    return self.default_devel()


@subpackage("granite-demo")
def _(self):
    self.subdesc = "demo application"
    return ["usr/bin", "usr/share"]
