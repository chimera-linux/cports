pkgname = "ktextaddons"
pkgver = "1.8.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
make_check_args = [
    "-E",
    "(texttospeechwidgettest"  # hangs
    + "|texttospeechactionstest"  # fail in headless
    + "|grammalecteresultwidgettest"
    + "|grammalecteconfigwidgettest"
    + "|languagetoolconfigwidgettest"
    + "|texttospeechactionstest"  # need translator plugins
    + "|translatorwidgettest"
    + "|translatorengineloadertest"
    + ")",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "karchive-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "ktextwidgets-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtspeech-devel",
    "qt6-qttools-devel",
    "qtkeychain-devel",
    "sonnet-devel",
    "syntax-highlighting-devel",
]
pkgdesc = "KDE text handling addons library"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/libraries/ktextaddons"
source = f"$(KDE_SITE)/ktextaddons/ktextaddons-{pkgver}.tar.xz"
sha256 = "159c605d3d031bf818e164ea410150103c5f9f87cea35e2979e42d86c3318c99"


@subpackage("ktextaddons-devel")
def _(self):
    self.depends += ["kconfigwidgets-devel"]
    return self.default_devel()
