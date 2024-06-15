pkgname = "python-sqlalchemy"
pkgver = "2.0.31"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest", "sqlite"]
pkgdesc = "Database abstraction library"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://www.sqlalchemy.org"
source = f"$(PYPI_SITE)/S/SQLAlchemy/SQLAlchemy-{pkgver}.tar.gz"
sha256 = "b607489dd4a54de56984a0c7656247504bd5523d9d0ba799aef59d4add009484"
# too long with broken selection of backends on some
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
