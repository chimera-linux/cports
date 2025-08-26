pkgname = "comrak"
pkgver = "0.41.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "CommonMark compatible GitHub Flavored Markdown parser and formatter"
license = "BSD-2-Clause"
url = "https://github.com/kivikakk/comrak"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0f80341d6da8c2e5713521c8442b123fd06c1a04d5602fdb217c4ec2ec2658f8"

if self.profile().arch in ["loongarch64"]:
    broken = "linux-raw-sys does not support, can't bump (semver)"


def post_install(self):
    self.install_license("COPYING")
