pkgname = "python-typing_extensions"
pkgver = "4.14.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
license = "Python-2.0"
url = "https://github.com/python/typing_extensions"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "38b39f4aeeab64884ce9f74c94263ef78f3c22467c8724005483154c26648d36"
# in early path
options = ["!check"]
