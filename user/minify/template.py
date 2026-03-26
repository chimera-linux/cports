pkgname = "minify"
pkgver = "2.24.11"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/minify"]
hostmakedepends = ["go"]
pkgdesc = "Minifier for web formats"
license = "MIT"
url = "https://github.com/tdewolff/minify"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f43c2ec205d395483d3e731f13da01cb12003ca583030c349b3b6dcfd75615c9"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("cmd/minify/bash_completion", "bash")
