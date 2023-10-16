pkgname = "udev"
pkgver = "254"
pkgrel = 2
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
    "meson",
    "pkgconf",
    "perl",
    "gperf",
    "bash",
    "docbook-xsl-nons",
    "python-jinja2",
    "xsltproc",
]
makedepends = [
    "libblkid-devel",
    "libmount-devel",
    "libcap-devel",
    "libkmod-devel",
    "linux-headers",
]
checkdepends = ["xz", "perl"]
triggers = ["/usr/lib/udev/rules.d", "/usr/lib/udev/hwdb.d", "/etc/udev/hwdb.d"]
pkgdesc = "Standalone build of systemd-udev"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/systemd/systemd"
source = (
    f"https://github.com/systemd/systemd/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "244da7605800a358915e4b45d079b0b89364be35da4bc8d849821e67bac0ce62"
options = ["!splitudev"]

_have_sd_boot = False

# supported efi architectures
match self.profile().arch:
    case "x86_64" | "aarch64" | "riscv64":
        _have_sd_boot = True

if _have_sd_boot:
    configure_args += [
        "-Dbootloader=true",
        "-Defi=true",
        # secure boot
        "-Dsbat-distro=chimera",
        "-Dsbat-distro-summary=Chimera Linux",
        "-Dsbat-distro-pkgname=systemd-boot",
        "-Dsbat-distro-url=https://chimera-linux.org",
        f"-Dsbat-distro-version={pkgver}-r{pkgrel}",
    ]
    hostmakedepends += ["python-pyelftools"]


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
        "usr/include/systemd",
        "usr/lib/tmpfiles.d",
        "usr/share/dbus-1",
        "usr/share/doc",
    ]:
        self.rm(ddir / f, recursive=True)

    for f in (ddir / "usr/lib/systemd").iterdir():
        # keep efi stubs
        if f.name == "boot":
            continue
        self.rm(f, recursive=True)

    # move standalone in its place
    self.mv(
        self.destdir / "usr/bin/systemd-tmpfiles.standalone",
        self.destdir / "usr/bin/systemd-tmpfiles",
    )

    # predictable interface names
    self.install_file(
        self.files_path / "80-net-name-slot.rules",
        "usr/lib/udev/rules.d",
        mode=0o644,
    )

    # initramfs-tools
    self.install_file(
        self.files_path / "udev.hook",
        "usr/share/initramfs-tools/hooks",
        mode=0o755,
        name="udev",
    )
    self.install_file(
        self.files_path / "udev.init-top",
        "usr/share/initramfs-tools/scripts/init-top",
        mode=0o755,
        name="udev",
    )
    self.install_file(
        self.files_path / "udev.init-bottom",
        "usr/share/initramfs-tools/scripts/init-bottom",
        mode=0o755,
        name="udev",
    )
    # services
    self.install_file(
        self.files_path / "systemd-tmpfiles-clean", "usr/libexec", mode=0o755
    )
    self.install_file(
        self.files_path / "udevd.wrapper", "usr/libexec", mode=0o755
    )
    self.install_service(self.files_path / "tmpfiles-clean", enable=True)
    self.install_service(self.files_path / "udevd", enable=True)


@subpackage("udev-devel")
def _devel(self):
    return self.default_devel()


@subpackage("udev-libs")
def _libs(self):
    return self.default_libs()


@subpackage("systemd-boot", _have_sd_boot)
def _boot(self):
    self.pkgdesc = "UEFI boot manager"
    self.depends += [f"systemd-boot-efi={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/bootctl",
        "usr/libexec/systemd-bless-boot",
        "usr/share/bash-completion/completions/bootctl",
        "usr/share/zsh/site-functions/_bootctl",
        "usr/share/man/man1/bootctl.1",
        "usr/share/man/man5/loader.conf.5",
        "usr/share/man/man7/sd-boot.7",
        "usr/share/man/man7/systemd-boot.7",
    ]


@subpackage("systemd-boot-efi", _have_sd_boot)
def _efi(self):
    self.pkgdesc = "UEFI boot manager (EFI binaries)"

    return [
        "usr/lib/systemd/boot/efi",
        "usr/share/man/man7/linux*.efi.stub.7",
        "usr/share/man/man7/systemd-stub.7",
        "usr/share/man/man7/sd-stub.7",
    ]


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
