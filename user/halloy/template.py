pkgname = "halloy"
pkgver = "2026.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "libxcb-devel",
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
    "zstd-devel",
]
pkgdesc = "IRC client"
license = "GPL-3.0-or-later"
url = "https://halloy.chat"
source = f"https://github.com/squidowl/halloy/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "fa9a95668717677de7f30c98b019b74451fdd2e5b0287a56574d7e953ef5c800"
# no tests in top-level project
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/halloy")
    with self.pushd("assets/linux"):
        self.install_file(
            "org.squidowl.halloy.desktop",
            "usr/share/applications",
        )
        self.install_file(
            "org.squidowl.halloy.appdata.xml",
            "usr/share/metainfo",
        )
        self.install_files("icons", "usr/share")
