pkgname = "kgpg"
pkgver = "24.12.1"
pkgrel = 0
build_style = "cmake"
# flaky
make_check_args = ["-E", "(kgpg-import|kgpg-encrypt)"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-contacts-devel",
    "gpgme-devel",
    "karchive-devel",
    "kcodecs-devel",
    "kcontacts-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "kjobwidgets-devel",
    "knotifications-devel",
    "kservice-devel",
    "kstatusnotifieritem-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE GnuPG interface"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kgpg"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kgpg-{pkgver}.tar.xz"
sha256 = "4bda4335cbd1e1adaded9fe781a6248a57fdafc2af897053740a542952c58667"
