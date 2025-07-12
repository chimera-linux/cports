pkgname = "gomplate"
pkgver = "4.3.2"
pkgrel = 0
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
sha256 = "647d8775f170fb8b8954a76a59c4a23db50b5c1fdd9faf6b51e17737d8b402a5"
# some checks need internet connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
