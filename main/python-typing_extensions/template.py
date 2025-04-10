pkgname = "python-typing_extensions"
pkgver = "4.13.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
license = "Python-2.0"
url = "https://github.com/python/typing_extensions"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "98795af00fb9640edec5b8e31fc647597b4691f099ad75f469a2616be1a76dff"
# in early path
options = ["!check"]
