pkgname = "tuned"
pkgver = "2.24.0"
pkgrel = 0
build_style = "makefile"
make_install_target = "install-ppd"
hostmakedepends = ["pkgconf", "python"]
depends = ["python-dbus", "python-linux-procfs", "virt-what"]
pkgdesc = "Daemon for monitoring and adaptive tuning of system devices"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-2.0-only"
url = "https://github.com/redhat-performance/tuned"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0f4a72c89772deb8a4e572df70ee3967ba33c1351096a6e87d67674f72830e0e"
# check: tests are broken due to no device binding to cbuild container
options = ["!check"]


def pre_install(self):
    self.install_dir("usr/bin")
    self.install_link("usr/sbin", "bin")


def post_install(self):
    self.uninstall("usr/sbin")
    self.install_service(self.files_path / "tuned")
    self.install_service(self.files_path / "tuned-ppd")
    # GUI depends on systemctl / service CLIs to interact with tuned
    # these depends on systemtap
    for uninstalled in ["tuned-gui", "diskdevstat", "netdevstat", "scomes"]:
        self.uninstall(f"usr/share/man/man8/{uninstalled}.8")
