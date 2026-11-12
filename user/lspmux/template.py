pkgname = "lspmux"
pkgver = "0.3.0"
# changed upstream
_cname = "ra-multiplex"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["dinit-chimera", "dinit-dbus", "rust-std"]
depends = ["dinit-dbus"]
pkgdesc = "Share a language server instance between multiple clients"
license = "EUPL-1.2"
url = "https://codeberg.org/p2502/lspmux"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "28caab4a2f74dc4b8117ac5eed3af2b30258eab1affb47f47363afece0982243"
if self.profile.wordsize == 32:
    broken = "needs atomic64"


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "lspmux.user")


# old package compat
@subpackage(f"lspmux-{_cname}")
def _(self):
    self.subdesc = f"{_cname} compatibility link"
    self.renames = [f"{_cname}"]
    self.install_if = [self.parent, _cname]
    return [
        f"@usr/bin/{_cname}=>lspmux",
        f"@usr/lib/dinit.d/user/{_cname}.user=>lspmux.user",
    ]
