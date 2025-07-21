pkgname = "akonadi"
pkgver = "25.04.3"
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
# itemcreatehandlertest: no idea
# sqlite: all hang (?)
# mysql: needs running mysql
# statisticsproxymodeltest: prolly broken with qt 6.8
make_check_args = [
    "-E",
    "(entitytreemodeltest|mimetypecheckertest|itemcreatehandlertest|.*sqlite.*|.*mysql.*|statisticsproxymodeltest)",
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
    "libxslt-progs",
    "ninja",
    "pkgconf",
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
checkdepends = ["dbus", "xwayland-run", *depends]
pkgdesc = "KDE storage service for PIM data"
license = "LGPL-2.1-or-later"
url = "https://userbase.kde.org/Akonadi"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-{pkgver}.tar.xz"
sha256 = "042cd3319eadfb82547773e52ce7d41d361d58c4e92fe75a5179c1574ed4f5df"
tool_flags = {
    # disable debug mode
    "CXXFLAGS": ["-DNDEBUG"],
    # lots of recursion
    "LDFLAGS": ["-Wl,-z,stack-size=0x200000"],
}


@subpackage("akonadi-devel")
def _(self):
    self.depends += [
        "kconfig-devel",
        "kconfigwidgets-devel",
        "kcoreaddons-devel",
        "kitemmodels-devel",
        "kxmlgui-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
