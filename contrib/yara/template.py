pkgname = "yara"
pkgver = "4.5.0"
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
    "openssl-devel",
]
pkgdesc = "C library for pattern matching"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://virustotal.github.io/yara"
source = (
    f"https://github.com/VirusTotal/yara/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "f6db34bd102703bf56cc2878ddfb249c3fb2e09c9194d3adb78c3ab79282c827"


def post_install(self):
    self.install_license("COPYING")


@subpackage("yara-devel")
def _devel(self):
    return self.default_devel()
