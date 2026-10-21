pkgname = "pam_fde_boot_pw"
pkgver = "0_git20250214"
pkgrel = 0
_gitrev = "49bf498fd8d13f73e4a24221818a8a5d2af20088"
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["keyutils-devel", "linux-pam-devel"]
pkgdesc = "PAM module to unlock user gnome/kde keyrings with FDE passwords"
license = "MIT"
url = "https://git.sr.ht/~kennylevinsen/pam_fde_boot_pw"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "986c4b06cebdd7d4dac109761d0df7a9794edac391781e6942cbc906388e1c0b"


def post_install(self):
    self.install_license("LICENSE")
