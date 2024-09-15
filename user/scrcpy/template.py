pkgname = "scrcpy"
pkgver = "2.7"
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
    "3ceea215f6eccb59535f68a16db6db2b05a8a1c91bdcb4a6e222d3093a9daf8c",
    "a23c5659f36c260f105c022d27bcb3eafffa26070e7baa9eda66d01377a1adba",
]


def post_install(self):
    self.install_file(
        self.sources_path / f"scrcpy-server-v{pkgver}",
        "usr/share/scrcpy",
        name="scrcpy-server",
    )
