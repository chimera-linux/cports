pkgname = "include-what-you-use"
pkgver = "0.27"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
# tied to specific llvm version
makedepends = ["llvm23-clang-devel", "llvm23-devel"]
checkdepends = ["python"]
depends = ["python"]
pkgdesc = "Analyze #includes in C and C++ source files"
license = "NCSA"
url = "https://include-what-you-use.org"
source = f"{url}/downloads/include-what-you-use-{pkgver}.src.tar.gz"
sha256 = "f6871eeea7dc9741cd00aae546d7514abe84b91ca3d1f096f15095e6ac14875f"
# IWYU_EXTRA_FLAGS is wonky and treated differently for various tests,
# and there is no way to cleanly override path to c++ stdlib otherwise
options = ["!check", "llvmflags"]


def post_install(self):
    self.rename("usr/bin/fix_includes.py", "fix_include")
    self.rename("usr/bin/iwyu_tool.py", "iwyu_tool")
    self.install_license("LICENSE.TXT")
