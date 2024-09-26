pkgname = "bambootracker"
pkgver = "0.6.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSYSTEM_RTAUDIO=ON",
    "-DSYSTEM_RTMIDI=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "rtaudio-devel",
    "rtmidi-devel",
    "qt6-qt5compat-devel",
    "qt6-qttools-devel",
]
pkgdesc = "YM2608 music tracker"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://bambootracker.github.io/BambooTracker"
source = f"https://github.com/BambooTracker/BambooTracker/releases/download/v{pkgver}/BambooTracker-src-v{pkgver}.tar.gz"
sha256 = "fad9f045ff525ad406b25d2f58c23faca64008abf27b1326c33021a8e4436adf"
# crashes instantly with default stack size
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
