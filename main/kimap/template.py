pkgname = "kimap"
pkgver = "26.04.2"
pkgrel = 0
build_style = "cmake"
# no valid mechs
# make_check_args = ["-E", "loginjobtest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kmime-devel",
    "libsasl-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE IMAP access API"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kimap/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kimap-{pkgver}.tar.xz"
sha256 = "0cdb8c01869f82891375f5c7587f02ef8a751e68031aed94e3d0b47f301fc9a8"


@subpackage("kimap-devel-static")
def _(self):
    return ["usr/lib/*.a"]


@subpackage("kimap-devel")
def _(self):
    self.depends += [
        # for cmake detection.. static-only test lib
        self.with_pkgver("kimap-devel-static"),
        "kcoreaddons-devel",
        "kmime-devel",
    ]
    return self.default_devel()
