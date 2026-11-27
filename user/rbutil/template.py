pkgname = "rbutil"
pkgver = "1.5.1"
pkgrel = 0
build_style = "cmake"
# requires network
make_check_args = ["-E", "TestHttpGet"]
cmake_dir = "utils"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libusb-devel",
    "qt6-qt5compat-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "quazip-devel",
    "speex-devel",
    "speexdsp-devel",
]
pkgdesc = "Rockbox OS installer GUI"
license = "GPL-2.0-only"
url = "https://www.rockbox.org/wiki/RockboxUtility"
source = f"https://download.rockbox.org/rbutil/source/RockboxUtility-v{pkgver}-src.tar.bz2"
sha256 = "82e34ed756b4777d117b13c400040622057d5b5ef38138d9fcb373fe8527e073"
tool_flags = {"CFLAGS": ["-Dloff_t=off_t"], "CXXFLAGS": ["-Dloff_t=off_t"]}
# TODO: test with an actual player
hardening = ["vis", "!cfi"]
# TODO: check stage
options = ["!cross"]


def install(self):
    self.install_license("docs/COPYING")
    self.install_bin(f"{self.make_dir}/ipodpatcher")
    self.install_bin(f"{self.make_dir}/sansapatcher")
    self.install_bin(f"{self.make_dir}/rbutilqt/RockboxUtility")
    self.install_file(
        "utils/rbutilqt/RockboxUtility.desktop", "usr/share/applications"
    )
    self.install_file("docs/logo/rockbox-clef.svg", "usr/share/icons")
