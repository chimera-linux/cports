pkgname = "s-tui"
pkgver = "1.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-psutil",
    "python-typing_extensions",
    "python-urwid",
]
pkgdesc = "CPU performance monitor"
license = "GPL-2.0-or-later"
url = "https://github.com/amanusk/s-tui"
source = f"$(PYPI_SITE)/s/s-tui/s_tui-{pkgver}.tar.gz"
sha256 = "93d7a1da2399d6af88228fc945986c14e21edc442fde9582cd8693224c20aa84"
# check: no tests
options = ["!check"]
