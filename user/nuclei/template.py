pkgname = "nuclei"
pkgver = "3.3.9"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/nuclei"]
hostmakedepends = ["go"]
pkgdesc = "Web vulnerability scanner"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "MIT"
url = "https://github.com/projectdiscovery/nuclei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2eedcb04b82e8ce973eced74a2e900ab778ddb67c8f7e970b79003271a3db0c0"
# Nuclei tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
