pkgname = "dinit"
pkgver = "0.12.0_git20220221"
pkgrel = 0
# pin to a git commit for the time being
_commit = "d975e76d20730d6e7ceb68bb500d51053faf199b"
build_style = "makefile"
make_cmd = "gmake"
make_check_args = ["check-igr"] # additional target
hostmakedepends = ["gmake", "bsdm4"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "418c9bd732af23af9ed3a3184704f4cf770d64a3224138552c3a5c5a491f11e8"

def init_configure(self):
    self.make_build_args += [
        "HOSTCXX=" + self.get_tool("CXX", target = "host"),
        "HOSTCXXOPTS=" + self.get_cxxflags(target = "host", shell = True),
        "HOSTLDFLAGS=" + self.get_ldflags(target = "host", shell = True),
    ]

def post_patch(self):
    self.cp(self.files_path / "mconfig", self.cwd)
    (self.cwd / "mconfig").touch() # mtime
