pkgname = "halloy"
pkgver = "2026.9"
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
sha256 = "5d35f1f6cb2902225b5267b62423d3f41d088147a66c0044148c16a6ca7cd4cd"
# no tests in top-level project
options = ["!check"]

if self.profile.wordsize == 32:
    broken = "needs atomic64"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "halloy"))
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
