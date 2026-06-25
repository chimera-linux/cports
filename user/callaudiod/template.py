pkgname = "callaudiod"
pkgver = "0.1.10"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "glib-devel",
    "libpulse-devel",
]
pkgdesc = "Call audio routing daemon"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/mobian1/callaudiod"
source = f"https://gitlab.com/mobian1/callaudiod/-/archive/{pkgver}/callaudiod-{pkgver}.tar.gz"
sha256 = "7e70c0eb26f05c9b9967fc3814306d28e996c3757b7c303410e97b96bb4a704a"


@subpackage("callaudiod-devel")
def _(self):
    return self.default_devel()
