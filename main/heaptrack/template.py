pkgname = "heaptrack"
pkgver = "1.5.0"
pkgrel = 4
build_style = "cmake"
configure_args = [
    "-DHEAPTRACK_USE_QT6=ON",
    "-DLIBUNWIND_INCLUDE_DIR=/usr/include/libunwind-nongnu",
    "-DLIBUNWIND_LIBRARY=unwind-nongnu",
]
configure_env = {"CMAKE_POLICY_VERSION_MINIMUM": "3.5"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "elfutils-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kdiagram-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kitemmodels-devel",
    "libunwind-nongnu-devel",
    "linux-headers",
    "qt6-qtbase-devel",
    "threadweaver-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "KDE heap memory profiler"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/heaptrack"
source = f"$(KDE_SITE)/heaptrack/{pkgver}/heaptrack-{pkgver}.tar.xz"
sha256 = "a278d9d8f91e8bfb8a1c2f5b73eecab47fd45d0693f5dbea637536413cec2ea5"
# FIXME: weird failures
options = ["!check"]
