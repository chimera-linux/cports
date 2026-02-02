pkgname = "oxipng"
pkgver = "10.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Multithreaded PNG optimizer"
license = "MIT"
url = "https://github.com/shssoichiro/oxipng"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6c5e1d021a844ba730193943ab63ad99e7d9f1089c36f3db59014517ea99cf99"


def post_extract(self):
    # makes aarch64 run in qemu lol
    self.rm(".cargo/config.toml")


def post_install(self):
    self.install_license("LICENSE")
