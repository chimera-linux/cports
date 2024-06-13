pkgname = "akregator"
pkgver = "24.05.1"
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
    "akonadi-devel",
    "grantleetheme-devel",
    "kcmutils-devel",
    "kcodecs-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kontactinterface-devel",
    "kparts-devel",
    "kstatusnotifieritem-devel",
    "ktextaddons-devel",
    "ktextwidgets-devel",
    "kuserfeedback-devel",
    "kxmlgui-devel",
    "libkdepim-devel",
    "messagelib-devel",
    "pimcommon-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwebengine-devel",
    "syndication-devel",
]
pkgdesc = "KDE RSS feed reader"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/akregator"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akregator-{pkgver}.tar.xz"
sha256 = "3f09a17c3bb79ed19e21c628900786bd3eab73f482199a2dd09c865de83c8244"
# INT: probably a shift overflow in remap.cpp:CalcHash
hardening = ["!int"]
