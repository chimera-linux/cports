pkgname = "python-requests-file"
pkgver = "1.4.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-six"]
checkdepends = ["python-pytest", "python-pluggy"]
pkgdesc = "File transport adapter for python-requests"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/dashea/requests-file"
source = f"$(PYPI_SITE)/r/requests-file/requests-file-{pkgver}.tar.gz"
sha256 = "8f04aa6201bacda0567e7ac7f677f1499b0fc76b22140c54bc06edf1ba92e2fa"
# FIXME: ???
options = ["!check"]
