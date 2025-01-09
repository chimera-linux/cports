pkgname = "editline"
pkgver = "1.17.1"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Small replacement for GNU readline() for UNIX"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "custom:editline"
url = "https://troglobit.com/projects/editline"
source = f"https://github.com/troglobit/editline/releases/download/{pkgver}/editline-{pkgver}.tar.xz"
sha256 = "df223b3333a545fddbc67b49ded3d242c66fadf7a04beb3ada20957fcd1ffc0e"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("editline-devel")
def _(self):
    return self.default_devel()
