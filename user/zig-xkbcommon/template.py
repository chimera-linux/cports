pkgname = "zig-xkbcommon"
pkgver = "0.1.0"
pkgrel = 0
pkgdesc = "Zig bindings for xkbcommon"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "MIT"
url = "https://codeberg.org/ifreund/zig-xkbcommon"
source = f"{url}/archive/3a2eefdad6b4d48757274061dd2b5df3b89a2bfd.tar.gz"
sha256 = "9140440d82266b9d912a988a0bb219cd01e65582104f01870cfc3dc47635a9ba"


def do_install(self):
    self.install_files(
        ".",
        "usr/src/zig/packages/",
        name="1220ed0ec8a6cb1990c2f95bfd71fe7f8bcb6b8e4778573f03b3c755ea81fbf74ee8",
    )


def post_install(self):
    self.install_license("LICENSE")
