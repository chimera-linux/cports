pkgname = "python-sphinx-removed-in"
pkgver = "0.2.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
checkdepends = ["python-sphinx"]
depends = ["python-sphinx"]
pkgdesc = "Sphinx extension for versionremoved and removed-in directives"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/MrSenko/sphinx-removed-in"
source = f"$(PYPI_SITE)/s/sphinx-removed-in/sphinx-removed-in-{pkgver}.tar.gz"
sha256 = "0588239cb534cd97b1d3900d0444311c119e45296a9f73f1ea81ea81a2cd3db1"
# dependency of pytest
options = ["!check"]

# FIXME visibility
hardening = ["!vis"]
