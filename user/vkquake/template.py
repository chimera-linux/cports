pkgname = "vkquake"
pkgver = "1.33.1"
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
    "libvorbis-devel",
    "libxcb-devel",
    "mpg123-devel",
    "sdl2-devel",
    "vulkan-headers",
]
pkgdesc = "Vulkan Quake port based on QuakeSpasm"
license = "GPL-2.0-only"
url = "https://github.com/Novum/vkQuake"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7032a690e377617974933174640e9eb2ed59352c4b9f3e8dd8ff9c184a0a8caa"
hardening = ["vis", "!cfi"]


def install(self):
    self.install_bin("build/vkquake")
    self.install_file("build/vkquake.pak", f"usr/share/games/{pkgname}")
    self.install_file("Misc/vkquake.desktop", "usr/share/applications")
    self.install_file(
        "Misc/vkQuake_256.png",
        "usr/share/icons/hicolor/256x256/apps",
        name=f"{pkgname}.png",
    )
    self.install_file(
        "Misc/vkQuake_512.png",
        "usr/share/icons/hicolor/512x512/apps",
        name=f"{pkgname}.png",
    )
    self.install_license("LICENSE.txt")
    self.install_file("readme.md", f"usr/share/doc/{pkgname}")
