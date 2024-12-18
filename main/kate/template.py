pkgname = "kate"
pkgver = "24.12.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
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
    "kuserfeedback-devel",
    "kwallet-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
depends = ["konsole"]
pkgdesc = "KDE Advanced Text Editor"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/kate"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kate-{pkgver}.tar.xz"
sha256 = "a5926a0d85c69ca2cc34d87e567501e795e95050e16f896e39cd8cac4ced2348"
hardening = ["vis"]
# no idea
options = ["!check"]


# for kwrite to not pull in kate
@subpackage("kate-libs")
def _(self):
    return self.default_libs()


@subpackage("kwrite")
def _(self):
    self.subdesc = "KWrite"
    return [
        "usr/bin/kwrite",
        "usr/share/icons/hicolor/*/apps/kwrite.*",
        "usr/share/applications/org.kde.kwrite.desktop",
        "usr/share/metainfo/org.kde.kwrite.appdata.xml",
    ]
