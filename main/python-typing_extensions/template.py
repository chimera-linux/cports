pkgname = "python-typing_extensions"
pkgver = "4.8.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = ["python-build", "python-installer", "python-flit_core"]
depends = ["python"]
pkgdesc = "Static typing extensions for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://github.com/python/typing"
source = f"$(PYPI_SITE)/t/typing_extensions/typing_extensions-{pkgver}.tar.gz"
sha256 = "df8e4339e9cb77357558cbdbceca33c303714cf861d1eef15e1070055ae8b7ef"
# in early path
options = ["!check"]
