pkgname = "libmediainfo"
pkgver = "25.03"
pkgrel = 0
build_wrksrc = "Project/CMake"
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DBUILD_SHARED_LIBS=ON",
]
hostmakedepends = ["pkgconf", "cmake", "ninja"]
makedepends = [
    "curl-devel",
    "libmms-devel",
    "libzen-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Shared library for mediainfo"
license = "BSD-2-Clause"
url = "https://mediaarea.net/en/MediaInfo"
source = f"https://mediaarea.net/download/source/libmediainfo/{pkgver}/libmediainfo_{pkgver}.tar.bz2"
sha256 = "5852567e90b0ad2f51ad7cc18a13ba1389c83250437e541f9a2bb749b24b60ba"


def post_install(self):
    self.install_license("../../LICENSE")


@subpackage("libmediainfo-devel")
def _(self):
    return self.default_devel()
