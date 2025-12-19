pkgname = "python-pyclip"
pkgver = "0.7.0"
pkgrel = 3
build_style = "python_pep517"
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest", "xclip", "xserver-xorg-xvfb"]
pkgdesc = "Python cross-platform clipboard module"
license = "Apache-2.0"
url = "https://github.com/spyoungtech/pyclip"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6fd5e0eaa40ff349959d1cee2872eee90ae32065cc5df9714b1066981535acde"
# 11/16 tests fail with exit code 1 & "Error: Can't open display: (null)" even under xvfb
options = ["!check"]


@subpackage("python-pyclip-wayland")
def _(self):
    self.subdesc = "Wayland support"
    self.install_if = [self.parent]
    self.depends = ["wl-clipboard"]
    self.options = ["empty"]
    return []


@subpackage("python-pyclip-x11")
def _(self):
    self.subdesc = "X11 support"
    self.install_if = [self.parent]
    self.depends = ["xclip"]
    self.options = ["empty"]
    return []
