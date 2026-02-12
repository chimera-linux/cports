pkgname = "kmail-account-wizard"
pkgver = "25.12.2"
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
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kio-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "qt6-qtdeclarative-devel",
    "qtkeychain-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE KMail account wizard"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://userbase.kde.org/KMail/Account_Wizard"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kmail-account-wizard-{pkgver}.tar.xz"
sha256 = "d3a25bd5a3618f92ebf8bcf3666399cfb9f715d6724265000f463818dd0a99ad"
