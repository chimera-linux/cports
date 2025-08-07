pkgname = "nuclei"
pkgver = "3.4.5"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/nuclei"]
hostmakedepends = ["go"]
pkgdesc = "Web vulnerability scanner"
license = "MIT"
url = "https://github.com/projectdiscovery/nuclei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5ea8c1f1fc932032328c1f864a85db65715b12b62a9f3ad0bb5b37d3363f2e1c"
# Nuclei tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
