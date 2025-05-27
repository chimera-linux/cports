pkgname = "python-pytest-asyncio"
pkgver = "1.0.0"
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
sha256 = "d15463d13f4456e1ead2594520216b225a16f781e144f8fdf6c5bb4667c48b3f"
