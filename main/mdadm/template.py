pkgname = "mdadm"
pkgver = "4.3"
pkgrel = 3
build_style = "makefile"
make_build_args = ["CWFLAGS=", "BINDIR=/usr/bin"]
make_install_args = ["STRIP=", "PREFIX=/usr", "BINDIR=/usr/bin"]
hostmakedepends = ["pkgconf"]
makedepends = ["dinit-chimera", "linux-headers", "udev-devel"]
checkdepends = ["bash", "e2fsprogs", "udev"]
pkgdesc = "Tool for handling Linux md arrays"
license = "GPL-2.0-or-later"
url = "https://raid.wiki.kernel.org/index.php/A_guide_to_mdadm"
source = f"$(KERNEL_SITE)/utils/raid/mdadm/mdadm-{pkgver}.tar.gz"
sha256 = "61a1c22477555364dea1862df7c3b4e8b9a53ee733bad320a45fda27dd0ed44f"
# does not work in sandbox
options = ["!check"]

tool_flags = {
    "CFLAGS": [
        "-DNO_COROSYNC",
        "-DNO_DLM",
        '-DSendmail="sendmail -t"',
        '-DCONFFILE="/etc/mdadm.conf"',
        '-DCONFFILE2="/etc/mdadm/mdadm.conf"',
        '-DMAP_DIR="/run/mdadm"',
        '-DMAP_FILE="map"',
        '-DMDMON_DIR="/run/mdadm"',
        '-DFAILED_SLOTS_DIR="/run/mdadm/failed-slots"',
        "-DUSE_PTHREADS",
    ]
}


def install(self):
    # do not pass STRIP
    self.make.install()


def post_install(self):
    self.install_file("mdadm.conf-example", "etc", name="mdadm.conf")
    self.install_file(
        self.files_path / "modprobe.conf",
        "usr/lib/modprobe.d",
        name="mdadm.conf",
    )
    self.install_service(self.files_path / "mdadm")
    self.install_initramfs(self.files_path / "mdadm.hook")
    self.install_initramfs(self.files_path / "mdadm.local-block", "local-block")
    self.install_initramfs(
        self.files_path / "mdadm.local-bottom", "local-bottom"
    )
