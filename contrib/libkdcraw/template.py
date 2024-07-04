pkgname = "libkdcraw"
pkgver = "24.05.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # manual test bins
    "-DBUILD_TESTING=OFF",
    "-DQT_MAJOR_VERSION=6",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libraw-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE wrapper around libraw"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/libkdcraw/html/index.html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkdcraw-{pkgver}.tar.xz"
sha256 = "59ebc1634eccfc5b9a10c92ec2ab9f3e49245c2044692c6cfb717239a28b8a28"
# CFI: check
hardening = ["vis", "!cfi"]


@subpackage("libkdcraw-devel")
def _devel(self):
    return self.default_devel()
