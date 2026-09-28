pkgname = "sad"
pkgver = "0.4.32"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "python"]
makedepends = ["rust-std"]
pkgdesc = "CLI search and replace"
license = "MIT"
url = "https://github.com/ms-jpq/sad"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a67902b9edb287861668ee3e39482c17b41c60e244ece62b3f8016250286294f"


def post_install(self):
    self.install_license("LICENSE")
