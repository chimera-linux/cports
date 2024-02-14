pkgname = "granite"
pkgver = "7.4.0"
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
    "gtk4-devel",
    "libgee-devel",
]
pkgdesc = "GTK widget extension library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later"
url = "https://github.com/elementary/granite"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "594fe6670940bf2e5d094c73071025d77efab9c5b147a6f64134fe10d370e40e"


@subpackage("granite-devel")
def _devel(self):
    return self.default_devel()


@subpackage("granite-demo")
def _demo(self):
    self.pkgdesc = f"{pkgdesc} (demo application)"
    return ["usr/bin", "usr/share"]
