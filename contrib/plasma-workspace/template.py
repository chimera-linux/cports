pkgname = "plasma-workspace"
pkgver = "6.0.5.1"
pkgrel = 2
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
    + "|testimagebackend"  # cannot find org.kde.plasma.wallpapers.image QML module, try QML2_IMPORT_PATH?
    + "|locationsrunnertest"
    + "|testimagefrontend)",  # ^ same as above
    "-j1",  # parallel causes a bunch of flaky tests
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session", "xwfb-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "appmenu-gtk-module-devel",
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
    "krunner-devel",
    "kquickcharts-devel",
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
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
    "xcb-util-devel",
    # TODO: AppStreamQt (main/appstream + -Dqt=true)
    # NOTE: make sure PolkitQt6-1 doesn't get pulled in?! just -DGLIBC_LOCALE_GEN=OFF
    # TODO: SeleniumWebDriverATSPI? (GUI accessibility tests)
]
depends = [
    "appmenu-gtk-module",
    "iso-codes",
    "kirigami-addons",
    "kio-extras",
    "kio-fuse",
    "kquickcharts",
    "kwin",
    "milou",
    "xwayland",
]
checkdepends = [
    "dbus",
    "python-gobject",
    "xwayland-run",
] + depends
pkgdesc = "KDE Plasma Workspace"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "(GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-or-later AND GPL-2.0-or-later AND MIT AND LGPL-2.1-only AND LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only) AND LGPL-2.0-only"
url = "https://api.kde.org/plasma/plasma-workspace/html"
source = f"$(KDE_SITE)/plasma/6.0.5/plasma-workspace-{pkgver}.tar.xz"
sha256 = "8907f9fded5fc6e5d95355f8346328de18d7c8850dabd9109d75458d5aeed813"
# FIXME: cfi breaks at least 3 tests
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")
    # in KF5 kservice shipped this, but in KF6 it's been moved to here; but also not named this anymore
    # krunner via invocation of kbuildsycoca6 then fails to see any applications outside of kde
    # TODO: find out how this is meant to work at all
    self.install_link(
        "etc/xdg/menus/applications.menu", "plasma-applications.menu"
    )

    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)


@subpackage("plasma-workspace-devel")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (development files)"
    self.depends += [
        "kitemmodels-devel",
        "libplasma-devel",
        "qt6-qtbase-devel",
        "qt6-qtdeclarative-devel",
    ]
    # libkrdb.so unversined, avoid plasma-workspace pulling in plasma-workspace-devel
    return [
        "usr/include",
        "usr/lib/libcolorcorrect.so",
        "usr/lib/libkfontinst*.so",
        "usr/lib/libkmpris.so",
        "usr/lib/libkworkspace6.so",
        "usr/lib/libnotificationmanager.so",
        "usr/lib/libtaskmanager.so",
        "usr/lib/libweather_ion.so",
        "usr/lib/cmake",
    ]
