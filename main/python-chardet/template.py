pkgname = "python-chardet"
pkgver = "5.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-pip", "python-flit_core", "python-wheel"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Universal encoding detector for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://github.com/chardet/chardet"
source = f"$(PYPI_SITE)/c/chardet/chardet-{pkgver}.tar.gz"
sha256 = "0d62712b956bc154f85fb0a266e2a3c5913c2967e00348701b32411d6def31e5"
# dependency of pytest
options = ["!check"]
