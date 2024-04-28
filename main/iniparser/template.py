pkgname = "iniparser"
pkgver = "4.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_dir = "."
# unset extra defaults
make_build_args = ["ADDITIONAL_CFLAGS="]
hostmakedepends = ["gmake"]
checkdepends = ["bash"]
pkgdesc = "C library for INI file parsing"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/ndevilla/iniparser"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dbcbaf3aedb4f88a9fc0df4b315737ddd10e6c37918e3d89f0ecc475333bde4d"
# vis breaks symbols
hardening = []


def do_install(self):
    self.install_license("LICENSE")
    # bruh moment
    self.install_file("libiniparser.*", "usr/lib", glob=True)
    self.install_link("usr/lib/libiniparser.so", "libiniparser.so.1")
    self.install_file("src/*.h", "usr/include", glob=True)


@subpackage("iniparser-devel")
def _devel(self):
    return self.default_devel()
