pkgname = "python-iso8601"
pkgver = "2.1.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python"]
checkdepends = [
    "python-hypothesis",
    "python-pytest",
    "python-pytz",
]
pkgdesc = "ISO 8601 parser for Python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/micktwomey/pyiso8601"
source = f"$(PYPI_SITE)/i/iso8601/iso8601-{pkgver}.tar.gz"
sha256 = "6b1d3829ee8921c4301998c909f7829fa9ed3cbdac0d3b16af2d743aed1ba8df"


def post_install(self):
    self.install_license("LICENSE")
