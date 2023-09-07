pkgname = "python-pyelftools"
pkgver = "0.30"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools"]
depends = ["python"]
pkgdesc = "ELF and DWARF parsing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unlicense"
url = "https://github.com/eliben/pyelftools"
source = f"$(PYPI_SITE)/p/pyelftools/pyelftools-{pkgver}.tar.gz"
sha256 = "2fc92b0d534f8b081f58c7c370967379123d8e00984deb53c209364efd575b40"
# FIXME: tests cannot locate utils module?
options = ["!check"]
