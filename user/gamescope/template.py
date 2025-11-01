pkgname = "gamescope"
pkgver = "3.16.17"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Ddefault_library=static",
    "-Davif_screenshots=enabled",
    "-Ddrm_backend=enabled",
    "-Dinput_emulation=enabled",
    "-Dpipewire=enabled",
    "-Drt_cap=enabled",
    "-Dsdl2_backend=enabled",
]
configure_env = {"CMAKE_POLICY_VERSION_MINIMUM": "3.5"}
make_install_args = ["--skip-subprojects"]
hostmakedepends = [
    "cmake",
    "git",
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
    "libavif-devel",
    "libcap-devel",
    "libdisplay-info-devel",
    "libei-devel",
    "libinput-devel",
    "libseat-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxmu-devel",
    "libxrender-devel",
    "libxres-devel",
    "libxtst-devel",
    "libxxf86vm-devel",
    "luajit-devel",
    "pipewire-devel",
    "pixman-devel",
    "sdl2-compat-devel",
    "stb",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-protocols",
    "xcb-util-wm-devel",
    "xwayland-devel",
]
pkgdesc = "SteamOS compositor"
license = "BSD-2-Clause"
url = "https://github.com/ValveSoftware/gamescope"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    "https://github.com/ValveSoftware/openvr/archive/ff87f683f41fe26cc9353dd9d9d7028357fd8e1a.tar.gz",
    "https://github.com/Joshua-Ashton/vkroots/archive/5106d8a0df95de66cc58dc1ea37e69c99afc9540.tar.gz",
    "https://github.com/Joshua-Ashton/wlroots/archive/54e844748029d4874e14d0c086d50092c04c8899.tar.gz",
    "https://gitlab.freedesktop.org/emersion/libliftoff/-/archive/8b08dc1c14fd019cc90ddabe34ad16596b0691f4.tar.gz",
    "https://github.com/Joshua-Ashton/reshade/archive/696b14cd6006ae9ca174e6164450619ace043283.tar.gz",
]
source_paths = [
    ".",
    "subprojects/openvr",
    "subprojects/vkroots",
    "subprojects/wlroots",
    "subprojects/libliftoff",
    "src/reshade",
]
sha256 = [
    "315d30faa7cc73b15f58d4169fba669da978fbddf707e87a85e79d83eb15d530",
    "22ea84da76f0f37f15d3433aef5f202ad6f8df12c280da7caa47e0475eeb22fd",
    "37b77586e91f7ebee70380dcddd73bf01ae4acef1053e6be41d0485ede022422",
    "2398969e27fd7eae43fe0a3d90cc214b5668f1cb1e926552b8f2f4e97c6062af",
    "8de28aee6f90f47b7fc7037dcd2360166197c0b5d2033f3afdbd34f2ea1bf216",
    "3aa6feda7773cc8ffa8fb012fe95e6207c776101e29198d0e0d34a0c5e339f6a",
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
