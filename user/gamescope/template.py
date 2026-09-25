pkgname = "gamescope"
pkgver = "3.16.30"
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
    "https://github.com/ValveSoftware/openvr/archive/0924064316de3effbcd1acf1e309182a2deb1c05.tar.gz",
    "https://github.com/misyltoad/vkroots/archive/5106d8a0df95de66cc58dc1ea37e69c99afc9540.tar.gz",
    "https://gitlab.freedesktop.org/emersion/libliftoff/-/archive/8b08dc1c14fd019cc90ddabe34ad16596b0691f4.tar.gz",
    "https://github.com/misyltoad/reshade/archive/4245743a8c41abbe3dc73980c1810fe449359bf1.tar.gz",
]
source_paths = [
    ".",
    "subprojects/openvr",
    "subprojects/vkroots",
    "subprojects/libliftoff",
    "src/reshade",
]
sha256 = [
    "e85b06cfa0fce1f7609bb3a691911029b1014bc6014f5d20dc9fbeac80a3d628",
    "95006a99a7fd26158055fbbeb03ae27421db7fa5fa863b3b9b76ffb55f84c3b1",
    "37b77586e91f7ebee70380dcddd73bf01ae4acef1053e6be41d0485ede022422",
    "8de28aee6f90f47b7fc7037dcd2360166197c0b5d2033f3afdbd34f2ea1bf216",
    "a85d1e4c4546afd23fc4324654bcb08b281d8583820e74c178c4e983c81cb802",
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
