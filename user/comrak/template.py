pkgname = "comrak"
pkgver = "0.45.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
license = "BSD-2-Clause"
url = "https://github.com/kivikakk/comrak"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0fe58e74bbc47705192a25352e131cdf1de1f868b614e56c9b28b714db010500"

if self.profile().arch in ["loongarch64"]:
    broken = "linux-raw-sys does not support, can't bump (semver)"


def post_install(self):
    self.install_license("COPYING")
