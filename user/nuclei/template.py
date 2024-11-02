pkgname = "nuclei"
pkgver = "3.3.5"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/nuclei"]
hostmakedepends = ["go"]
pkgdesc = "Web vulnerability scanner"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "MIT"
url = "https://github.com/projectdiscovery/nuclei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "aafdfd00a65c72bf1414934cc932b262316f167838835e619b7c079db825b569"
# Nuclei tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
