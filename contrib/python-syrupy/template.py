pkgname = "python-syrupy"
pkgver = "4.6.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python-pytest"]
checkdepends = list(depends)
pkgdesc = "Pytest snapshot plugin"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://tophat.github.io/syrupy"
source = f"$(PYPI_SITE)/s/syrupy/syrupy-{pkgver}.tar.gz"
sha256 = "37a835c9ce7857eeef86d62145885e10b3cb9615bc6abeb4ce404b3f18e1bb36"
# unpackaged dependencies
options = ["!check"]
