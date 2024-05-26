pkgname = "yara"
pkgver = "4.5.1"
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
sha256 = "011b95f903d8fc22de50aa1e3c1bf4ed598dbde6f9ea45176945cec5520452dc"


def post_install(self):
    self.install_license("COPYING")


@subpackage("yara-devel")
def _devel(self):
    return self.default_devel()
