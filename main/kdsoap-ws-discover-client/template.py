pkgname = "kdsoap-ws-discover-client"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = ["kdsoap-devel"]
pkgdesc = "WS-Discovery client library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://invent.kde.org/libraries/kdsoap-ws-discovery-client"
source = f"$(KDE_SITE)/kdsoap-ws-discovery-client/kdsoap-ws-discovery-client-{pkgver}.tar.xz"
sha256 = "2cd247c013e75f410659bac372aff93d22d71c5a54c059e137b9444af8b3427a"
hardening = ["vis"]
# FIXME: needs network?
options = ["!check"]


@subpackage("kdsoap-ws-discover-client-devel")
def _(self):
    self.depends += [
        "kdsoap-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
