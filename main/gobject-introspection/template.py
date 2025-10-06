pkgname = "gobject-introspection"
pkgver = "1.86.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "bison",
    "flex",
    "meson",
    "pkgconf",
    "python-mako",
    "python-markdown",
]
makedepends = [
    "glib-bootstrap",
    "libffi8-devel",
    "python-devel",
]
depends = [
    "gobject-introspection-devel",
    "python-mako",
    "python-markdown",
    "python-setuptools",
]
pkgdesc = "Introspection system for GObject-based libraries"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GObjectIntrospection"
source = f"$(GNOME_SITE)/gobject-introspection/{pkgver[:-2]}/gobject-introspection-{pkgver}.tar.xz"
sha256 = "920d1a3fcedeadc32acff95c2e203b319039dd4b4a08dd1a2dfd283d19c0b9ae"
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


@subpackage("gobject-introspection-freedesktop")
def _(self):
    self.pkgdesc = "Introspection data for some freedesktop components"
    # transitional
    self.provides = [self.with_pkgver("gir-freedesktop")]

    return ["usr/lib/girepository-1.0"]


@subpackage("gobject-introspection-libs")
def _(self):
    self.depends += [self.with_pkgver("gobject-introspection-freedesktop")]
    # transitional
    self.provides = [self.with_pkgver("libgirepository")]

    return self.default_libs()


@subpackage("gobject-introspection-devel")
def _(self):
    self.depends += ["cairo-devel", "libffi8-devel"]
    # transitional
    self.provides = [self.with_pkgver("libgirepository-devel")]

    return self.default_devel()
