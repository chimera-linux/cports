pkgname = "gamescope"
pkgver = "3.12.5"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "cmake",
    "glslang-progs",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "benchmark-devel",
    "glslang-devel",
    "hwdata-devel",
    "glm",
    "libcap-devel",
    "libdisplay-info-devel",
    "libliftoff-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxmu-devel",
    "libxrender-devel",
    "libxres-devel",
    "libxtst-devel",
    "libxxf86vm-devel",
    "pipewire-devel",
    "sdl-devel",
    "stb",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-protocols",
    "wlroots-devel",
    "xwayland",
]
pkgdesc = "SteamOS compositor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/ValveSoftware/gamescope"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    "https://github.com/ValveSoftware/openvr/archive/1a0ea26642e517824b66871e6a12280a426cfec3.tar.gz",
    "https://github.com/Joshua-Ashton/vkroots/archive/26757103dde8133bab432d172b8841df6bb48155.tar.gz",
]
source_paths = [
    ".",
    "subprojects/openvr",
    "subprojects/vkroots",
]
sha256 = [
    "32a020e35b8443862c900306fb6edb84a8ecb009c89184d2062b0b8ce2811e17",
    "6285504e64a37df47856ffa4a12709d0703da37ee1b0c9fe9e8e52a55127dd7d",
    "adf158c3da572f1dfaa6e1a7a51943aafb824222e77f512a4666472d71321244",
]
# sus
options = ["!cross"]

tool_flags = {"CXXFLAGS": ["-DRTLD_DEEPBIND=0"]}


def post_install(self):
    self.install_license("LICENSE")
    # already installed
    self.rm(self.destdir / "usr/share/licenses/gamescope/LICENSE")
    # don't need it
    self.rm(self.destdir / "usr/lib/libopenvr_api.a")
    self.rm(self.destdir / "usr/lib/pkgconfig/vkroots.pc")
    self.rm(self.destdir / "usr/include/vkroots.h")
