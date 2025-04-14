pkgname = "python-typing_extensions"
pkgver = "4.13.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
license = "Python-2.0"
url = "https://github.com/python/typing_extensions"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "e6c81219bd689f51865d9e372991c540bda33a0379d5573cddb9a3a23f7caaef"
# in early path
options = ["!check"]
