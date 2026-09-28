pkgname = "libgd"
pkgver = "2.3.3_git20230727"
pkgrel = 0
_commit = "0d75136bd3e8651ded7c64a140791ed10de1c63c"
build_style = "gnu_configure"
configure_args = ["--without-xpm"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = [
    "fontconfig-devel",
    "libavif-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libtiff-devel",
    "libwebp-devel",
]
checkdepends = ["fonts-liberation-otf"]
pkgdesc = "Graphics library for the dynamic creation of images"
license = "custom:libgd"
url = "https://libgd.github.io"
# source = f"https://github.com/libgd/libgd/releases/download/gd-{pkgver}/libgd-{pkgver}.tar.xz"
source = f"https://github.com/libgd/libgd/archive/{_commit}.tar.gz"
sha256 = "bf35259c186726b26e486465ef1c9dab75a6be00a2b93e5357b4b71299e6c13a"
# sus codebase, FIXME later (perhaps when investigating newer version)
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libgd-devel")
def _(self):
    return self.default_devel()


@subpackage("libgd-progs")
def _(self):
    self.depends += ["perl"]

    return self.default_progs()
