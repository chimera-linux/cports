pkgname = "nuclei"
pkgver = "3.3.7"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/nuclei"]
hostmakedepends = ["go"]
pkgdesc = "Web vulnerability scanner"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "MIT"
url = "https://github.com/projectdiscovery/nuclei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3d12498f90b4babead541578f095c8f8aac7d08038073f0f239142356d3a4c79"
# Nuclei tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
