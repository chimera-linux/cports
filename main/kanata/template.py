pkgname = "kanata"
pkgver = "1.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Software keyboard remapper"
maintainer = "hge <h.gersen@gmail.com>"
license = "LGPL-3.0-only"
url = "https://github.com/jtroo/kanata"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eb7e11511f77558d72b5b3b0c9defb04b269637e5c8a4ad9b45d21382e9247d2"

if self.profile().wordsize == 32:
    broken = "needs atomic64"
