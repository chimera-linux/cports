pkgname = "kanata"
pkgver = "1.6.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Software keyboard remapper"
maintainer = "hge <h.gersen@gmail.com>"
license = "LGPL-3.0-only"
url = "https://github.com/jtroo/kanata"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c0e047197af23cf434adf20e21a871b7b12c876b58ac75852d662c004bf49f2c"


def pre_prepare(self):
    # rust 1.80 type inference regression
    self.do(
        "cargo",
        "update",
        "--package",
        "time",
        "--precise",
        "0.3.36",
        allow_network=True,
    )
