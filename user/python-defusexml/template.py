pkgname = "python-defusexml"
pkgver = "0.7.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "XML bomb protection for Python stdlib modules"
license = "PSF-2.0"
url = "https://github.com/tiran/defusedxml"
source = f"$(PYPI_SITE)/d/defusedxml/defusedxml-{pkgver}.tar.gz"
sha256 = "1bb3032db185915b62d7c6209c5a8792be6a32ab2fedacc84e01b52c51aa3e69"
# XXX
options = ["!check"]
