pkgname = "run-parts"
version = "4.11.2"
revision = 1
bootstrap = True
wrksrc = "debianutils"
build_style = "gnu_configure"
make_build_target = "run-parts"
short_desc = "Run scripts or programs in a directory"
maintainer = "Peter Bui <pbui@github.bx612.space>"
license = "GPL-2.0-or-later"
homepage = "https://tracker.debian.org/pkg/debianutils"
changelog = "http://metadata.ftp-master.debian.org/changelogs/main/d/debianutils/debianutils_${version}_changelog"

from cbuild import sites

distfiles = [f"{sites.debian}/main/d/debianutils/debianutils_{version}.tar.xz"]
checksum = ["3b680e81709b740387335fac8f8806d71611dcf60874e1a792e862e48a1650de"]

def do_install(self):
    self.install_bin("run-parts")
    self.install_man("run-parts.8")
