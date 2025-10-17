pkgname = "bacon"
pkgver = "3.18.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Background rust code checker"
license = "AGPL-3.0-only"
url = "https://dystroy.org/bacon"
source = f"https://github.com/Canop/bacon/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2136e7604bf92b209c1363393142e5bb369bbe06a4f75c7d6cbe16d3437ad9a0"

if self.profile().arch == "loongarch64":
    broken = "busted rustix"


def post_install(self):
    self.install_license("LICENSE")
