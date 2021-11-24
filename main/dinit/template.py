# XXX build: static binaries since init system ?
pkgname = "dinit"
pkgver = "0.12.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "bsdm4"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://davmac.org/projects/dinit"
source = f"https://github.com/davmac314/dinit/releases/download/v{pkgver}/dinit-{pkgver}.tar.xz"
sha256 = "d5f9afe7005da7c08224dddcf2b63f37a6c4120b7493bed4669ef362cde1b544"
tool_flags = {"CXXFLAGS": ["-fno-rtti"], "LDFLAGS": ["-fno-rtti"]}

def post_patch(self):
    # static mconfig file instead of generated one
    self.cp(self.files_path / "mconfig", self.cwd)

def do_check(self):
    self.make.invoke("check")
    # integration tests
    self.make.invoke("check-igr")
