pkgname = "nvidia-settings"
pkgver = "620.73.04"
pkgrel = 0
archs = ["aarch64", "x86_64"]
build_style = "makefile"
make_install_args = ["-j1", "DO_STRIP="]
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = [
    "gtk+3-devel",
    "libglvnd-devel",
    "libvdpau-devel",
    "libx11-devel",
    "libxv-devel",
    "libxxf86vm-devel",
    "vulkan-loader-devel",
]
pkgdesc = "NVIDIA settings utility"
license = "GPL-2.0-or-later"
url = "https://www.nvidia.com/en-us/drivers/unix"
source = f"https://github.com/NVIDIA/nvidia-settings/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c6ae554d08a6d7376ede85ae70164b84fa503f1806963d31fa6a44c1404eddfe"
tool_flags = {"CFLAGS": ["-Wno-single-bit-bitfield-constant-conversion"]}
# no test suite
options = ["!check"]


def post_install(self):
    self.install_file(
        "doc/nvidia-settings.png", "usr/share/icons/hicolor/128x128/apps"
    )
    self.install_file("doc/nvidia-settings.desktop", "usr/share/applications")
