pkgname = "mpdris2-rs"
pkgver = "1.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "dinit-chimera",
    "dinit-dbus",
    "mpd",
    "rust-std",
]
pkgdesc = "Exposing MPRIS V2.2 D-Bus interface for mpd"
license = "GPL-3.0-or-later"
url = "https://github.com/szclsya/mpdris2-rs"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "50ffaa10c47122921ca382beaffa399cb11fa67b42a25f2a117001121ff76662"


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "mpdris2-rs.user")
