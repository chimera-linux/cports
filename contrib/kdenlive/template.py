pkgname = "kdenlive"
pkgver = "24.08.0"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    # FIXME: flaky segfaults/aborts
    "(keyframetest|mixtest|effectstest|filetest|timelinepreviewtest)",
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
    "v4l-utils-devel",
]
depends = [
    "ffmpeg",
    "frei0r",
]
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE video editor"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kdenlive"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdenlive-{pkgver}.tar.xz"
sha256 = "e4306a2aa5a7535cea50aeff493ea9de8b7292d499d7204c41780cb044752f96"
# avoid crashes
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# INT: crashes spacertest/trimmingtest
hardening = ["vis", "!int"]
# TODO
options = ["!cross"]


def init_configure(self):
    ljobs = 3 if self.make_jobs >= 3 else self.make_jobs
    # test links are extremely spicy so ensure there is not more than three
    self.configure_args += [
        f"-DCMAKE_JOB_POOLS=nyanya={ljobs}",
        "-DCMAKE_JOB_POOL_LINK=nyanya",
    ]
