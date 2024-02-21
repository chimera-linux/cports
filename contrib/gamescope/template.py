pkgname = "gamescope"
pkgver = "3.14.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "cmake",
    "glslang-progs",
    "libcap-progs",
    "meson",
    "ninja",
    "pkgconf",
    "spirv-headers",
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
    "wlroots0.17-devel",
    "xwayland",
]
pkgdesc = "SteamOS compositor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/ValveSoftware/gamescope"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    "https://github.com/ValveSoftware/openvr/archive/15f0838a0487feb7da60acd39aab8099b994234c.tar.gz",
    "https://github.com/Joshua-Ashton/vkroots/archive/d5ef31abc7cb5c69aee4bcb67b10dd543c1ff7ac.tar.gz",
    "https://github.com/Joshua-Ashton/reshade/archive/9fdbea6892f9959fdc18095d035976c574b268b7.tar.gz",
]
source_paths = [
    ".",
    "subprojects/openvr",
    "subprojects/vkroots",
    "src/reshade",
]
sha256 = [
    "91ed63557d3601723f1b1d554ea65a3850656a78bb7e32610330035160704836",
    "cf63f641985a70e6a4cb6aad081832f3a33bf26f8973f71c69af24debc8ceadf",
    "b4eca5edca75355ea1443ad96fd59b0a407f6a2ce17ef5a8f9849c05fc10155f",
    "165726ad21fbfc221c0363e40b597834068a416a11a1204ae2ac6d13ec161035",
]
file_modes = {
    "usr/bin/gamescope": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/gamescope": {
        "security.capability": "cap_sys_nice+ep",
    },
}
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
