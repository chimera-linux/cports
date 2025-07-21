pkgname = "python-urllib3"
pkgver = "2.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
pkgdesc = "HTTP library with thread-safe connection pooling"
license = "MIT"
url = "https://urllib3.readthedocs.io"
source = f"$(PYPI_SITE)/u/urllib3/urllib3-{pkgver}.tar.gz"
sha256 = "414bc6535b787febd7567804cc015fee39daab8ad86268f1310a9250697de466"
# unpackaged dependency
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
