pkgname = "udev"
pkgver = "256.11"
pkgrel = 2
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dacl=enabled",
    "-Dadm-group=false",
    "-Danalyze=false",
    "-Dapparmor=disabled",
    "-Daudit=disabled",
    "-Dbacklight=false",
    "-Dbinfmt=false",
    "-Dbootloader=disabled",
    "-Dbpf-framework=disabled",
    "-Dbzip2=disabled",
    "-Dcoredump=false",
    "-Ddbus=disabled",
    "-Defi=false",
    "-Delfutils=disabled",
    "-Denvironment-d=false",
    "-Dfdisk=disabled",
    "-Dgcrypt=disabled",
    "-Dglib=disabled",
    "-Dgshadow=false",
    "-Dgnutls=disabled",
    "-Dhibernate=false",
    "-Dhostnamed=false",
    "-Didn=false",
    "-Dima=false",
    "-Dinitrd=false",
    "-Dfirstboot=false",
    "-Dkernel-install=false",
    "-Dldconfig=false",
    "-Dlibcryptsetup=disabled",
    "-Dlibcurl=disabled",
    "-Dlibfido2=disabled",
    "-Dlibidn=disabled",
    "-Dlibidn2=disabled",
    "-Dlibiptc=disabled",
    "-Dlocaled=false",
    "-Dlogind=false",
    "-Dlz4=disabled",
    "-Dmachined=false",
    "-Dmicrohttpd=disabled",
    "-Dnetworkd=false",
    "-Dnscd=false",
    "-Dnss-myhostname=false",
    "-Dnss-resolve=disabled",
    "-Dnss-systemd=false",
    "-Doomd=false",
    "-Dopenssl=disabled",
    "-Dp11kit=disabled",
    "-Dpam=disabled",
    "-Dpcre2=disabled",
    "-Dpolkit=disabled",
    "-Dportabled=false",
    "-Dpstore=false",
    "-Dpwquality=disabled",
    "-Drandomseed=false",
    "-Dresolve=false",
    "-Drfkill=false",
    "-Dseccomp=disabled",
    "-Dselinux=disabled",
    "-Dsmack=false",
    "-Dsysext=false",
    "-Dsysusers=false",
    "-Dtimedated=false",
    "-Dtimesyncd=false",
    "-Dtmpfiles=false",
    "-Dtpm=false",
    "-Dqrencode=disabled",
    "-Dquotacheck=false",
    "-Duserdb=false",
    "-Dukify=disabled",
    "-Dutmp=false",
    "-Dvconsole=false",
    "-Dwheel-group=false",
    "-Dxdg-autostart=false",
    "-Dxkbcommon=disabled",
    "-Dxz=disabled",
    "-Dzlib=disabled",
    "-Dzstd=disabled",
    "-Dhwdb=true",
    "-Dman=enabled",
    "-Dstandalone-binaries=true",
    "-Dstatic-libudev=true",
    "-Dtests=false",
    "-Dlink-boot-shared=false",
    "-Dlink-journalctl-shared=false",
    "-Dlink-networkd-shared=false",
    "-Dlink-systemctl-shared=false",
    "-Dlink-timesyncd-shared=false",
    "-Dlink-udev-shared=false",
    "-Dsplit-bin=false",
    "-Dsysvinit-path=",
    "-Drpmmacrosdir=no",
    "-Dpamconfdir=no",
]
hostmakedepends = [
    "bash",
    "docbook-xsl-nons",
    "gperf",
    "libxslt-progs",
    "meson",
    "perl",
    "pkgconf",
    "python-jinja2",
]
makedepends = [
    "acl-devel",
    "kmod-devel",
    "libcap-devel",
    "linux-headers",
    "util-linux-blkid-devel",
    "util-linux-mount-devel",
]
checkdepends = ["xz", "perl"]
depends = ["so:libkmod.so.2!kmod-libs"]
triggers = ["/usr/lib/udev/rules.d", "/usr/lib/udev/hwdb.d", "/etc/udev/hwdb.d"]
pkgdesc = "Standalone build of systemd-udev"
license = "LGPL-2.1-or-later"
url = "https://github.com/systemd/systemd"
source = (
    f"https://github.com/systemd/systemd/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "5038424744b2ed8c1d7ecc75b00eeffe68528f9789411da60f199d65762d9ba5"
# the tests that can run are mostly useless
options = ["!splitudev", "!check"]


def init_configure(self):
    # bypass some ugly configure checks
    self.configure_args.append(f"-Dtime-epoch={self.source_date_epoch}")


def post_install(self):
    # oh boy, big cleanup time

    # drop some more systemd bits
    for f in [
        "etc/systemd",
        "usr/lib/libsystemd.*",
        "usr/lib/pkgconfig/libsystemd.pc",
        "usr/share/dbus-1",
        "usr/share/pkgconfig/systemd.pc",
        "usr/share/polkit-1",
    ]:
        self.uninstall(f, glob=True)

    for f in (self.destdir / "usr/lib/systemd").iterdir():
        self.rm(f, recursive=True, glob=True)

    # predictable interface names
    self.install_file(
        self.files_path / "80-net-name-slot.rules",
        "usr/lib/udev/rules.d",
        mode=0o644,
    )

    # hecc
    self.uninstall("usr/bin/bootctl")
    self.uninstall("usr/share/man/man1/bootctl.1")
    self.uninstall("usr/share/man/man1/ukify.1")
    self.uninstall("usr/share/man/man5/loader.conf.5")
    self.uninstall("usr/share/man/man7/linux*", glob=True)
    self.uninstall("usr/share/man/man7/*-boot.7", glob=True)
    self.uninstall("usr/share/man/man7/*-stub.7", glob=True)

    # initramfs-tools
    self.install_initramfs(self.files_path / "udev.hook")
    self.install_initramfs(self.files_path / "udev.init-top", "init-top")
    self.install_initramfs(self.files_path / "udev.init-bottom", "init-bottom")
    # services
    self.install_dir("usr/lib")
    self.install_link("usr/lib/udevd", "../bin/udevadm")
    self.install_file(self.files_path / "udevd.wrapper", "usr/lib", mode=0o755)
    self.install_file(self.files_path / "dinit-devd", "usr/lib", mode=0o755)
    self.install_tmpfiles(self.files_path / "tmpfiles.conf", name="udev")
    self.install_service(self.files_path / "udevd", enable=True)


@subpackage("udev-devel")
def _(self):
    return self.default_devel()


@subpackage("udev-libs")
def _(self):
    return self.default_libs()


@subpackage("udev-meta")
def _(self):
    self.pkgdesc = "Base package for udev configs"
    self.depends = [self.parent]
    self.install_if = [self.parent]
    # transitional
    self.provides = [self.with_pkgver("base-udev")]
    self.options = ["empty"]

    return []
