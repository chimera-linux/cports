pkgname = "python-pytest-asyncio"
pkgver = "0.25.3"
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
sha256 = "fc1da2cf9f125ada7e710b4ddad05518d4cee187ae9412e9ac9271003497f07a"
# missing dependencies
options = ["!check"]
