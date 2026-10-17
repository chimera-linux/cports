pkgname = "rassumfrassum"
pkgver = "0.3.5"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Connect an LSP client to multiple LSP servers"
license = "GPL-3.0-only"
url = "https://github.com/joaotavora/rassumfrassum"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "5cd3215d59a1d13bf2a7ae65ad94387b70160365bae206cc0d03c3abeb060a5f"
# Per the Nixpkgs package, the tests are timing-sensitive
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
