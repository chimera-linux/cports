pkgname = "minify"
pkgver = "2.21.2"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/minify"]
hostmakedepends = ["go"]
pkgdesc = "Minifier for web formats"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://github.com/tdewolff/minify"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "ecbd0e55014aaaee275e3463b6bdccbf102ab3b8efa1164a3d7970c5c7c0bb41"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("cmd/minify/bash_completion", "bash")
