pkgname = "vkquake"
pkgver = "1.35.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddo_userdirs=enabled",
]
hostmakedepends = [
    "glslang-progs",
    "meson",
    "pkgconf",
    "spirv-tools",
]
makedepends = [
    "flac-devel",
    "libvorbis-devel",
    "libxcb-devel",
    "mpg123-devel",
    "opus-devel",
    "opusfile-devel",
    "sdl3-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
]
pkgdesc = "Vulkan Quake port based on QuakeSpasm"
license = "GPL-2.0-only"
url = "https://github.com/Novum/vkQuake"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9f3a2bbf7ef22224c26a1a0d574562573fdaae2dc9758a98068617062d49c584"


def install(self):
    self.install_bin("build/vkquake")
    self.install_file("build/vkquake.pak", "usr/share/games/vkquake")
    self.install_file("Misc/vkquake.desktop", "usr/share/applications")
    self.install_file(
        "Misc/vkQuake_256.png",
        "usr/share/icons/hicolor/256x256/apps",
        name="vkquake.png",
    )
    self.install_file(
        "Misc/vkQuake_512.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="vkquake.png",
    )
    self.install_file("readme.md", "usr/share/doc/vkquake")
