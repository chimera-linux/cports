pkgname = "python-pyxdg"
pkgver = "0.28"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["shared-mime-info", "python-pytest"]
pkgdesc = "Freedesktop.org standards module for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-only"
url = "https://freedesktop.org/Software/pyxdg"
source = f"$(PYPI_SITE)/p/pyxdg/pyxdg-{pkgver}.tar.gz"
sha256 = "3267bb3074e934df202af2ee0868575484108581e6f3cb006af1da35395e88b4"
# FIXME: fails a inode!=image test because a symlink !follow still follows
options = ["!check"]
