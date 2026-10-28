pkgname = "gamescope"
pkgver = "3.17.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=static",
    "-Davif_screenshots=enabled",
    "-Ddrm_backend=enabled",
    "-Denable_zenity=false",
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
    "catch2-devel",
    "glm",
    "glslang-devel",
    "hwdata-devel",
    "libavif-devel",
    "libcap-devel",
    "libdisplay-info-devel",
    "libei-devel",
    "libinput-devel",
    "libx11-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxmu-devel",
    "libxrender-devel",
    "libxres-devel",
    "libxxf86vm-devel",
    "luajit-devel",
    "pipewire-devel",
    "pixman-devel",
    "sdl2-compat-devel",
    "stb",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-protocols",
    "wlroots0.20-devel",
    "xcb-util-wm-devel",
    "xwayland-devel",
]
pkgdesc = "SteamOS compositor"
license = "BSD-2-Clause"
url = "https://github.com/ValveSoftware/gamescope"
source = [
    f"{url}/archive/refs/tags/{pkgver}.tar.gz",
    "https://github.com/ValveSoftware/openvr/archive/ff87f683f41fe26cc9353dd9d9d7028357fd8e1a.tar.gz",
    "https://github.com/misyltoad/vkroots/archive/20733b938267dcac60f6ac105dbb757f9cc8df9c.tar.gz",
    "https://gitlab.freedesktop.org/emersion/libliftoff/-/archive/8b08dc1c14fd019cc90ddabe34ad16596b0691f4.tar.gz",
    "https://github.com/misyltoad/reshade/archive/696b14cd6006ae9ca174e6164450619ace043283.tar.gz",
]
source_paths = [
    ".",
    "subprojects/openvr",
    "subprojects/vkroots",
    "subprojects/libliftoff",
    "src/reshade",
]
sha256 = [
    "77d96c2c68c7a98dd4e0b951407fa23dfb4fc30632d5ee740471c7d612f288e0",
    "22ea84da76f0f37f15d3433aef5f202ad6f8df12c280da7caa47e0475eeb22fd",
    "863ee36f80faa84d28e1f73b588f6f52d391d210267938a57f7a8fa14b9fd1ce",
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
