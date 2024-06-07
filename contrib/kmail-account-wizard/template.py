pkgname = "kmail-account-wizard"
pkgver = "24.05.0"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "akonadi-sqlite-.*"]
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
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE KMail account wizard"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://userbase.kde.org/KMail/Account_Wizard"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kmail-account-wizard-{pkgver}.tar.xz"
sha256 = "440209528700fe648fffbe143cb657d0bc8c6275776aef6a4e35d5f45385c3ad"
