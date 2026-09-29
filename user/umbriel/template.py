pkgname = "umbriel"
pkgver = "0_git20260929"
pkgrel = 0
_commit = "b9301a679f2f7986ebfd266fb4bfb627ad2a9eb2"
build_style = "meson"
configure_args = [
    "-Djemalloc=disabled",
    "-Dtest_ipc=disabled",
    "-Dtracy=disabled",
]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "cairo-devel",
    "lcms2-devel",
    "libdrm-devel",
    "libinput-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "mesa-devel",
    "mesa-gbm-devel",
    "nlohmann-json",
    "pango-devel",
    "pixman-devel",
    "tomlplusplus-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
]
depends = ["dbus", "xwayland-satellite"]
pkgdesc = "Wayland compositor with a custom effects renderer"
license = "MIT"
url = "https://github.com/noctalia-dev/umbriel"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "9118123f8a6c50c75e52271055c949fbbb3535305b4f659c3c15b9a185f8a8c9"


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("umbrielfx/LICENSE", name="LICENSE.umbrielfx")
    self.rm(self.destdir / "usr/lib/systemd", recursive=True)
