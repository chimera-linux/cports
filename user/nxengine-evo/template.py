pkgname = "nxengine-evo"
# change source on update
pkgver = "2.6.5.1"
pkgrel = 3
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "libjpeg-turbo-devel",
    "libpng-devel",
    "nlohmann-json",
    "sdl2-compat-devel",
    "sdl2_image-devel",
    "sdl2_mixer-devel",
    "spdlog-devel",
    "utfcpp",
]
pkgdesc = "Open-source rewrite of the Cave Story engine"
license = "GPL-3.0-or-later"
url = "https://github.com/nxengine/nxengine-evo"
source = [
    f"{url}/archive/refs/tags/v2.6.5-1.tar.gz",
    f"{url}/releases/download/v2.6.5-1/NXEngine-Evo-v2.6.5-1-Win64.zip",
]
source_paths = [".", "win"]
sha256 = [
    "db9b78b0c4005959ab8f3a6a05c02d86e764e6593cdd11a2178c581bb03a0699",
    "b7f8b57e555ac84a75f436100e395719153102b1b8a7238349957b5734dafd0d",
]


def post_install(self):
    self.uninstall("usr/share/nxengine/data")
    self.install_files("win/data", "usr/share/nxengine")
