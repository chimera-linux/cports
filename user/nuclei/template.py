pkgname = "nuclei"
pkgver = "3.3.6"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/nuclei"]
hostmakedepends = ["go"]
pkgdesc = "Web vulnerability scanner"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "MIT"
url = "https://github.com/projectdiscovery/nuclei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7fb42cf5c9c4fa8800d40a997466dbfeac9954e1cae8d98a7af25c19801eb113"
# Nuclei tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
