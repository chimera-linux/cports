pkgname = "kitinerary"
pkgver = "24.05.0"
pkgrel = 0
build_style = "cmake"
# difference in AT/österreich key
make_check_args = ["-E", "extractortest"]
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
    "ki18n-devel",
    "kmime-devel",
    "kpkpass-devel",
    "libphonenumber-devel",
    "libpoppler-devel",
    "libxml2-devel",
    "openssl-devel",
    "qt6-qtdeclarative-devel",
    "shared-mime-info",
    "zlib-devel",
    "zxing-cpp-devel",
]
pkgdesc = "KDE travel reservation parsing library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kitinerary/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kitinerary-{pkgver}.tar.xz"
sha256 = "f4fd921417ce9c982af1bdc1afdf713b6ff0f80eabc2781e5ab573f57ed525a3"


@subpackage("kitinerary-devel")
def _devel(self):
    self.depends += [
        "kcalendarcore-devel",
        "kcontacts-devel",
        "kmime-devel",
        "kpkpass-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
