pkgname = "python-sqlalchemy"
pkgver = "2.0.32"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest", "sqlite"]
pkgdesc = "Database abstraction library"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://www.sqlalchemy.org"
source = f"$(PYPI_SITE)/S/SQLAlchemy/SQLAlchemy-{pkgver}.tar.gz"
sha256 = "c1b88cc8b02b6a5f0efb0345a03672d4c897dc7d92585176f88c67346f565ea8"
# too long with broken selection of backends on some
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
