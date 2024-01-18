pkgname = "python-pytest-asyncio"
pkgver = "0.23.3"
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
source = f"$(PYPI_SITE)/p/pytest-asyncio/pytest-asyncio-{pkgver}.tar.gz"
sha256 = "af313ce900a62fbe2b1aed18e37ad757f1ef9940c6b6a88e2954de38d6b1fb9f"
# missing dependencies
options = ["!check"]
