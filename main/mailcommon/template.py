pkgname = "mailcommon"
pkgver = "25.12.0"
pkgrel = 0
build_style = "cmake"
# sqlite all fail
# encryptions fail for some reason
make_check_args = ["-E", "(akonadi-sqlite-.*|filteractionencrypttest)"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "libxslt-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-mime-devel",
    "gpgme-qt-devel",
    "karchive-devel",
    "kcodecs-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kdbusaddons-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kitemviews-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "ktextaddons-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "libkdepim-devel",
    "mailimporter-devel",
    "messagelib-devel",
    "phonon-devel",
    "pimcommon-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qttools-devel",
    "syntax-highlighting-devel",
]
pkgdesc = "KDE PIM library for mail applications"
license = "LGPL-3.0-only AND GPL-3.0-only"
url = "https://api.kde.org/kdepim/mailcommon/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/mailcommon-{pkgver}.tar.xz"
sha256 = "18831ad5a92b2c8705873d4776ad460d3b38cbce600f6e60feb6093be4b1d652"


@subpackage("mailcommon-devel")
def _(self):
    self.depends += [
        "akonadi-devel",
        "akonadi-mime-devel",
        "libkdepim-devel",
        "messagelib-devel",
        "pimcommon-devel",
        "kcompletion-devel",
    ]
    return self.default_devel()
