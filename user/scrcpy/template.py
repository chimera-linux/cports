pkgname = "scrcpy"
pkgver = "3.0.2"
pkgrel = 0
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
    "sdl-devel",
]
depends = ["android-tools"]
pkgdesc = "Display and control an Android device"
maintainer = "triallax <triallax@tutanota.com>"
license = "Apache-2.0"
url = "https://github.com/Genymobile/scrcpy"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/scrcpy-server-v{pkgver}",
]
sha256 = [
    "5ab92d091f308679fe81851666acec1b161e6810ac73eb9bade705ade285e109",
    "e19fe024bfa3367809494407ad6ca809a6f6e77dac95e99f85ba75144e0ba35d",
]


def post_install(self):
    self.install_file(
        self.sources_path / f"scrcpy-server-v{pkgver}",
        "usr/share/scrcpy",
        name="scrcpy-server",
    )
