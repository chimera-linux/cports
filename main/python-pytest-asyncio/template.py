pkgname = "python-pytest-asyncio"
pkgver = "1.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
]
depends = ["python-pytest"]
checkdepends = ["python-hypothesis", *depends]
pkgdesc = "Asyncio support for pytest"
license = "Apache-2.0"
url = "https://github.com/pytest-dev/pytest-asyncio"
source = f"$(PYPI_SITE)/p/pytest-asyncio/pytest_asyncio-{pkgver}.tar.gz"
sha256 = "796aa822981e01b68c12e4827b8697108f7205020f24b5793b3c41555dab68ea"
