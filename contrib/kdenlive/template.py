pkgname = "kdenlive"
pkgver = "24.05.1"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    # FIXME: segfaults/aborts
    "(keyframetest|mixtest|effectstest|filetest)",
]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kbookmarks-devel",
    "kcodecs-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kfilemetadata-devel",
    "kguiaddons-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "mlt-devel",
    "purpose-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtnetworkauth-devel",
    "qt6-qtsvg-devel",
    "solid-devel",
]
depends = ["frei0r"]
checkdepends = ["xwayland-run"] + depends
pkgdesc = "KDE video editor"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kdenlive"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdenlive-{pkgver}.tar.xz"
sha256 = "1092592de71675afb08ee67ac9a71d3115b3ee3548da52759971c5b0026103da"
# avoid crashes
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# CFI: crashes most tests
# INT: crashes spacertest/trimmingtest
hardening = ["vis", "!cfi", "!int"]
# TODO
options = ["!cross"]


def init_configure(self):
    ljobs = 3 if self.make_jobs >= 3 else self.make_jobs
    # test links are extremely spicy so ensure there is not more than two
    self.configure_args += [
        f"-DCMAKE_JOB_POOLS=nyanya={ljobs}",
        "-DCMAKE_JOB_POOL_LINK=nyanya",
    ]
