pkgname = "libtsm"
pkgver = "4.8.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["check-devel", "libxkbcommon-devel"]
pkgdesc = "Terminal emulator state machine"
license = "MIT"
url = "https://github.com/kmscon/libtsm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "50811e9e94fc798eb5dcbaff20f81067c942ec47f329f91bbe4caeb35a61ff05"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libtsm-devel")
def _(self):
    return self.default_devel()
