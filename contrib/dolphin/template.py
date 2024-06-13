pkgname = "dolphin"
pkgver = "24.05.1"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    # testIndexForKeyboardSearch() Compared values are not the same (7 vs 6), kfileitemmodeltest.cpp:1297,
    "(kfileitemmodel"
    # fails to baloo index
    + "|dolphinquerytest|"
    # testOpenInNewTabTitle() 'tabWidget->tabText(0) != tabWidget->tabText(1)' returned FALSE, dolphinmainwindowtest.cpp:221
    # other times SEGFAULT in testClosingTabsWithSearchBoxVisible() due to rlimit?
    + "|dolphinmainwindow)test",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "baloo-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kfilemetadata-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "kparts-devel",
    "ktextwidgets-devel",
    "kuserfeedback-devel",
    "musl-fts-devel",
    "phonon-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
    # TODO: PackageKitQt6 (service menu installer)
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE File Manager"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/dolphin"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/dolphin-{pkgver}.tar.xz"
sha256 = "aafc4fba0a03c9af397f878b0cbc0ec23c6ebd08cfb9cddcbf6bd23ca806bab8"
# fixes copy/pasting file segfault in kio_file.so (KIO::WorkerThread) https://bugs.kde.org/show_bug.cgi?id=470763
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# FIXME: cfi breaks at least dolphinmainwindowtest in libdolphinprivate
hardening = ["vis", "!cfi"]


def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)


@subpackage("dolphin-devel")
def _devel(self):
    self.depends += [
        "kio-devel",
        "qt6-qtbase-devel",
    ]

    return self.default_devel()
