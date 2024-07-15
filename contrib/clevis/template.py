pkgname = "clevis"
pkgver = "20"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Duser=_clevis",
    "-Dgroup=_clevis",
]
hostmakedepends = [
    "asciidoc",
    "cryptsetup",
    "initramfs-tools",
    "meson",
    "pkgconf",
    "tpm2-tools",
]
makedepends = [
    "bash-completion",
    "jansson-devel",
    "jose-devel",
    "luksmeta-devel",
]
depends = [
    "bash",
    "jq",
    "luksmeta",
]
checkdepends = [
    "curl",
    "keyutils",
    "socat",
    "tang",
]
pkgdesc = "Pluggable framework for automated decryption"
maintainer = "natthias <natthias@proton.me>"
license = "GPL-3.0-or-later WITH custom:openssl-exception"
url = "https://github.com/latchset/clevis"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "67eb9cbbb9c90f9802cae76503f74f23d0046ee6570553407035e9fae3b4b4dd"
# cfi causes some tests to fail
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING.openssl")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
