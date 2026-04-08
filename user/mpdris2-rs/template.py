pkgname = "mpdris2-rs"
pkgver = "1.1.1"
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
sha256 = "f94eba0022282cb81f5a3c70c7f844ef5c42236e6765cab7a113f902395bd999"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "mpdris2-rs.user")
