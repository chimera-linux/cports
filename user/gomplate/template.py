pkgname = "gomplate"
pkgver = "4.3.3"
pkgrel = 1
build_style = "go"
make_build_args = [
    "-ldflags",
    f"-X github.com/hairyhenderson/gomplate/v4/version.Version=v{pkgver}",
    "./cmd/gomplate",
]
hostmakedepends = ["go"]
depends = ["ca-certificates"]
pkgdesc = "Template renderer with datasources"
license = "MIT"
url = "https://github.com/hairyhenderson/gomplate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d15c66230d72bdc13b0155f28d391c55cac45b7fdbe1ff4a73db8ee263471a3d"
# lots of tests need network
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
