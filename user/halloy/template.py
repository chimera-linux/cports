pkgname = "halloy"
pkgver = "2025.11"
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
sha256 = "19546fb2c49ea342e39c38b6771536089b16892b8de6ae4e4a09e4f25db3cd1b"
# no tests in top-level project
options = ["!check"]

if self.profile().arch in ["loongarch64", "ppc", "ppc64", "ppc64le", "riscv64"]:
    broken = "ring 0.16.20 fails to build"


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
