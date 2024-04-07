pkgname = "python-websocket-client"
pkgver = "1.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "ca-certificates"]
pkgdesc = "WebSocket client for Python3"
maintainer = "shtayerc <david.murko@mailbox.org>"
license = "Apache-2.0"
url = "https://github.com/websocket-client/websocket-client"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "923c3b7d0cecfdc449eec5e95c90ae6b0ea24e8782d42f23c05d2bb43bfabd39"
# no python-socks in repo yet
options = ["!check"]
