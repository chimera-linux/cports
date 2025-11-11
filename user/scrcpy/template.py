pkgname = "scrcpy"
pkgver = "3.3.3"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dcompile_server=false",
    # just a android apk not worth the extra effort of figuring out how to waste
    # time running gradle and build a whole thing for it
    "-Dprebuilt_server=/usr/share/scrcpy/scrcpy-server",
]
hostmakedepends = [
    "meson",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "libusb-devel",
    "sdl2-compat-devel",
]
depends = ["android-tools"]
pkgdesc = "Display and control an Android device"
license = "Apache-2.0"
url = "https://github.com/Genymobile/scrcpy"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/scrcpy-server-v{pkgver}",
]
sha256 = [
    "87fcd360a6bb6ca070ffd217bd33b33fb808b0a1572b464da51dde3fd3f6f60e",
    "7e70323ba7f259649dd4acce97ac4fefbae8102b2c6d91e2e7be613fd5354be0",
]


def post_install(self):
    self.install_file(
        self.sources_path / f"scrcpy-server-v{pkgver}",
        "usr/share/scrcpy",
        name="scrcpy-server",
    )
