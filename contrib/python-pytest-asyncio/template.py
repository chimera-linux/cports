pkgname = "python-pytest-asyncio"
pkgver = "0.24.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-pytest"]
pkgdesc = "Asyncio support for pytest"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "Apache-2.0"
url = "https://github.com/pytest-dev/pytest-asyncio"
source = f"$(PYPI_SITE)/p/pytest-asyncio/pytest_asyncio-{pkgver}.tar.gz"
sha256 = "d081d828e576d85f875399194281e92bf8a68d60d72d1a2faf2feddb6c46b276"
# missing dependencies
options = ["!check"]
