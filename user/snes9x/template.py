pkgname = "snes9x"
pkgver = "1.62.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_INSTALL_DATAROOTDIR=share",
    "-DUSE_ALSA=OFF",
    "-DUSE_OSS=OFF",
    "-DUSE_PORTAUDIO=OFF",
]
cmake_dir = "gtk"
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gtkmm3.0-devel",
    "libpulse-devel",
    "libxv-devel",
    "minizip-devel",
    "sdl-devel",
]
pkgdesc = "SNES emulator"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "custom:snes9x"
url = "https://www.snes9x.com"
_commit_spirv_cross = "4e2fdb25671c742a9fbe93a6034eb1542244c7e1"
_commit_glslang = "6d41bb9c557c5a0eec61ffba1f775dc5f717a8f7"
_commit_vkheaders = "a3dd2655a3a68c2a67c55a0f8b77dcb8b166ada2"
source = [
    f"https://github.com/snes9xgit/snes9x/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/KhronosGroup/SPIRV-Cross/archive/{_commit_spirv_cross}.tar.gz",
    f"https://github.com/KhronosGroup/glslang/archive/{_commit_glslang}.tar.gz",
    f"https://github.com/KhronosGroup/Vulkan-Headers/archive/{_commit_vkheaders}.tar.gz",
]
source_paths = [
    ".",
    "external/SPIRV-Cross",
    "external/glslang",
    "external/vulkan-headers",
]
sha256 = [
    "6912c69290ae854ea22b1b2c917d885b1c4a1a95acbe73cd4243ccb2071600fe",
    "775c3105effe232a8848f57cdab9baccb8c3ca00ac4363c35212fc5f087c2659",
    "c2c8e72c8ae247da76e19ecbf7e688a201565dd297689fa80d18b137ac213d77",
    "a43534974d6e4163da549abb073598b7461cbed13cc7acc52b8eeac3c88e5e32",
]
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")
