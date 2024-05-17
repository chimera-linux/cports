pkgname = "gamescope"
pkgver = "3.14.16"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=static"]
make_install_args = ["--skip-subprojects", "wlroots"]
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
    "glm",
    "glslang-devel",
    "hwdata-devel",
    "libcap-devel",
    "libdisplay-info-devel",
    "libinput-devel",
    "libliftoff-devel",
    "libseat-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxmu-devel",
    "libxrender-devel",
    "libxres-devel",
    "libxtst-devel",
    "libxxf86vm-devel",
    "pipewire-devel",
    "pixman-devel",
    "sdl-devel",
    "stb",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-protocols",
    "xcb-util-wm-devel",
    "xwayland",
]
pkgdesc = "SteamOS compositor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/ValveSoftware/gamescope"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    "https://github.com/ValveSoftware/openvr/archive/15f0838a0487feb7da60acd39aab8099b994234c.tar.gz",
    "https://github.com/Joshua-Ashton/vkroots/archive/5106d8a0df95de66cc58dc1ea37e69c99afc9540.tar.gz",
    "https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/a5c9826e6d7d8b504b07d1c02425e6f62b020791.tar.gz",
    "https://github.com/Joshua-Ashton/reshade/archive/9fdbea6892f9959fdc18095d035976c574b268b7.tar.gz",
]
source_paths = [
    ".",
    "subprojects/openvr",
    "subprojects/vkroots",
    "subprojects/wlroots",
    "src/reshade",
]
sha256 = [
    "6f1db6dedde89f6f6b8d4abd984177a7c9320bb8f5e5430784ced8d36494e009",
    "cf63f641985a70e6a4cb6aad081832f3a33bf26f8973f71c69af24debc8ceadf",
    "37b77586e91f7ebee70380dcddd73bf01ae4acef1053e6be41d0485ede022422",
    "f3f91b679114e565d94e87cd0c4c61444e48d7ef8a77cd101ef3081fd87f4726",
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
