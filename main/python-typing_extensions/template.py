pkgname = "python-typing_extensions"
pkgver = "4.12.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://github.com/python/typing_extensions"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "1a7ead55c7e559dd4dee8856e3a88b41225abfe1ce8df57b7c13915fe121ffb8"
# in early path
options = ["!check"]
