pkgname = "python-typing_extensions"
pkgver = "4.10.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://github.com/python/typing"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "b0abd7c89e8fb96f98db18d86106ff1d90ab692004eb746cf6eda2682f91b3cb"
# in early path
options = ["!check"]
