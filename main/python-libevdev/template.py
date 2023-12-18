pkgname = "python-libevdev"
pkgver = "0.11"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "libevdev"]
checkdepends = ["python-pytest", "libevdev"]
pkgdesc = "Python wrapper around libevdev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/libevdev/python-libevdev"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "60eebb58ff20be2d8443d716c3c299392720aac89db269fdb4b9de14fe313c24"


def post_install(self):
    self.install_license("COPYING")


def do_check(self):
    self.do(
        "pytest",
        "-v",
        *map(lambda p: f"test/{p.name}", (self.cwd / "test").glob("*.py")),
    )
