pkgname = "nuclei"
pkgver = "3.3.8"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/nuclei"]
hostmakedepends = ["go"]
pkgdesc = "Web vulnerability scanner"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "MIT"
url = "https://github.com/projectdiscovery/nuclei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e03e36778ff9736882e52c43c19da8888443c9130cafd30a3305e42cbfb86467"
# Nuclei tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
