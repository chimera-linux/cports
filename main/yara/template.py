pkgname = "yara"
pkgver = "4.5.3"
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
sha256 = "59323f69b55615fda3ee863062370b90a09016616da660ae00c7f84adf12238e"
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
