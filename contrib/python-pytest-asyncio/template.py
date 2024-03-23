pkgname = "python-pytest-asyncio"
pkgver = "0.23.6"
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
sha256 = "ffe523a89c1c222598c76856e76852b787504ddb72dd5d9b6617ffa8aa2cde5f"
# missing dependencies
options = ["!check"]
