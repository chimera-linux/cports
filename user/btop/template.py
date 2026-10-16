pkgname = "btop"
pkgver = "1.4.7"
_therock_ver = "10.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBTOP_LTO=OFF",
    "-DBTOP_FORTIFY=OFF",
    "-DBTOP_RSMI_STATIC=ON",
]
hostmakedepends = ["cmake", "ninja", "lowdown", "pkgconf", "libdrm-devel"]
makedepends = ["linux-headers"]
checkdepends = ["gtest-devel"]
pkgdesc = "TUI monitor of system resources"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = [
    f"{url}/archive/v{pkgver}/btop-{pkgver}.tar.gz",
    f"https://github.com/ROCm/rocm-systems/releases/download/therock-{_therock_ver}/rocm-smi-lib.tar.gz",
]
source_paths = [".", "lib/rocm_smi_lib"]
sha256 = [
    "933de2e4d1b2211a638be463eb6e8616891bfba73aef5d38060bd8319baeefc6",
    "9648663235c93bbdec91149003c7b1b9e7dcdf3a3728d527298f2ce457916ecb",
]
hardening = ["cfi", "vis"]
