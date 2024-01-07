pkgname = "python-gobject"
pkgver = "3.46.0"
pkgrel = 1
build_style = "meson"
make_check_env = {"PYGI_TEST_VERBOSE": "1"}
make_check_wrapper = ["weston-headless-run"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "python-markupsafe",
]
makedepends = ["glib-devel", "python-cairo-devel", "python-devel"]
checkdepends = [
    "python-pytest",
    "gtk+3",
    "weston",
    "fonts-dejavu-otf",
    "bash",
]
depends = ["python", "gir-freedesktop", "python-cairo"]
pkgdesc = "Python bindings for GObject"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://pygobject.readthedocs.io"
source = f"$(GNOME_SITE)/pygobject/{pkgver[:-2]}/pygobject-{pkgver}.tar.xz"
sha256 = "426008b2dad548c9af1c7b03b59df0440fde5c33f38fb5406b103a43d653cafc"
# cyclic + gtk3 does not handle seatless displays
options = ["!check"]


@subpackage("python-gobject-devel")
def _devel(self):
    self.depends += [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "python-cairo-devel",
        "libgirepository-devel",
    ]

    return self.default_devel()
