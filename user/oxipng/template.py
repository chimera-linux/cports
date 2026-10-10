pkgname = "oxipng"
pkgver = "10.2.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Multithreaded PNG optimizer"
license = "MIT"
url = "https://github.com/shssoichiro/oxipng"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "460ccfcdcc9c3877b9f7fae1dfd4f2a3f93d3b2a2af3e3b62ca32b163f923cca"


def post_install(self):
    self.install_license("LICENSE")
