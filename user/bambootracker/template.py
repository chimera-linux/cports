pkgname = "bambootracker"
pkgver = "0.6.5"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DSYSTEM_RTAUDIO=ON",
    "-DSYSTEM_RTMIDI=ON",
    "-DWARNINGS_ARE_ERRORS=OFF",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "qt6-qt5compat-devel",
    "qt6-qttools-devel",
    "rtaudio-devel",
    "rtmidi-devel",
]
pkgdesc = "YM2608 music tracker"
license = "GPL-2.0-or-later"
url = "https://bambootracker.github.io/BambooTracker"
source = f"https://github.com/BambooTracker/BambooTracker/releases/download/v{pkgver}/BambooTracker-src-v{pkgver}.tar.gz"
sha256 = "28cf80b7e96526085b533f2fc9b59dd16216e07d26cd84445da60a36a9e6f443"
# crashes instantly with default stack size
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
