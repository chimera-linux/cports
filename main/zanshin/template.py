pkgname = "zanshin"
pkgver = "25.12.1"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    "(akonadi-akonadi.*|editingtaskfeature|inboxpagemodeltest|alltaskspagemodeltest|migrationtest|pageviewtest)",
    "-j1",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-calendar-devel",
    "akonadi-devel",
    "boost-devel",
    "kcalendarcore-devel",
    "kcrash-devel",
    "ki18n-devel",
    "kontactinterface-devel",
    "kparts-devel",
    "krunner-devel",
    "kwindowsystem-devel",
    "qt6-qtbase-devel",
]
checkdepends = [
    "dbus",
    "kdepim-runtime",
]
pkgdesc = "KDE time management assistant"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://zanshin.kde.org"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/zanshin-{pkgver}.tar.xz"
sha256 = "cab673e121caacbaa9db5203dc307fb137696d4ff615968b7eecd2146cef9ecd"
