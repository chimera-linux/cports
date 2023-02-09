pkgname = "dinit"
pkgver = "0.16.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_args = ["check-igr"] # additional target
hostmakedepends = ["gmake"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "020da31210322e01c07d30343671f6ba2b1024fab0699a1df49f390d462e8f69"
hardening = ["vis", "cfi"]

def init_configure(self):
    self.make_build_args += [
        "HOSTCXX=" + self.get_tool("CXX", target = "host"),
        "HOSTCXXOPTS=" + self.get_cxxflags(target = "host", shell = True),
        "HOSTLDFLAGS=" + self.get_ldflags(target = "host", shell = True),
    ]

def post_patch(self):
    self.cp(self.files_path / "mconfig", self.cwd)
    (self.cwd / "mconfig").touch() # mtime
