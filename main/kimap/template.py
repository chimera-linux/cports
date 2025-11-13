pkgname = "kimap"
pkgver = "25.08.3"
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
sha256 = "d6b8307cb2b8833a8df485b87783d58151a28905b7b6e790827c52433489ab3d"


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
