pkgname = "dinit"
pkgver = "0.12.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_args = ["check-igr"] # additional target
hostmakedepends = ["gmake", "bsdm4"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d5f9afe7005da7c08224dddcf2b63f37a6c4120b7493bed4669ef362cde1b544"

def post_patch(self):
    self.cp(self.files_path / "mconfig", self.cwd)
    (self.cwd / "mconfig").touch() # mtime

def post_install(self):
    # dinit does not install this link by itself right now
    self.install_link("shutdown", "usr/bin/poweroff")
    self.install_link("shutdown.8", "usr/share/man/man8/poweroff.8")
