pkgname = "autotiling"
pkgver = "1.9.3"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-i3ipc"]
pkgdesc = "Automatically switch horizontal/vertical split orientation in sway"
license = "GPL-3.0-or-later"
url = "https://github.com/nwg-piotr/autotiling"
source = f"$(PYPI_SITE)/a/autotiling/autotiling-{pkgver}.tar.gz"
sha256 = "b286671106c8d68f0ae1f89e2cd49739ec944313423296763bb0bf7a14347027"
# No test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
