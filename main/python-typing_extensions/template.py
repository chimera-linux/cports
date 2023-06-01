pkgname = "python-typing_extensions"
pkgver = "4.5.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://github.com/python/typing"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "5cb5f4a79139d699607b3ef622a1dedafa84e115ab0024e0d9c044a9479ca7cb"
# in early path
options = ["!check"]
