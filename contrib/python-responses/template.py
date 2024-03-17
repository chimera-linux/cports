pkgname = "python-responses"
pkgver = "0.25.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-pyyaml",
    "python-requests",
    "python-urllib3",
]
pkgdesc = "Utility library for mocking out the requests python library"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/getsentry/responses"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "54b552af2a48bc1af563a9397df3ffa8c2d761e123a4bbc13d23568d4cb628b7"
# deprecated check dependencies
options = ["!check"]
