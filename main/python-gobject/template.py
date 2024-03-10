pkgname = "python-gobject"
pkgver = "3.48.1"
pkgrel = 0
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
sha256 = "3a0a2c0c0f25931b5840649c54834b9e58a63148d37fa9f6308887b7027e15c2"
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
