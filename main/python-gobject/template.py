pkgname = "python-gobject"
pkgver = "3.48.2"
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
sha256 = "0794aeb4a9be31a092ac20621b5f54ec280f9185943d328b105cdae6298ad1a7"
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
