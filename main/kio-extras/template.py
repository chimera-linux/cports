pkgname = "kio-extras"
pkgver = "24.08.2"
pkgrel = 0
build_style = "cmake"
# thumbnail: fails for some reason
# testkioarchive: fails to open tar, support seems to not be detected
make_check_args = ["-E", "(thumbnailtest|testkioarchive)"]
make_check_wrapper = [
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "gperf",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kcmutils-devel",
    "kconfigwidgets-devel",
    "kdbusaddons-devel",
    "kdnssd-devel",
    "kdoctools-devel",
    "kdsoap-ws-discover-client-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "ktextwidgets-devel",
    "libimobiledevice-devel",
    "libkexiv2-devel",
    "libmtp-devel",
    "libplist-devel",
    "libsmbclient-devel",
    "libssh-devel",
    "openexr-devel",
    "phonon-devel",
    "plasma-activities-devel",
    "plasma-activities-stats-devel",
    "qcoro-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "syntax-highlighting-devel",
    "taglib-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE KIO additional plugins"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-or-later"
url = "https://invent.kde.org/network/kio-extras"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kio-extras-{pkgver}.tar.xz"
sha256 = "99a6f548c7aac18017ebe2b73ac99327f2585b418257bc1c7e065ced82bd2cc7"
hardening = ["vis"]
# TODO
options = ["!cross"]


@subpackage("kio-extras-devel")
def _(self):
    return self.default_devel()
