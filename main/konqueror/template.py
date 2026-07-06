pkgname = "konqueror"
pkgver = "26.04.3"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    # FIXME: crashes / hangs
    "(konqviewtest"
    + "|konqhtmltest"
    + "|sidebar-modulemanagertest"
    + "|konqpopupmenutest"
    + "|webengine_partapi_test"
    + "|konqviewmgrtest)",
]
make_check_wrapper = ["dbus-run-session", "--", "wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "hunspell",
    "ninja",
    "pkgconf",
]
makedepends = [
    "hunspell-devel",
    "karchive-devel",
    "kcmutils-devel",
    "kcodecs-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdesu-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "knotifications-devel",
    "kparts-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "kwindowsystem-devel",
    "plasma-activities-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtwebengine-devel",
    "sonnet-devel",
]
checkdepends = ["dbus", "xwayland-run"]
pkgdesc = "KDE web browser and file previewer"
license = "LGPL-3.0-only AND GPL-2.0-or-later"
url = "https://apps.kde.org/konqueror"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/konqueror-{pkgver}.tar.xz"
sha256 = "c5ad4e700f9f43f9c647e3c011d7918911cf5c0e4d7811875967cb37a34692e3"
hardening = ["vis"]
options = ["etcfiles"]


@subpackage("konqueror-devel")
def _(self):
    return self.default_devel()
