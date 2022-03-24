pkgname = "python-gobject"
pkgver = "3.42.0"
pkgrel = 0
build_style = "meson"
make_check_env = {"PYGI_TEST_VERBOSE": "1"}
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "python-markupsafe"
]
makedepends = ["libglib-devel", "python-cairo-devel", "python-devel"]
checkdepends = [
    "python-pytest", "gtk+3", "xserver-xorg-xvfb", "fonts-dejavu-otf", "bash"
]
depends = ["gir-freedesktop", "python-cairo"]
pkgdesc = "Python bindings for GObject"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://pygobject.readthedocs.io"
source = f"$(GNOME_SITE)/pygobject/{pkgver[:-2]}/pygobject-{pkgver}.tar.xz"
sha256 = "9b12616e32cfc792f9dc841d9c472a41a35b85ba67d3a6eb427e307a6fe4367b"

@subpackage("python-gobject-devel")
def _devel(self):
    self.depends += [
        f"{pkgname}={pkgver}-r{pkgrel}", "python-cairo-devel",
        "libgirepository-devel"
    ]

    return self.default_devel()
