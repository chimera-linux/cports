pkgname = "rsgain"
pkgver = "3.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DINSTALL_MANPAGE=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "fmt-devel",
    "inih-devel",
    "libebur128-devel",
    "taglib-devel",
    "zlib-devel",
]
pkgdesc = "ReplayGain 2.0 tagging utility"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause"
url = "https://github.com/complexlogic/rsgain"
source = f"{url}/releases/download/v{pkgver}/rsgain-{pkgver}-source.tar.xz"
sha256 = "8098d8cbe5c4dccc604e0d75667a71678e6802f9c623286eba772a42a8e2a062"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
