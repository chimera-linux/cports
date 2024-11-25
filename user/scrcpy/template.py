pkgname = "scrcpy"
pkgver = "3.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/Genymobile/scrcpy"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"!{url}/releases/download/v{pkgver}/scrcpy-server-v{pkgver}",
]
sha256 = [
    "6ad2306dcdf17a8c927691d1004ec632a694069187ded73d30113a5db780fc43",
    "800044c62a94d5fc16f5ab9c86d45b1050eae3eb436514d1b0d2fe2646b894ea",
]


def post_install(self):
    self.install_file(
        self.sources_path / f"scrcpy-server-v{pkgver}",
        "usr/share/scrcpy",
        name="scrcpy-server",
    )
