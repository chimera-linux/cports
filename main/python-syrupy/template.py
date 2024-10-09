pkgname = "python-syrupy"
pkgver = "4.7.2"
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
url = "https://syrupy-project.github.io/syrupy"
source = f"$(PYPI_SITE)/s/syrupy/syrupy-{pkgver}.tar.gz"
sha256 = "ea45e099f242de1bb53018c238f408a5bb6c82007bc687aefcbeaa0e1c2e935a"
# unpackaged dependencies
options = ["!check"]
