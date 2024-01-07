pkgname = "libcdio-paranoia"
_v1 = "10.2"
_v2 = "2.0.1"
pkgver = f"{_v1}.{_v2}"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-example-progs", "--enable-cpp-progs"]
make_cmd = "gmake"
# out of tree build is broken
make_dir = "."
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["libcdio-devel", "linux-headers"]
pkgdesc = "CD paranoia utility/libraries from libcdio"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/libcdio"
source = f"$(GNU_SITE)/libcdio/{pkgname}-{_v1}+{_v2}.tar.bz2"
sha256 = "33b1cf305ccfbfd03b43936975615000ce538b119989c4bec469577570b60e8a"


@subpackage("libcdio-paranoia-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libcdio-paranoia-progs")
def _progs(self):
    return self.default_progs()


configure_gen = []
