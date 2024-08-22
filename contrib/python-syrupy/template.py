pkgname = "python-syrupy"
pkgver = "4.6.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = ["python-pytest"]
checkdepends = [*depends]
pkgdesc = "Pytest snapshot plugin"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://tophat.github.io/syrupy"
source = f"$(PYPI_SITE)/s/syrupy/syrupy-{pkgver}.tar.gz"
sha256 = "a6facc6a45f1cff598adacb030d9573ed62863521755abd5c5d6d665f848d6cc"
# unpackaged dependencies
options = ["!check"]
