pkgname = "mpdris2-rs"
pkgver = "1.1.0"
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
sha256 = "16d754c87aeadec8ab29e91eb42f2bfd397e1bc0f3676784a80cbefecd7f9475"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "mpdris2-rs.user")
