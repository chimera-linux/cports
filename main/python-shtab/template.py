pkgname = "python-shtab"
pkgver = "1.7.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["bash", "python-pytest"]
pkgdesc = "Shell completion generation for Python CLI applications"
license = "Apache-2.0"
url = "https://docs.iterative.ai/shtab"
source = f"$(PYPI_SITE)/s/shtab/shtab-{pkgver}.tar.gz"
sha256 = "8c16673ade76a2d42417f03e57acf239bfb5968e842204c17990cae357d07d6f"
