pkgname = "halloy"
pkgver = "2026.7.2"
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
sha256 = "2dcb4623eb5a904aedcd35cf28e29a6fd1719c5414a210b03c1a729c07c207ba"
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
