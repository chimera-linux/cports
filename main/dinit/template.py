pkgname = "dinit"
pkgver = "0.15.1"
pkgrel = 0
_gitrev = "b856c50c5a2dd1a8e34e9857603483485f779e65"
build_style = "makefile"
make_cmd = "gmake"
make_check_args = ["check-igr"] # additional target
hostmakedepends = ["gmake"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/{pkgname}/archive/{_gitrev}.tar.gz"
sha256 = "32cbaf8c56921214f9f5520c46b5708b3823d32107988a9e847ffb9b8012ed8c"

def init_configure(self):
    self.make_build_args += [
        "HOSTCXX=" + self.get_tool("CXX", target = "host"),
        "HOSTCXXOPTS=" + self.get_cxxflags(target = "host", shell = True),
        "HOSTLDFLAGS=" + self.get_ldflags(target = "host", shell = True),
    ]

def post_patch(self):
    self.cp(self.files_path / "mconfig", self.cwd)
    (self.cwd / "mconfig").touch() # mtime
