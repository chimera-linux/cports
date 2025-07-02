pkgname = "intel-media-driver"
pkgver = "25.2.6"
pkgrel = 0
# doesn't build elsewhere
archs = ["x86_64"]
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
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
license = "BSD-3-Clause"
url = "https://github.com/intel/media-driver"
source = f"{url}/archive/refs/tags/intel-media-{pkgver}.tar.gz"
sha256 = "ba0f124c8e08e0675725f9631b7b1b1c371944b31b7a58a62d2c99338e7ce230"
# INT: crashes during certain vaapi decode (twitch.tv?)
hardening = ["vis", "!cfi", "!int"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-media-driver-devel")
def _(self):
    return self.default_devel()
