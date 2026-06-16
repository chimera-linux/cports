pkgname = "audiotube"
pkgver = "26.04.2"
pkgrel = 0
build_style = "cmake"
_deps = [
    "kirigami-addons",
    "python-ytmusicapi",
    "yt-dlp",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    *_deps,
]
makedepends = [
    "futuresql-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kwindowsystem-devel",
    "python-devel",
    "python-pybind11-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
]
depends = [*_deps]
pkgdesc = "KDE Youtube Music player"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/audiotube"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/audiotube-{pkgver}.tar.xz"
sha256 = "af049214826346351215c8604e74ab74409cc9bf3005565b2a280fcd5afed393"
# ??? since pybind or audiotube update
tool_flags = {
    "CXXFLAGS": ["-I/usr/include/python3.14"],
    "LDFLAGS": ["-lpython3.14"],
}
# only test needs net
options = ["!check"]
