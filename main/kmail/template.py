pkgname = "kmail"
pkgver = "24.12.2"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "akonadi-sqlite-.*"]
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
    "akonadi-devel",
    "akonadi-mime-devel",
    "akonadi-search-devel",
    "gpgme-devel",
    "kbookmarks-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcontacts-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kitemviews-devel",
    "kjobwidgets-devel",
    "kldap-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kontactinterface-devel",
    "kparts-devel",
    "kpimtextedit-devel",
    "kservice-devel",
    "kstatusnotifieritem-devel",
    "ktextaddons-devel",
    "ktextwidgets-devel",
    "ktnef-devel",
    "kuserfeedback-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libgravatar-devel",
    "libkdepim-devel",
    "libkleo-devel",
    "libksieve-devel",
    "mailcommon-devel",
    "messagelib-devel",
    "pimcommon-devel",
    "qt6-qtbase-devel",
    "qt6-qtwebengine-devel",
    "qtkeychain-devel",
    "sonnet-devel",
]
depends = [
    "kdepim-runtime",
    "kmail-account-wizard",
]
checkdepends = [*depends]
pkgdesc = "KDE Mail Client"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-2.0-only"
url = "https://apps.kde.org/kmail2"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kmail-{pkgver}.tar.xz"
sha256 = "316949439902dde5130c7e2ef96d2bee458123ed33d160b478d57f9a6a864271"
