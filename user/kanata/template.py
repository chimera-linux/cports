pkgname = "kanata"
pkgver = "1.9.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Software keyboard remapper"
license = "LGPL-3.0-only"
url = "https://github.com/jtroo/kanata"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "754bed4c7317ae14c228288f3a24d23ab6c245e067f996336fc03b58f71c34b6"

if self.profile().wordsize == 32:
    broken = "needs atomic64"

if self.profile().arch in ["loongarch64"]:
    broken = "outdated nix crate, can't update"
