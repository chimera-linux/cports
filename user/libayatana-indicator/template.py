pkgname = "libayatana-indicator"
pkgver = "0.9.4"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DENABLE_TESTS=ON"]
# Tests run xvfb-run on their own but that fails for some reason
make_check_wrapper = ["xvfb-run"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "ayatana-ido-devel",
    "glib-devel",
    "gtk+3-devel",
]
checkdepends = ["bash", "dbus-test-runner", "xserver-xorg-xvfb"]
pkgdesc = "Ayatana Indicators Shared Library"
license = "GPL-3.0-only"
url = "https://github.com/AyatanaIndicators/libayatana-indicator"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a18d3c682e29afd77db24366f8475b26bda22b0e16ff569a2ec71cd6eb4eac95"
# test-indicator-ng-tester times out
options = ["!check"]


@subpackage("libayatana-indicator-devel")
def _(self):
    return self.default_devel()
