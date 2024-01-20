pkgname = "iniparser"
pkgver = "4.1"
pkgrel = 1
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
source = (
    f"https://github.com/ndevilla/iniparser/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "960daa800dd31d70ba1bacf3ea2d22e8ddfc2906534bf328319495966443f3ae"
# vis breaks symbols
hardening = []


def do_install(self):
    self.install_license("LICENSE")
    # bruh moment
    self.install_file("libiniparser.*", "usr/lib", glob=True)
    self.install_link("libiniparser.so.1", "usr/lib/libiniparser.so")
    self.install_file("src/*.h", "usr/include", glob=True)


@subpackage("iniparser-devel")
def _devel(self):
    return self.default_devel()
