pkgname = "sad"
pkgver = "0.4.29"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "python"]
makedepends = ["rust-std"]
pkgdesc = "CLI search and replace"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/ms-jpq/sad"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2f66d3031a662c197dba1758ccc9f670694e825b7f90b20fa32c1670c4ae9ee4"


def post_install(self):
    self.install_license("LICENSE")
