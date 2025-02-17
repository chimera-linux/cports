pkgname = "intel-media-driver"
pkgver = "25.1.2"
pkgrel = 0
# doesn't build elsewhere
archs = ["x86_64"]
build_style = "cmake"
configure_args = [
    "-DINSTALL_DRIVER_SYSCONF=OFF",
    "-DMEDIA_BUILD_FATAL_WARNINGS=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "intel-gmmlib-devel",
    "libpciaccess-devel",
    "libva-devel",
    "libx11-devel",
    "linux-headers",
]
pkgdesc = "Intel Media Driver for VAAPI"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/intel/media-driver"
source = f"{url}/archive/refs/tags/intel-media-{pkgver}.tar.gz"
sha256 = "6c11cfe1b9012011d0354b010d191a527fa3a4086152726ba642ca51808029bb"
# INT: crashes during certain vaapi decode (twitch.tv?)
hardening = ["vis", "!cfi", "!int"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-media-driver-devel")
def _(self):
    return self.default_devel()
