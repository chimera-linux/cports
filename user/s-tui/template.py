pkgname = "s-tui"
pkgver = "1.2.0"
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
    "stress-ng",
]
pkgdesc = "CPU performance monitor"
license = "GPL-2.0-or-later"
url = "https://github.com/amanusk/s-tui"
source = f"$(PYPI_SITE)/s/s-tui/s_tui-{pkgver}.tar.gz"
sha256 = "82097f463cc8a6977bedfa574ba8b2fe2dfdcaa3322a6e16041e2392ee4a74b8"
# check: no tests
options = ["!check"]
