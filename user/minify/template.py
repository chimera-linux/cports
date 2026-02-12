pkgname = "minify"
pkgver = "2.24.5"
pkgrel = 2
build_style = "go"
make_build_args = ["./cmd/minify"]
hostmakedepends = ["go"]
pkgdesc = "Minifier for web formats"
license = "MIT"
url = "https://github.com/tdewolff/minify"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4f384f6d7fd9509026f582b3a1e4afb30c1d8855efbc607a15a9943d9a73e362"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("cmd/minify/bash_completion", "bash")
