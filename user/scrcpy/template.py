pkgname = "scrcpy"
pkgver = "3.1"
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
    "beaa5050a3c45faa77cedc70ad13d88ef26b74d29d52f512b7708671e037d24d",
    "958f0944a62f23b1f33a16e9eb14844c1a04b882ca175a738c16d23cb22b86c0",
]


def post_install(self):
    self.install_file(
        self.sources_path / f"scrcpy-server-v{pkgver}",
        "usr/share/scrcpy",
        name="scrcpy-server",
    )
