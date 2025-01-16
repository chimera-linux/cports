pkgname = "sdbus-cpp"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE:STRING=Release"]
hostmakedepends = ["cmake", "pkgconf", "ninja"]
makedepends = ["elogind-devel", "libexpat-devel", "gtest-devel"]
pkgdesc = "High-level C++ D-Bus library for Linux"
maintainer = "kkflt <kkflt@cyberdude.com>"
license = "LGPL-2.1-only"
url = "https://github.com/Kistler-Group/sdbus-cpp"
source = f"{url}/archive/v{pkgver}/sdbus-v{pkgver}.tar.gz" 
sha256 = "6025e5dc6cddd532ff960d14e68ced5f42a1916b23a73fea6bcb437f06992eaf"

def post_install(self):
	self.install_license("COPYING")

@subpackage("sdbus-cpp-devel")
def _(self):
	return self.default_devel()
