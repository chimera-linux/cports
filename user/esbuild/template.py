pkgname = "esbuild"
pkgver = "0.27.0"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/esbuild"]
hostmakedepends = ["go"]
pkgdesc = "JavaScript and CSS bundler and minifier"
license = "MIT"
url = "https://esbuild.github.io"
source = f"https://github.com/evanw/esbuild/archive/v{pkgver}.tar.gz"
sha256 = "a4fd2af11353d41999b51bfa4276cbdd562b5f5fc19b3ca56ab69a520b176529"


def post_install(self):
    self.install_license("LICENSE.md")
