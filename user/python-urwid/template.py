pkgname = "python-urwid"
pkgver = "3.0.3"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # wrong os silly
    "--ignore=urwid/display/_win32.py",
    "--ignore=urwid/display/_win32_raw_display.py",
    # missing checkdep: python-tornado
    "--ignore=urwid/event_loop/tornado_loop.py",
    # missing checkdep: python-zmq
    "--ignore=urwid/event_loop/zmq_loop.py",
    # TypeError: Can't instantiate abstract class Screen without an
    # implementation for abstract methods '_read_raw_input', '_start',
    # '_stop', 'hook_event_loop', 'unhook_event_loop'
    "--ignore=urwid/display/_raw_display_base.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
]
depends = ["python-wcwidth"]
checkdepends = [
    "python-gobject",
    "python-pyserial",
    "python-pytest",
    "python-trio",
    "python-twisted",
    *depends,
]
pkgdesc = "Console UI library"
license = "LGPL-2.1-or-later"
url = "https://urwid.org"
source = f"$(PYPI_SITE)/u/urwid/urwid-{pkgver}.tar.gz"
sha256 = "300804dd568cda5aa1c5b204227bd0cfe7a62cef2d00987c5eb2e4e64294ed9b"
