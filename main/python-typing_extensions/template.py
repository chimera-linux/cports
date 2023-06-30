pkgname = "python-typing_extensions"
pkgver = "4.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://github.com/python/typing"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "935ccf31549830cda708b42289d44b6f74084d616a00be651601a4f968e77c82"
# in early path
options = ["!check"]
