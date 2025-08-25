pkgname = "kwin"
pkgver = "6.4.4"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
make_check_args = [
    "-E",
    "(kwin-testClientMachine"  # initTestCase() segfaults in libc.so after 5s
    + "|kwin-testPlasmaWindow"  # libc++abi: terminating; testLockScreenNoPlasmaWindow() 'lockStateChangedSpy.wait()' returned FALSE, plasmawindow_test.cpp(262)
    + "|kwin-testDrm"  # testAmsDetection() segfaults
    + "|kwin-testButtonRebind"  # ppc64le fail weirdness?
    + "|kwin-testColorspaces"  # out of range on ppc64le float accuracy
    + "|kwin-testX11Window"  # flaky testStack* subtests
    + "|kwin-testWindowRules"  # flakes
    + "|kwin-testInputMethod"  # flakes
    + "|kwin-testFifo"  # always fails on 24Hz when run with other tests, works alone
    + "|kwin-testXwaylandInput"  # flaky testPointerEnterLeaveSsd() '!window->readyForPainting()' returned FALSE
    + "|^kwayland-testServerSideDecoration$"  # Tried to add event to destroyed queue
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
    "libcap-progs",
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
    "kpipewire-devel",
    "kscreenlocker-devel",
    "kservice-devel",
    "ksvg-devel",
    "kwayland-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "lcms2-devel",
    "libcanberra-devel",
    "libdisplay-info-devel",
    "libei-devel",
    "libplasma-devel",
    "libqaccessibilityclient-devel",
    "libxcvt-devel",
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
depends = ["aurorae", "hwdata", "qt6-qtmultimedia", "xwayland"]
checkdepends = ["breeze", "dbus", "mesa-demos-core", "xwayland-run", *depends]
pkgdesc = "KDE Wayland compositor"
license = (
    "GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-only"
)
url = "https://invent.kde.org/plasma/kwin"
source = f"$(KDE_SITE)/plasma/{'.'.join(pkgver.split('.')[0:3])}/kwin-{pkgver}.tar.xz"
sha256 = "b0742a12133b052519cb5af09132114ebf4d96b44e320015cc0d2d0bf055dae6"
file_modes = {
    "usr/bin/kwin_wayland": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/kwin_wayland": {
        "security.capability": "cap_sys_nice+ep",
    },
}
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kwin-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
