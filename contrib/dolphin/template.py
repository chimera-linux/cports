pkgname = "dolphin"
pkgver = "24.05.0"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    # testIndexForKeyboardSearch() Compared values are not the same (7 vs 6), kfileitemmodeltest.cpp:1297,
    "(kfileitemmodel"
    # testOpenInNewTabTitle() 'tabWidget->tabText(0) != tabWidget->tabText(1)' returned FALSE, dolphinmainwindowtest.cpp:221
    # other times SEGFAULT in testClosingTabsWithSearchBoxVisible() due to rlimit?
    "|dolphinmainwindow)test",
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
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "kparts-devel",
    "ktextwidgets-devel",
    "musl-fts-devel",
    "phonon-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
    # "kuserfeedback-devel",  TODO: package
    # TODO: PackageKitQt6 (service menu installer)
    # TODO: KF6Baloo + KF6BalooWidgets
    # TODO: KF6FileMetaData
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE File Manager"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/dolphin"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/dolphin-{pkgver}.tar.xz"
sha256 = "e009ce734355481a08ffff13e6f6a7db8b6b74fa320030b35d9180a1d9ca0794"
# fixes copy/pasting file segfault in kio_file.so (KIO::WorkerThread) https://bugs.kde.org/show_bug.cgi?id=470763
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# FIXME: cfi breaks at least dolphinmainwindowtest in libdolphinprivate
hardening = ["vis", "!cfi"]


@subpackage("dolphin-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
