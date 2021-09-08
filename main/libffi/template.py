pkgname = "libffi"
version = "3.3"
revision = 0
build_style = "gnu_configure"
configure_args = [
    "--includedir=/usr/include", "--disable-multi-os-directory", "--with-pic"
]
checkdepends = ["dejagnu"]
short_desc = "Library supporting Foreign Function Interfaces"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
homepage = "http://sourceware.org/libffi"
distfiles = [f"ftp://sourceware.org/pub/{pkgname}/{pkgname}-{version}.tar.gz"]
checksum = ["72fba7922703ddfa7a028d513ac15a85c8d54c8d67f55fa5a4802885dc652056"]

options = ["bootstrap", "!check"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libffi-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [f"libffi={version}-r{revision}"]

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
        "usr/share",
    ]
