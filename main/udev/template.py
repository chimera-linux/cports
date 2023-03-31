pkgname = "udev"
pkgver = "253"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dadm-group=false",
    "-Danalyze=false",
    "-Dapparmor=false",
    "-Daudit=false",
    "-Dbacklight=false",
    "-Dbinfmt=false",
    "-Dbpf-framework=false",
    "-Dbzip2=false",
    "-Dcoredump=false",
    "-Ddbus=false",
    "-Defi=false",
    "-Delfutils=false",
    "-Denvironment-d=false",
    "-Dfdisk=false",
    "-Dgcrypt=false",
    "-Dglib=false",
    "-Dgshadow=false",
    "-Dgnutls=false",
    "-Dhibernate=false",
    "-Dhostnamed=false",
    "-Didn=false",
    "-Dima=false",
    "-Dinitrd=false",
    "-Dfirstboot=false",
    "-Dgnu-efi=false",
    "-Dkernel-install=false",
    "-Dldconfig=false",
    "-Dlibcryptsetup=false",
    "-Dlibcurl=false",
    "-Dlibfido2=false",
    "-Dlibidn=false",
    "-Dlibidn2=false",
    "-Dlibiptc=false",
    "-Dlocaled=false",
    "-Dlogind=false",
    "-Dlz4=false",
    "-Dmachined=false",
    "-Dmicrohttpd=false",
    "-Dnetworkd=false",
    "-Dnscd=false",
    "-Dnss-myhostname=false",
    "-Dnss-resolve=false",
    "-Dnss-systemd=false",
    "-Doomd=false",
    "-Dopenssl=false",
    "-Dp11kit=false",
    "-Dpam=false",
    "-Dpcre2=false",
    "-Dpolkit=false",
    "-Dportabled=false",
    "-Dpstore=false",
    "-Dpwquality=false",
    "-Drandomseed=false",
    "-Dresolve=false",
    "-Drfkill=false",
    "-Dseccomp=false",
    "-Dselinux=false",
    "-Dsmack=false",
    "-Dsysext=false",
    "-Dsysusers=false",
    "-Dtimedated=false",
    "-Dtimesyncd=false",
    "-Dtpm=false",
    "-Dqrencode=false",
    "-Dquotacheck=false",
    "-Duserdb=false",
    "-Dutmp=false",
    "-Dvconsole=false",
    "-Dwheel-group=false",
    "-Dxdg-autostart=false",
    "-Dxkbcommon=false",
    "-Dxz=false",
    "-Dzlib=false",
    "-Dzstd=false",

    "-Dhwdb=true",
    "-Dman=true",
    "-Dstandalone-binaries=true",
    "-Dstatic-libudev=true",

    "-Dtests=false",
    "-Dlink-boot-shared=false",
    "-Dlink-journalctl-shared=false",
    "-Dlink-networkd-shared=false",
    "-Dlink-systemctl-shared=false",
    "-Dlink-timesyncd-shared=false",
    "-Dlink-udev-shared=false",
    "-Dsplit-usr=false",
    "-Dsplit-bin=false",
    "-Dsysvinit-path=",
    "-Drpmmacrosdir=no",
    "-Dpamconfdir=no",

    # unrelated but we build it while at it
    "-Dtmpfiles=true",
]
hostmakedepends = [
    "meson", "pkgconf", "perl", "gperf", "bash",
    "docbook-xsl-nons", "python-jinja2", "xsltproc",
]
makedepends = [
    "libblkid-devel", "libmount-devel", "libcap-devel",
    "libkmod-devel", "linux-headers"
]
checkdepends = ["xz", "perl"]
triggers = [
    "/usr/lib/udev/rules.d", "/usr/lib/udev/hwdb.d", "/etc/udev/hwdb.d"
]
pkgdesc = "Standalone build of systemd-udev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/systemd/systemd"
source = f"https://github.com/systemd/systemd/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "acbd86d42ebc2b443722cb469ad215a140f504689c7a9133ecf91b235275a491"
options = ["!splitudev"]

def init_configure(self):
    # bypass some ugly configure checks
    self.configure_args.append(f"-Dtime-epoch={self.source_date_epoch}")

def post_patch(self):
    # the patch won't rename
    self.mv("man/systemd-hwdb.xml", "man/udev-hwdb.xml")

def post_install(self):
    # oh boy, big cleanup time

    ddir = self.destdir

    # drop some more systemd bits
    for f in [
        "usr/include/systemd", "usr/lib/systemd", "usr/lib/tmpfiles.d",
        "usr/share/dbus-1", "usr/share/doc",
    ]:
        self.rm(ddir / f, recursive = True)

    # remove tmpfiles that links to libsystemd
    self.rm(self.destdir / "usr/bin/systemd-tmpfiles")

    # move standalone in its place
    self.mv(
        self.destdir / "usr/bin/systemd-tmpfiles.standalone",
        self.destdir / "usr/bin/systemd-tmpfiles"
    )

    # predictable interface names
    self.install_file(
        self.files_path / "80-net-name-slot.rules",
        "usr/lib/udev/rules.d", mode = 0o644
    )

    # initramfs-tools
    self.install_file(
        self.files_path / "udev.hook",
        "usr/share/initramfs-tools/hooks",
        mode = 0o755, name = "udev"
    )
    self.install_file(
        self.files_path / "udev.init-top",
        "usr/share/initramfs-tools/scripts/init-top",
        mode = 0o755, name = "udev"
    )
    self.install_file(
        self.files_path / "udev.init-bottom",
        "usr/share/initramfs-tools/scripts/init-bottom",
        mode = 0o755, name = "udev"
    )
    # services
    self.install_file(
        self.files_path / "systemd-tmpfiles-clean", "usr/libexec", mode = 0o755
    )
    self.install_file(
        self.files_path / "udevd.wrapper", "usr/libexec", mode = 0o755
    )
    self.install_service(self.files_path / "tmpfiles-clean", enable = True)
    self.install_service(self.files_path / "udevd", enable = True)

@subpackage("udev-devel")
def _devel(self):
    return self.default_devel()

@subpackage("udev-libs")
def _libs(self):
    return self.default_libs()

@subpackage("systemd-tmpfiles")
def _tmpfiles(self):
    self.pkgdesc = "Manage temporary/volatile files/directories"
    self.depends = ["virtual:cmd:snooze!snooze"]

    return [
        "etc/dinit.d/tmpfiles-clean",
        "usr/bin/systemd-tmpfiles",
        "usr/libexec/systemd-tmpfiles-clean",
        "usr/lib/dinit.d/boot.d/tmpfiles-clean",
        "usr/share/man/man5/tmpfiles.d.5",
        "usr/share/man/man8/systemd-tmpfiles.8",
    ]

@subpackage("base-udev")
def _base(self):
    self.pkgdesc = "Base package for udev configs"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.build_style = "meta"

    return []
