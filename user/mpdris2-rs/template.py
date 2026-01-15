pkgname = "mpdris2-rs"
pkgver = "1.0.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "dinit-chimera",
    "mpd",
    "rust-std",
]
depends = ["mpd"]
pkgdesc = "Exposing MPRIS V2.2 D-Bus interface for mpd"
license = "GPL-3.0-or-later"
url = "https://github.com/szclsya/mpdris2-rs"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "465d5662df14156eb9994d1fc88d51144b14bcf568f4f7cebd930a591bf7840b"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "mpdris2-rs.user")
