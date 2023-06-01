pkgname = "python-typing_extensions"
pkgver = "4.6.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://github.com/python/typing"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "06006244c70ac8ee83fa8282cb188f697b8db25bc8b4df07be1873c43897060c"
# in early path
options = ["!check"]
