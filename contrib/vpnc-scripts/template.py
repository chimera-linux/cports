pkgname = "vpnc-scripts"
_commit = "4ed41c21e3857f96ab935b45092bbb07c3ccd5be"
pkgver = "0_git20240308"
pkgrel = 0
pkgdesc = "OpenConnect network routing script"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://www.infradead.org/openconnect/vpnc-script.html"
source = f"https://gitlab.com/openconnect/vpnc-scripts/-/archive/{_commit}/vpnc-scripts-{_commit}.tar.bz2"
sha256 = "82eb6b28236988bf7b64863ed8698e9204ff99610c73775aa3d67b1a63aab33e"


def install(self):
    self.install_file("vpnc-script", "usr/libexec", 0o755)
    self.install_file("vpnc-script-ptrtd", "usr/libexec", 0o755)
    self.install_file("vpnc-script-sshd", "usr/libexec", 0o755)
