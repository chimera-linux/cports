pkgname = "python-scour"
pkgver = "0.38.2"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-setuptools", "python-six"]
checkdepends = ["python-six"]
pkgdesc = "Python SVG scrubber"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/scour-project/scour"
source = f"$(PYPI_SITE)/s/scour/scour-{pkgver}.tar.gz"
sha256 = "6881ec26660c130c5ecd996ac6f6b03939dd574198f50773f2508b81a68e0daf"
# no tests in pypi
options = ["!check"]
