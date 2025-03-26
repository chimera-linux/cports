pkgname = "kanata"
pkgver = "1.8.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Software keyboard remapper"
license = "LGPL-3.0-only"
url = "https://github.com/jtroo/kanata"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "396a379d7620001531b856913a2677baa56fa16c5c9d329f6937dfb57d3ac704"

if self.profile().wordsize == 32:
    broken = "needs atomic64"

if self.profile().arch in ["loongarch64"]:
    broken = "outdated nix crate, can't update"
