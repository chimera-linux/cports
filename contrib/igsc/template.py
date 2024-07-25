pkgname = "igsc"
pkgver = "0.9.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSYSLOG=OFF", "-DENABLE_WERROR=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "linux-headers",
    "metee-devel",
    "udev-devel",
]
pkgdesc = "Intel graphics system controller firmware update library"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/intel/igsc"
source = f"{url}/archive/refs/tags/V{pkgver}.tar.gz"
sha256 = "cb7ef80359ad677782a912f26e71a926e8a6b4e1b9bb21a2de0d27781b1d31f9"


@subpackage("igsc-devel")
def _devel(self):
    return self.default_devel()
