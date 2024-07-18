pkgname = "python-pytest-asyncio"
pkgver = "0.23.8"
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
sha256 = "759b10b33a6dc61cce40a8bd5205e302978bbbcc00e279a8b61d9a6a3c82e4d3"
# missing dependencies
options = ["!check"]
