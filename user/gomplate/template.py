pkgname = "gomplate"
pkgver = "5.0.0"
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
sha256 = "b4f24768c994dd62c95d7243cef4dc2354b47976fa8fbbda3889aeade8e39d69"
# lots of tests need network
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
