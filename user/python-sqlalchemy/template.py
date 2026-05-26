pkgname = "python-sqlalchemy"
pkgver = "2.0.50"
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
license = "MIT"
url = "https://www.sqlalchemy.org"
source = f"$(PYPI_SITE)/S/SQLAlchemy/sqlalchemy-{pkgver}.tar.gz"
sha256 = "af5607d11ef90fd6a5c0549fe0045dce1663d427426bcfb506dcb5346a85a3b9"
# too long with broken selection of backends on some
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
