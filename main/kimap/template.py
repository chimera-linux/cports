pkgname = "kimap"
pkgver = "25.12.0"
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
sha256 = "c520f4dad64c3c719035b8f0ed6842551a85008c365383cba22ec64cc997a3b4"


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
