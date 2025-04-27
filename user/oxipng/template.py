pkgname = "oxipng"
pkgver = "9.1.5"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Multithreaded PNG optimizer"
license = "MIT"
url = "https://github.com/shssoichiro/oxipng"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8f99d5c67efa2a7550023bf610b90e65d421375c9ed7f37097f83ae5c05f85bd"


def post_extract(self):
    # makes aarch64 run in qemu lol
    self.rm(".cargo/config.toml")


def post_install(self):
    self.install_license("LICENSE")
