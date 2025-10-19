pkgname = "comrak"
pkgver = "0.44.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
license = "BSD-2-Clause"
url = "https://github.com/kivikakk/comrak"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8a33eae71f6296a6c8b3630a35bb04f5c42c8fc8467f52e3c52e1d1c92904604"

if self.profile().arch in ["loongarch64"]:
    broken = "linux-raw-sys does not support, can't bump (semver)"


def post_install(self):
    self.install_license("COPYING")
