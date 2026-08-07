pkgname = "python-gobject"
pkgver = "3.56.3"
pkgrel = 0
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
license = "LGPL-2.1-or-later"
url = "https://pygobject.readthedocs.io"
source = f"$(GNOME_SITE)/pygobject/{pkgver[:-2]}/pygobject-{pkgver}.tar.gz"
sha256 = "12760e4a0e3d04b6eb95e06f7a27e362c826d567ea613373a92c003b6c70d2d6"
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
