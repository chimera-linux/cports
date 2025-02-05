pkgname = "python-gobject"
pkgver = "3.50.0"
pkgrel = 1
build_style = "meson"
make_check_env = {"PYGI_TEST_VERBOSE": "1"}
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gobject-introspection",
    "meson",
    "pkgconf",
    "python-markupsafe",
]
makedepends = [
    "glib-devel",
    "python-cairo-devel",
    "python-devel",
]
checkdepends = [
    "bash",
    "fonts-dejavu-otf",
    "gtk+3",
    "python-pytest",
    "xwayland-run",
]
depends = ["python", "gobject-introspection-freedesktop", "python-cairo"]
pkgdesc = "Python bindings for GObject"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://pygobject.readthedocs.io"
source = f"$(GNOME_SITE)/pygobject/{pkgver[:-2]}/pygobject-{pkgver}.tar.xz"
sha256 = "8d836e75b5a881d457ee1622cae4a32bcdba28a0ba562193adb3bbb472472212"
# cyclic + gtk3 does not handle seatless displays
options = ["!check"]


@subpackage("python-gobject-devel")
def _(self):
    self.depends += [
        self.parent,
        "gobject-introspection-devel",
        "python-cairo-devel",
    ]

    return self.default_devel()
