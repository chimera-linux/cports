pkgname = "bambootracker"
pkgver = "0.6.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSYSTEM_RTAUDIO=ON",
    "-DSYSTEM_RTMIDI=ON",
    "-DWARNINGS_ARE_ERRORS=OFF",
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
sha256 = "75e2e1c0c4c99254de96503aea6da0d7effd84b800f93327fc4d9fc16846ca46"
# crashes instantly with default stack size
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
