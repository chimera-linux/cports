pkgname = "chrony"
pkgver = "4.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-user=_chrony",
    "--with-sendmail=/usr/bin/sendmail",
    "--enable-ntp-signd",
    "--enable-scfilter",
]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["pkgconf", "gmake"]
makedepends = [
    "libcap-devel", "libedit-devel", "libseccomp-devel",
    "nettle-devel", "gnutls-devel", "linux-headers",
]
checkdepends = ["bash"]
pkgdesc = "NTP client and server"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://chrony.tuxfamily.org"
source = f"https://download.tuxfamily.org/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "9d0da889a865f089a5a21610ffb6713e3c9438ce303a63b49c2fb6eaff5b8804"
file_modes = {
    "var/log/chrony": ("_chrony", "_chrony", 0o755),
    "var/lib/chrony": ("_chrony", "_chrony", 0o755),
}

system_users = [
    {
        "name": "_chrony",
        "id": None,
        "home": "/var/lib/chrony",
    }
]

def post_install(self):
    # config
    self.install_file("examples/chrony.conf.example1", "etc", name = "chrony.conf")
    # default dirs
    self.install_dir("var/log/chrony", empty = True)
    self.install_dir("var/lib/chrony", empty = True)
    # dinit services
    self.install_service(self.files_path / "chrony-dir")
    self.install_service(self.files_path / "chrony")
