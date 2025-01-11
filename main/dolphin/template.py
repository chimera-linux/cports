pkgname = "dolphin"
pkgver = "24.12.1"
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
    "chimerautils-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kfilemetadata-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "kparts-devel",
    "ktextwidgets-devel",
    "kuserfeedback-devel",
    "phonon-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
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
sha256 = "481c0aaa2186354e091256332df1b1c5ca14bec8b59bc8c1e75b6934830a8663"
# fixes copy/pasting file segfault in kio_file.so (KIO::WorkerThread) https://bugs.kde.org/show_bug.cgi?id=470763
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("dolphin-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "qt6-qtbase-devel",
    ]

    return self.default_devel()
