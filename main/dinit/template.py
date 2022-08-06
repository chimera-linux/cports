pkgname = "dinit"
pkgver = "0.15.1"
pkgrel = 0
_gitrev = "f3557a59a98479f1926aaa0c0f2c33b2211f63ef"
build_style = "makefile"
make_cmd = "gmake"
make_check_args = ["check-igr"] # additional target
hostmakedepends = ["gmake"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/{pkgname}/archive/{_gitrev}.tar.gz"
sha256 = "802a9aafba4a117bd1670a55c471eee0e1958a95a8a82a9070554dbeffe5d902"

def init_configure(self):
    self.make_build_args += [
        "HOSTCXX=" + self.get_tool("CXX", target = "host"),
        "HOSTCXXOPTS=" + self.get_cxxflags(target = "host", shell = True),
        "HOSTLDFLAGS=" + self.get_ldflags(target = "host", shell = True),
    ]

def post_patch(self):
    self.cp(self.files_path / "mconfig", self.cwd)
    (self.cwd / "mconfig").touch() # mtime
