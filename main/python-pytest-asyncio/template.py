pkgname = "python-pytest-asyncio"
pkgver = "0.26.0"
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
license = "Apache-2.0"
url = "https://github.com/pytest-dev/pytest-asyncio"
source = f"$(PYPI_SITE)/p/pytest-asyncio/pytest_asyncio-{pkgver}.tar.gz"
sha256 = "c4df2a697648241ff39e7f0e4a73050b03f123f760673956cf0d72a4990e312f"
# missing dependencies
options = ["!check"]
