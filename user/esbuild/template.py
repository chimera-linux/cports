pkgname = "esbuild"
pkgver = "0.27.2"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/esbuild"]
hostmakedepends = ["go"]
pkgdesc = "JavaScript and CSS bundler and minifier"
license = "MIT"
url = "https://esbuild.github.io"
source = f"https://github.com/evanw/esbuild/archive/v{pkgver}.tar.gz"
sha256 = "d16527a0b29c747d80afaa1cd362d7eee5814c0569af6cc2080e7343482b28d2"


def post_install(self):
    self.install_license("LICENSE.md")
