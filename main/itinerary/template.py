pkgname = "itinerary"
pkgver = "25.08.3"
pkgrel = 0
build_style = "cmake"
# fails with no output
make_check_args = ["-E", "itinerary-self-test"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcalendarcore-devel",
    "kcontacts-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kfilemetadata-devel",
    "khealthcertificate-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kitemmodels-devel",
    "kitinerary-devel",
    "knotifications-devel",
    "kopeninghours-devel",
    "kosmindoormap-devel",
    "kpkpass-devel",
    "kpublictransport-devel",
    "kunitconversion-devel",
    "kwindowsystem-devel",
    "libical-devel",
    "libquotient-devel",
    "networkmanager-qt-devel",
    "prison-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtbase-private-devel",  # qjson_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtlocation-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtpositioning-devel",
    "solid-devel",
    "zlib-ng-compat-devel",
]
depends = [
    "kirigami-addons",
    "kitemmodels",
    "kopeninghours",
    "prison",
    "qt6-qtlocation",
]
pkgdesc = "KDE digital travel assistant"
license = "LGPL-2.0-or-later"
url = "https://apps.kde.org/itinerary"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/itinerary-{pkgver}.tar.xz"
sha256 = "28f8cef47f949ce48326f6d2882d58c1c797a6e324c51f5d3510e7db22161f87"
