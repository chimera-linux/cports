pkgname = "rassumfrassum"
pkgver = "0.3.4"
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
sha256 = "9dbef8253bc2cf4f0d3cca18fa29d405a5b2b28430b84122be11eb7315b0dcfe"
# Per the Nixpkgs package, the tests are timing-sensitive
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
