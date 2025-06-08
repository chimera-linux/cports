pkgname = "yara"
pkgver = "4.5.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-cuckoo",
    "--enable-dex",
    "--enable-magic",
]
hostmakedepends = [
    "automake",
    "flex",
    "libtool",
    "pkgconf",
]
makedepends = [
    "file-devel",
    "jansson-devel",
    "linux-headers",
    "openssl3-devel",
]
pkgdesc = "C library for pattern matching"
license = "BSD-3-Clause"
url = "https://virustotal.github.io/yara"
source = (
    f"https://github.com/VirusTotal/yara/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "586c9c21878f8b4d1b9423b89ac937f21f8057b03e3e9706f310549d453966fa"
# tests may be disabled
options = []

if self.profile().arch in ["loongarch64", "riscv64"]:
    # forkbombs the build machine
    options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("yara-devel")
def _(self):
    return self.default_devel()
