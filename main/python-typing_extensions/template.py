pkgname = "python-typing_extensions"
pkgver = "4.14.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
license = "Python-2.0"
url = "https://github.com/python/typing_extensions"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "8676b788e32f02ab42d9e7c61324048ae4c6d844a399eebace3d4979d75ceef4"
# in early path
options = ["!check"]
