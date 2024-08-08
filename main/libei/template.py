pkgname = "libei"
pkgver = "1.3.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsd-bus-provider=libelogind",
    "-Dliboeffis=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-attrs",
    "python-jinja2",
]
makedepends = [
    "elogind-devel",
    "libevdev-devel",
    "libxkbcommon-devel",
]
pkgdesc = "Emulated Input Library"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://gitlab.freedesktop.org/libinput/libei"
_munit = "fbbdf1467eb0d04a6ee465def2e529e4c87f2118"
source = [
    f"https://gitlab.freedesktop.org/libinput/libei/-/archive/{pkgver}/libei-{pkgver}.tar.bz2",
    f"https://github.com/nemequ/munit/archive/{_munit}.tar.gz",
]
source_paths = [".", "subprojects/munit"]
sha256 = [
    "167692196e735e6141dd7027e294fd9f99a4ce7cf0c797b5051764ffe147ec80",
    "d0c8bf80b9804d4df5301bd428702352fe7e14f84f22027c3a2c084a0d9f69a7",
]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libei-devel")
def _devel(self):
    return self.default_devel()
