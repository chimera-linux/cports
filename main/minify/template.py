pkgname = "minify"
pkgver = "2.20.37"
pkgrel = 4
build_style = "go"
make_build_args = ["./cmd/minify"]
hostmakedepends = ["go"]
pkgdesc = "Minifier for web formats"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://github.com/tdewolff/minify"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "33d9bf68d416c9e256412d5045562371bd202f1dabeb111c17bf914b71cabedb"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("cmd/minify/bash_completion", "bash")
