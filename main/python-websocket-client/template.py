pkgname = "python-websocket-client"
pkgver = "1.8.0"
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
sha256 = "03306a5a5afb4e5bffd7fce4e2fb6438be91c14543cf1d6f506893f831047bfc"
# no python-socks in repo yet
options = ["!check"]
