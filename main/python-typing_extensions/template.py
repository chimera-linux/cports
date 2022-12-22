pkgname = "python-typing_extensions"
pkgver = "4.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-pip", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://github.com/python/typing"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "1511434bb92bf8dd198c12b1cc812e800d4181cfcb867674e0f8279cc93087aa"
# in early path
options = ["!check"]

# FIXME visibility
hardening = ["!vis"]
