pkgname = "akregator"
pkgver = "24.08.3"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
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
    "kiconthemes-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kontactinterface-devel",
    "kparts-devel",
    "kstatusnotifieritem-devel",
    "ktextaddons-devel",
    "ktexttemplate-devel",
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
checkdepends = ["xwayland-run"]
pkgdesc = "KDE RSS feed reader"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/akregator"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akregator-{pkgver}.tar.xz"
sha256 = "78e6f8702b9b32bfad8ba16751abdcac40ac86dc771a5f6b7e9790679d5cf01b"
# INT: probably a shift overflow in remap.cpp:CalcHash
hardening = ["!int"]
