pkgname = "minify"
pkgver = "2.21.3"
pkgrel = 5
build_style = "go"
make_build_args = ["./cmd/minify"]
hostmakedepends = ["go"]
pkgdesc = "Minifier for web formats"
license = "MIT"
url = "https://github.com/tdewolff/minify"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a5440b8488e0a47ffd7b8428f7bd2f332bd812461646bad376b3536cb59079b8"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("cmd/minify/bash_completion", "bash")
