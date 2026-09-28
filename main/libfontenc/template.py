pkgname = "libfontenc"
pkgver = "1.1.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-encodingsdir=/usr/share/fonts/encodings"]
# cycle with mkfontscale
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["xorgproto", "zlib-ng-compat-devel"]
pkgdesc = "Fontenc Library from X.org"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libfontenc-{pkgver}.tar.xz"
sha256 = "7b02c3d405236e0d86806b1de9d6868fe60c313628b38350b032914aa4fd14c6"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libfontenc-devel")
def _(self):
    return self.default_devel()
