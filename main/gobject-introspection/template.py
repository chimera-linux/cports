pkgname = "gobject-introspection"
pkgver = "1.82.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "flex", "bison"]
makedepends = [
    "glib-bootstrap",
    "libffi-devel",
    "python-devel",
    "python-mako",
    "python-markdown",
]
depends = [
    "libgirepository-devel",
    "python-mako",
    "python-markdown",
    "python-setuptools",
]
pkgdesc = "Introspection system for GObject-based libraries"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GObjectIntrospection"
source = f"$(GNOME_SITE)/gobject-introspection/{pkgver[:-2]}/gobject-introspection-{pkgver}.tar.xz"
sha256 = "0f5a4c1908424bf26bc41e9361168c363685080fbdb87a196c891c8401ca2f09"
# FIXME int (fails e.g. gstreamer)
hardening = ["!int"]
# check creates a dependency cycle
# cross compiling tons of janky hackery
options = ["!check", "!cross"]


def post_install(self):
    from cbuild.util import python

    for f in (self.destdir / f"usr/lib/{pkgname}/giscanner").glob(
        "_giscanner*.so"
    ):
        self.mv(f, f.with_name("_giscanner.so"))

    python.precompile(self, f"usr/lib/{pkgname}/giscanner")


@subpackage("gir-freedesktop")
def _(self):
    self.pkgdesc = "Introspection data for some freedesktop components"

    return ["usr/lib/girepository-1.0"]


@subpackage("libgirepository")
def _(self):
    self.pkgdesc = "Library for handling gir data"
    self.subdesc = "runtime library"
    self.depends += [self.with_pkgver("gir-freedesktop")]

    return self.default_libs()


@subpackage("libgirepository-devel")
def _(self):
    self.pkgdesc = "Library for handling gir data"
    self.depends += ["cairo-devel", "libffi-devel"]

    return self.default_devel()
