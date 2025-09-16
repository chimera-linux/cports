pkgname = "rrdtool"
pkgver = "1.9.0"
pkgrel = 2
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "bash",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "python-setuptools",
]
makedepends = [
    "dinit-chimera",
    "glib-devel",
    "libxml2-devel",
    "pango-devel",
    "python-devel",
]
pkgdesc = "Round Robin Database Tool"
license = "GPL-2.0-or-later AND custom:FLOSS-License-Exception"
url = "https://oss.oetiker.ch/rrdtool"
source = f"https://github.com/oetiker/rrdtool-1.x/releases/download/v{pkgver}/rrdtool-{pkgver}.tar.gz"
sha256 = "5e65385e51f4a7c4b42aa09566396c20e7e1a0a30c272d569ed029a81656e56b"


def post_install(self):
    self.install_license("COPYRIGHT")
    self.install_service(self.files_path / "rrdcached")


@subpackage("rrdtool-devel")
def _(self):
    return self.default_devel()


@subpackage("rrdtool-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*", "usr/share/rrdtool/examples/*.py"]
