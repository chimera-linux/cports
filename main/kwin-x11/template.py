pkgname = "kwin-x11"
pkgver = "6.4.5"
pkgrel = 1
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
make_check_args = [
    "-E",
    "(kwin-testClientMachine"  # initTestCase() segfaults in libc.so after 5s
    + "|^kwin-testXdgShellWindow$"  # testDesktopFileName() Compared values are not the same ("" vs "kwin-x11"), xdgshellwindow_test.cpp(705)
    + "|kwin-testScreenEdges"  # 8/20 subtests fail, testPushBack() & testTouchCallback() invalid touch moves
    + "|kwin-testPlasmaWindow"  # testLockScreenNoPlasmaWindow() '!waylandServer()->isScreenLocked()' returned FALSE, plasmawindow_test.cpp(267)
    + "|kwin-testScriptingScreenEdge"  # 4/18 subtests fail, testTouchEdge() & testDeclarativeTouchEdge() invalid touch moves
    + "|kwin-testColorspaces"  # out of range on ppc64le float accuracy
    + "|kwin-testWindowRules"  # flakes
    + "|kwin-testInputMethod"  # flakes
    + "|kwin-testX11Window"  # flaky subtests (especially testStackAboveFromApplication)
    + "|kwin-testXwaylandInput"  # flaky testPointerEnterLeaveSsd() '!window->readyForPainting()' returned FALSE
    + ")",
    # parallel tests cause a bunch of flakes
    "-j1",
]
# D-Bus session needed by kwin-testLibinputDevice, X11 required by half the tests
make_check_wrapper = ["dbus-run-session", "xwfb-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "breeze-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdeclarative-devel",
    "kdecoration-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "kglobalacceld-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kidletime-devel",
    "kirigami-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "kpackage-devel",
    "kscreenlocker-devel",
    "kservice-devel",
    "ksvg-devel",
    "kwayland-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "lcms2-devel",
    "libcanberra-devel",
    "libdisplay-info-devel",
    "libplasma-devel",
    "libqaccessibilityclient-devel",
    "plasma-activities-devel",
    "plasma-wayland-protocols",
    "qt6-qt5compat-devel",
    "qt6-qtbase-private-devel",  # qtguiglobal_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsensors-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
    "xcb-util-devel",
]
depends = ["aurorae", "hwdata", "qt6-qtmultimedia"]
checkdepends = ["breeze", "dbus", "mesa-demos-core", "xwayland-run", *depends]
pkgdesc = "KDE X11 window manager and compositor"
license = (
    "GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-only"
)
url = "https://invent.kde.org/plasma/kwin-x11"
source = f"$(KDE_SITE)/plasma/{'.'.join(pkgver.split('.')[0:3])}/kwin-x11-{pkgver}.tar.xz"
sha256 = "cea91879467afdfa2caf0ec6dd7256eae78defa970cdc9a947fefd85d417acb1"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kwin-x11-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
