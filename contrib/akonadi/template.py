pkgname = "akonadi"
pkgver = "24.05.2"
pkgrel = 0
build_style = "cmake"
# TODO: add mariadb since it's usually the default
configure_args = [
    "-DDATABASE_BACKEND=SQLITE",
    "-DINSTALL_APPARMOR=OFF",
]
# entitytreemodeltest: Collection/Col differ
# mimetypecheckertest: x-vnd.akonadi.calendar.event mime invalid
# collectionschedulertest: flaky
# sqlite: all hang (?)
# mysql: needs running mysql
make_check_args = [
    "-E",
    "(entitytreemodeltest|mimetypecheckertest|.*sqlite.*|.*mysql.*)",
    # flaky
    "-j1",
]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "kaccounts-integration-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kitemmodels-devel",
    "kxmlgui-devel",
    "libaccounts-qt-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "sqlite-devel",
    "xz-devel",
]
depends = ["qt6-qtbase-sql"]
checkdepends = ["dbus", "xwayland-run"] + depends
pkgdesc = "KDE storage service for PIM data"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://userbase.kde.org/Akonadi"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-{pkgver}.tar.xz"
sha256 = "887966e46ce80c974ed27902531ffbf38cb621c6ad429e5576e5510da190fd79"
tool_flags = {
    # disable debug mode
    "CXXFLAGS": ["-DNDEBUG"],
    # lots of recursion
    "LDFLAGS": ["-Wl,-z,stack-size=0x200000"],
}


@subpackage("akonadi-devel")
def _devel(self):
    self.depends += [
        "kconfig-devel",
        "kconfigwidgets-devel",
        "kcoreaddons-devel",
        "kitemmodels-devel",
        "kxmlgui-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel(extra=["usr/lib/qt6/plugins/designer"])
