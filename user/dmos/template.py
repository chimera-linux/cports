pkgname = "dmos"
pkgver = "0.7.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf", "scdoc"]
makedepends = ["oniguruma-devel", "rust-std"]
pkgdesc = "Djot HTML renderer"
license = "GPL-3.0-or-later"
url = "https://git.sr.ht/~bitfehler/dmos"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "47ca36418932d6eaa663e5a7c85537fdf1c16e6909794e447d3a6c16cf560181"


def post_build(self):
    with open(self.cwd / "man" / "dmos.1.scd", "rb") as i:
        with open(self.cwd / "man" / "dmos.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)


def install(self):
    self.install_man("man/dmos.1")
    self.install_bin(f"target/{self.profile().triplet}/release/dmos")
