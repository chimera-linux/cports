pkgname = "akregator"
pkgver = "25.12.2"
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
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/akregator"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/akregator-{pkgver}.tar.xz"
sha256 = "aebdb1e994d61ea447e23880eb837a4aa0dfca1cc05ef7bc223c4060cbd76fd8"
# INT: probably a shift overflow in remap.cpp:CalcHash
hardening = ["!int"]
