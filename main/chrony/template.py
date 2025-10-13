pkgname = "chrony"
pkgver = "4.8"
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
    "dinit-chimera",
    "gnutls-devel",
    "libcap-devel",
    "libedit-devel",
    "libseccomp-devel",
    "linux-headers",
    "nettle-devel",
]
checkdepends = ["bash"]
pkgdesc = "NTP client and server"
license = "GPL-2.0-or-later"
url = "https://chrony-project.org"
source = f"https://chrony-project.org/releases/chrony-{pkgver}.tar.gz"
sha256 = "33ea8eb2a4daeaa506e8fcafd5d6d89027ed6f2f0609645c6f149b560d301706"


def post_install(self):
    # config
    self.install_file(
        "examples/chrony.conf.example1", "etc", name="chrony.conf"
    )
    self.install_sysusers("^/sysusers.conf")
    self.install_tmpfiles("^/tmpfiles.conf")
    # dinit services
    self.install_service("^/chronyd")
    self.install_service("^/chrony", enable=True)
