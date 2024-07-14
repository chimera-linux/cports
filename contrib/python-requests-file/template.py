pkgname = "python-requests-file"
pkgver = "2.1.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-requests"]
checkdepends = [
    "python-pytest",
    "python-pytest-mock",
    *depends,
]
pkgdesc = "File transport adapter for python-requests"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/dashea/requests-file"
source = f"$(PYPI_SITE)/r/requests_file/requests_file-{pkgver}.tar.gz"
sha256 = "0f549a3f3b0699415ac04d167e9cb39bccfb730cb832b4d20be3d9867356e658"
