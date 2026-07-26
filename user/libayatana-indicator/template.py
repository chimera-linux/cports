pkgname = "libayatana-indicator"
pkgver = "0.9.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_TESTS=ON",
]
# Tests run xvfb-run on their own but that fails for some reason
make_check_wrapper = ["xvfb-run"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "ayatana-ido-devel",
    "glib-devel",
    "gtk+3-devel",
]
checkdepends = ["dbus-test-runner", "xserver-xorg-xvfb"]
pkgdesc = "Ayatana Indicators Shared Library"
license = "GPL-3.0-only"
url = "https://github.com/AyatanaIndicators/libayatana-indicator"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "73d71c908b803f12e4a5ecd8392511b58afbdd0c82ad7909611a17bb7847c5c8"


@subpackage("libayatana-indicator-devel")
def _(self):
    return self.default_devel()
