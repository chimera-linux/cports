pkgname = "chrony"
pkgver = "4.6.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-user=_chrony",
    "--with-sendmail=/usr/bin/sendmail",
    "--enable-ntp-signd",
    "--enable-scfilter",
]
configure_gen = []
make_dir = "."
hostmakedepends = ["pkgconf"]
makedepends = [
    "gnutls-devel",
    "libcap-devel",
    "libedit-devel",
    "libseccomp-devel",
    "linux-headers",
    "nettle-devel",
]
checkdepends = ["bash"]
pkgdesc = "NTP client and server"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://chrony-project.org"
source = f"https://chrony-project.org/releases/chrony-{pkgver}.tar.gz"
sha256 = "571ff73fbf0ae3097f0604eca2e00b1d8bb2e91affe1a3494785ff21d6199c5c"


def post_install(self):
    # config
    self.install_file(
        "examples/chrony.conf.example1", "etc", name="chrony.conf"
    )
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    # dinit services
    self.install_service(self.files_path / "chronyd")
    self.install_service(self.files_path / "chrony", enable=True)
