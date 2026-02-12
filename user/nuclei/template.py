pkgname = "nuclei"
pkgver = "3.7.0"
pkgrel = 0
build_style = "go"
prepare_after_patch = True
make_build_args = ["./cmd/nuclei"]
hostmakedepends = ["go"]
pkgdesc = "Web vulnerability scanner"
license = "MIT"
url = "https://github.com/projectdiscovery/nuclei"
# source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
# temporary while the release can't support go 1.26
source = f"{url}/archive/8aa427a6ea8d5e1faf4f109ccc94156431018582.tar.gz"
sha256 = "a5a97b4953f053c08d8ecdd7bdb50bb45aa98b8204fc00a7dcb788befa85a24f"
# Nuclei tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
