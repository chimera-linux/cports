pkgname = "nuclei"
pkgver = "3.4.10"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/nuclei"]
hostmakedepends = ["go"]
pkgdesc = "Web vulnerability scanner"
license = "MIT"
url = "https://github.com/projectdiscovery/nuclei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d5604ef47d31abba42814876b637105f0b1e9b9167b79206aeeeb2935f102102"
# Nuclei tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
