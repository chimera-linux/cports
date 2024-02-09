pkgname = "python-pytest-asyncio"
pkgver = "0.23.5"
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
sha256 = "3a048872a9c4ba14c3e90cc1aa20cbc2def7d01c7c8db3777ec281ba9c057675"
# missing dependencies
options = ["!check"]
