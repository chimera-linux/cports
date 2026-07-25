pkgname = "s-tui"
pkgver = "1.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-psutil",
    "python-urwid",
]
pkgdesc = "CPU performance monitor"
license = "GPL-2.0-or-later"
url = "https://github.com/amanusk/s-tui"
source = f"$(PYPI_SITE)/s/s-tui/s_tui-{pkgver}.tar.gz"
sha256 = "5153f1def01bf1eae62aaf37fe9562a804d09232644d1e2482c7d52e18c6653a"
# check: no tests
options = ["!check"]
