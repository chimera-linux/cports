pkgname = "keyd"
pkgver = "2.6.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
make_use_env = True
makedepends = ["dinit-chimera", "linux-headers", "turnstile"]
pkgdesc = "Key remapping daemon for linux"
license = "MIT"
url = "https://github.com/rvaiya/keyd"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "697089681915b89d9e98caf93d870dbd4abce768af8a647d54650a6a90744e26"
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
