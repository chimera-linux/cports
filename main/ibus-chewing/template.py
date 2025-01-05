pkgname = "ibus-chewing"
pkgver = "2.1.3"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = [
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk4-devel",
    "ibus-devel",
    "libadwaita-devel",
    "libchewing-devel",
]
checkdepends = [
    "gsettings-desktop-schemas",
    "ibus",
    "xwayland-run",
]
pkgdesc = "Chewing engine for IBus"
maintainer = "xunil-cloud <river_electron@proton.me>"
license = "GPL-2.0-or-later"
url = "https://github.com/chewing/ibus-chewing"
source = (
    f"{url}/releases/download/v{pkgver}/ibus-chewing-{pkgver}-Source.tar.xz"
)
sha256 = "f3b815668eba0c0f2d5a6585242c98f24c7b68b80affec2aa4dfe1ba43816cb8"


def pre_check(self):
    # copy from upstream ci:
    #   https://github.com/chewing/ibus-chewing/blob/9eed0c2b4e1f1524f208fffd49040dcb35c16be9/.github/workflows/ci.yml#L34
    # we need to run glib-compile-schemas, otherwise, the tests will fail
    self.do(
        "glib-compile-schemas",
        "src/setup",
        "--targetdir",
        "build/bin",
        wrksrc=self.chroot_srcdir,
    )
