pkgname = "python-gobject"
pkgver = "3.56.1"
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
sha256 = "2ec1cc8c55c7ffeebb97e58a9bba7aa1e74611f1173628084685446804a8881a"
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
