pkgname = "nuclei"
pkgver = "3.4.4"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/nuclei"]
hostmakedepends = ["go"]
pkgdesc = "Web vulnerability scanner"
license = "MIT"
url = "https://github.com/projectdiscovery/nuclei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "977726c98398fc3f9348bc7ffbf3704b5eedcaa754f7f964a8de25d3c9ca6c59"
# Nuclei tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
