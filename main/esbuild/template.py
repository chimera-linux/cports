pkgname = "esbuild"
pkgver = "0.28.0"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/esbuild"]
hostmakedepends = ["go"]
pkgdesc = "JavaScript and CSS bundler and minifier"
license = "MIT"
url = "https://esbuild.github.io"
source = f"https://github.com/evanw/esbuild/archive/v{pkgver}.tar.gz"
sha256 = "7aae83b197db3fd695e6f378d30fd6cbddeb93e4b1057b2c41d36ecb1dfebbc2"


def post_install(self):
    self.install_license("LICENSE.md")
