pkgname = "chroot-gawk"
version = "5.0.1"
revision = 1
bootstrap = True
wrksrc = f"gawk-{version}"
build_style = "gnu_configure"
configure_args = [
    "--disable-nls", "--without-readline", "ac_cv_libsigsegv=/bin/false"
]
short_desc = "GNU awk utility -- for xbps-src use"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "https://directory.fsf.org/wiki/Gawk"

from cbuild import sites

distfiles = [f"{sites.gnu}/gawk/gawk-{version}.tar.xz"]
checksum = ["8e4e86f04ed789648b66f757329743a0d6dfb5294c3b91b756a474f1ce05a794"]

def post_install(self):
    self.rmtree("usr/share")
    self.rmtree("etc/profile.d")
    self.rmtree("usr/include")
