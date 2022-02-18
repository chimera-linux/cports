pkgname = "dinit"
pkgver = "0.12.0_git20220218"
pkgrel = 0
# pin to a git commit for the time being
_commit = "c76a688694e8c109b2b76638bb53e345b6154c19"
build_style = "makefile"
make_cmd = "gmake"
make_check_args = ["check-igr"] # additional target
hostmakedepends = ["gmake", "bsdm4"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "f40875fd68b1fb465af3e37f6d8fdbb3eefaf78a642ac31f5cd39f8164d370e9"

def post_patch(self):
    self.cp(self.files_path / "mconfig", self.cwd)
    (self.cwd / "mconfig").touch() # mtime
