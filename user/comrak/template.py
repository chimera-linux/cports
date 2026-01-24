pkgname = "comrak"
pkgver = "0.50.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
license = "BSD-2-Clause"
url = "https://github.com/kivikakk/comrak"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "68adc783055136d7012d8a9f0f2ef1e876f92c8f8708f22977f89a6a1fe7e185"


def post_install(self):
    self.install_license("COPYING")
