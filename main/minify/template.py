pkgname = "minify"
pkgver = "2.21.1"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/minify"]
hostmakedepends = ["go"]
pkgdesc = "Minifier for web formats"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://github.com/tdewolff/minify"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "076ea8bb067f2a17036fa4b37ccc42648090ba3ffadfc5d57a469d289b19d354"


def post_install(self):
    self.install_license("LICENSE")
    self.install_completion("cmd/minify/bash_completion", "bash")
