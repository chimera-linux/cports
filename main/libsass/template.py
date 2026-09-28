pkgname = "libsass"
pkgver = "3.6.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "C implementation of the Sass CSS preprocessor"
license = "MIT"
url = "https://www.sass-lang.com/libsass"
source = f"https://github.com/sass/libsass/archive/{pkgver}.tar.gz"
sha256 = "11f0bb3709a4f20285507419d7618f3877a425c0131ea8df40fe6196129df15d"


def pre_configure(self):
    # otherwise the .pc file will have 'na' version
    with open(self.cwd / "VERSION", "w") as vf:
        vf.write(pkgver)


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libsass-devel")
def _(self):
    return self.default_devel()
