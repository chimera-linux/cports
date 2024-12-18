pkgname = "plasma-workspace"
pkgver = "6.2.4"
pkgrel = 1
build_style = "cmake"
# TODO: -DINSTALL_SDDM_WAYLAND_SESSION=ON experiments?
configure_args = ["-DGLIBC_LOCALE_GEN=OFF"]
make_check_args = [
    "-E",
    "(^tasksmodeltest$"  # failing test_moveLauncherBug472524() & test_moveBug444816()
    + "|shelltest"  # SEGFAULT in initTestCase(), Invalid home screen package + missing org.kde.desktopcontainment (plasmoid)?
    + "|tst_triangleFilter"  # needs installed org.kde.plasma.private.kicker QML module
    + "|systemtraymodeltest"  # testPlasmoidModel() seems to have another case of broken QFINDTESTDATA, systemtraymodeltest.cpp(79)
    + "|testimagefinder"  # ImageFinder doesn't find testdata/default/.BUG460287/*.webp for some reason, test_imagefinder.cpp(64)
    + "|testimagelistmodel"  # ^ probably same as above, test_imagelistmodel.cpp(81)
    + "|testpackageimagelistmodel"  # just SEGFAULTS after testPackageListModelRemoveBackground(), broken kio? test_packagelistmodel.cpp(262)
    + "|testimageproxymodel"  # looks like same issue as testimagefinder & testimagelistmodel
    + "|testslidemodel"  # ^ same as above
    + "|testrunnermodel"  # segfaults on aarch64
    + "|keystatetest"  # fails in offscreen
    + "|lockedtest"  # needs selenium
    + "|klipper*"  # most of these segfault
    + "|dbusmethodcalltest"  # fails to send something to ksplash (?)
    + "|servicerunnertest"  # fails to spawn stuff in sandbox somehow
    + "|lookandfeel-kcmTest"  # segfaults with our patch to default theme
    + "|testimagebackend"  # cannot find org.kde.plasma.wallpapers.image QML module, try QML2_IMPORT_PATH
    + "|locationsrunnertest"
    + "|testimagefrontend)",  # ^ same as above
    "-j1",  # parallel causes a bunch of flaky tests
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen", "XDG_RUNTIME_DIR": "/tmp"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "appmenu-gtk-module-devel",
    "appstream-qt-devel",
    "baloo-devel",
    "breeze-devel",
    "fontconfig-devel",
    "karchive-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdeclarative-devel",
    "kded-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidletime-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kparts-devel",
    "kpipewire-devel",
    "kquickcharts-devel",
    "krunner-devel",
    "kscreenlocker-devel",
    "kstatusnotifieritem-devel",
    "ksvg-devel",
    "ktexteditor-devel",
    "ktextwidgets-devel",
    "kunitconversion-devel",
    "kuserfeedback-devel",
    "kwallet-devel",
    "kwayland-devel",
    "kwin-devel",
    "layer-shell-qt-devel",
    "libcanberra-devel",
    "libice-devel",
    "libkexiv2-devel",
    "libkscreen-devel",
    "libksysguard-devel",
    "libplasma-devel",
    "libqalculate-devel",
    "libsm-devel",
    "networkmanager-qt-devel",
    "phonon-devel",
    "plasma-activities-devel",
    "plasma-activities-stats-devel",
    "plasma-wayland-protocols",
    "plasma5support-devel",
    "prison-devel",
    "qcoro-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtpositioning-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
    "xcb-util-devel",
    # NOTE: make sure PolkitQt6-1 doesn't get pulled in?! just -DGLIBC_LOCALE_GEN=OFF
    # TODO: SeleniumWebDriverATSPI? (GUI accessibility tests)
]
depends = [
    "appmenu-gtk-module",
    "chimera-artwork-kde",
    "iso-codes",
    "kio-extras",
    "kio-fuse",
    "kirigami-addons",
    "kquickcharts",
    "kwin",
    "milou",
    "xwayland",
]
checkdepends = [
    "dbus-x11",
    "python-gobject",
    *depends,
]
# kde-portals.conf is now here
replaces = ["xdg-desktop-portal-kde<6.2.1"]
pkgdesc = "KDE Plasma Workspace"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT AND GPL-3.0-only AND LGPL-3.0-only"
url = "https://api.kde.org/plasma/plasma-workspace/html"
source = f"$(KDE_SITE)/plasma/{'.'.join(pkgver.split('.')[0:3])}/plasma-workspace-{pkgver}.tar.xz"
sha256 = "32aa3bda29d7b76a7dae7e1f8c9789cfe7f609eb878e1a793db4b1490ca3c174"
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
    # in KF5 kservice shipped this, but in KF6 it's been moved to here; but also not named this anymore
    # krunner via invocation of kbuildsycoca6 then fails to see any applications outside of kde
    # TODO: find out how this is meant to work at all
    self.install_link(
        "etc/xdg/menus/applications.menu", "plasma-applications.menu"
    )

    for theme in ["breeze", "breezedark", "breezetwilight"]:
        previews_path = f"usr/share/plasma/look-and-feel/org.kde.{theme}.desktop/contents/previews"
        self.uninstall(f"{previews_path}/*", glob=True)

    self.uninstall("usr/lib/systemd/user")


@subpackage("plasma-workspace-devel")
def _(self):
    return self.default_devel()
