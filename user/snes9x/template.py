pkgname = "snes9x"
pkgver = "1.63"
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
    "sdl2-compat-devel",
]
pkgdesc = "SNES emulator"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "custom:snes9x"
url = "https://www.snes9x.com"
_commit_spirv_cross = "bccaa94db814af33d8ef05c153e7c34d8bd4d685"
_commit_glslang = "9c7fd1a33e5cecbe465e1cd70170167d5e40d398"
_commit_vkheaders = "577baa05033cf1d9236b3d078ca4b3269ed87a2b"
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
    "84560ce38a734ac8299645883d8e0c0423b7da2430bde5f88276bba1be6d5330",
    "b2455457ff31704c4a2ad22f58387fd57b76f0c342ddf9c50af94f13e241268f",
    "a0aebec9795e41818f31cc3e2d3e0e320ba7e6686f16d069428c18437af573a4",
    "82bb2262cfb72d2f6029533f757173b55b5fa866de224183cbaab17e179174b7",
]
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")
