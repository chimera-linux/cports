pkgname = "python-libevdev"
pkgver = "0.10"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python", "libevdev"]
checkdepends = ["python-pytest", "libevdev"]
pkgdesc = "Python wrapper around libevdev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://gitlab.freedesktop.org/libevdev/python-libevdev"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "8deaad5ca7450d9dac9a491382eb829801194410555fadfa13a6991c7cba594b"

def post_install(self):
    self.install_license("COPYING")

def do_check(self):
    self.do("pytest", "-v", *map(
        lambda p: f"test/{p.name}", (self.cwd / "test").glob("*.py")
    ))
