pkgname = "musl-locales"
pkgver = "0.1.0"
pkgrel = 0
build_style = "cmake"
# We patch musl to default `MUSL_LOCPATH` to the appropriate path, so the
# profile script isn't necessary
configure_args = ["-DLOCALE_PROFILE=OFF", "-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "gettext", "ninja"]
makedepends = ["gettext-devel"]
pkgdesc = "Locale program and translation files for musl"
license = "LGPL-3.0-only AND MIT"
url = "https://git.adelielinux.org/adelie/musl-locales"
source = f"{url}/-/archive/{pkgver}/musl-locales-{pkgver}.tar.gz"
sha256 = "9527cb6450a247f6db8e02d837bc169c1f4e4dba3ab8e6bd997f6ff4e530808d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE.MIT")
