pkgname = "dinit"
pkgver = "0.12.0_git20220215"
pkgrel = 0
# pin to a git commit for the time being
_commit = "49f4b5f3daea3174fcb78d4fd50354c24399f30a"
build_style = "makefile"
make_cmd = "gmake"
make_check_args = ["check-igr"] # additional target
hostmakedepends = ["gmake", "bsdm4"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/{pkgname}/archive/{_commit}.tar.gz"
sha256 = "49526385c1b1a7174fbdd8278915d1f5942e6052c65c5b9297e2a043914bc569"

def post_patch(self):
    self.cp(self.files_path / "mconfig", self.cwd)
    (self.cwd / "mconfig").touch() # mtime
