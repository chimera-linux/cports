pkgname = "dinit"
pkgver = "0.13.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_args = ["check-igr"] # additional target
hostmakedepends = ["gmake", "bsdm4"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "bdf23a69c6778aee323b73a67e0d5b3f2871608df9815857b9ff1ac63208a267"

def init_configure(self):
    self.make_build_args += [
        "HOSTCXX=" + self.get_tool("CXX", target = "host"),
        "HOSTCXXOPTS=" + self.get_cxxflags(target = "host", shell = True),
        "HOSTLDFLAGS=" + self.get_ldflags(target = "host", shell = True),
    ]

def post_patch(self):
    self.cp(self.files_path / "mconfig", self.cwd)
    (self.cwd / "mconfig").touch() # mtime
