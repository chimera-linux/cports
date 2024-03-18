pkgname = "python-requests-file"
pkgver = "2.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools_scm",
    "python-wheel",
]
depends = ["python-requests"]
checkdepends = depends + [
    "python-pytest",
    "python-pytest-mock",
]
pkgdesc = "File transport adapter for python-requests"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/dashea/requests-file"
source = f"$(PYPI_SITE)/r/requests-file/requests-file-{pkgver}.tar.gz"
sha256 = "20c5931629c558fda566cacc10cfe2cd502433e628f568c34c80d96a0cc95972"
