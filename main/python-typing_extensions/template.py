pkgname = "python-typing_extensions"
pkgver = "4.7.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://github.com/python/typing"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "b75ddc264f0ba5615db7ba217daeb99701ad295353c45f9e95963337ceeeffb2"
# in early path
options = ["!check"]
