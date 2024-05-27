pkgname = "kate"
pkgver = "24.05.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "ktexteditor-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "qt6-qtdeclarative-devel",
    # TODO: KF6UserFeedback
]
# depends = ["?"]
pkgdesc = "KDE Advanced Text Editor"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/kate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kate-{pkgver}.tar.xz"
sha256 = "d2dc5fdf099068d315be9562d334c980c80ef6df7cd7400013abc38d4a4ed626"
# FIXME: cfi breaks at least location_history_test & kate_view_mgmt_tests
hardening = ["vis", "!cfi"]


# TODO: subpkg to allow installing kwrite without bringing in kate as well?
# @subpackage("kwrite")
# def _kwrite(self):
#    _icons = []
#    for f in (self.destdir / "usr/share/icons/hicolor").glob("*/apps/kwrite.*"):
#        # _icons.append(f.removeprefix(self.destdir))  # FIXME: busted
#    return [
#        "usr/bin/kwrite",
#        "usr/share/applications/org.kde.kwrite.desktop",
#        "usr/share/metainfo/org.kde.kwrite.appdata.xml",
#    ] + _icons
