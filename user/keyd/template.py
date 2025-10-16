pkgname = "keyd"
pkgver = "2.5.0"
pkgrel = 2
build_style = "makefile"
make_check_target = "test"
make_use_env = True
makedepends = ["dinit-chimera", "linux-headers", "turnstile"]
pkgdesc = "Key remapping daemon for linux"
license = "MIT"
url = "https://github.com/rvaiya/keyd"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "93ec6c153ef673a7a8b4d8b686494dee11d182513f4531c71dce15a8db7f6c1c"
hardening = ["vis", "cfi"]
# tests want /dev/uinput
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "time64 input_event brokenness"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service("^/keyd")
    self.install_service("^/keyd.user")
    self.install_sysusers("^/sysusers.conf")
