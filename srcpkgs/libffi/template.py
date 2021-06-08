pkgname = "libffi"
version = "3.3"
revision = 2
build_style = "gnu_configure"
configure_args = [
    "--includedir=/usr/include", "--disable-multi-os-directory", "--with-pic"
]
checkdepends = ["dejagnu"]
short_desc = "Library supporting Foreign Function Interfaces"
maintainer = "q66 <daniel@octaforge.org>"
license = "MIT"
homepage = "http://sourceware.org/libffi"
distfiles = [f"ftp://sourceware.org/pub/{pkgname}/{pkgname}-{version}.tar.gz"]
checksum = ["72fba7922703ddfa7a028d513ac15a85c8d54c8d67f55fa5a4802885dc652056"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libffi-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [f"libffi>={version}_{revision}"]

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")
        self.take("usr/lib/pkgconfig")
        self.take("usr/share")

    return install
